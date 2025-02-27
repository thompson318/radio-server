from flask import Flask, request, render_template, jsonify, send_file
import subprocess
import vlc
import logging

# Declare a flask app
app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

class audio_player():
    def __init__(self):
        self.player=vlc.Instance()
        self.myplayer =  self.player.media_player_new()

    def play(self, channel):
        self.myplayer.set_media
        media=self.player.media_new(channel)
        self.myplayer.set_media(media)
        self.myplayer.play()

    def stop(self):
        self.myplayer.stop()


my_audio_player = audio_player()

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
    my_audio_player.play(channel)
    return channel

@app.route('/stop', methods=['GET'])
def stop():

    my_audio_player.stop()
    return "Stopping"

@app.route('/status', methods=['GET'])
def status():
    if myplayer.is_playing():
        return 'playing'
    else:
        return 'idle'

@app.route('/screenoff', methods=['GET'])
def screenoff():
    try:
        subprocess.run(['xset', '-display', ':0.0', 'dpms', 'force', 'off'])
    except:
        pass

@app.route('/screenon', methods=['GET'])
def screenon():
    try:
        subprocess.run(['xset', '-display', ':0.0', 'dpms', 'force', 'on'])
    except:
        pass

if __name__ == '__main__':
    app.run(port=5002, threaded=True)

