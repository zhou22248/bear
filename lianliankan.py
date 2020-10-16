import random
import math

#建一个随机列表，存放地图里的元素
list1 = []
for i in range(0,50):
    r = random.randint(0,9)
    list1.append(r)
    list1.append(r)
random.shuffle(list1)   #将1到9的数字打乱放入地图

#建地图
map1 = []
map2 = []
list2 = []
for i in range(0,10):
    map1 += [0]
for i in range(0,100,10):
    k = int(i/10)
    map2 = list1[i:i+10]
    map1[k] = map2
for i in range(0,10):
    list2.append("")
map1.insert(0,list2)
map1.append(list2)
for i in range(0,12):
    map1[i].insert(0,"")
    map1[i].append("")
#map1为10*10的地图，序号从1~10，最外面一圈是""


r =l =u =d =1
go1 = 1
go2 = 1
go3 = 1
list1 = []
list2 = []
mylist1 = []
mylist2 = []




#寻找点（x1,y1）附近的空白点，并将坐标存入列表list1
def judgepoint(x1,y1):
    global list1,list2,map1,r,l,u,d
    list1 = []
    list2 = []
    r = l = u = d = 1
    for i in range(1,12):
        if (x1+i)<=11:
            if (map1[x1+i][y1] == "")&(d == 1):
                list2 = [x1+i,y1]
                list1.append(list2)
            else:
                d = 0
        else:
            d = 0
    for i in range(1,12):
        if (x1-i)>=0:
            if (map1[x1-i][y1] == "")&(u == 1):
                list2 = [x1-i,y1]
                list1.append(list2)
            else:
                u = 0
        else:
            u = 0
    for i in range(1,12):
        if (y1+i)<=11:
            if (map1[x1][y1+i] == "")&(r == 1):
                list2 = [x1,y1+i]
                list1.append(list2)
            else:
                r = 0
        else:
            r = 0
    for i in range(1,12):
        if (y1-i)>=0:
            if (map1[x1][y1-i] == "")&(l == 1):
                list2 = [x1,y1-i]
                list1.append(list2)
            else:
                l = 0
        else:
            l = 0


for i in range(12):
    print(map1[i])

count=0
while(count < 50):
    x1 = input("请输入坐标x1:")
    y1 = input("请输入坐标y1:")
    x2 = input("请输入坐标x2:")
    y2 = input("请输入坐标y2:")
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    go1 = 1#表示用一条直线即可完成连接
    go2 = 1#表示用两条
    go3 = 1#用三条
    if map1[x1][y1] == map1[x2][y2]:    #先判断输入的两个坐标对应的值是否相等
        if (x1 <= 11)&(x1 >=0)&(y1 >= 0)&(y1 <= 11):
            if go1 == 1:        #一条直线的情况
                if (int(math.fabs(x1-x2)) == 1)&(y1 == y2):
                    map1[x1][y1]=map1[x2][y2]=""
                    go2 = go3 = 0
                if (int(math.fabs(y1-y2)) == 1)&(x1 == x2):
                    map1[x1][y1]=map1[x2][y2]=""
                    count += 1
                    go2 = go3 = 0

            if go2 == 1:        #两条直线的情况
                judgepoint(x1,y1)
                list3 = list1
                judgepoint(x2,y2)
                for i in range(len(list1)):
                    for k in range(len(list3)):
                        if (i <= (len(list1)-1))&(k <= (len(list3)-1)):
                            if list1[i]==list3[k]:
                                map1[x1][y1]=map1[x2][y2]=""
                                count += 1
                                go3 = 0
                                break
            if go3 == 1:        #三条直线的情况
                judgepoint(x1,y1)
                list3 = list1
                judgepoint(x2,y2)
                list4 = list1
                mylist1 = []
                #以点（x1,y1）周围空白点为坐标进行第二次寻找空白点
                for i in range(len(list3)):
                    judgepoint(list3[i][0],list3[i][1])
                    mylist1 += list1
                #遍历列表，与点(x2,y2)形成的列表进行比较，寻找交叉点
                for i in range(len(mylist1)):
                    for k in range(len(list4)):
                        if (i <= (len(mylist1)-1))&(k <= (len(list4)-1)):
                            if mylist1[i]==list4[k]:
                                map1[x1][y1]=map1[x2][y2]=""
                                count += 1
                                mylist1 = []
                                break
            for i in range(12):
                print(map1[i])
        else:
            print("越界了")
    else:
        print("不对哦")
if (count==50):
    print("YOU WIN!!!")


