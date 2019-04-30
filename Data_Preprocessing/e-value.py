from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
import networkx as nx
import tkinter.font as tkFont
root = Tk()
root.geometry("420x350")
root.title('相似性计算')
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
def selectPath4():
    global file_path4
    file_path4 = filedialog.askdirectory()
    path4.set(file_path4)
def show_msg1(*args):
    val1 = numberChosen1.get()
def show_msg2(*args):
    val2 = numberChosen2.get()
def show_msg3(*args):
    val3 = numberChosen3.get()
def show_msg4(*args):
    val4 = numberChosen4.get()
def read_network(file_path):
    read_file = file_path
    style = numberChosen1.get()
    G = nx.Graph()
    f1=open(read_file,'r')
    if style=='space':
        for lines in f1.readlines():
            line=lines.rstrip().split(' ')
            G.add_edge(line[0],line[1])
    elif style=='tab':
        for lines in f1.readlines():
            line=lines.rstrip().split('\t')
            G.add_edge(line[0],line[1])
    elif style == ',':
        for lines in f1.readlines():
            line=lines.rstrip().split(',')
            G.add_edge(line[0],line[1])
    elif style == 'net':
        lines = f1.readlines()
        line = lines[0].rstrip().split(' ')
        f1.seek(0)
        node_number = int(line[1])
        for line in f1.readlines()[1:node_number + 1]:
            data = line.rstrip().split(' ')
            G.add_node(data[1])
        G_list = list(G.nodes())
        f1.seek(0)
        for line in f1.readlines()[node_number + 2:]:
            data = line.rstrip().split(' ')
            if data[0] == data[1]:
                pass
            else:
                G.add_edge(G_list[int(data[0]) - 1], G_list[int(data[1]) - 1])
    elif style == 'gw':
        lines = f1.readlines()
        line = lines[4].rstrip().split(' ')
        f1.seek(0)
        node_number = int(line[0])
        for line in f1.readlines()[5:node_number + 5]:
            data = line.rstrip().split(' ')
            node = data[0].replace('|{', '').replace('}|', '')
            G.add_node(node)
        G_list = list(G.nodes())
        f1.seek(0)
        for line in f1.readlines()[node_number + 6:]:
            data = line.rstrip().split(' ')
            if data[0] == data[1]:
                pass
            else:
                G.add_edge(G_list[int(data[0])-1], G_list[int(data[1])-1])
    return G
def similarity():
    read_file1 = file_path1
    read_file2 = file_path2
    G=read_network(read_file1)
    H=read_network(read_file2)
    select_file=file_path3
    file_s=open(select_file,'r')
    edge1 = int(numberChosen2.get())
    edge2 = int(numberChosen3.get())
    sim = int(numberChosen4.get())
    edge_1 = int(edge1) - 1
    edge_2 = int(edge2) - 1
    sim_1=int(sim)-1
    out_file=file_path4+'/'+name.get()
    f = open(out_file, 'w')
    for line in file_s.readlines():
        data = line.rstrip().split(' ')
        if data[0] in G.nodes() and data[1] in H.nodes():
            if float(data[sim_1])>1:#最后一列为value值
                data[sim_1]=1#value值大于1的，设置为1
            score=1-float(data[sim_1])#1-value作为得分
            score=float("%.12f" % score)#精度为小数点后12位
            f.write(data[edge_1] + ' ' + data[edge_2] + ' ' + str(score) + '\n')
    tkinter.messagebox.showinfo('提示', '1-evalue计算完成!')
def evalue():
    read_file1 = file_path1
    read_file2 = file_path2
    G=read_network(read_file1)
    H=read_network(read_file2)
    select_file=file_path3
    file_s=open(select_file,'r')
    out_file = file_path4+'/'+name.get()
    edge1=numberChosen2.get()
    edge2 = numberChosen3.get()
    sim=numberChosen4.get()
    edge_1=int(edge1)-1
    edge_2=int(edge2)-1
    sim_1=int(sim)-1
    f = open(out_file, 'w')
    for line in file_s.readlines():
        if ' 'not in line:
            tkinter.messagebox.showinfo('提示', '请检查相似性文件是否以空格划分!')
        else:
            data=line.rstrip().split(' ')
            if len(data)<int(sim):
                tkinter.messagebox.showinfo('提示', '请检查evalue值所在列是否正确!')
                break
            else:
                if data[0] in G.nodes() and data[1] in H.nodes():
                    f.write(data[edge_1]+' '+data[edge_2]+' '+data[sim_1]+'\n')
    tkinter.messagebox.showinfo('提示', 'evalue计算完成!')
path1 = StringVar()
path2 = StringVar()
path3 = StringVar()
path4 = StringVar()
Label(root, text="输入一个网络的文件路径:").grid(row=1, column=0)
Entry(root, textvariable=path1,state='readonly' ).grid(row=1, column=1)
Button(root, text="路径选择", command=selectPath1).grid(row=1, column=2)
Label(root, text="输入另一个网络的文件路径:").grid(row=2, column=0)
Entry(root, textvariable=path2,state='readonly' ).grid(row=2, column=1)
Button(root, text="路径选择", command=selectPath2).grid(row=2, column=2)
Label(root, text="输入包含相似性的文件路径:").grid(row=3, column=0)
Entry(root, textvariable=path3,state='readonly').grid(row=3, column=1)
Button(root, text="路径选择", command=selectPath3).grid(row=3, column=2)
Label(root, text="输出文件的文件夹路径:").grid(row=4, column=0)
Entry(root, textvariable=path4,state='readonly').grid(row=4, column=1)
Button(root, text="路径选择", command=selectPath4).grid(row=4, column=2)
Label(root, text="输出文件的名称:").grid(row=5, column=0)
name=Entry()
name.grid(row=5, column=1)
Label(root, text="请选择网络文件的格式").grid(row=7, column=0)
number1 = StringVar()
numberChosen1 = ttk.Combobox(root, width=12, textvariable=number1,state='readonly')
numberChosen1['values'] = ('space', 'tab', ',', 'net', 'gw')     # 设置下拉列表的值
numberChosen1.grid(row=7,column=1)      # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen1.current(1)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
numberChosen1.bind("<<ComboboxSelected>>", show_msg1)
number2 = StringVar()
numberChosen2 = ttk.Combobox(root, width=12, textvariable=number2,state='readonly')
numberChosen2['values'] = ('1', '2','3','4','5','6','7','8','9','10')     # 设置下拉列表的值
numberChosen2.grid(row=8,column=1)      # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen2.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
numberChosen2.bind("<<ComboboxSelected>>", show_msg2)
number3 = StringVar()
numberChosen3 = ttk.Combobox(root, width=12, textvariable=number3,state='readonly')
numberChosen3['values'] = ('1', '2','3','4','5','6','7','8','9','10')    # 设置下拉列表的值
numberChosen3.grid(row=9,column=1)      # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen3.current(1)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
numberChosen3.bind("<<ComboboxSelected>>", show_msg3)
number4 = StringVar()
numberChosen4 = ttk.Combobox(root, width=12, textvariable=number4,state='readonly')
numberChosen4['values'] = ('1', '2','3','4','5','6','7','8','9','10')     # 设置下拉列表的值
numberChosen4.grid(row=10,column=1)      # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen4.current(6)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
numberChosen4.bind("<<ComboboxSelected>>", show_msg4)
Label(root,text='相似文件中一条边所在的列数').grid(row=8,column=0)
Label(root,text='相似文件中另一条边所在的列数').grid(row=9,column=0)
Label(root,text='e_value所在的列数').grid(row=10,column=0)
ttk.Button(root, text="e_value", command=evalue).grid(row=11,column=0)  # 创建一个按钮
ttk.Button(root, text="1-e_value", command=similarity).grid(row=11,column=1)  # 创建一个按钮
root.mainloop()