from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
import networkx as nx
import tkinter.font as tkFont
root = Tk()
root.geometry("600x400")
root.title('格式转换')
def show_msg1(*args):
    val1 = numberChosen1.get()
def show_msg2(*args):
    val2 = numberChosen2.get()
def show_msg3(*args):
    val3 = numberChosen3.get()
def show_msg4(*args):
    val4 = numberChosen4.get()
def show_msg5(*args):
    val5 = numberChosen5.get()
def selectPath1():
    global file_path1
    file_path1 = filedialog.askopenfilename()
    path1.set(file_path1)
def selectPath2():
    global file_path2
    file_path2 = filedialog.askdirectory()
    path2.set(file_path2)
def style_split(x,y,f_r, f_w):
    db = f_r.read()
    if x=='space' and y=='tab':
        if ' ' not in db:
            tkinter.messagebox.showinfo('提示', '输入文件格式不是space！')
        else:
            f_w.write(db.replace(' ', '\t'))
    elif y=='space'and x=='tab':
        if '\t' not in db:
            tkinter.messagebox.showinfo('提示', '输入文件格式不是tab！')
        else:
            f_w.write(db.replace('\t', ' '))
    elif x=='space' and y==',':
        if ' ' not in db:
            tkinter.messagebox.showinfo('提示', '输入文件格式不是space！')
        else:
            f_w.write(db.replace(' ', ','))
    elif y=='space'and x==',':
        if ',' not in db:
            tkinter.messagebox.showinfo('提示', '输入文件格式不是,！')
        else:
            f_w.write(db.replace(',', ' '))
    elif x=='tab' and y==',':
        if '\t' not in db:
            tkinter.messagebox.showinfo('提示', '输入文件格式不是tab！')
        else:
            f_w.write(db.replace('\t', ','))
    elif y=='tab'and x==',':
        if ',' not in db:
            tkinter.messagebox.showinfo('提示', '输入文件格式不是,！')
        else:
            f_w.write(db.replace(',', '\t'))
    else:
        if x not in db:
            tkinter.messagebox.showinfo('提示', '输入格式错误！')
        else:
            f_w.write(db.replace(x, y))
    f_r.close()
    f_w.close()
def style_net(x,f_r, f_w):
    G=nx.Graph()
    if x == 'space':
        for line in f_r.readlines():
            data = line.rstrip().split(' ')
            G.add_edge(data[0],data[1])
    elif x == 'tab':
        for line in f_r.readlines():
            data = line.rstrip().split('\t')
            G.add_edge(data[0],data[1])
    else:
        for line in f_r.readlines():
            data = line.rstrip().split(x)
            G.add_edge(data[0],data[1])
    if G.number_of_nodes()==0 or G.number_of_edges()==0:
        tkinter.messagebox.showinfo('提示', '输入格式错误，网络构建失败！')
    else:
        f_w.write('*Vertices ' + str(G.number_of_nodes()) + '\n')
        G_list=list(G.nodes())
        for i in range(len(G_list)):
            f_w.write(str(i+1)+' '+G_list[i]+'\n')
        f_w.write('*Edges '+str(G.number_of_edges())+'\n')
        for edge in G.edges():
            f_w.write(str(G_list.index(edge[0]) + 1)+' '+str(G_list.index(edge[1]) + 1)+'\n')
def style_gw(x,f_r, f_w):
    G=nx.Graph()
    f_w.write('LEDA.GRAPH\n')
    head1 = numberChosen3.get()
    head2 = numberChosen4.get()
    head3 = numberChosen5.get()
    f_w.write(head1 + '\n' + head2 + '\n' + head3 + '\n')
    if x == 'space':
        for line in f_r.readlines():
            data = line.rstrip().split(' ')
            if data[0] == data[1]:
                pass
            else:
                G.add_edge(data[0], data[1])
    elif x == 'tab':
        for line in f_r.readlines():
            data = line.rstrip().split('\t')
            if data[0] == data[1]:
                pass
            else:
                G.add_edge(data[0], data[1])
    else:
        for line in f_r.readlines():
            data = line.rstrip().split(x)
            if data[0] == data[1]:
                pass
            else:
                G.add_edge(data[0], data[1])
    if G.number_of_nodes()==0 or G.number_of_edges()==0:
        tkinter.messagebox.showinfo('提示', '输入格式错误！')
    else:
        N = G.number_of_nodes()
        M = G.number_of_edges()
        new_edge = []
        G_list = list(G.nodes())
        for edge in G.edges():
            new_edge.append((G_list.index(edge[0]) + 1, G_list.index(edge[1]) + 1))
        f_w.write(str(N) + '\n')
        for i in G.nodes():
            f_w.write('|' + '{' + i + '}' + '|' + '\n')
        f_w.write(str(M) + '\n')
        for edge in sorted(new_edge):
            f_w.write(str(edge[0]) + ' ' + str(edge[1]) + ' 0 |{}|\n')
def net_style(y,f_r, f_w):
    G=nx.Graph()
    lines = f_r.readlines()
    line = lines[0].split(' ')
    f_r.seek(0)
    node_number = int(line[1])
    for line in f_r.readlines()[1:node_number + 1]:
        data = line.rstrip().split(' ')
        G.add_node(data[1])
    G_list = list(G.nodes())
    f_r.seek(0)
    for line in f_r.readlines()[node_number + 2:]:
        data = line.rstrip().split(' ')
        if data[0] == data[1]:
            pass
        else:
            G.add_edge(G_list[int(data[0])-1], G_list[int(data[1])-1])
    f_r.seek(0)
    f_r.close()
    if G.number_of_nodes()==0 or G.number_of_edges()==0:
        tkinter.messagebox.showinfo('提示', '输入格式错误！')
    else:
        if y == 'space':
            for edge in G.edges():
                f_w.write(edge[0] + ' ' + edge[1] + '\n')
        elif y == 'tab':
            for edge in G.edges():
                f_w.write(edge[0] + '\t' + edge[1] + '\n')
        elif y == ',':
            for edge in G.edges():
                f_w.write(edge[0] + ',' + edge[1] + '\n')
def net_gw(f_r, f_w):
    G=nx.Graph()
    H = nx.Graph()
    f_w.write('LEDA.GRAPH\n')
    head1 = numberChosen3.get()
    head2 = numberChosen4.get()
    head3 = numberChosen5.get()
    f_w.write(head1 + '\n' + head2 + '\n' + head3 + '\n')
    lines = f_r.readlines()
    line = lines[0].rstrip().split(' ')
    f_r.seek(0)
    node_number = int(line[1])
    for line in f_r.readlines()[1:node_number + 1]:
        data = line.rstrip().split(' ')
        G.add_node(data[1])
    f_r.seek(0)
    for line in f_r.readlines()[node_number + 2:]:
        data = line.rstrip().split(' ')
        if data[0] == data[1]:
            pass
        else:
            H.add_edge(data[0], data[1])
    f_r.seek(0)
    f_r.close()
    if G.number_of_nodes()==0 or H.number_of_edges()==0:
        tkinter.messagebox.showinfo('提示', '输入格式错误，网络构建失败！')
    else:
        N = G.number_of_nodes()
        M = H.number_of_edges()
        new_edge = []
        for edge in H.edges():
            new_edge.append((edge[0], edge[1]))
        f_w.write(str(N) + '\n')
        for i in G.nodes():
            f_w.write('|' + '{' + i + '}' + '|' + '\n')
        f_w.write(str(M) + '\n')
        for edge in sorted(new_edge):
            f_w.write(str(edge[0]) + ' ' + str(edge[1]) + ' 0 |{}|\n')
def gw_style(y,f_r, f_w):
    G = nx.Graph()
    H = nx.Graph()
    lines = f_r.readlines()
    line = lines[4].split(' ')
    f_r.seek(0)
    node_number = int(line[0])
    if y=='space':
        for line in f_r.readlines()[5:node_number+5]:
            data = line.rstrip().split(' ')
            node=data[0].replace('|{', '').replace('}|', '')
            G.add_node(node)
        G_list = list(G.nodes())
        f_r.seek(0)
        for line in f_r.readlines()[node_number+6:]:
            data = line.rstrip().split(' ')
            if data[0] == data[1]:
                pass
            else:
                H.add_edge(data[0], data[1])
        f_r.seek(0)
        f_r.close()
        for edges in H.edges():
            f_w.write(G_list[int(edges[0])-1]+' '+G_list[int(edges[1])-1]+'\n')
        f_w.close()
    elif y=='tab':
        for line in f_r.readlines()[5:node_number+5]:
            data = line.rstrip().split(' ')
            node=data[0].replace('|{', '').replace('}|', '')
            G.add_node(node)
        G_list = list(G.nodes())
        f_r.seek(0)
        for line in f_r.readlines()[node_number+6:]:
            data = line.rstrip().split(' ')
            if data[0] == data[1]:
                pass
            else:
                H.add_edge(data[0], data[1])
        f_r.seek(0)
        f_r.close()
        for edges in H.edges():
            f_w.write(G_list[int(edges[0])-1]+'\t'+G_list[int(edges[1])-1]+'\n')
        f_w.close()
    else:
        for line in f_r.readlines()[5:node_number+5]:
            data = line.rstrip().split(' ')
            node=data[0].replace('|{', '').replace('}|', '')
            G.add_node(node)
        G_list = list(G.nodes())
        f_r.seek(0)
        for line in f_r.readlines()[node_number+6:]:
            data = line.rstrip().split(' ')
            if data[0] == data[1]:
                pass
            else:
                H.add_edge(data[0], data[1])
        f_r.seek(0)
        f_r.close()
        for edges in H.edges():
            f_w.write(G_list[int(edges[0])-1]+y+G_list[int(edges[1])-1]+'\n')
        f_w.close()
def gw_net(f_r, f_w):
    G=nx.Graph()
    H = nx.Graph()
    lines = f_r.readlines()
    line = lines[4].rstrip().split(' ')
    f_r.seek(0)
    node_number = int(line[0])
    for line in f_r.readlines()[5:node_number + 5]:
        data = line.rstrip().split(' ')
        node = data[0].replace('|{', '')
        node = node.replace('}|', '')
        G.add_node(node)
    G_list = list(G.nodes())
    f_r.seek(0)
    for line in f_r.readlines()[node_number + 6:]:
        data = line.rstrip().split(' ')
        if data[0] == data[1]:
            pass
        else:
            H.add_edge(data[0], data[1])
    f_r.seek(0)
    if G.number_of_nodes()==0 or H.number_of_edges()==0:
        tkinter.messagebox.showinfo('提示', '输入格式错误，网络构建失败！')
    else:
        f_w.write('*Vertices ' + str(G.number_of_nodes()) + '\n')
        for i in range(len(G_list)):
            f_w.write(str(i + 1) + ' ' + G_list[i] + '\n')
        for line in f_r.readlines()[node_number + 6:]:
            data = line.rstrip().split(' ')
            H.add_edge(data[0],data[1])
        f_w.write('*Edges ' +str(H.number_of_edges()) + '\n')
        for edge in H.edges():
            f_w.write(edge[0] + ' ' + edge[1] + '\n')
def clickMe():
    val1 = numberChosen1.get()
    val2 = numberChosen2.get()
    if val1==val2:
        tkinter.messagebox.showinfo('提示', '同种格式无需转换！')
    else:
        f_r = open(file_path1, 'r')
        f_w = open(file_path2 + '/' + name1.get(), 'w')
        if val1=='space' and val2=='tab':
            style_split(val1, val2, f_r, f_w)
            tkinter.messagebox.showinfo('提示', 'space转换tab完成！')
        elif val1=='space' and val2==',':
            style_split(val1, val2, f_r, f_w)
            tkinter.messagebox.showinfo('提示', 'space转换,完成！')
        elif val1=='space' and val2=='net':
            style_net(val1, f_r, f_w)
            tkinter.messagebox.showinfo('提示', 'space转换net完成！')
        elif val1=='space' and val2=='gw':
            style_gw(val1, f_r, f_w)
            tkinter.messagebox.showinfo('提示', 'space转换gw完成！')
        elif val1=='tab' and val2=='space':
            style_split(val1, val2, f_r, f_w)
            tkinter.messagebox.showinfo('提示', 'tab转换space完成！')
        elif val1=='tab' and val2==',':
            style_split(val1, val2, f_r, f_w)
            tkinter.messagebox.showinfo('提示', 'tab转换,完成！')
        elif val1=='tab' and val2=='net':
            style_net(val1, f_r, f_w)
            tkinter.messagebox.showinfo('提示', 'tab转换net完成！')
        elif val1=='tab' and val2=='gw':
            style_gw(val1, f_r, f_w)
            tkinter.messagebox.showinfo('提示', 'tab转换gw完成！')
        elif val1==',' and val2=='space':
            style_split(val1, val2, f_r, f_w)
            tkinter.messagebox.showinfo('提示', ',转换space完成！')
        elif val1==',' and val2=='tab':
            style_split(val1, val2, f_r, f_w)
            tkinter.messagebox.showinfo('提示', ',转换tab完成！')
        elif val1==',' and val2=='net':
            style_net(val1, f_r, f_w)
            tkinter.messagebox.showinfo('提示', ',转换net完成！')
        elif val1==',' and val2=='gw':
            style_gw(val1, f_r, f_w)
            tkinter.messagebox.showinfo('提示', ',转换gw完成！')
        elif val1=='net' and val2=='space':
            net_style(val2, f_r, f_w)
            tkinter.messagebox.showinfo('提示', 'net转换space完成！')
        elif val1=='net' and val2=='tab':
            net_style(val2, f_r, f_w)
            tkinter.messagebox.showinfo('提示', 'net转换tab完成！')
        elif val1=='net' and val2==',':
            net_style(val2, f_r, f_w)
            tkinter.messagebox.showinfo('提示', 'net转换,完成！')
        elif val1=='net' and val2=='gw':
            net_gw(f_r, f_w)
            tkinter.messagebox.showinfo('提示', 'net转换gw完成！')
        elif val1=='gw' and val2=='space':
            gw_style(val2, f_r, f_w)
            tkinter.messagebox.showinfo('提示', 'gw转换space完成！')
        elif val1=='gw' and val2=='tab':
            gw_style(val2, f_r, f_w)
            tkinter.messagebox.showinfo('提示', 'gw转换tab完成！')
        elif val1=='gw' and val2==',':
            gw_style(val2, f_r, f_w)
            tkinter.messagebox.showinfo('提示', 'gw转换,完成！')
        elif val1=='gw' and val2=='net':
            gw_net( f_r, f_w)
            tkinter.messagebox.showinfo('提示', 'gw转换net完成！')
path1 = StringVar()
path2 = StringVar()
ft = tkFont.Font(family='Fixdsys', size=15, weight=tkFont.BOLD)
Label(root, text="输入文件路径:").grid(row=1, column=0)
Entry(root, textvariable=path1,state='readonly').grid(row=1, column=1)
Button(root, text="路径选择", command=selectPath1).grid(row=1, column=2)
Label(root, text="输出文件路径:").grid(row=2, column=0)
Entry(root, textvariable=path2,state='readonly').grid(row=2, column=1)
Button(root, text="路径选择", command=selectPath2).grid(row=2, column=2)
Label(root, text="输出文件的名称:").grid(row=3, column=0)
name1=Entry()
name1.grid(row=3, column=1)

number1 = StringVar()
numberChosen1 = ttk.Combobox( width=12, textvariable=number1,state='readonly')
numberChosen1['values'] = ('space', 'tab', ',', 'net', 'gw')     # 设置下拉列表的值
numberChosen1.grid(row=4,column=0)      # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen1.current(1)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
numberChosen1.bind("<<ComboboxSelected>>", show_msg1)

Label(root,text='——转换成——>').grid(row=4,column=1)
number2 = StringVar()
numberChosen2 = ttk.Combobox(width=12, textvariable=number2,state='readonly')
numberChosen2['values'] = ('space', 'tab', ',', 'net', 'gw')     # 设置下拉列表的值
numberChosen2.grid(row=4,column=2)      # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen2.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
numberChosen2.bind("<<ComboboxSelected>>", show_msg2)
Label(root,text='注意：转换成gw格式时，',font=ft).grid(row=6,column=0)
Label(root,text='需要选择下面三行信息:',font=ft).grid(row=6,column=1)
number3 = StringVar()
numberChosen3 = ttk.Combobox(root, width=12, textvariable=number3,state='readonly')
numberChosen3['values'] = ('void', 'string', 'int', 'short', 'long')     # 设置下拉列表的值
numberChosen3.grid(row=7,column=1)      # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen3.current(1)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
numberChosen3.bind("<<ComboboxSelected>>", show_msg3)
number4 = StringVar()
numberChosen4 = ttk.Combobox(root, width=12, textvariable=number4,state='readonly')
numberChosen4['values'] = ('void', 'string', 'int', 'short', 'long')     # 设置下拉列表的值
numberChosen4.grid(row=8,column=1)      # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen4.current(2)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
numberChosen4.bind("<<ComboboxSelected>>", show_msg4)
number5 = StringVar()
numberChosen5 = ttk.Combobox(root, width=12, textvariable=number5,state='readonly')
numberChosen5['values'] = ('-1', '-2')     # 设置下拉列表的值
numberChosen5.grid(row=9,column=1)      # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen5.current(1)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
numberChosen5.bind("<<ComboboxSelected>>", show_msg5)
label_1 = Label(text='请选择节点类型：')
label_2 = Label(text='请选择边类型：')
label_3 = Label(text='请选择图类型，-1为有向图，-2为无向图：')

label_1.grid(row=7, column=0, sticky=W)  # 一个有sticky,一个没有sticky，以作区分,sticky=W依靠所在单元格的某一边角：N：北 上、E：东 右、S：南 下、W：西 左
label_2.grid(row=8, column=0, sticky=W)
label_3.grid(row=9, column=0, sticky=W)

# 按钮
ttk.Button(root, text="确认转换格式", command=clickMe).grid(row=10,column=1)  # 创建一个按钮
root.mainloop()