<!--
 * @Author: Frank Chu
 * @Date: 2022-10-20 21:42:03
 * @LastEditors: Frank Chu
 * @LastEditTime: 2022-12-05 23:14:57
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
# or
ssh pi@raspberrypi.local
```

### SSH RSA ed25519

```bash
ssh-keygen -o -a 100 -t ed25519 -f ~/.ssh/id_ed25519
# -o output

# -a rounds
#              When saving a private key, this option specifies the
#              number of KDF (key derivation function, currently
#              bcrypt_pbkdf(3)) rounds used.  Higher numbers result in
#              slower passphrase verification and increased resistance
#              to brute-force password cracking (should the keys be
#              stolen).  The default is 16 rounds.

# -t dsa | ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa
#              Specifies the type of key to create.  The possible
#              values are “dsa”, “ecdsa”, “ecdsa-sk”, “ed25519”,
#              “ed25519-sk”, or “rsa”.

# - Specify file in which to save the key:
#     ssh-keygen -f ~/.ssh/filename

cat .ssh/id_ed25519 | ssh foobar@remote 'cat >> ~/.ssh/authorized_keys'
ssh-copy-id -i ~/.ssh/id_ed25519.pub yongfrank@franks-macbook-pro.local
ssh-copy-id -i .ssh/id_ed25519.pub foobar@remote
# -i identity_file
# - Copy the given public key to the remote:
#     ssh-copy-id -i path/to/certificate username@remote_host

# - Copy the given public key to the remote with specific port:
#     ssh-copy-id -i path/to/certificate -p port username@remote_host

```

### Raspberry Pi SSH Access Denied

[stack overflow Link](https://stackoverflow.com/questions/71804429/raspberry-pi-ssh-access-denied)

Recently, the default usre setup of Raspbian was significantly changed, rendering most existing online tutorials invalid.

In essence, the default `pi` user no longer exists, so you have to create it and set its passwod using either the official [Imager](https://www.raspberrypi.com/software/) tool or by creating a `userconf` file in the boot partition of your microSD card, which should contain a single line of text: `username:hashed-password`, replacing `username` with the name of the user you want (e.g., `pi`) and `hashed-password` with the hash of the password you want.

According to the [official guide](https://www.raspberrypi.com/news/raspberry-pi-bullseye-update-april-2022/), the easiest way to do this is by running the following in a terminal(Linux or macOS) - use OpenSSL on a Raspberry Pi that is already running - open a terminal window and enter:

```bash
# run it in Raspberry Pi terminal
echo 'raspberry' | openssl passwd -6 -stdin
# you will get
# $6$uSdJO/T1cf.0tRhI$BRXUD4TGUKNKBEPjvum2ynl.k/htXw.o7Wf8TyQw7J4KTq002JmJpshKw428FbCmhg68aLZBT7YeTK2EBCqrb0
```

This will produce what looks like a string of random characters, which is actually an encrypted version of the supplied password.

```bash
# in userconf file
$6$uSdJO/T1cf.0tRhI$BRXUD4TGUKNKBEPjvum2ynl.k/htXw.o7Wf8TyQw7J4KTq002JmJpshKw428FbCmhg68aLZBT7YeTK2EBCqrb0
```

![imager by Raspberry Pi](https://i.stack.imgur.com/8vRMw.png)

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

country=CN # replace with your country code
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
    ssid="Mi 10"
    psk="z18937905682."
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

sudo scp -r ./raspcopy pi@raspberrypi.local:/home/pi/Developer
```

## Update vs Upgrade

[sudo apt-get update vs upgrade – What is the Difference?](https://www.freecodecamp.org/news/sudo-apt-get-update-vs-upgrade-what-is-the-difference/
)

The main difference is that `sudo apt-get update` fetches the latest version of the package list from your distro's software repository, and any third-party repositories you may have configured. In other words, it'll figure out what the latest version of each package and dependency is, but will not actually download or install any of those updates.

The `sudo apt-get upgrade` command downloads and installs the updates for each outdated package and dependency on your system. But just running sudo apt-get upgrade will not automatically upgrade the outdated packages – you'll still have a chance to review the changes and confirm that you want to perform the upgrades.

## CTRL + M

[How to remove CTRL-M (^M) characters from a file in Linux](https://support.microfocus.com/kb/doc.php?id=7014821)

## New User

[How to Create a New User on Raspberry Pi](https://linuxhint.com/create-new-user-raspberry-pi/)

```bash
sudo adduser <new_username>
sudo adduser <new_username> sudo
sudo raspi-config
# Then, select the “Boot/Auto Login” option available in the “System Options”.

# Replace the “<new_username>” in the above command; in our case, we are removing the sudo password restriction for the user “linuxhint”.
echo '<username> ALL=(ALL) NOPASSWD: ALL' | sudo tee /etc/sudoers.d/010_<new_username>-nopasswd
echo 'frank ALL=(ALL) NOPASSWD: ALL' | sudo tee /etc/sudoers.d/010_frank-nopasswd
```

## GPIO

[Raspberry Pi Intro - bilibili](https://www.bilibili.com/video/BV16U4y1879Q)

[第24回 Raspberry PiのGPIOを制御する(コマンド編)](https://tool-lab.com/raspberrypi-startup-24/)

[using the GPIO command](https://forums.raspberrypi.com/viewtopic.php?t=137414)

[gpio - Command-line access to Raspberry Pi's GPIO](https://manpages.ubuntu.com/manpages/jammy/man1/gpio.1.html)

```bash
-g     Use the BCM_GPIO pins numbers rather than wiringPi pin numbers. Note: The BCM_GPIO pin numbers are always used with the export and edge commands.

read <pin>
        Read the digital value of the  given  pin  and  print  0  or  1  to  represent  the
        respective logic levels.

write <pin> <value>
        Write  the  given value (0 or 1) to the pin. You need to set the pin to output mode
        first.
```

[gpio - Command-line access to Raspberry Pi's GPIO](https://manpages.ubuntu.com/manpages/jammy/man1/gpio.1.html)

```bash
EXAMPLES

       gpio mode 4 output # Set pin 4 to output

       gpio -g mode 23 output # Set GPIO pin 23 to output (same as WiringPi pin 4)

       gpio mode 1 pwm # Set pin 1 to PWM mode

       gpio pwm 1 512 # Set pin 1 to PWM value 512 - half brightness

       gpio export 17 out # Set GPIO Pin 17 to output

       gpio export 0 in # Set GPIO Pin 0 (SDA0) to input.

       gpio -g read 0 # Read GPIO Pin 0 (SDA0)

```

```bash
pinout
gpio readall 
# gpio readall for a quick printout of your connector details


gpio -g read 4
gpio -g read 17

gpio -g mode 4 out # -g BCM Coding no -g wiringPi
gpio -g read 4
gpio -g write 4 1 

# -g     Use  the  BCM_GPIO  pins numbers rather than wiringPi pin numbers.  
            # Note:
            #   The BCM_GPIO pin numbers are always used with the export  and  edge  com‐
            #   mands.
```

## VNC

[Cannot currently show the desktop](https://blog.csdn.net/qq_43619832/article/details/124243048?spm=1001.2014.3001.5502)

【ラズパイ4】「Cannot currently show the desktop」エラーでデスクトップ画面が表示されない場合の対策

[link](https://algorithm.joho.info/raspberry-pi/cannot-currently-show-the-desktop-raspberry-pi/)

ラズベリーパイ4をVNCでリモート操作した際に「Cannot currently show the desktop」エラーでデスクトップ画面が表示されない場合があります.

これは, ラズベリーパイーを外部モニタにHDMI接続していない場合に発生します.
HDMIにモニタが接続されていない状態でラズベリーパイーを起動すると、NTSC(コンポジット)に切り替わってしまいます.
それを防ぐために、以下のように設定します.

● 以下のコマンドを実行してファイルを開きます.

```bash
sudo nano /boot/config.txt 
```

●「#hdmi_force_hotplug=1」をコメントアウトして「hdmi_force_hotplug=1」に修正し保存します.

以上.

## Socket Programming

[TCP/IP网络通信之Socket编程入门](https://www.bilibili.com/video/BV1eg411G7pW/)

[Python中的with-as用法](https://www.jianshu.com/p/c00df845323c)

```python
file = open("/tmp/foo.txt")
data = file.read() # 二是文件读取数据发生异常，没有进行任何处理。
file.close() # 这里有两个问题。一是可能忘记关闭文件句柄；
```

```python
# 下面是处理异常的加强版本：
file = open("/tmp/foo.txt")
try: 
    data = file.read()
finally:
    file.close()
```

```python
# 虽然这段代码运行良好，但是太冗长了。这时候就是with一展身手的时候了。除了有更优雅的语法，with还可以很好的处理上下文环境产生的异常。下面是with版本的代码：
with open("/tmp/foo.txt") as file:
    data = file.read()
```

[RaspberryPiとMacでSocket通信(Python3)](https://xp-cloud.jp/blog/2020/09/14/7527/)

![Socket-Mac-RaspberryPi-gif](http://xp-cloud.jp/blog/wp-content/uploads/2020/09/a9f3c804bcfc8f520f43841448c67b2d.gif)

RaspberryPiでサーバー側の実装

```python
</p>
#!/usr/bin/env python3
 
import socket
import time
 
def start():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as streamSocket:
        # 10000番ポートでサーバーを立ち上げる
        # Start a server on port 10000
        streamSocket.bind(('0.0.0.0', 10000))
        # 1クライアントだけ受け入れる
        # 1 Accept only the client
        streamSocket.listen(1)
        # クライアントからの接続待ち
        # Waiting for a connection from the client
        clientSocket, addr = streamSocket.accept()
        # クライアントへメッセージ送信
        # Send a message to the client
        clientSocket.sendall(b'from server 1st message')
        time.sleep(1)
        # クライアントへメッセージ送信
        # Send a message to the client
        clientSocket.sendall(b'from server 2st message')
        # クライアントからのメッセージ受信待ち
        # Waiting for a message from the client
        byteData = clientSocket.recv(1024)
        print(byteData)
        # クライアントからのメッセージ受信待ち
        # Waiting for a message from the client
        byteData = clientSocket.recv(1024)
        print(byteData)
 
if __name__ == "__main__":
    start()
<p>
```

Macでクライアント側の実装

```python
</p>
#!/usr/bin/python3
import socket
import time
 
def start():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as streamSocket:
        # RaspberryPiへ10000番ポートで接続
        # ラズパイはデフォルトでraspberrypi.localというPC名が設定されています
        # Raspberry Pi has a PC name called raspberrypi.local by default.
        streamSocket.connect(('raspberrypi.local', 10000))
        # サーバーからのメッセージ受信待ち
        # Waiting for messages from the server
        byteData = streamSocket.recv(1024)
        print(byteData)
        # サーバーからのメッセージ受信待ち
        byteData = streamSocket.recv(1024)
        print(byteData)
        time.sleep(1)
        # サーバーへメッセージ送信
        streamSocket.sendall(b'from client 1st message')
        time.sleep(1)
        # サーバーへメッセージ送信
        streamSocket.sendall(b'from client 2st message')
 
if __name__ == "__main__":
    start()
<p>
```

サーバー側の実行

```python
</p>
python3 MySocketServer.py
<p>
```

クライアント側の実行

```python
</p>
python3 MySocketClient.py
<p>
```

## Picture Capture / Video Recording

[Working with USB webcams on your Raspberry Pi](https://raspberrypi-guide.github.io/electronics/using-usb-webcams)

1.Setting UP USB camera

Pros and cons of a USB webcam

USB Webcams generally have inferior quality to the camera modules that connect to the CSI interface. They can also not be controlled using the raspistill and rasivid commands in the terminal neither by the picamera recording package in Python. Nevertheless, there may be reasons why you want to connect a USB camera to your Raspberry Pi, such as because of the benefit that it is much easier to set up multiple camera’s with a single Raspberry Pi (see below).

USB网络摄像头的利弊

USB网络摄像头的质量通常低于连接到CSI接口的相机模块。它们也不能使用终端中的raspistill和rasivid命令来控制，也无法通过Python中的picamera记录包来控制。尽管如此，您可能想将USB相机连接到树莓派，例如，使用单个树莓派设置多个摄像头要容易得多（见下文）。

Setting up and using a USB webcam
You can control a USB webcam both using bash in the terminal and with Python. First plugin the camera and see if the Raspberry Pi recognises it by entering lsusb in the terminal. It should show something like this:

```bash
lsusb

- output
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 003: ID 038f:6001 lihappe8 Corp. USB 2.0 Camera
Bus 001 Device 002: ID 2109:3431 VIA Labs, Inc. Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

# https://raspberrypi-guide.github.io/electronics/using-usb-webcams
sudo fswebcam output.jpg

sudo tldr fswebcam
sudo fswebcam -r 1920x1080 --no-banner output.jpg
# -r, --resolution <dimensions>
#               Set the image resolution of the source or device. 
#               The actual resolution used may differ if the source or device cannot
#               capture at the specified resolution.

#               Default is "384x288".
scp output.jpg yongfrank@franks-macbook-pro.local:~
```

2.树莓派图像、视频采集；

[How to fix raspistill ERROR: the system should be configured for the legacy camera stack](https://techoverflow.net/2022/03/14/how-to-fix-raspistill-error-the-system-should-be-configured-for-the-legacy-camera-stack/)

Recent versions of Raspbian use libcamera instead of the broadcom legacy camera API. You can capture an image using libcamera-still similarly to raspistill:

最近版本的树莓派使用了 libcamera。故可以使用 libcamera-still 代替 raspistill。

```bash
libcamera-still -o test.jpg
raspivid –o video.h264 -t 10000
```

3.用VLC做网络摄像头。

```bash
sudo apt-get install vlc
sudo raspivid -o - -t 0 -w 640 -h 360 -fps 25|cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264
```

在电脑端，打开 VLC，然后点击File->Open Networ，输入 http://raspberrypi.local:8090 查看实时网络摄像头。

## `apt-get` problem

[apt-get 报错怎么办： E: Could not get lock /var/lib/dpkg/lock - open (11: Resource temporary unavailable)](https://qiita.com/jizo/items/9496496a3156dd39d91a)

[E: Could not get lock /var/lib/dpkg/lock - open (11: Resource temporarily unavailable) [duplicate]](https://askubuntu.com/questions/346143/e-could-not-get-lock-var-lib-dpkg-lock-open-11-resource-temporarily-unavai)

## GitHub Download specific folder

Update Apr. 2021: there are a few tools created by the community that can do this for you:

Download Directory (Credits to fregante)
It has also been integrated into the excellent Refined Github chrome extension as a button in the Github web UI.
GitZip (Credits to Kino - see his answer here)
DownGit (Credits to Minhas Kamal - see his answer here)
Note: if you're trying to download a large number of files, you may need to provide a token to these tools to avoid rate limiting.