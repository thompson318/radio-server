from flask import Flask, request, render_template, jsonify, send_file
import subprocess
import vlc


# Declare a flask app
app = Flask(__name__)

class audio_player():
    def __init__(self):
        self.player=vlc.Instance()
        self.myplayer =  self.player.media_player_new()
        self.myplayer.audio_output_device_set(None, "hdmi:CARD=vc4hdmi,DEV=0")

    def play(self, channel):
        self.myplayer.set_media
        media=self.player.media_new(channel)
        self.myplayer.set_media(media)
        self.myplayer.play()

    def stop(self):
        self.myplayer.stop()
        del self.myplayer
        del self.player
        self.__init__()


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

