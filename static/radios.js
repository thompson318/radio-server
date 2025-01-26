
const radio3 = "http://as-hls-ww-live.akamaized.net/pool_23461179/live/ww/bbc_radio_three/bbc_radio_three.isml/bbc_radio_three-audio=320000.m3u8"

const radio4 = "http://as-hls-ww-live.akamaized.net/pool_55057080/live/ww/bbc_radio_fourfm/bbc_radio_fourfm.isml/bbc_radio_fourfm-audio=320000.m3u8"

const radio6 ="http://as-hls-ww-live.akamaized.net/pool_81827798/live/ww/bbc_6music/bbc_6music.isml/bbc_6music-audio%3d320000.norewind.m3u8"

const radio5sportsextra ="http://as-hls-uk-live.akamaized.net/pool_47700285/live/uk/bbc_radio_five_live_sports_extra/bbc_radio_five_live_sports_extra.isml/bbc_radio_five_live_sports_extra-audio%3d96000.norewind.m3u8"

const talksport2 = "http://radio.talksport.com/stream2?ref=rf"

const rrr = "http://realtime.rrr.org.au/p1h"

function play(channel){
	address = String("/play?channel=" + channel)
	console.log("Playing", address)
	fetch(address,{method:"GET"})
}
function stop(){
	console.log("Stopping")
	fetch("/stop",{method:"GET"})
}
function screenoff(){
	console.log("screen off")
	fetch("/screenoff",{method:"GET"})
}
function screenon(){
	console.log("screen on")
	fetch("/screenon",{method:"GET"})
}
