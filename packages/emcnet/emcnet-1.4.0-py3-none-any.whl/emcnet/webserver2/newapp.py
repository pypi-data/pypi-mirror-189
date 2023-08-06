from dash import Dash
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import flask
from werkzeug.serving import run_simple
import dash_html_components as html

server = flask.Flask(__name__)
dash_app1 = Dash(__name__, server=server, url_base_pathname='/dashboard/')
dash_app2 = Dash(__name__, server=server, url_base_pathname='/reports/')
dash_app1.layout = html.Div([html.H1('Hi there, I am app1 for dashboards')])
dash_app2.layout = html.Div([html.H1('Hi there, I am app2 for reports')])


# @server.route('/')
# @server.route('/hello')
# def hello():
#     return 'hello world!'


@server.route('/emcnet/<site_id>')
def render_site_dashboard():
    #return flask.redirect('/dash1')
    return dash_app1.layout


# @server.route('/reports')
# def render_reports():
#     return flask.redirect('/dash2')


# @server.route('/emcnet/<site_id>')
# def show_site_dashboard(site_id):
#     return 'Site %s' % escape(site_id)
#
#
app = DispatcherMiddleware(server, {
    '/dash1': dash_app1.server,
    '/dash2': dash_app2.server
})

run_simple('0.0.0.0', 8080, app, use_reloader=True, use_debugger=True)
