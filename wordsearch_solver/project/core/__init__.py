from .api import api
from .web.home import home
from sanic import Sanic

def app_factory(conf:str):
    app = Sanic(__name__)
    app.config.from_pyfile(conf)

    app.blueprint(api, url_prefix="/api")
    app.blueprint(home, url_prefix="/")
    return app

