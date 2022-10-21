###
 # @Author: Frank Linux
 # @Date: 2022-10-20 17:46:39
 # @LastEditors: Frank Linux
 # @LastEditTime: 2022-10-21 12:07:49
 # @FilePath: /EE/Embeded-System/bashPrgramming/loopExample.bash
 # @Description: 
 # 
 # Copyright (c) 2022 by Frank Linux, All Rights Reserved. 
### 
#!/bin/bash

now=`date+'%Y%m%d%H%M'`
deadline=`date --date='1 hour'+'%Y%m%d%H%M'`

while [ $now -lt $deadline ]
do
    date
    echo "not yet"
    sleep 10
    now=`date +'%Y%m%d%H%M'`
done

echo "now, deadline reached"