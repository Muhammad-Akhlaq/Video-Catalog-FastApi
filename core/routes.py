# -*- coding: utf-8 -*-
from api.v1.video import routes as video_routes


def add_routes(app):
    """
    add app routes
    """
    app.router.prefix = "/api/v1"
    app.include_router(video_routes.router)
