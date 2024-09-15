from flask import Flask, request, render_template, jsonify, send_file
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

@app.route('/radio4', methods=['GET'])
def radio4():

    media=player.media_new("http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_radio_fourfm/bbc_radio_fourfm.isml/bbc_radio_fourfm-audio=320000.m3u8")
    myplayer.set_media(media)
    myplayer.play()
    return "Playing radio 4"

@app.route('/stop', methods=['GET'])
def stop():

    myplayer.stop()
    return "Stopping"

@app.route('/radio6', methods=['GET'])
def radio6():

    media=player.media_new("http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_6music/bbc_6music.isml/bbc_6music-audio=320000.m3u8")
    myplayer.set_media(media)
    myplayer.play()
    return "Playing radio 4"



if __name__ == '__main__':
    app.run(port=5002, threaded=True)

