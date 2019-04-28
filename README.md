# Web Radio for Rasberry PI or similar

## Description

## Hardware setup

## Software setup 

I have used Bananna PI with Ubuntu Server, but it will work in the same way in all Rasberry PIs. Depending on the OS you may have slight differences

- Install MPD 
```
sudo apt-get install mpc mpd alsa-utils
```
- **Create your Playlist** or use example in *./sources/radio.m3u*
- **Playlist install** Copy the playlist file in  */var/lib/mpd/playlists/radio.m3u* on your Rasberry
- **HDMI Output** If you want to use HDMI audio output, then copy file *./sources/asound.conf* to */etc/asound.conf*.Otherwise you will use the analog output. I recommend HDMI since provides better sound quality
- **Conrol programm** Copy *./sources/webradio_control.py* to */home/pi/webradio_control.py* on your RPI (Rasberry PI) 
- **Create Service** Copy *./sources/init-radio.service* to */etc/systemd/system/init-radio.service* on your PRI  
- **Init the service** to start on boot with `service init-radio enable`. You can manage it with  `service init-radio start|stop|status`

