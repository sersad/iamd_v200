http://192.168.1.182//httpapi.asp?command=setPlayerCmd:play:http://nashe1.hostingradio.ru/nashe-256


httpapi.asp?command=setPlayerCmd:play:  - вызов команды
 
http://1.stream.laut.fm/celtic-rock - адрес аудиопотока или файла для проигрывания

Остановка делается с помощью следующего запроса:
http://172.16.1.11/httpapi.asp?command=setPlayerCmd:stop


httpapi.asp?command=getPlayerStatus
Выдает код в JSON, в котором при желании можно увидеть
"status":"play","curpos":"28591" - статус и время в миллисекундах с начала воспроизведения.

https://www.diyaudio.com/forums/class-d/302748-am-v200-wifi.html#post4964189


#EXTM3U
#EXTINF:0,Наше Радио
http://variant.fm:8000/NASHE-192

#EXTINF:0,Наше Радио 128
http://nashe1.hostingradio.ru:80/nashe-128.mp3

#EXTINF:2,НАШЕ Радио 256kbps
http://nashe1.hostingradio.ru/nashe-256

#EXTINF:0,Ретро FM
http://retro256.streamr.ru

#EXTINF:0,Радио Мелодия
http://stream128.melodiafm.spb.ru:8000/melodia128

#EXTINF:0,Легенды FM 192kbps
http://live.legendy.by:8000/legendyfm

#EXTINF:2,Сектор - 90s 192kbps
http://89.223.45.5:8000/next-160

#EXTINF:0,Radio Jazz
http://nashe1.hostingradio.ru/jazz-128.mp3

#EXTINF:0,Relax FM 32kbps
http://ic7.101.ru:8000/a200

#EXTINF:1,Romantika 256kbps
http://ic4.101.ru:8000/v4_1

#EXTINF:0,Просто Радио 128kbps
http://89.254.163.122:8000/live

#EXTINF:2,Rock FM 256kbps
http://nashe1.hostingradio.ru/rock-256


#EXTINF:0,Радио Шансон
http://chanson.hostingradio.ru:8041/chanson256.mp3

#EXTINF:0,HITFM Златоуст
http://variant.fm:8000/RECORD-192

#EXTINF:0,Ultra FM
http://nashe1.hostingradio.ru/ultra-192.mp3

#EXTINF:0,Свое радио
http://source.hostingradio.ru:8010/svoe-320.mp3

#EXTINF:-1,Radio Record (320kbps MP3)
http://air.radiorecord.ru:8101/rr_320

#EXTINF:0,bookradio
http://bookradio.hostingradio.ru:8069/fm

#EXTINF:0,Радио Юность
http://icecast-vgtrk.cdnvideo.ru/unost_mp3_192kbps

