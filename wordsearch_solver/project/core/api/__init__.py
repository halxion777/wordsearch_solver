from sanic import Blueprint


api = Blueprint("api")
from . import routes