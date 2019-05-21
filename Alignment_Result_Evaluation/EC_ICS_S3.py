from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import networkx as nx
import tkinter.font as tkFont
import linecache
root = Tk()
root.geometry("450x400")
root.title('比对衡量')
def selectPath1():
    global file_path1
    file_path1 = filedialog.askopenfilename()
    path1.set(file_path1)
def selectPath2():
    global file_path2
    file_path2 = filedialog.askopenfilename()
    path2.set(file_path2)
def selectPath3():
    global file_path3
    file_path3 = filedialog.askopenfilename()
    path3.set(file_path3)
def readgraph(filename):
    G = nx.Graph()
    line=linecache.getline(filename,5)
    data=line.strip('\n').split(' ')
    node_num=int(data[0])
    G_list=[]
    f = open(filename, "r")
    for nodes in f.readlines()[5:5+node_num]:
        node=nodes.rstrip('\n').replace('|{','').replace('}|','')
        G.add_node(node)
        G_list.append(node)
    f.seek(0)
    for line in f.readlines()[node_num+6:]:
        data = line.rstrip().split(' ')
        if data[0]!=data[1]:
            edge1=int(data[0])-1
            edge2 = int(data[1]) - 1
            G.add_edge(G_list[edge1],G_list[edge2])
    f.seek(0)
    return G
def click():
    G1 = readgraph(file_path1)  # 图1
    G2 = readgraph(file_path2)  # 图2
    G1_list = []  # 二分图左图,E1
    G2_list = []  # 二分图右图,E2
    # 比对结果放在两个列表内
    FE=0
    file = open(file_path3, "r")
    for line in file.readlines():
        data = line.strip().split(' ')
        G1_list.append(data[0])
        G2_list.append(data[1])


    for G1_edge in G1.edges():
        m=G1_list.index(G1_edge[0])
        n=G1_list.index(G1_edge[1])
        if (G2_list[m],G2_list[n]) in G2.edges() or (G2_list[n],G2_list[m]) in G2.edges():
            FE +=1
    EC = FE / len(G1.edges())
    ################################################
    # ICS
    for i in G2.nodes():
        if i not in G2_list:
            G2.remove_node(i)
    EG = G2.number_of_edges()
    ICS = FE / EG
    S3 = FE / (G1.number_of_edges() + EG - FE)
    ec.set(EC)
    ics.set(ICS)
    s3.set(S3)

path1 = StringVar()
path2 = StringVar()
path3 = StringVar()

ec = StringVar()
ics = StringVar()
s3= StringVar()
ft = tkFont.Font(family='Fixdsys', size=15, weight=tkFont.BOLD)
Label(root, text="请选择小网络文件路径(gw格式):").grid(row=1, column=0)
Entry(root, textvariable=path1,state='readonly').grid(row=1, column=1)
Button(root, text="路径选择", command=selectPath1).grid(row=1, column=2)
Label(root, text="请选择大网络文件路径(gw格式):").grid(row=2, column=0)
Entry(root, textvariable=path2,state='readonly').grid(row=2, column=1)
Button(root, text="路径选择", command=selectPath2).grid(row=2, column=2)
Label(root, text="请选择比对结果文件的路径(txt格式):").grid(row=3, column=0)
Entry(root, textvariable=path3,state='readonly').grid(row=3, column=1)
Button(root, text="路径选择", command=selectPath3).grid(row=3, column=2)

Button(root, text="measure", command=click).grid(row=4, column=1)

Label(root, text="EC:").grid(row=5, column=0)
Entry(root, textvariable=ec, state='readonly').grid(row=5, column=1)
Label(root, text="ICS:").grid(row=6, column=0)
Entry(root, textvariable=ics, state='readonly').grid(row=6, column=1)
Label(root, text="S3:").grid(row=7, column=0)
Entry(root, textvariable=s3, state='readonly').grid(row=7, column=1)

root.mainloop()