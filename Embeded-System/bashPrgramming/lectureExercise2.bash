###
 # @Author: Frank Linux
 # @Date: 2022-10-21 16:11:07
 # @LastEditors: Frank Linux
 # @LastEditTime: 2022-10-21 16:18:08
 # @FilePath: /EE/Embeded-System/bashPrgramming/lectureExercise2.bash
 # @Description: 
 # 
 # Copyright (c) 2022 by Frank Linux, All Rights Reserved. 
### 
time=0
while true
do
    echo ${time}s passed
    sleep 5
    time=$(( $time + 5 ))
done