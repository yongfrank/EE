###
 # @Author: Frank Linux
 # @Date: 2022-10-21 16:02:00
 # @LastEditors: Frank Linux
 # @LastEditTime: 2022-10-21 16:02:18
 # @FilePath: /EE/Embeded-System/bashPrgramming/loopExample7.bash
 # @Description: 
 # 
 # Copyright (c) 2022 by Frank Linux, All Rights Reserved. 
### 
#!/bin/bash
total=0

for number in `seq 1 1 100`
do
    if (( $number % 3 == 0))
    then
        continue
    fi
    total=$(( $total + $number ))
done

echo $total