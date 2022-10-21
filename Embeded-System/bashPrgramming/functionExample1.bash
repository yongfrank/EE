###
 # @Author: Frank Linux
 # @Date: 2022-10-20 16:39:57
 # @LastEditors: Frank Linux
 # @LastEditTime: 2022-10-20 16:40:28
 # @FilePath: /EE/Embeded-System/bashPrgramming/functionExample1.bash
 # @Description: 
 # 
 # Copyright (c) 2022 by Frank Linux, All Rights Reserved. 
### 
#!/bin/bash
# Define Function my_info
function my_info() {
    lscpu >> log
    uname -a >> log
    free -h >> log
}

# use function
my_info