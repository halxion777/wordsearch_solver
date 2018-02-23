from sanic import Blueprint

home = Blueprint("home")
from . import routes