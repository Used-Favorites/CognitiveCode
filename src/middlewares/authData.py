# Este é um exemplo de um middleware. Este arquivo pode conter a lógica para autenticação e autorização.

from werkzeug.wrappers import Request, Response, ResponseStream


class Middleware:
    def __init__(self, app):
        self.app = app
        self.username = 'Tony'
        self.password = 'IamIronMan'

    def __call__(self, environ, start_response):
        request = Request(environ)
        username: str | None = request.authorization['username']
        password = request.authorization['password']

        # these are hardcoded for demonstration
        # verify the username and password from some database or env config variable
        if username == self.username and password == self.password:
            environ['user'] = {'name': 'Tony'}
            return self.app(environ, start_response)

        res = Response(u'Authorization failed', mimetype='text/plain', status=401)
        return res(environ, start_response)

