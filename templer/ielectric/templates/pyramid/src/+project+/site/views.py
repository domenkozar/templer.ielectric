
from pyramid.view import view_config


@view_config(renderer='templates/index.jinja2')
def index(request):
    return {}
