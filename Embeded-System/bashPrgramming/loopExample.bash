###
 # @Author: Frank Linux
 # @Date: 2022-10-20 17:46:39
 # @LastEditors: Frank Linux
 # @LastEditTime: 2022-10-21 14:26:06
 # @FilePath: /EE/Embeded-System/bashPrgramming/loopExample.bash
 # @Description: 
 # 
 # Copyright (c) 2022 by Frank Linux, All Rights Reserved. 
### 
#!/bin/bash

now=`date +'%H%M%S'`
deadline=`date --date='20 seconds' +'%H%M%S'`

echo now is $now
echo deadline is $deadline
while [ $now -lt $deadline ]
do
    date
    echo "not yet"
    sleep 1
    now=`date +'%H%M%S'`
    echo now is $now
done

echo "now, deadline reached"