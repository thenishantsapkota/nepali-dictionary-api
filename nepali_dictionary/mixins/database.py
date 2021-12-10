from starlette.requests import Request
from sqlmodel import Session
from nepali_dictionary.common.db import engine

class DBMixin:
    def __init__(self, request: Request):
        self.request = request
        self.session = Session
        self.engine = engine
