http://192.168.1.182/httpapi.asp?command=setPlayerCmd:play:http://nashe1.hostingradio.ru/nashe-256


httpapi.asp?command=setPlayerCmd:play:  - вызов команды
 
http://1.stream.laut.fm/celtic-rock - адрес аудиопотока или файла для проигрывания

Остановка делается с помощью следующего запроса:
http://172.16.1.11/httpapi.asp?command=setPlayerCmd:stop

http://192.168.1.4/httpapi.asp?command=getPlayerStatus

Выдает код в JSON, в котором при желании можно увидеть
"status":"play","curpos":"28591" - статус и время в миллисекундах с начала воспроизведения.

https://www.diyaudio.com/forums/class-d/302748-am-v200-wifi.html#post4964189

https://enceintesetmusiques.com/forum/verdict-sur-le-fda-v200-1732

key_id_press:wps
key_id_press:wpss
GUARD_WPS_SERVER:1  GUARD_WPS_CANNEL
key_id_press:PlayPause  /tmp/Requesta01controller
setPlayerCmd:onepause
key_id_press:prev
setPlayerCmd:prev
key_id_press:next
setPlayerCmd:next
key_id_press:key_circle
setPlayerCmd:channel_next
key_id_press:like
setPlayerCmd:song_like
MCUKeyShortClick:1  MCUKeyPlay  MCUKeyCircle--  MCUKeyCircle++
setPlayerCmd:stop
setPlayerCmd:pause  setPlayerCmd:resume setPlayerCmd:play
setPlayerCmd:ext_getPlayStatus  setPlayerCmd:ext_getPlayMode
 setPlayerCmd:ext_getLoopMode
 key_id_press:mic
 /tmp/RequestASRTTS  talkstart:0 talkstop
 TtsTime TtsWeather  SetPresetNum:%d
key_id_press:voldown
setPlayerCmd:vol--  key_id_press:volup  setPlayerCmd:vol++  setPlayerCmd:slave_vol:%d
setPlayerCmd:slave_mute:%d  key_id_press:mute
setPlayerCmd:ext_vol_get
setPlayerCmd:ext_mute_get
setPlayerCmd:ext_slave_vol:%d
setPlayerCmd:ext_slave_mute:%d  setPlayerCmd:switchmode:udisk
setPlayerCmd:switchmode_by_mcu:wifi setPlayerCmd:switchmode_by_mcu:line-in  setPlayerCmd:switchmode_by_mcu:bluetooth
setPlayerCmd:switchmode_by_mcu:optical  setPlayerCmd:switchmode_by_mcu:udisk
setPlayerCmd:switchmode_by_mcu:mirror
key_id_press:mode
setPlayerCmd:switch_DAC_by_mcu:wifi 
setPlayerCmd:switch_DAC_by_mcu:line-in  
setPlayerCmd:switch_DAC_by_mcu:bluetooth
setPlayerCmd:switch_DAC_by_mcu:optical  
setPlayerCmd:switch_DAC_by_mcu:udisk
setPlayerCmd:switch_DAC_by_mcu:mirror
AirplayGet
shutdown