from flask import Flask, request, render_template, jsonify, send_file
import subprocess
import vlc


# Declare a flask app
app = Flask(__name__)

player=vlc.Instance()
myplayer =  player.media_player_new()



@app.route('/favicon.ico', methods=['GET'])
def favicon():
    """
    returns the icon
    """
    return send_file('favicon.ico', mimetype='image/ico')


@app.route('/', methods=['GET'])
def index():
    """
    returns the main page, template/index.html
    """
    return render_template('index.html')

@app.route('/play', methods=['GET'])
def play():
    channel = request.args.get("channel")
    media=player.media_new(channel)
    myplayer.set_media(media)
    myplayer.play()
    return channel

@app.route('/stop', methods=['GET'])
def stop():

    myplayer.stop()
    return "Stopping"


@app.route('/screenoff', methods['GET'])
def screenoff():
    subprocess.run(['xset', '-display', ':0.0', 'dpms', 'force', 'off'])

@app.route('/screenon', methods['GET'])
def screenoff():
    subprocess.run(['xset', '-display', ':0.0', 'dpms', 'force', 'on'])

if __name__ == '__main__':
    app.run(port=5002, threaded=True)

