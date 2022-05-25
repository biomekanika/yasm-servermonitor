import os
import utilities.config as config
import services.hostchecker as hostchecker
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/ping/<string:host>")
def ping(host):

    # Call Service
    response = hostchecker.pingHost(host)

    # Render
    return response.host + " : " + response.text


@app.route('/')
@app.route("/checkAllHosts")
def checkAllHosts():

    baseDir = os.path.abspath(os.path.dirname(__file__))
    configFile = os.path.join(baseDir, 'config/config.yml')

    # Call Service
    responseList = hostchecker.getHostStatus(config.getHosts(configFile))

    # Render
    return render_template('home.html', hosts=responseList)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
