from flask import Flask
app = Flask(__name__)

import salt
import salt.config
import salt.wheel
import salt.loader
opts = salt.config.master_config('/etc/salt/master')
wheel = salt.wheel.WheelClient(opts)

def testing():
    ret = {}
    dupa = wheel.cmd('key.list', ['all'])
    return ret


@app.route('/')
def index():
    testing()
    return '<h1>Hello world!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9999', debug=True)
