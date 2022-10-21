###
 # @Author: Frank Linux
 # @Date: 2022-10-20 17:23:47
 # @LastEditors: Frank Linux
 # @LastEditTime: 2022-10-20 17:31:14
 # @FilePath: /EE/Embeded-System/bashPrgramming/switchExample1.bash
 # @Description: 
 # 
 # Copyright (c) 2022 by Frank Linux, All Rights Reserved. 
### 
#!/bin/bash

var=`whoami`
# 赋值就是把文本World存入名为var的变量
# 根据bash的语法，赋值 符号的左右不留空格
# 赋值符号右边的文本内容会存入赋值符号左边的变量中
if [ var="apple" ]
then
    echo "You are root"
    echo "You are my God."
fi