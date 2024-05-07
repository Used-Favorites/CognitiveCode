# Este é o arquivo que você executa para iniciar o projeto.

from src import app
from config import Config

app.run(Config.host, Config.PORT, Config.debug)