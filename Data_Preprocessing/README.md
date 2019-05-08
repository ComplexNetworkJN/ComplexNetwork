# 该文件夹集合了各种工具、脚本，用以对输入文件的格式进行转换
***
## 网络文件格式包括    ： net, gw,     el

## 相似性文件格式包括  ： txt, align,  sim


### all_similarity<br>
    - 用来set某两物种的全部protein pair的相似性为1
    - eg: 
        - A={a1,a2},B={b1,b2,b3}
        - 需要在A-B.sim中 写 2*3 行
        - line1: a1\tb1\t1
        - line2: a1\tb2\t1
        ...
    - 平均每个文件4.5G大小

