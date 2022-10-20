###
 # @Author: Frank Chu
 # @Date: 2022-10-19 18:35:47
 # @LastEditors: Frank Linux yongfrank@outlook.com
 # @LastEditTime: 2022-10-20 15:14:32
 # @FilePath: /EE/Embeded-System/bashPrgramming/hw_info.bash
 # @Description: 
 # 
 # Copyright (c) 2022 by Frank Chu, All Rights Reserved. 
### 
#!/bin/bash
# Output Explanation
echo "Information of Frank's computer" > log

# Output Hardware Info
lscpu >> log
uname -a >> log
free -k >> log
