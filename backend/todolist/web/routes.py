from . import web
from .controllers import Home

web.add_resource(Home, "/")