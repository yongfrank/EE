###
 # @Author: Frank Linux
 # @Date: 2022-10-21 16:05:11
 # @LastEditors: Frank Linux
 # @LastEditTime: 2022-10-21 16:10:33
 # @FilePath: /EE/Embeded-System/bashPrgramming/lectureExercise.bash
 # @Description: 
 # 
 # Copyright (c) 2022 by Frank Linux, All Rights Reserved. 
### 
#!/bin/bash

for i in `seq 1 1 10`
do
    rm file$i
    touch file$i
    echo This file is file$i >> file$i
done
