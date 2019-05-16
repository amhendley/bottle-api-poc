import os
import bottle
import api


app = bottle.app()

app_port = os.environ.get('PORT', 9000)

if __name__=='__main__':
    bottle.debug(True)
    bottle.run(app=app,host='localhost',port=8080)
