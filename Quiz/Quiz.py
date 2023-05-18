import tkinter as tk
from tkinter import *
from bs4 import BeautifulSoup as b
from PIL import ImageTk, Image
from io import BytesIO
import random
import requests

def Acheck():
   global streak,sc,wrong,correct,cc,wc
   tkey = s[0].text[0]
   if tkey == key:
      button1.configure(bg = "lime")
      if sc == True:
         streak += 1    
      if cc == True:
         correct +=1
         cc = False
         wc = False
   else:      
      button1.configure(bg = "red")
      streak = 0
      sc = False
      if wc == True:
         wrong += 1
         wc = False
         cc = False
def Bcheck():
   global streak,sc,wrong,correct,cc,wc
   tkey = s[1].text[0]
   if tkey == key:
      button2.configure(bg = "lime")
      if sc == True:
            streak += 1
      if cc == True:
         correct +=1
         cc = False
         wc = False
   else:
      button2.configure(bg = "red")
      streak = 0
      sc = False
      if wc == True:
         wrong += 1
         wc = False
         cc = False
def Ccheck():
   global streak,sc,wrong,correct,cc,wc
   tkey = s[2].text[0]
   if tkey == key:
      button3.configure(bg = "lime")
      if sc == True:
            streak += 1
      if cc == True:
         correct +=1
         cc = False
         wc = False
   else:      
      button3.configure(bg = "red")
      streak = 0
      sc = False
      if wc == True:
         wrong += 1
         wc = False
         cc = False
def Dcheck():
   global streak,sc,wrong,correct,cc,wc
   tkey = s[3].text[0]
   if tkey == key:
      button4.configure(bg = "lime")
      if sc == True:
         streak += 1
      if cc == True:
         correct +=1
         cc = False
         wc = False
   else:
      button4.configure(bg = "red")
      streak = 0
      sc = False
      if wc == True:
         wrong += 1
         wc = False
         cc = False

def nxt():
   global x
   win.destroy()
   x = True

streak = 0
correct = 0
wrong = 0


ofont = ("Arial",11,"bold")

while True:
   x = False
   sc,cc,wc = True,True,True

   while True:
      link = "https://www.generatormix.com/random-trivia-questions-game?cat=sciencetechnology&number=1"
      req = requests.get(link)
      soup = b(req.text,"html.parser")
      ques = soup.find("p",class_ = "marg-bottom").text
      ans = soup.find("div",id="answer_block_0")
      s = soup.find_all("button",class_="answer btn btn-default col-12 marg-bottom")
      for i in s:
         try:
            if i["data-ans"] == "1":
               key = i.text[0]
         except:
            None
      if len(s) ==4:
         break

   win = Tk()
   win.state("zoomed")
   canvas = Canvas(win, width=1366, height=780)


   img = Image.open("quiz.jpg")
   reimg = img.resize((1366,780),Image.LANCZOS)
   photo = ImageTk.PhotoImage(reimg)
   canvas.create_image(0,0,anchor="nw",image=photo)


   qt = Label(win,text=ques,font=("Comic Sans MS",21,"bold"),bg="white",bd=4,relief="solid")
   qt.config(wraplength=1300)
   canvas.create_window(680,80,window=qt)

   st = Label(win,text="Streak : "+str(streak),bg="white",height=3,width=10,font=ofont,bd=3,relief="solid")
   wt = Label(win,text="Wrong : "+str(wrong),bg="white",height=3,width=10,font=ofont,bd=3,relief="solid") 
   ct = Label(win,text="Correct : "+str(correct),bg="white",height=3,width=10,font=ofont,bd=3,relief="solid")

   
   canvas.create_window(200,500,window=wt)
   canvas.create_window(200,400,window=ct)
   canvas.create_window(200,300,window=st)


   button1 = Button(win,height=2,width=60,text=s[0].text,bg="white",command=Acheck,bd=3,relief="solid")
   button1.configure(font=ofont)
   button2 = Button(win,height=2,width=60,text=s[1].text,bg="white",command=Bcheck,bd=3,relief="solid")
   button2.configure(font=ofont)
   button3 = Button(win,height=2,width=60,text=s[2].text,bg="white",command=Ccheck,bd=3,relief="solid")
   button3.configure(font=ofont)
   button4 = Button(win,height=2,width=60,text=s[3].text,bg="white",command=Dcheck,bd=3,relief="solid")
   button4.configure(font=ofont)
   button5 = Button(win,height=2,width=15,text="Next",bg="white",command=nxt,bd=3,relief="solid")
   button5.configure(font=ofont)



   canvas.create_window(680,300, window=button1)
   canvas.create_window(680,400, window=button2)
   canvas.create_window(680,500, window=button3)
   canvas.create_window(680,600, window=button4)
   canvas.create_window(680,700, window=button5)



   canvas.pack()
   win.mainloop()
   if x ==False:
      break
