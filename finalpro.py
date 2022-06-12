#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import numpy as np
from powell import *


# In[2]:


sport=tk.Tk()
sport.title('漸增性運動最佳化')
sport.geometry('800x700')


# In[3]:


frame1 = tk.Frame(sport)
frame1.grid(row=0 , column=0 ,sticky='w')
frame2 = tk.Frame(sport)
frame2.grid(row=1 , column=0 ,sticky='w')
frame3 = tk.Frame(sport)
frame3.grid(row=2 , column=0 ,sticky='w')
frame4 = tk.Frame(sport)
frame4.grid(row=3 , column=0 ,sticky='w')
frame5 = tk.Frame(sport)
frame5.grid(row=4 , column=0 ,sticky='w')
frame6 = tk.Frame(sport)
frame6.grid(row=5 , column=0 ,sticky='w')
frame7 = tk.Frame(sport)
frame7.grid(row=6 , column=0 ,sticky='w')
frame8 = tk.Frame(sport)
frame8.grid(row=7 , column=0 ,sticky='w')
frame9 = tk.Frame(sport)
frame9.grid(row=8 , column=0 ,sticky='w')


# In[4]:


label1 = tk.Label(frame1,text='你想要在',font=('Arial',12))
label1.grid(row = 0,column = 0,padx = 10,pady = 10,sticky='w')
text1 = tk.Text(frame1,width = 10,height = 1)
text1.grid(row = 0,column = 1,padx = 10,pady = 10)
label2 = tk.Label(frame1,text='週內，達到原先運動量的',font=('Arial',12))
label2.grid(row = 0,column = 2,padx = 10,pady = 10,sticky='w')
text2 = tk.Text(frame1,width = 10,height = 1)
text2.grid(row = 0,column = 3,padx = 10,pady = 10)
label3 = tk.Label(frame1,text='%',font=('Arial',12))
label3.grid(row = 0,column = 4,padx = 10,pady = 10,sticky='w')


# In[5]:


label4 = tk.Label(frame2,text='! 建議 : 週數小於等於五週 !',font=('Arial',12))
label4.grid(row = 0,column = 0,padx = 10,pady = 10,sticky='w')
label5 = tk.Label(frame2,text='請評估自己的身體素質 :',font=('Arial',12))
label5.grid(row = 1,column = 0,padx = 10,pady = 10,sticky='w')
button1 = tk.Button(frame2,width = 25,text = '身體素質強(平常有在運動)',font=('Arial',12),command=lambda:Button1_on())
button1.grid(row = 1,column = 1,padx = 10,pady = 10)
button2 = tk.Button(frame2,width = 25,text = '身體素質低(平常沒在運動)',font=('Arial',12),command=lambda:Button2_on())
button2.grid(row = 1,column = 2,padx = 10,pady = 10)


# In[6]:


#身體素質強的人
def Button1_on ():             
    global week, percent
    week = int(((text1.get("1.0","end")).replace(" ","")).replace("\n",""))
    percent = int(((text2.get("1.0","end")).replace(" ","")).replace("\n",""))
    y = (-0.4167*week**4)+(5.83338*week**3)+(-29.5833*week**2)+(74.1667*week)
    #如果他希望的程度超出建議值，仍讓結果靠近他自己的期望
    if(percent>y):
        Calculate_c()
    #如果他希望的程度低於建議值，則讓結果靠近建議值
    else:
        Calculate_s()
    
#身體素質弱的人
def Button2_on ():
    global week, percent
    week = int(((text1.get("1.0","end")).replace(" ","")).replace("\n",""))
    percent = int(((text2.get("1.0","end")).replace(" ","")).replace("\n",""))
    y = (-0.4167*week**4)+(5.83338*week**3)+(-29.5833*week**2)+(74.1667*week)
    #如果他希望的程度超出建議值，則讓結果靠近建議值
    if(percent>y):
        Calculate_s()
    #如果他希望的程度低於建議值，仍讓結果靠近他自己的期望
    else:
        Calculate_c()


# In[7]:


def F_c(x):             #跟自訂的相似(Customize)
    lam = 0.01
    c = (-0.4167*x[0]**4)+(5.83338*x[0]**3)+(-29.5833*x[0]**2)+(74.1667*x[0])-x[1]
    return (x[0]-week)**2 + (x[1]-percent)**2 + lam*c**2

def Calculate_c():
    xStart = np.array([0,0])
    xMin,nIter = powell(F_c,xStart)
    lam = 0.01
    c = (-0.4167*xMin[0]**4)+(5.83338*xMin[0]**3)+(-29.5833*xMin[0]**2)+(74.1667*xMin[0])-xMin[1]
    
    while(round(xMin[0])==0):
        xMin[0]+=1
    
    label5 = tk.Label(frame3,text=('建議您在',round(xMin[0]),'週內增加運動量到原先運動量的',round(xMin[1]),'%'),font=('Arial',12))
    label5.grid(row = 0,column = 0,padx = 10,pady = 10,sticky='w')
    
    
def F_s(x):             #跟建議的相似 (suggest)
    lam = 800
    c = (-0.4167*x[0]**4)+(5.83338*x[0]**3)+(-29.5833*x[0]**2)+(74.1667*x[0])-x[1]
    return (x[0]-week)**2 + (x[1]-percent)**2 + lam*c**2

def Calculate_s():
    xStart = np.array([0,0])
    xMin,nIter = powell(F_s,xStart)
    lam = 800
    c = (-0.4167*xMin[0]**4)+(5.83338*xMin[0]**3)+(-29.5833*xMin[0]**2)+(74.1667*xMin[0])-xMin[1]
    while(round(xMin[0])==0):
        xMin[0]+=1
    
    label6 = tk.Label(frame3,text=('建議您在',round(xMin[0]),'週內增加運動量到原先運動量的',round(xMin[1]),'%'),font=('Arial',12))
    label6.grid(row = 0,column = 0,padx = 10,pady = 10,sticky='w')


# In[8]:


#算要吃多少健康蛋白質
label7 = tk.Label(frame4,text='你的體重',font=('Arial',12))
label7.grid(row = 0,column = 0,padx = 10,pady = 10,sticky='w')
text3 = tk.Text(frame4,width = 10,height = 1)
text3.grid(row = 0,column = 1,padx = 10,pady = 10)
label7 = tk.Label(frame5,text='你的今日活動量',font=('Arial',12))
label7.grid(row = 0,column = 0,padx = 10,pady = 10,sticky='w')
button4 = tk.Button(frame5,width = 10,text = '一般',font=('Arial',12),command=lambda:Button4_on())
button4.grid(row = 0,column = 1,padx = 10,pady = 10)
button5 = tk.Button(frame5,width = 10,text = '中度活動量',font=('Arial',12),command=lambda:Button5_on())
button5.grid(row = 0,column = 2,padx = 10,pady = 10)
button5 = tk.Button(frame5,width = 10,text = '高度活動量',font=('Arial',12),command=lambda:Button6_on())
button5.grid(row = 0,column = 3,padx = 10,pady = 10)
button3 = tk.Button(frame5,width = 25,text = '你今天應該吃多少蛋白質',font=('Arial',12),command=lambda:Button3_on())
button3.grid(row = 1,column = 0,padx = 10,pady = 10)


# In[9]:


def Button3_on ():
    label7 = tk.Label(frame6,text=('你應該吃',int(kg),'克蛋白質'),font=('Arial',12))
    label7.grid(row = 0,column = 0,padx = 10,pady = 10,sticky='w')


# In[10]:


def Button4_on ():   #一般
    global kg
    kg = int(((text3.get("1.0","end")).replace(" ","")).replace("\n",""))
    kg = 0.8*kg
def Button5_on ():   #中度活動量
    global kg
    kg = float(((text3.get("1.0","end")).replace(" ","")).replace("\n",""))
    kg = 1.2*kg
def Button6_on ():   #高度活動量
    global kg
    kg = float(((text3.get("1.0","end")).replace(" ","")).replace("\n",""))
    kg = 1.6*kg


# In[11]:


label8 = tk.Label(frame6,text='選你想吃的健康蛋白質',font=('Arial',12))
label8.grid(row = 1,column = 0,padx = 10,pady = 10,sticky='w')
button6 = tk.Button(frame7,width = 10,text = '一顆蛋',font=('Arial',12),command=lambda:Button6_on())
button6.grid(row = 0,column = 0,padx = 10,pady = 10)
button7 = tk.Button(frame7,width = 10,text = '半塊豆腐',font=('Arial',12),command=lambda:Button7_on())
button7.grid(row = 0,column = 1,padx = 10,pady = 10)
button8 = tk.Button(frame7,width = 10,text = '一杯豆漿',font=('Arial',12),command=lambda:Button8_on())
button8.grid(row = 0,column = 2,padx = 10,pady = 10)
button9 = tk.Button(frame7,width = 10,text = '一片雞胸',font=('Arial',12),command=lambda:Button9_on())
button9.grid(row = 0,column = 3,padx = 10,pady = 10)
button10 = tk.Button(frame7,width = 10,text = '一隻雞腿',font=('Arial',12),command=lambda:Button10_on())
button10.grid(row = 1,column = 0,padx = 10,pady = 10)
button11 = tk.Button(frame7,width = 10,text = '一片鮭魚',font=('Arial',12),command=lambda:Button11_on())
button11.grid(row = 1,column = 1,padx = 10,pady = 10)
button12 = tk.Button(frame7,width = 10,text = '100克毛豆',font=('Arial',12),command=lambda:Button12_on())
button12.grid(row = 1,column = 2,padx = 10,pady = 10)
button13 = tk.Button(frame7,width = 10,text = '一紙杯牛奶',font=('Arial',12),command=lambda:Button13_on())
button13.grid(row = 1,column = 3,padx = 10,pady = 10)
button14 = tk.Button(frame8,width = 10,text = '結算',font=('Arial',12),command=lambda:Button14_on())
button14.grid(row = 0,column = 0,padx = 10,pady = 10)


# In[12]:


def Button6_on ():
    global kg
    kg -= 6
def Button7_on ():
    global kg
    kg -= 7
def Button8_on ():
    global kg
    kg -= 10
def Button9_on ():
    global kg
    kg -= 25
def Button10_on ():
    global kg
    kg -= 20
def Button11_on ():
    global kg
    kg -= 24
def Button12_on ():
    global kg
    kg -= 12
def Button13_on ():
    global kg
    kg -= 10
def Button14_on ():
    global kg
    if(kg<0):
        label8 = tk.Label(frame9,text=('你攝取過量了，超過',abs(kg),'克'),font=('Arial',12))
        label8.grid(row = 0,column = 0,padx = 10,pady = 10,sticky='w')
    else:
        label9 = tk.Label(frame9,text=('你攝取不足，還差',kg,'克'),font=('Arial',12))
        label9.grid(row = 0,column = 0,padx = 10,pady = 10,sticky='w')


# In[13]:


sport.mainloop()


# In[ ]:




