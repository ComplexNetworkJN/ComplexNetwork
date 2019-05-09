# 该文件夹集合了各种工具、脚本，用以对输入文件的格式进行转换
***
## 网络文件格式包括    ： net, gw,  el

## 相似性文件格式包括  ： txt, align,  sim


### all_similarity<br>
    - 用来set某两物种的全部protein pairs的相似性为1
    - eg: 
        - A={a1,a2},B={b1,b2,b3}
        - 需要在A-B.sim中 写 2*3 行
        - line1: a1\tb1\t1
        - line2: a1\tb2\t1
        ...
    - 平均每个文件4.5G大小

### BEAMS_sim<br>
    - BEAMS 相似性文件
    - no_sim 为修改相似性文件，使值为1.0的转换文件,按提示输入相似性文件名称进行转换
    - eg:
        Input similarity file's Name:
        human-rat
        con_sim 为生成全部节点相似性为1的文件,输入生成的文件名，和物种节点数
    - eg:
        Input species' name:
        human-rat
        Input number of nodes:
        54,25     //前者为human节点数，后者为rat节点数


