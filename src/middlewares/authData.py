# Este é um exemplo de um middleware. Este arquivo pode conter a lógica para autenticação e autorização.

from typing import Iterable
from flask import Flask
from werkzeug.wrappers import Request, Response, ResponseStream


class Middleware:
    def __init__(self, app) -> None:
        self.app: Flask = app
        self.username: str = "Gabriel"
        self.password: str = "casa123"

    def AuthCheck(self, username: str, password: str) -> bool:
        return username == self.username and password == self.password

    
