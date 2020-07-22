import re
import tkinter as tk
from Steganography import Convert
from Morsecode import Morse

class Secret1(object):
    def __init__(self, master, **kwargs):
        global x,var
        x=Morse()
        var=tk.IntVar()
        l1=tk.Label(text="Select a task",font=("Helvetica",30,"bold"),activeforeground="black",fg="black",bg="yellow")
        l1.place(x=140,y=100)
        l2=tk.Label(text="Message:",font=("Helvetica",20,"bold"),activeforeground="black",fg="black",bg="yellow")
        l2.place(x=140,y=230)
        l3=tk.Label(text="Morse code:",font=("Helvetica",20,"bold"),activeforeground="black",fg="black",bg="yellow")
        l3.place(x=140,y=400)
        
        textBox1= tk.Text(height =5, width =80,relief="sunken",bd=5,font=("Helvetica", 15))
        textBox1.configure(state='disabled')
        textBox1.place(x=340,y=400)
        textBox2 = tk.Text(height =3, width =80,relief="sunken",bd=5,font=("Helvetica", 15))
        textBox2.configure(state='disabled')
        textBox2.place(x=340,y=230)
        action=tk.Button(root, bd=5,activeforeground="#ffffff",activebackground="violet",
                         fg="white",bg="#ed91af",width=12, height=1,font=("verdana",15,'bold'))
        btn1 = tk.Button(root, text="Encode", bd=5,activebackground="#ed91af",bg="#ed91af",font=("verdana",20), command=lambda:self.task(1,textBox1,textBox2,action))
        btn1.place(x=550,y=100)
        btn2 = tk.Button(root, text="Decode", bd=5,activebackground="#ed91af",bg="#ed91af",font=("verdana",20), command=lambda:self.task(2,textBox1,textBox2,action))
        btn2.place(x=1050,y=100)
       
        btn4 = tk.Button(root, text="Back", bd=5,activeforeground="#ffffff",activebackground="violet",
                         fg="white",bg="#ed91af",width=12, height=1,font=("verdana",12,'bold'), command=lambda:self.back(l1,l2,l3,textBox1,textBox2,btn1,btn2,action,btn4))
        btn4.place(x=140,y=628)
        
    def back(self,*widgets):
        for i in widgets:
            i.destroy()
        Start(root)
    def task(self,num,textBox1,textBox2,action):
        if num==1:
            name="Encode"
            action["text"]=name
            action['command']=lambda:self.perform(num,textBox1,textBox2)
            textBox1.configure(state="disabled")
            textBox2.configure(state="normal")
        else:
            textBox1.configure(state="normal")
            textBox2.configure(state="disabled")
            name="Decode"
            action["text"]=name
            action['command']=lambda:self.perform(num,textBox1,textBox2)
        action.place(x=1050,y=570)
    def perform(self,num,textBox1,textBox2):
        if num==1:
            textBox2.configure(state="disabled")
            f=textBox2.get("1.0","end")
            f=f.lower().replace("\n"," ")
            s=x.encode(f)
            textBox1.configure(state='normal')
            textBox1.delete("1.0","end")
            textBox1.insert("end",s)
            textBox1.configure(state='disabled')
        else:
            f=textBox1.get("1.0","end")
            f=f.replace("\n","")
            f=f.strip()
            s=x.decode(f)
            textBox1.configure(state='disabled')
            textBox2.configure(state='normal')
            textBox2.delete("1.0","end")
            textBox2.insert("end",s)
            textBox2.configure(state='disabled')

class Secret2(object):
    def __init__(self, master, **kwargs):
        global x,var,rc
        rc='^[a-zA-Z0-9.?,+-;:&`~"/*<>\'\n\t|\(\)\}\{\[\]\$@!#%=^_ ]+$'
        x=Convert()
        var=tk.IntVar()
        l1=tk.Label(text="Select a task",font=("Helvetica",30,"bold"),activeforeground="black",fg="black",bg="yellow")
        l1.place(x=140,y=100)
        l2=tk.Label(text="Message:",font=("Helvetica",20,"bold"),activeforeground="black",fg="black",bg="yellow")
        l2.place(x=140,y=400)
        textBox1= tk.Text(height =5, width =80,relief="sunken",bd=5,font=("Helvetica", 15))
        textBox1.configure(state='disabled')
        textBox1.place(x=340,y=400)
        textBox2 = tk.Text(height =3, width =80,relief="sunken",bd=5,font=("Helvetica", 15))
        textBox2.configure(state='disabled')
        textBox2.place(x=340,y=230)
        action=tk.Button(root, bd=5,activeforeground="#ffffff",activebackground="violet",
                         fg="white",bg="#ed91af",width=12, height=1,font=("verdana",15,'bold'))
        btn1 = tk.Button(root, text="Encode", bd=5,activebackground="#ed91af",bg="#ed91af",font=("verdana",20), command=lambda:self.task(1,textBox1,action))
        btn1.place(x=550,y=100)
        btn2 = tk.Button(root, text="Decode", bd=5,activebackground="#ed91af",bg="#ed91af",font=("verdana",20), command=lambda:self.task(2,textBox1,action))
        btn2.place(x=1050,y=100)
        
        btn3 = tk.Button(root, text="Select Image", bd=5,activeforeground="#ffffff",activebackground="violet",
                         fg="white",bg="#ed91af",width=12, height=1,font=("verdana",12,'bold'), command=lambda:self.open_img(textBox2))
        btn3.place(x=140,y=250)
       
        btn4 = tk.Button(root, text="Back", bd=5,activeforeground="#ffffff",activebackground="violet",
                         fg="white",bg="#ed91af",width=12, height=1,font=("verdana",12,'bold'), command=lambda:self.back(l1,l2,textBox1,textBox2,btn1,btn2,btn3,btn4,action))
        btn4.place(x=140,y=628)
        
    def back(self,*widgets):
        for i in widgets:
            i.destroy()
        Start(root)
    def task(self,num,textBox1,btn5):
        if num==1:
            name="Encode"
            btn5["text"]=name
            btn5['command']=lambda:self.perform(num,textBox1)
            textBox1.configure(state="normal")
        else:
            textBox1.configure(state="disabled")
            name="Decode"
            btn5["text"]=name
            btn5['command']=lambda:self.perform(num,textBox1)
        btn5.place(x=1050,y=570)
    def perform(self,num,textBox1):
        f=root.filename
        if num==1:
            s=textBox1.get("1.0","end")
            if re.match(rc,s):
                x.encode(f,s)
            else:
                textBox1.delete("1.0","end")
                textBox1.insert("end","Sorry cannot encode special characters")
            textBox1.configure(state="disabled")
        else:
            s=x.decode(f)
            textBox1.configure(state='normal')
            textBox1.delete("1.0","end")
            if re.match(rc,s):
                textBox1.insert("end",s)
            else:
                textBox1.insert("end","Sorry, cannot decode message. Given text may contain special characters. If not, try changing the image.")
            textBox1.configure(state='disabled')
    def open_img(self,textBox2):
        root.filename =  tk.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("jpeg files","*.jpg")))
        textBox2.configure(state='normal')
        textBox2.delete("1.0","end")
        textBox2.insert('end',root.filename)
        textBox2.configure(state='disabled')
class Start(object):
    def __init__(self, master, **kwargs):
        l1=tk.Label(text="Select a technique",font=("Helvetica",50,"bold"),bg="#fbff12",fg="black",bd=5)
        l1.place(x=380,y=100)
        l2=tk.Label(text="* Steganography is the process of hiding a message inside an image.",font=("Helvetica",20,"bold"),bg="#fbff12",fg="black",bd=5)
        l2.place(x=100,y=600)
        btn1 = tk.Button(root, text="Morse code",activeforeground="#ffffff",activebackground="violet",
                         fg="white",bg="#ed91af",width=12, height=1,relief="raised",bd=8,font=("verdana",35,'bold'), command=lambda:self.clear(1,l1,l2,btn1,btn2))
        btn1.place(x=140,y=320)
        btn2 = tk.Button(root, text="Steganography",activeforeground="#ffffff",activebackground="violet",
                         fg="white",bg="#ed91af",width=12, height=1,relief="raised",bd=8,font=("verdana",35,'bold'), command=lambda:self.clear(2,l1,l2,btn1,btn2))
        btn2.place(x=800,y=320)
        
    def clear(self,*widgets):
        if widgets[0]==1:
            for i in widgets[1:]:
                i.destroy()
            Secret1(root)
        else:
            for i in widgets[1:]:
                i.destroy()
            Secret2(root)

root=tk.Tk()
root.title("Hide a message")
pad=10
root._geom='1300x600+0+0'
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth()-pad,root.winfo_screenheight()-pad))
root.resizable(width = True, height = True) 
root.configure(bg="#fbff12")
app=Start(root)
root.mainloop()

