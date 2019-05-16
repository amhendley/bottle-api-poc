from bottle import route, template
import subprocess


p1 = subprocess.Popen(['ip','addr','show','eth0'],stdout=subprocess.PIPE)
p2 = subprocess.Popen(['sed','-rn',r's/\s*inet\s(([0-9]{1,3}\.){3}[0-9]{1,3}).*/\1/p'],stdin=p1.stdout,stdout=subprocess.PIPE)
p1.stdout.close()
ip_addr = p2.communicate()[0].strip()
p1.wait()


@route('/')
def root_index():
    return template('index',ip_addr = ip_addr)


@route('/v1/hello/<name>', method="GET")
def hello(name):
    return template('<b>Hello {{name.title() if name else "stranger"}}</b>!', name=name)


@route('/v2/hello/<name:re:.*>', "GET")
def hello2(name=''):
    return template('<b>Hello {{name.title() if name else "stranger"}}</b>!', name=name)
