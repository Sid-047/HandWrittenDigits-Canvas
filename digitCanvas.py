import os
import cv2
import glob
import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
from colorama import Fore, Style
from PIL import Image, ImageDraw

a=0
tk=Tk()
img_l_=[]
if not os.path.isdir("testDigits"):
   os.makedirs("testDigits")
os.chdir("testDigits")
img_l=glob.glob("*.jpg")
for i in img_l:
    try:
        img_l_.append(int(i.split(".")[0]))
    except:
        pass
img_l_.sort()

if len(img_l_)==0:
    a=0
else:
    a=img_l_[len(img_l_)-1]+1

tk.title("Digit - "+str(a)[-1])
c=Canvas(tk, width=280, height=280, bg='black')
c.pack(expand=NO)

img = Image.new("L", (280, 280), "black")
draw = ImageDraw.Draw(img)

def fig(event):
    x1,y1=(event.x-15),(event.y-15)
    x2,y2=(event.x+15),(event.y+15)
    c.create_oval(x1+4, y1+4, x2+4, y2+4, fill='#dadada', outline='#dadada', tags='overlay')
    draw.ellipse([x1+4, y1+4, x2+4, y2+4], fill='#dadada', outline='#dadada')
    c.create_oval(x1, y1, x2, y2, fill='white', outline='white', tags='overlay_')
    draw.ellipse([x1, y1, x2, y2], fill='white', outline='white')

def del_con(event):
    tk.title("Digit - "+str(a)[-1])
    plt.close('all')
    c.delete('overlay_')
    c.delete('overlay')

def img_con(event):
    global a
    global ar

    outImg = str(a)+'.jpg'
    print(Fore.BLUE+Style.BRIGHT+"---->"+outImg+Fore.RESET)
    img_ar = np.array(img)
    print('----------------->',img_ar.shape)
    plt.imshow(img_ar, cmap='gray')
    plt.show(block=False)
    img.save(outImg)
    
    img=cv2.imread(str(a)+'.jpg', cv2.IMREAD_GRAYSCALE)
    print(Fore.BLUE+Style.BRIGHT+str(np.shape(img))+Fore.RESET)
    img_=cv2.resize(img, dsize=(28,28), interpolation=cv2.INTER_AREA)
    print(np.shape(img_))
    cv2.imwrite(str(a)+'.jpg', img_)
    print("---->"+Fore.BLUE+Style.BRIGHT+str(a)+'.jpg'+Fore.RESET)
    ar=np.asarray(img_)
    plt.figure(figsize=[10,5])
    plt.subplot(121)
    plt.imshow(ar, cmap='gray')
    plt.show(block=False)
    a+=1
    c.delete('all')
    tk.title("Digit - "+str(a)[-1])

c.bind('<B1-Motion>', fig)
c.bind('<Button-3>', del_con)
c.bind('<Button-2>', img_con)

tk.mainloop()
