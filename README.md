# Web Radio for Rasberry PI

Build your Web radio for streaming on Resberry Pi (Bannan PI) in simple step by step manual. 
 
## Description

Building your own radio is much fun than buying one. Using Raberry PI (Banana PI) can be interesting also for kids to understand basic of hardware and programming. 

## Hardware setup

The result may look like thi pictur, but feel free to use  your creativity

![Front](./sources/pics/front.jpg)
![Side](./sources/pics/side.jpg)
![Back](./sources/pics/back.jpg)


### Materials
- You need two push button, like for example ![Button1](https://www.amazon.de/RUNCCI-spst-drucktastenschalter-momentary-Verriegelung-drucktastenschalter/dp/B07N1N1T7R/) or![Button](https://www.conrad.de/de/p/tru-components-tc-mt312bl-drucktaster-tastend-1-st-1589485.html) 
- Jumper wires with connectors for the Rasberry PI 
- Wooden board 
- Corks for side decoration
- Rasberry PI, OS on SD Card, HDMI, power and LAN cable  

### Steps

- 

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

