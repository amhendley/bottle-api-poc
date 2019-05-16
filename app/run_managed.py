import os
from managed_routes import app


app_port = os.environ.get('PORT', 9000)

app.run(host='localhost', port=app_port)
