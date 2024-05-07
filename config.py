# Este arquivo contém todas as configurações do seu aplicativo, como configurações de banco de dados, configurações de aplicativo, etc.

class Config:
    PORT: int = 5000
    host: str = '127.0.0.1'
    debug: bool = True
    def __init__(self):
        pass
