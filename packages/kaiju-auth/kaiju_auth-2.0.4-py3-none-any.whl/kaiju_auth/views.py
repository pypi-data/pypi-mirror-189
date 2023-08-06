import asyncio

from aiohttp import web  # noqa pycharm?

from kaiju_tools.serialization import dumps, loads
from kaiju_tools.http.views import JSONRPCView
from kaiju_tools.rpc.etc import JSONRPCHeaders
from kaiju_tools.rpc.services import JSONRPCServer

from kaiju_auth.login import AuthService
from kaiju_auth.sessions import SessionService

__all__ = ['RestrictedJSONRPCView']


class RestrictedJSONRPCView(JSONRPCView):
    """JSON RPC HTTP view with session based authorization."""

    route = '/rpc'
    session_cookie_fmt = '{env}-{app}-session'

    async def post(self):
        """Post to the rpc view with authorization."""
        app = self.request.app
        headers = self.request.headers
        session_service: SessionService = app.services[SessionService.service_name]  # noqa
        auth_service: AuthService = app.services[AuthService.service_name]  # noqa
        rpc: JSONRPCServer = app.services[JSONRPCServer.service_name]  # noqa
        session_cookie_key = self.session_cookie_fmt.format(env=app['env'], app=app['name'])
        user_agent = headers.get('User-Agent')
        cookie_session = False

        # checking for session and auth

        session = None
        session_id = None
        auth_str = headers.get('Authorization')
        if auth_str:
            if auth_str.startswith('Bearer '):
                session = await auth_service.token_auth(auth_str.replace('Bearer ', '', 1))
            else:
                session = await auth_service.basic_auth(auth_str)
        elif JSONRPCHeaders.SESSION_ID_HEADER in headers:
            session_id = headers[JSONRPCHeaders.SESSION_ID_HEADER]
            session = await session_service.load_session(session_id, user_agent=user_agent)
        else:
            session_id = self.request.cookies.get(session_cookie_key)
            if session_id:
                session = await session_service.load_session(session_id, user_agent=user_agent)
                cookie_session = True
        if not session:
            session = session_service.get_new_session({}, user_agent=user_agent)
            session_id = None

        # method call

        body = await self.request.json(loads=loads)
        headers, result = await rpc.call(body, dict(headers), session, nowait=False, scope=session.scope)
        response = web.json_response(result.repr(), dumps=dumps, headers=headers, status=200)
        if session.stored and (session_id or session.changed):  # this session has been referenced or changed
            asyncio.create_task(session_service.save_session(session))
            if cookie_session:
                response.set_cookie(session_cookie_key, session.id, secure=True)
            else:
                response.headers[JSONRPCHeaders.SESSION_ID_HEADER] = session.id

        return response
