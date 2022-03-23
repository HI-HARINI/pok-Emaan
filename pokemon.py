from tkinter import*
from PIL import ImageTk, Image
import random
root=Tk()
root.geometry("1000x1000")
root.title("Endless Dice GAME")
root.configure(background="#AD0034")
img=ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
img2=ImageTk.PhotoImage(Image.open("abra.jpg"))
img3=ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
img4=ImageTk.PhotoImage(Image.open("charmender.jpg"))
img5=ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
img6=ImageTk.PhotoImage(Image.open("kadabra.jpg"))
img7=ImageTk.PhotoImage(Image.open("meowth.jpg"))
img8=ImageTk.PhotoImage(Image.open("nidoking.jpg"))
img9=ImageTk.PhotoImage(Image.open("paras.jpg"))
img10=ImageTk.PhotoImage(Image.open("persion.jpg"))
img11=ImageTk.PhotoImage(Image.open("pikachu.jpg"))
img12=ImageTk.PhotoImage(Image.open("ratata.jpg"))
img13=ImageTk.PhotoImage(Image.open("squirtle.jpg"))
buttonimg=ImageTk.PhotoImage(Image.open("button.jpg"))
label1=Label(root,text="Player 1",bg="#AD3D9C")
label1.place(relx=0.2, rely=0.2,anchor=CENTER)
label2=Label(root,text="Player 2",bg="#AD3D9C")
label2.place(relx=0.8, rely=0.2,anchor=CENTER)
label0=Label(root,bg="#AD3D9C")
label0.place(relx=0.5, rely=0.2,anchor=CENTER)
label3=Label(root,image=img,bg="#AD3D9C")
label3.place(relx=0.5, rely=0.5,anchor=CENTER)
label4=Label(root,text="",bg="#AD3D9C")
label4.place(relx=0.2, rely=0.4,anchor=CENTER)
label5=Label(root,text="",bg="#AD3D9C")
label5.place(relx=0.8, rely=0.4,anchor=CENTER)
pokemon_list = [img,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,img13]
powerlist=[70,30,60,50,100,70,60,90,40,70,200,40,50]
playerscore=0
def player1():
    global playerscore
    randomnumber=random.randint(0,12)
    rp=pokemon_list[randomnumber]
    rpl=powerlist[randomnumber]
    playerscore=playerscore+rpl
    label0["text"]="Power Points of Player 1 "+str(playerscore)
    label3["image"]=rp
    label4["text"]=rpl

playerscore2=0
def player2():
    global playerscore2
    randomnumber=random.randint(0,12)
    rp=pokemon_list[randomnumber]
    rpl=powerlist[randomnumber]
    playerscore2=playerscore2+rpl
    label0["text"]="Power Points of Player 2 "+str(playerscore2)
    label3["image"]=rp
    label5["text"]=rpl
    
button1=Button(root,image=buttonimg,command=player1)
button1.place(relx=0.2, rely=0.6,anchor=CENTER)
button2=Button(root,image=buttonimg,command=player2)
button2.place(relx=0.8, rely=0.6,anchor=CENTER)
root.mainloop()