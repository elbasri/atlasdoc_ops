# src/app.py
from fastapi import FastAPI
def create_app():
    app = FastAPI()
    @app.get('/')
    def read_root():
        return {'message': 'Hello, AtlasDoc Ops!'}
    return app