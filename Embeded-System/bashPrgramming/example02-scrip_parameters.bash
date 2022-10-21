###
 # @Author: Frank Linux yongfrank@outlook.com
 # @Date: 2022-10-20 15:17:16
 # @LastEditors: Frank Linux
 # @LastEditTime: 2022-10-20 16:11:31
 # @FilePath: /EE/Embeded-System/bashPrgramming/example02.bash
 # @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
### 

#!/bin/bash
# Output Explanation
echo "Information of Frank's computer" > $1

# Output Hardware Info
lscpu >> $1
uname -a >> $1
free -k >> $1

###
#  $0 is filename
#  $1 is the first parameter
#➜  bashPrgramming git:(master) ✗ ./example02.bash hi.txt     
# ./example02.bash: 19: Syntax error: word unexpected (expecting ")")
###