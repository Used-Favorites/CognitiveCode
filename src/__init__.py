# Este arquivo inicializa o aplicativo Flask e reúne todas as partes do projeto.

from flask import Flask, request
from src.middlewares import authData

app = Flask('DemoApp')

# calling our middleware
app.wsgi_app = authData.Middleware(app.wsgi_app)

@app.route('/', methods=['GET', 'POST'])
def hello():
    # using 
    user = request.environ['user']
    return "Hi %s" % user['name']


if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
