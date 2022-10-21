###
 # @Author: Frank Linux
 # @Date: 2022-10-20 17:32:11
 # @LastEditors: Frank Linux
 # @LastEditTime: 2022-10-20 17:35:11
 # @FilePath: /EE/Embeded-System/bashPrgramming/switchExample2.bash
 # @Description: 
 # 
 # Copyright (c) 2022 by Frank Linux, All Rights Reserved. 
### 

#!/bin/bash
filename=$1

# if后面的"-e $filename"作为判断条件。
# 如果条件成立，即文件存 在，那么执行then后面的代码
# 如果文件不存在，那么脚本将执行else 语句中的echo命令
# 末尾的fi结束整个语法结构。脚本继续以顺序的方式执行剩余内容。运行脚本：
if [ -e $filename ] 
then
    echo "$filename exists"
else
    echo "$filename NOT exists"
fi

echo "The End"