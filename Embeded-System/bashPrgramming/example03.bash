###
 # @Author: Frank Linux
 # @Date: 2022-10-20 16:09:29
 # @LastEditors: Frank Linux
 # @LastEditTime: 2022-10-20 16:28:46
 # @FilePath: /EE/Embeded-System/bashPrgramming/example03.bash
 # @Description: 
 # 
 # Copyright (c) 2022 by Frank Linux, All Rights Reserved. 
### 

#!/bin/bash

echo Hello
exit 1
echo World
exit 0

# 其实在脚本的末尾加一句exit 0并不必要
# 一个脚本如果正常运行完最后一句，会自动返回代码0
# 在脚本运行后，可以通过$?变量查询 脚本的返回代码:
# $./hello_world.bash
# $echo $?
# 0