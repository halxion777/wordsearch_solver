from core import app_factory
import os

conf_file = lambda file_name: os.path.join(os.path.dirname(os.path.abspath(__file__)), "conf", file_name)

app = app_factory(conf_file("prod.py"))
app.static("/static", "/app/core/web/static")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)