import tkinter as tk
from tkinter import *
from bs4 import BeautifulSoup as b
from PIL import ImageTk, Image
from io import BytesIO
import random
import requests

Font = ("Comic Sans MS", 13, "bold")

def RandomBird():
    global text
    req1 = requests.get("https://www.generatormix.com/random-birds?number=1")
    soup1 = b(req1.text,"html.parser")
    s1 = soup1.find("h3",class_="text-center")
    i = soup1.find("img",class_="lazy thumbnail")
    img = i["data-src"]
    text = s1.text.replace(" ", "+")
    x = findmeaning()

    

    root = tk.Toplevel()
    root.title(s1.text)
    response = requests.get(img)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    resized_image= img.resize((500,300), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    ti = Label(root, text=x, image=photo, compound='top')
    ti.config(wraplength = 400)
    ti.config(justify = "center")
    ti.configure(font = Font)
    ti.pack()
    root.mainloop()




def RandomDino():
    global text
    lines = open("dino.txt").read() 
    line = lines[0:] 
    words = line.split()
    word = random.choice(words).lower()

    req1 = requests.get("https://www.nhm.ac.uk/discover/dino-directory/"+word)
    soup1 = b(req1.text,"html.parser")
    i = soup1.find("img" , class_="dinosaur--image")
    img = i["src"]
    text = word.replace(" ", "+")
    x = findmeaning()
    

    root = tk.Toplevel()
    root.title(word.upper())
    response = requests.get(img)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    resized_image= img.resize((500,300), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    ti = Label(root, text=x, image=photo, compound='top')
    ti.config(wraplength = 400)
    ti.config(justify="center")
    ti.configure(font =Font)
    ti.pack()
    root.mainloop()






def RandomGalaxy():
    global text
    req1 = requests.get("https://www.generatormix.com/random-galaxies?number=1")
    soup1 = b(req1.text,"html.parser")
    s1 = soup1.find("h3",class_="text-center")
    text = s1.text.replace(" ", "+")
    x = findmeaning()
    i = soup1.find("img",class_="lazy thumbnail aspect-wide-contain")
    img = i["data-src"]
    

    root = tk.Toplevel()
    root.title(s1.text)
    response = requests.get(img)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    resized_image= img.resize((500,300), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    ti = Label(root, text=x, image=photo, compound='top')
    ti.config(wraplength = 400)
    ti.config(justify = "center")
    ti.configure(font = Font)
    ti.pack()
    root.mainloop()

def RandomPlanet():
    global text
    req1 = requests.get("https://www.generatormix.com/random-planet?number=1")
    soup1 = b(req1.text,"html.parser")
    s1 = soup1.find("h3",class_="text-center")
    i = soup1.find("img",class_="lazy thumbnail aspect-wide-contain")
    img = i["data-src"]
    text = s1.text.replace(" ", "+")
    x = findmeaning()
    


    root = tk.Toplevel()
    root.title(s1.text)
    response = requests.get(img)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    resized_image= img.resize((500,300), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    ti = Label(root, text=x, image=photo, compound='top')
    ti.config(wraplength = 400)
    ti.config(justify = "center")
    ti.configure(font = Font)
    ti.pack()
    root.mainloop()

def RandomNebula():
    global text
    req1 = requests.get("https://www.generatormix.com/random-nebula?number=1")
    soup1 = b(req1.text,"html.parser")
    s1 = soup1.find("h3",class_="text-center")
    text = s1.text.replace(" ", "+")
    x = findmeaning()
  

    i = soup1.find("img",class_="lazy thumbnail aspect-wide-contain")
    img = i["data-src"]

    root = tk.Toplevel()
    root.title(s1.text)
    response = requests.get(img)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    resized_image= img.resize((500,300), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    ti = Label(root, text=x, image=photo, compound='top')
    ti.config(wraplength = 400)
    ti.config(justify = "center")
    ti.configure(font = Font)
    ti.pack()
    root.mainloop()

def RandomSpace():
    s = [1,2,3]
    c = random.choice(s)
    if c == 1:
        RandomGalaxy()
    elif c == 2:
        RandomPlanet()
    elif c == 3:
        RandomNebula()

def RandomSea():
    global text
    req1 = requests.get("https://www.generatormix.com/random-sea-animals?number=1")
    soup1 = b(req1.text,"html.parser")
    s1 = soup1.find("h3",class_="text-center")
    i = soup1.find("img",class_="lazy thumbnail aspect-wide-contain")
    img = i["data-src"]
    text = s1.text.replace(" ", "+")
    x = findmeaning()
    


    root = tk.Toplevel()
    root.title(s1.text)
    response = requests.get(img)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    resized_image= img.resize((500,300), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    ti = Label(root, text=x, image=photo, compound='top')
    ti.config(wraplength = 400)
    ti.config(justify = "center")
    ti.configure(font = Font)
    ti.pack()
    root.mainloop()





def RandomAnimal():
    global text
    req1 = requests.get("https://www.generatormix.com/random-animal-generator?number=1")
    soup1 = b(req1.text,"html.parser")
    s1 = soup1.find("h3",class_="text-center")
    i = soup1.find("img",class_="lazy thumbnail")
    img = i["data-src"]
    text = s1.text.replace(" ", "+")
    x = findmeaning()

    root = tk.Toplevel()
    root.title(s1.text)
    response = requests.get(img)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    resized_image= img.resize((500,300), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    ti = Label(root, text=x, image=photo, compound='top')
    ti.config(wraplength = 400)
    ti.config(justify = "center")
    ti.configure(font = Font)
    ti.pack()
    root.mainloop()






def RandomFact():
    global text
    reql = [1,2,3,4]
    req = random.choice(reql)
    if req == 1:        
        req1 = requests.get("https://www.generatormix.com/random-facts-generator?number=1")
        req = req1
    elif req == 2:
        req2 = requests.get("https://www.generatormix.com/random-animal-facts?number=1")
        req = req2
    elif req == 3:
        req3 = requests.get("https://www.generatormix.com/random-science-facts?number=1")
        req = req3
    elif req == 4:
        req4 = requests.get("https://www.generatormix.com/random-weird-facts?number=1")
        req = req4
    
    
    soup = b(req.text,"html.parser")
    s = soup.find("blockquote")
    fact = s.text

    root = tk.Toplevel()
    ti = Label(root, text="Did You Know?\n"+fact,justify="center")
    ti.config(wraplength = 400)
    ti.configure(font = Font)
    ti.pack()
    root.mainloop()




def findmeaning():
    url = "https://www.google.com/search?q=define+"+text+"+wikipedia"
    req1 = requests.get(url)
    soup1 = b(req1.text,"html.parser")
    s = soup1.find("div",class_="Gx5Zad xpd EtOod pkphOe")
    result = s.text
    if result.startswith("ImagesView") or result.startswith("Did") :
        result = altmeaning()
    if "allThe" in result:
        result = result.partition("allThe")
        x = result[2]
        result = x
    if "Wikipediaen.wikipedia.org" in result:
        temp = result.partition("Wikipediaen.wikipedia.org")
        x = temp[0]
        result = x
    if result.startswith("People"):
        result = alt2()
    if result.lower().startswith("showing"):
        result = "Description Not Available Sorry!"
    return result.title()

def altmeaning():
    req1 = requests.get("https://www.google.com/search?q=define+"+text)
    soup1 = b(req1.text,"html.parser")
    s = soup1.find("div",class_="Gx5Zad xpd EtOod pkphOe")
    result = s.text
    return result
def alt2():
    url = "https://www.google.com/search?q=summary+"+text+"+wikipedia"
    req1 = requests.get(url)
    soup1 = b(req1.text,"html.parser")
    s = soup1.find("div",class_="Gx5Zad xpd EtOod pkphOe")
    result = s.text
    return result


  
  
def dc():
    root = tk.Toplevel()
    f = Label(root,text="I told you not to click you Alien!\nNow FAQ Off and go back you Apple!")
    f.configure(font = Font)
    f.pack()
    root.mainloop()

def info():
    root = tk.Toplevel()
    f = Label(root,text='''Confused What the icons mean? Here is Quick Summary\n
        The Atronaut -  His Name is Meet He'll Tell You About a Random Planet,Galaxy or a Nebula (You Know What That Means Right?)\n
        The Dinosaur - Her Name is Nately and She'll Tell You About a Random Dinosaur(She's Very Dangerous)\n
        The Shark - His Name Is Don He'll Tell You about a ranodm Sea Animal("He Looks Scary but he is not")\n
        The Bird - Her Name is Haely she'll tell you about a random Bird(She is very energetic)\n
        The Koala - Her Name is Riya She'll tell you About random animal(She is very slow)\n
        The Brain - His Name is Einstein He'll Tell You a Random Fact(He's a Nerd)''')
    f.configure(font = Font)
    f.pack()
    root.mainloop()





Font1 = ("Comic Sans MS", 12, "bold")
root = Tk()
root.title("By VoiD")
main = Label(text = "Welcome,Click On Any Button Below",justify = "center")
main.config(wraplength = 210)
main.grid(columnspan=3)
main.configure(font = Font1)

img1 = Image.open("dino.jpg")
reimg1 = img1.resize((150,150),Image.LANCZOS)
photo1 = ImageTk.PhotoImage(reimg1)
DinoBtn = Button(root,image = photo1,command = RandomDino)
DinoBtn.grid(row=2,column=2)

img2 = Image.open("space.jpg")
reimg2 = img2.resize((150,150),Image.LANCZOS)
photo2 = ImageTk.PhotoImage(reimg2)
SpaceBtn = Button(root,image = photo2,command = RandomSpace)
SpaceBtn.grid(row=2,column=1)

img3 = Image.open("bird.jpg")
reimg3 = img3.resize((150,150),Image.LANCZOS)
photo3 = ImageTk.PhotoImage(reimg3)
BirdBtn = Button(root,image = photo3,command = RandomBird)
BirdBtn.grid(row=3,column=2)

img4 = Image.open("sea.jpg")
reimg4 = img4.resize((150,150),Image.LANCZOS)
photo4 = ImageTk.PhotoImage(reimg4)
SeaBtn = Button(root,image = photo4,command = RandomSea)
SeaBtn.grid(row=3,column=1)

img5 = Image.open("animal.jpg")
reimg5 = img5.resize((150,150),Image.LANCZOS)
photo5 = ImageTk.PhotoImage(reimg5)
AniBtn = Button(root,image = photo5,command = RandomAnimal)
AniBtn.grid(row=4,column=1)

img6 = Image.open("fact.jpg")
reimg6 = img6.resize((150,150),Image.LANCZOS)
photo6 = ImageTk.PhotoImage(reimg6)
FloBtn = Button(root,image = photo6,command = RandomFact)
FloBtn.grid(row=4,column=2)

F = ("Comic Sans MS", 8, "bold")
Btn = Button(root,text="Dont Click Here!",justify="center",height=1,width=43,command=dc)
Btn.configure(font = F)
Btn.grid(row=5,columnspan=3)

Btn2 = Button(root,text="Confused? Click Here!",justify="center",height=1,width=43,command=info)
Btn2.configure(font = F)
Btn2.grid(row=1,columnspan=3)
root.mainloop()
