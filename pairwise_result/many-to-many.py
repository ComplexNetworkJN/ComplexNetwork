f=open('SMETANA_result_iid11.txt','r')
for lines in f.readlines():
    cat = []
    cow = []
    dog = []
    guinea_pig = []
    horse = []
    human = []
    mouse = []
    pig = []
    rabbit = []
    rat = []
    sheep = []
    c=[]
    line=lines.split(' ')
    for i in range(len(line)-1):
        if line[i][0:2]=='ca':
            cat.append(line[i])
        elif line[i][0:2]=='co':
            cow.append(line[i])
        elif line[i][0:2]=='do':
            dog.append(line[i])
        elif line[i][0:2]=='gu':
            guinea_pig.append(line[i])
        elif line[i][0:2]=='ho':
            horse.append(line[i])
        elif line[i][0:2]=='hu':
            human.append(line[i])
        elif line[i][0:2]=='mo':
            mouse.append(line[i])
        elif line[i][0:2]=='pi':
            pig.append(line[i])
        elif line[i][0:2]=='ra':
            rabbit.append(line[i])
        elif line[i][0:2]=='rt':
            rat.append(line[i])
        elif line[i][0:2]=='sh':
            sheep.append(line[i])
    c=[cat,cow,dog,guinea_pig,horse,human,mouse,pig,rabbit,rat,sheep]
    name=['ca','co','do','gu','ho','hu','mo','pi','ra','rt','sh']
    num=len(c)
    for i in range(num-1):
        for j in range(i+1,num):
            filename=name[i]+'-'+name[j]
            file=open(filename,'a+')
            for m in c[i]:
                for n in c[j]:
                    file.write(m+' '+n+'\n')


