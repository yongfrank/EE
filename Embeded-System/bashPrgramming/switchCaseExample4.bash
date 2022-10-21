###
 # @Author: Frank Linux
 # @Date: 2022-10-20 17:39:16
 # @LastEditors: Frank Linux
 # @LastEditTime: 2022-10-20 17:46:09
 # @FilePath: /EE/Embeded-System/bashPrgramming/switchCaseExample4.bash
 # @Description: 
 # 
 # Copyright (c) 2022 by Frank Linux, All Rights Reserved. 
### 
#!/bin/bash

# 这个脚本和上面的demo_nest.bash功能完全相同
# 可以看到 case 结构与 if 结构的区别
# 关键字case后面不再是逻辑表达式，而是一个作为条件的文本
# 后面的代码块分为三个部分，都以文本标签的形式开始，以;;结束
# case ... in
# text)
#   something
# ;;
# esac
# case结构运行时会逐个检查文本标签。当条件文本和文本标签对应时
# bash就会执行隶属于该文本标签的代码块。如果是用户vamei执行该bash脚本
# 那么条件文本和vamei标签对应上，脚本就会打印:
var=`whoami`
echo "You are $var"

case $var in
root)
    echo "You are God."
;;
parallels)
    echo "You are happy user."
;;
*)
echo "You are the Others."
;;
esac

# 文本标签除了是一串具体的文本
# 还可以包含文本通配符
# 结构 case 中常用的通配符，如表20-1所示。