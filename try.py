from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
from PIL import ImageTk, Image
import pyscreenshot as ImageGrab
import pyautogui
import cv2
import os 

def create_button(k,number):
    x = 0
    i = 0
    for x in number:
        i = int(i)+1
        bt = Button(k, text = str(x),command = lambda:open_img(k,"/home/hk/Desktop/python_examples/inovar3.png"))
        bt.grid() 

def open_img(self,openfn):
    x = openfn
    img = Image.open(x)
    img = img.resize((800, 800), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(self, image=img)
    panel.image = img
    panel.place(x=100, y=100)

def open_img1(self,openfn):
    x = openfn
    img = Image.open(x)
    img = img.resize((800, 800), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(self, image=img)
    panel.image = img
    panel.place(x=100, y=100)
# function for video streaming
def video_stream():
    ret, frame = cap.read()
    if ret is True:        
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(1, video_stream) 

    elif ret is False:
        openfn="/home/hk/Desktop/python_examples/inovar3.png"
        x = openfn
        img = Image.open(x)
        img = img.resize((root.winfo_screenwidth()-70, root.winfo_screenheight()-200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        lmain.img = img
        lmain.configure(image = img)
        global cap  
        cap = cv2.VideoCapture(host)
        lmain.after(1, video_stream)

def ss_button_callback():
    print("ekran goruntusu alindi")
    im=ImageGrab.grab()#bbox=(500,10,1000,500)
    im.save(r"/home/hk/Desktop/saved/fotograf/hk.png")
    l = Label(lmain, text = " ekran goruntusu alindi", font = "Helvetica 20 bold italic" )
    l.grid(row = 5, column = 10)    
    l.after(1000,lambda: l.destroy())

def record_button_callback():
    print("ekran kaydi alindi")
    l = Label(lmain, text = " ekran kaydi baslatildi", font = "Helvetica 20 bold italic" )
    l.grid(row = 5, column = 10)    
    l.after(1000,lambda: l.destroy())
   
def saved_button_callback():
    print("kaydedilenler acildi")
    #filename = tkFileDialog.askdirectory(initialdir = "/home/hk/Desktop/saved/")#,title = "Dosya sec",filetypes = (("png dosyalar","*.png"),("tum dosyalar","*.*")))
    #print(filename)
    top = Toplevel(root)
    top.title("kaydedilenler")
    top.geometry("250x60+500+100")
    top.lift()
    def fotograflar():
        top.destroy()
        box = Toplevel()
        box.title("fotograflar")
        box.geometry("500x500+300+100")
        box.lift()
        path = r"/home/hk/Desktop/saved/fotograf"
        doc = os.listdir(path)
        array = []
        for a in doc:
            path = "/home/hk/Desktop/saved/fotograf/"+str(a)
            #img =  Image.open(path)  
            #img = img.resize((800, 800), Image.ANTIALIAS)
            #img = ImageTk.PhotoImage(img)
            #panel = Label(, image=img)
            #panel.image = img
            #panel.place(x=100, y=100)         
            array.append(path)
            #array()
        create_button(box,array)
        #def image_viewer()
        #    bt_exit= Button(tox, text = "kapat", command = )
        #    bt_back = Button(tox, text = "geri",command = )
        #    bt_forward=Button(tox, text = " ileri", command = )
        

    def videolar():
        top.destroy()
    button_exit = Button(top, text = "fotograflar", command = fotograflar, padx = 30, pady =20, bg="green")
    button_exit.grid(row = 1,column = 1)
    button_exit1 = Button(top, text = "videolar", command = videolar, padx = 35, pady = 20, bg="green")
    button_exit1.grid(row = 1,column = 2)
    
    #x = filename
    #img = Image.open(x)
    #img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
    #img = ImageTk.PhotoImage(img)
    #panel = Label(top, image=img)
    #panel.image = img
    #panel.place(x=0, y=0)
    
    
def transfer():
    print("hastalik bulma baslatildi")

global root
global host
host = 0 #"http://192.168.43.1:8080"
root = Tk()
root.title("video laryngoscope")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))# Create a frame
root.configure(background='#787467')
#openfn="/home/hk/Desktop/python_examples/inovar.ico"
#x = openfn
#img = Image.open(x)
#img = ImageTk.PhotoImage(img)
#root.iconphoto(False, img)

#open_img()
app = LabelFrame(root, bg='#787467')
app.place(x = 0,y = 0)


# Create a label in the frame
lmain = Label(app, background='#787467')
lmain.grid()
lmain2 = Label(app, background='#787467')
lmain.grid(row = 3, column = 5)

# Capture from camera
cap = cv2.VideoCapture(host)

#photo = PhotoImage(file = "/home/hk/Desktop/python_examples/inovar3.png" ) 

ss_button = Button(root, text = "ekran fotografi", padx = 30, pady = 20, command = ss_button_callback,bg="yellow",font = "Helvetica 12 bold italic")
ss_button.place(x=root.winfo_screenwidth()/4+30, y=root.winfo_screenheight()-150)

record_button = Button(root, text = "ekran kaydet", padx = 30, pady = 20, command = record_button_callback,bg="yellow",font = "Helvetica 12 bold italic")
record_button.place(x=root.winfo_screenwidth()/4+185, y=root.winfo_screenheight()-150 )

saved_button= Button(root, text = "kaydedilenler", padx = 30, pady = 20, command = saved_button_callback,bg="yellow",font = "Helvetica 12 bold italic")
saved_button.place(x=root.winfo_screenwidth()/4+330, y=root.winfo_screenheight()-150 )

detecting = Button(root, text = "SD karta aktar", padx = 30, pady = 20, command = transfer,bg="yellow",font = "Helvetica 12 bold italic")
detecting.place(x=root.winfo_screenwidth()/4+475, y=root.winfo_screenheight()-150)

#open_img()
video_stream()
root.mainloop()