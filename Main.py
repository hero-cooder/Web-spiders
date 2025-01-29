import tkinter
import tkinter.messagebox
import requests
from tqdm.tk import tqdm
import time
from tkinter import *
import tkinter as tk
import threading
from tkinter import ttk
import webbrowser
import os
import wget
import requests
from requests import *

from bs4 import BeautifulSoup
root = tkinter.Tk()



for i  in tqdm(range(100),desc="正在加载工具"):
    time.sleep(0.01)
root.title("可视化爬虫工具")
root.resizable(False,False)#禁止最大化
root.geometry("480x480")#size
lable = tkinter.Label(root,text="可视化爬虫工具",fg="red").pack()
url_text=tkinter.Label(root,text="需要爬取的url").place(x=60,y=40)
need = tk.Entry(root, width=40)
need.place(x=60, y=80)

#$创建文件夹，后续存放
#初始化mk_dir =0;即为false。也可以拿来判定.最好写入函数，这样子可以反复调用

#################################
#version 0.1
#date 24/12/24
#################################




########################################################
#version 0.2
#date 25/01/15
#########################################################

try:
    os.makedirs("C://_download")
    sucess_windows = tkinter.messagebox.showinfo("目录创建成功","创建目录成功\n C://_download")
except Exception as e:
    fail_windows =   tkinter.messagebox.showinfo("目录创建失败","创建目录失败，该目录已存在")#失败窗口


def Url():
    url = need.get()
    label_2 = tk.Label(root, text="获取的链接为: " + url)
    label_2.place(x=60, y=180)
    time.sleep(0.4)
    time.sleep(2)
    open_url = tkinter.messagebox.askyesno("请确认","是否访问这个网页")
    if open_url == True:
        webbrowser.open(url)
        time.sleep(0.2)
        send_req = requests.get(url)
        if send_req.status_code == 200:
            print(send_req)
            #成功获取窗口
            connet_window = tkinter.messagebox.askyesno("链接成功","资源链接成功、状态码200")
            print(connet_window)
            if connet_window ==True:
                down_load_windows =tkinter.messagebox.askyesno("询问","资源链接成功，是否下载")
                if down_load_windows == True:                  
  #保存网页到C://_download
                    path = "C://_download/save.html"
                    down_load_web = wget.download(url,out=path)
                    print(down_load_web)
                    time.sleep(0.2)
                    with open("C://_download//网页源码.txt",'w',encoding="utf-8")as w:
                        w.write(str(send_req.text))
                        if down_load_windows == True:
                            time.sleep(0.2)
                    with open("C://_download//网页源码.txt",'w',encoding="utf")as w:
                        w.write(str(send_req.text))
                    with open("C://_download//网页源码.txt",'r',encoding="utf-8")as R:
                        read= R.read()
                        R.close()
                        Be  = BeautifulSoup(read,"html.parser")
                        divs = Be.find_all("div")
                        for i in divs:
                                with open('C://_download//解析结果.txt','w',encoding="utf-8")as w:
                                    w.write(i.get_text() +'\n')
                                    time.sleep(0.1)
                                    w.close()
                                    time.sleep(0.3)
                                sucess_download = tkinter.messagebox.askokcancel("成功","资源下载成功")
                                if sucess_download ==TRUE:
                                    break
                                time.sleep(0.2)
                                print(sucess_download)
    else:
        tkinter.messagebox.showinfo("感谢使用","您已取消操作\n感谢使用")
        exit()
        time.sleep(0.3)
button  =tkinter.Button(command=Url,text="获取",width=8,height=4).place(x=60,y=100)
root.mainloop()
