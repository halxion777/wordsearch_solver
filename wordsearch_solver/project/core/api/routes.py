import json
from sanic import response
from . import api

@api.route("/sample_data")
async def sample_data(request):
    filename = request.args.get("file_name")
    with open(f"/app/core/web/static/sample_files/{filename}.json") as sample_data:
        data = json.load(sample_data)
    return response.json(data)

