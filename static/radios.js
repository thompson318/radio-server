const bbc_world_service = "http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/nonuk/sbr_low/ak/bbc_world_service.m3u8"

const radio1 = "http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_radio_one/bbc_radio_one.isml/bbc_radio_one-audio=320000.m3u8"

const radio1extra = "http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_1xtra/bbc_1xtra.isml/bbc_1xtra-audio=320000.m3u8"

const radio1dance = "http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_radio_one_dance/bbc_radio_one_dance.isml/bbc_radio_one_dance-audio=320000.m3u8"

const radio1relax = "http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_radio_one_relax/bbc_radio_one_relax.isml/bbc_radio_one_relax-audio=320000.m3u8"

const radio2 = "http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_radio_two/bbc_radio_two.isml/bbc_radio_two-audio=320000.m3u8"

const radio3 = "http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_radio_three/bbc_radio_three.isml/bbc_radio_three-audio=320000.m3u8"

const radio4 = "http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_radio_fourfm/bbc_radio_fourfm.isml/bbc_radio_fourfm-audio=320000.m3u8"

const radio4lw = "http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_radio_fourlw/bbc_radio_fourlw.isml/bbc_radio_fourlw-audio=320000.m3u8"

const radio6 ="http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_6music/bbc_6music.isml/bbc_6music-audio=320000.m3u8"

const radio5sportsextra ="http://as-hls-uk-live.akamaized.net/pool_904/live/uk/bbc_radio_five_live_sports_extra/bbc_radio_five_live_sports_extra.isml/bbc_radio_five_live_sports_extra-audio%3d96000.norewind.m3u8"

function play(channel){
	address = String("/play?channel=" + channel)
	console.log("Playing", address)
	fetch(address,{method:"GET"})
}
function stop(){
	console.log("Stopping")
	fetch("/stop",{method:"GET"})
}
