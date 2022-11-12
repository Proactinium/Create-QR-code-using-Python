from tkinter import *
import qrcode

root= Tk()
root.title("QR Code Creator")
root.state("zoomed")
root.config(bg="#AE2321")

#screen scan qr code


def generate():
    name=title.get()
    text=entry.get()
    qr=qrcode.make(text)
    qr.save("C:\Python Programs\Tkinker programs\QR -Code_Project\QRcode/"+ str(name)+".png")
    Label(root,text="scan the above qr code to decrypt",fg="white",bg="#AE2321",font=(("times new roman"),15)).place(x=650,y=50)

    global Image
    Image=PhotoImage(file="C:\Python Programs\Tkinker programs\QR -Code_Project\QRcode/"+ str(name)+".png")
    Image_view.config(image=Image)

Image_view=Label(root,bg="#AE2321")
Image_view.place(x=650,y=100)


Label(root,text="QR Code Creator can be used for encrypting texts and link",fg="black",bg="#AE2321",font=(("times new roman"),12)).place(x=50,y=50)
Label(root,text="File name",fg="white",bg="#AE2321",font=(("times new roman"),15)).place(x=50,y=100)
title=Entry(root,width=13,font=(("times new roman"),13))
title.place(x=50,y=130)

entry=Entry(root,width=28,font=(("times new roman"),13))
entry.place(x=50,y=180)

def clear():
    title.delete(0,END)
    entry.delete(0,END)

Button(root,text="Generate",width=10,height=1,font=(("times new roman"),15),bg="black",fg="white",command=generate).place(x=50,y=230)
Button(root,text="Clear",width=10,height=1,font=(("times new roman"),15),bg="black",fg="white",command=clear).place(x=185,y=230)
root.mainloop()
