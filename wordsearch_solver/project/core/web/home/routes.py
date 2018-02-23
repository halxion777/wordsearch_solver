from . import home
from sanic import response

@home.route("/")
async def index(request):
    with open("/app/core/web/templates/index.html") as home_page:
        return response.html(home_page.read())
