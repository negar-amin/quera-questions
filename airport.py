class plane:
    def __init__(self,status,line):
        self.status=status
        self.line=line
nk=input().split(' ')
freeband=[i for i in range(1,int(nk[1])+1)]
planes=[]
dic={input():plane(1,None)}
for i in range(int(nk[0])-1):
    dic[input()]=plane(1,None)
orders=int(input())
ol=[]
for i in range(orders):
    o=input().split(' ')
    if o[1] not in dic:
        dic[o[1]]=plane(4,None)
    ol.append(o)
for i in range(len(ol)):
    if ol[i][0]=="TAKE-OFF":
        if dic[ol[i][1]].status==1 and len(freeband)==0:
            print('NO FREE BOUND')
        elif dic[ol[i][1]].status==2:
            print('YOU ARE TAKING OFF')
        elif dic[ol[i][1]].status==3:
            print('YOU ARE LANDING NOW')
        elif dic[ol[i][1]].status==4:
            print('YOU ARE NOT HERE')
        else:
            m=min(freeband)
            dic[ol[i][1]].status = 2
            dic[ol[i][1]].line = m
            freeband.remove(m) 
    if ol[i][0]=="LANDING":
        if dic[ol[i][1]].status==1:
            print('YOU ARE HERE')
        elif dic[ol[i][1]].status==2:
            print('YOU ARE TAKING OFF')
        elif dic[ol[i][1]].status==3:
            print('YOU ARE LANDING NOW')
        elif dic[ol[i][1]].status==4 and len(freeband)==0:
            print('NO FREE BOUND')
        else:
            m=max(freeband)
            dic[ol[i][1]].status=3
            dic[ol[i][1]].line=m
            freeband.remove(m) 
    if ol[i][0]=="PLANE-STATUS":
        print(dic[ol[i][1]].status)
    if ol[i][0]=="BAND-STATUS":
        if int(ol[i][1])in freeband:
            print("FREE")
        for k in dic.keys():
            if dic[k].line==int(ol[i][1]):
                print(k)
                break
            
    