from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from calc import app as flask_app
from view import app as dash
import sys

application = DispatcherMiddleware(flask_app, {
    '/view_count': dash.server,
})

if __name__ == '__main__':
    port = int(sys.argv[1])
    run_simple('0.0.0.0', port, application)
    # run_simple('localhost', 8050, application)