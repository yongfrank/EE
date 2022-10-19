###
 # @Author: Frank Chu
 # @Date: 2022-10-19 18:35:47
 # @LastEditors: Frank Chu
 # @LastEditTime: 2022-10-19 18:36:03
 # @FilePath: /EE/Embeded-System/bashPrgramming/hw_info.bash
 # @Description: 
 # 
 # Copyright (c) 2022 by Frank Chu, All Rights Reserved. 
### 
#!/bin/bash

echo "Information of Frank's computer" > log
lscpu >> log
uname -a >> log
free-k >> log
