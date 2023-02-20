from pyscript import Element
from js import document 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# แปลงข้อมูล ถ้าเป็นตัวหนังสือจะได้ str ถ้าเป็นเลขจะได้ int,float
def check_type(type):
    try:
        if isinstance(int(type[0]),int):
            return setList_int(type)
    except:
        return setList_str(type)
# แปลงข้อมูลจาก srt --> list
def setList_int(x):
    x = str(x)+' '
    sums = []
    a = ''
    for i in x: # loop text
        if(i == ' '): # เช็คว่าเจอช่องว่างไหม
            if '.' in a : # ถ้ามี . ให้ใส่ทศนิยม
                sums.append(float(a))
            else:
                sums.append(int(a))
            a = ''
        else:
            a += i
    return sums

def setList_str(x):
    x = x+' '
    sums = []
    a = ''
    for i in x:
        if i == ' ':
            sums.append(a)
            a =''  
        else:
            a += i
    return sums

# ตัดข้อมูลของแกน X,Y ให้เท่ากัน
def lenList(x,y):
    x = x
    y = y
    while True:
        if(len(x) == len(y)):
            return x, y
        else:
            if len(x) > len(y):
                x.pop()
            else:
                y.pop()

# เรียกใช้งาน กราฟแบบเส้น 
def ok_g1(*args, **kwargs):
    x = Element('x1').value
    y = Element('y1').value

    grid = document.querySelector('#grid').checked

    title = Element('title1')
    name_x = str(Element('name_x1').value)
    name_y = str(Element('name_y1').value)
    title_graph = str(Element('title_graph1').value)

    a = check_type(x)
    b = check_type(y)
    a,b = lenList(a,b)
    x1 = np.array(a)
    y1 = np.array(b)
            
            
    fig, ax = plt.subplots()
    ax.plot(x1,y1)
    ax.set(xlabel=name_x, ylabel=name_y,title=title_graph)
    if grid:
        ax.grid()
            
    title.write(fig)

def clear1(*args, **kwargs):
    title = Element('title1')
    title.element.innerHTML = "<div id='title1'></div>"
