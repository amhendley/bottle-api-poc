from bottle import Bottle
try:
    import api
except ImportError:
    from app import api


app = Bottle()

app.route('/', 'GET', api.root_index)
app.route('/v3/hello/<name>', "GET", api.hello)
app.route('/v4/hello/<name:re:.*>', "GET", api.hello2)
