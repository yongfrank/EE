#!/bin/bash
###
 # @Author: Frank Chu
 # @Date: 2022-10-29 18:15:39
 # @LastEditors: Frank Chu
 # @LastEditTime: 2022-10-29 18:15:41
 # @FilePath: /EE/Embeded-System/GPIO/led.sh
 # @Description: 
 # 
 # Copyright (c) 2022 by Frank Chu, All Rights Reserved. 
### 

# printing EXPORT PIN Number
echo Exporting pin $1

# when input pin number to export, there will be an file called gpio21
echo $1 > /sys/class/gpio/export

echo Setting direction to out.
echo out > /sys/class/gpio/gpio$1/direction

# High/Low Volt to GPIO21, PIN 40
echo Setting GPIO21-PIN40 to $2, Ground is PIN39.
echo $2 > /sys/class/gpio/gpio$1/value