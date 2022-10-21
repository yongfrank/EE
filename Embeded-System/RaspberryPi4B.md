<!--
 * @Author: Frank Chu
 * @Date: 2022-10-20 21:42:03
 * @LastEditors: Frank Chu
 * @LastEditTime: 2022-10-21 10:13:22
 * @FilePath: /EE/Embeded-System/RaspberryPi4B.md
 * @Description: 
 * 
 * Copyright (c) 2022 by Frank Chu, All Rights Reserved. 
-->
# Raspberry Pi 4B

## Change Resolution to 4k@60hz

[Running your Raspberry Pi 4 at 4k60hz](https://medium.com/@monofuel34089/running-your-raspberry-pi-4-at-4k60hz-78010a26e98d)

Open terminal with `Control-Option/Alt-T`.

```bash
sudo sh -c "echo hdmi_enable_4kp60=1 >> /boot/config.txt"
```

Then, reboot your Raspberry Pi 4B

```bash
# -r reboot 
# sudo shutdown -r now == reboot
# -h halt
# sudo shutdown -h now == halt
# -s sleep
sudo shutdown -r now
```

## How to Turn on the Raspberry Pi 4B

[How To Turn On And Shutdown The Raspberry Pi [Absolute Beginner Tip]
](https://itsfoss.com/turn-on-raspberry-pi/)

If you have never used Raspberry Pi like devices, you would probably search for the power button to turn on the Raspberry Pi. Unfortunately, that’s not the case here.

The USB-C port powers the Raspberry Pi and the way you turn it on is by plugging in the power cable into the USB-C port.

If you turned it off and you want to turn it on again, you’ll have to **unplug the power cord either from the power socket (preferred) or from the power port of the board. There is no power button.**

## SSH and CLI Configuration Tool

[How to Enable and Use SSH on Raspberry Pi 4 (Raspberry Pi OS/Raspbian)](https://roboticsbackend.com/enable-ssh-on-raspberry-pi-raspbian/)

```bash
# get IP Address
hostname -I

sudo raspi-config
```

On your computer terminal `ssh username@ip_address`, default password is **raspberry**

```bash
ssh 10.203.1.218 -l pi
# or
ssh pi@10.203.1.218
```

## Make the Pi automatically connect to Wi-Fi

Here create a file named “wpa_supplicant.conf” (remove any other extension like “.txt”).

```bash
country=US # replace with your country code
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
    ssid="WIFI_NETWORK_NAME"
    psk="WIFI_PASSWORD"
    # optional: key_mgmt
    key_mgmt=WPA-PSK
    # optional: priority
    priority=10
}
```

## Copy Files

[COPYING FILES TO AND FROM RASPBERRY PI AND MAC](https://spellfoundry.com/docs/copying-files-to-and-from-raspberry-pi-and-mac/)

The simplest way is to use **S**ecure **C**o**P**y from a Terminal Window (see also “Article on Using SSH On A Mac”).

```bash
scp pi@10.203.1.244:/etc/wpa_supplicant/wpa_supplicant.conf .
open ./
```

## Update vs Upgrade

[sudo apt-get update vs upgrade – What is the Difference?](https://www.freecodecamp.org/news/sudo-apt-get-update-vs-upgrade-what-is-the-difference/
)

The main difference is that `sudo apt-get update` fetches the latest version of the package list from your distro's software repository, and any third-party repositories you may have configured. In other words, it'll figure out what the latest version of each package and dependency is, but will not actually download or install any of those updates.

The `sudo apt-get upgrade` command downloads and installs the updates for each outdated package and dependency on your system. But just running sudo apt-get upgrade will not automatically upgrade the outdated packages – you'll still have a chance to review the changes and confirm that you want to perform the upgrades.
