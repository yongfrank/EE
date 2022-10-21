###
 # @Author: Frank Linux
 # @Date: 2022-10-20 17:36:25
 # @LastEditors: Frank Linux
 # @LastEditTime: 2022-10-20 17:38:44
 # @FilePath: /EE/Embeded-System/bashPrgramming/switchExample3.bash
 # @Description: 
 # 
 # Copyright (c) 2022 by Frank Linux, All Rights Reserved. 
### 

#!/bin/bash

var=`whoami`
echo $var
if [ $var="root" ]
then
    echo "You are my God."
else
    if [ $var="parallels"]
    then 
        echo "You are a happy user"
    else 
        echo "You are the others."
    fi
fi