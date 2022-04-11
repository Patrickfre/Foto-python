from tkinter import*
from PIL import ImageTk,Image
from matplotlib import image

myObj=Tk()
myObj.title("Attēlu pārlūks")
myObj.configure(bg="Black")
#myObj.geometry("800x500")
myObj.resizable(1,1)

img1=ImageTk.PhotoImage(Image.open("cat.jpg"))
img2=ImageTk.PhotoImage(Image.open("Dragon.jpg"))
img3=ImageTk.PhotoImage(Image.open("fruit.jpg"))
img4=ImageTk.PhotoImage(Image.open("Greensnake.jpg"))
img5=ImageTk.PhotoImage(Image.open("heheheha.jpg"))
img6=ImageTk.PhotoImage(Image.open("Minecraft.jpg"))
img7=ImageTk.PhotoImage(Image.open("Python.jpg"))
img8=ImageTk.PhotoImage(Image.open("Shiba.jpg"))

imageList=[img1, img2, img3, img4, img5, img6, img7, img8]
myLabel=Label(image=img1)
myLabel.grid(row=0,column=0,columnspan=3)

def forward(imgNumber):
    global myLabel,btnFwd, btnBack
    myLabel.grid_forget()
    myLabel=Label(image=imageList[imgNumber+1])
    myLabel.grid(row=0,column=0,columnspan=3)
    btnBack=Button(myObj,text="<<",command=lambda:back(imgNumber+1))
    btnFwd=Button(myObj,text=">>",command=lambda:forward(imgNumber+1))
    if imgNumber==6:
        btnFwd=Button(myObj,text=">>",state=DISABLED)
    btnBack.grid(row=1,column=0)
    btnFwd.grid(row=1, column=2)
    return 0

def back(imgNumber):
    global myLabel,btnBack,btnFwd
    myLabel.grid_forget()
    myLabel=Label(image=imageList[imgNumber-1])
    myLabel.grid(row=0,column=0,columnspan=3)
    btnBack=Button(myObj,text="<<",command=lambda:back(imgNumber-1))
    btnFwd=Button(myObj,text=">>",command=lambda:forward(imgNumber-1))
    if imgNumber==1:
        btnBack=Button(myObj,text="<<",state=DISABLED)
    btnBack.grid(row=1, column=0)
    btnFwd.grid(row=1, column=2)
    return 0
    


btnBack=Button(myObj,text="<<",state=DISABLED,command=back)
btnExit=Button(myObj,text="IZIET",command=myObj.quit)
btnFwd=Button(myObj,text=">>",command=lambda:forward(0))

btnBack.grid(row=1,column=0)
btnExit.grid(row=1,column=1)
btnFwd.grid(row=1,column=2)

myObj.mainloop()