from app.main.routes.victims import api as victims_ns

from app.main.api import api


api.add_namespace(victims_ns, path="/")
