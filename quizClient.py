import socket
from threading import Thread
from tkinter import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))
print("Connected with the server...")

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")
        self.login.configure(bg="#252525")

        self.score = 0

        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=300)
        
        self.pls = Label(self.login,text = "Please login to continue",justify = CENTER,font = "Helvetica 14 bold",fg="white",bg="#252525")
        self.pls.place( relheight = 0.15,relx = 0.2,rely = 0.07)

        self.labelName = Label(self.login,text = "Name: ",font = "Helvetica 12",fg="white",bg="#252525")
        self.labelName.place(relheight = 0.2,relx = 0.1,rely = 0.2)

        self.entryName = Entry(self.login,font = "Helvetica 14",fg="white",bg="#252525")
        self.entryName.place(relwidth = 0.4,relheight = 0.12,relx = 0.35,rely = 0.25)
        self.entryName.focus()

        self.loginButton = Button(self.login,text="Login",font="Helvetica 14",command=lambda:self.goAhead(self.entryName.get()),fg="black",bg="#868686")
        self.loginButton.place(relx=0.4,rely=0.55)

        self.Window.mainloop()

    def goAhead(self,name):
        self.name = name
        self.list = []
        self.login.destroy()
        receive = Thread(target=self.receive)
        receive.start()

    def showQuestion(self,question):
        self.Window.deiconify()
        self.Window.title("QUIZ")
        self.Window.resizable(width = False,height = False)
        self.Window.configure(width = 381,height = 450,bg = "#252525")
        stringData = question.split("\n")
        self.stringData = stringData
        newString = stringData[0].split(" ")
        finalString = ""
        counter = 40
        for i in newString:
            length = len(i)
            if counter - length >= 0:
                finalString = finalString + i + " "
                counter -= length+1
            else:
                finalString = finalString + "\n" + i + " "
                counter = 40-length-1

        self.app_label=Label(self.Window, text="Quiz Game", fg = "white", bg = "#252525", font=("Calibri", 20),bd=5,width=24)
        self.app_label.place(x=16, y=20)

        self.question_label=Label(self.Window, text=finalString, fg = "white", bg = "#252525", font=("Calibri", 12),bd=1,width=42)
        self.question_label.place(x=20, y=80)

        self.optionA_button = Button(self.Window,text="  "+stringData[1],fg="black",bg="#868686",font=("Calibri",12),bd=1,width=42,height=2,anchor="w",command=lambda:self.checkAns("a"))
        self.optionA_button.place(x=20,y=140)

        self.optionB_button = Button(self.Window,text="  "+stringData[2],fg="black",bg="#868686",font=("Calibri",12),bd=1,width=42,height=2,anchor="w",command=lambda:self.checkAns("b"))
        self.optionB_button.place(x=20,y=200)

        self.optionC_button = Button(self.Window,text="  "+stringData[3],fg="black",bg="#868686",font=("Calibri",12),bd = 1,width=42,height=2,anchor="w",command=lambda:self.checkAns("c"))
        self.optionC_button.place(x=20,y=260)

        self.optionD_button = Button(self.Window,text="  "+stringData[4],fg="black",bg="#868686",font=("Calibri",12),bd = 1,width=42,height=2,anchor="w",command=lambda:self.checkAns("d"))
        self.optionD_button.place(x=20,y=320)

        self.next_button = Button(self.Window,text="  Next Question ->",fg="black",bg="#868686",font=("Calibri",12),bd = 1,width=16,height=2,anchor="w",command=self.clearWindow)
        self.next_button.place(x=228,y=390)       

    def clearWindow(self):
        self.next_button.destroy()
        self.app_label.destroy()
        self.question_label.destroy()
        self.optionD_button.destroy()
        self.optionC_button.destroy()
        self.optionB_button.destroy()
        self.optionA_button.destroy()
        self.checkAns("next")

    def checkAns(self,answer):
        self.answer = answer
        client.send(self.answer.encode('utf-8'))

    def setGreen(self):
        if self.answer == "a":
            self.optionA_button.destroy()
            self.optionA_button = Button(self.Window,text="  "+self.stringData[1],fg="black",bg="green",font=("Calibri",12),bd=1,width=42,height=2,anchor="w",command=lambda:self.checkAns("a"))
            self.optionA_button.place(x=20,y=140)
        elif self.answer == "b":
            self.optionB_button.destroy()
            self.optionB_button = Button(self.Window,text="  "+self.stringData[2],fg="black",bg="green",font=("Calibri",12),bd=1,width=42,height=2,anchor="w",command=lambda:self.checkAns("b"))
            self.optionB_button.place(x=20,y=200)
        elif self.answer == "c":
            self.optionC_button.destroy()
            self.optionC_button = Button(self.Window,text="  "+self.stringData[3],fg="black",bg="green",font=("Calibri",12),bd = 1,width=42,height=2,anchor="w",command=lambda:self.checkAns("c"))
            self.optionC_button.place(x=20,y=260)
        elif self.answer == "d":
            self.optionD_button.destroy()
            self.optionD_button = Button(self.Window,text="  "+self.stringData[4],fg="black",bg="green",font=("Calibri",12),bd = 1,width=42,height=2,anchor="w",command=lambda:self.checkAns("d"))
            self.optionD_button.place(x=20,y=320)

    def setRed(self):
        if self.answer == "a":
            self.optionA_button.destroy()
            self.optionA_button = Button(self.Window,text="  "+self.stringData[1],fg="black",bg="red",font=("Calibri",12),bd=1,width=42,height=2,anchor="w",command=lambda:self.checkAns("a"))
            self.optionA_button.place(x=20,y=140)
        elif self.answer == "b":
            self.optionB_button.destroy()
            self.optionB_button = Button(self.Window,text="  "+self.stringData[2],fg="black",bg="red",font=("Calibri",12),bd=1,width=42,height=2,anchor="w",command=lambda:self.checkAns("b"))
            self.optionB_button.place(x=20,y=200)
        elif self.answer == "c":
            self.optionC_button.destroy()
            self.optionC_button = Button(self.Window,text="  "+self.stringData[3],fg="black",bg="red",font=("Calibri",12),bd = 1,width=42,height=2,anchor="w",command=lambda:self.checkAns("c"))
            self.optionC_button.place(x=20,y=260)
        elif self.answer == "d":
            self.optionD_button.destroy()
            self.optionD_button = Button(self.Window,text="  "+self.stringData[4],fg="black",bg="red",font=("Calibri",12),bd = 1,width=42,height=2,anchor="w",command=lambda:self.checkAns("d"))
            self.optionD_button.place(x=20,y=320) 

        if self.stringData[5] == "a":
            self.optionA_button.destroy()
            self.optionA_button = Button(self.Window,text="  "+self.stringData[1],fg="black",bg="green",font=("Calibri",12),bd=1,width=42,height=2,anchor="w",command=lambda:self.checkAns("a"))
            self.optionA_button.place(x=20,y=140)
        elif self.stringData[5] == "b":
            self.optionB_button.destroy()
            self.optionB_button = Button(self.Window,text="  "+self.stringData[2],fg="black",bg="green",font=("Calibri",12),bd=1,width=42,height=2,anchor="w",command=lambda:self.checkAns("b"))
            self.optionB_button.place(x=20,y=200)
        elif self.stringData[5] == "c":
            self.optionC_button.destroy()
            self.optionC_button = Button(self.Window,text="  "+self.stringData[3],fg="black",bg="green",font=("Calibri",12),bd = 1,width=42,height=2,anchor="w",command=lambda:self.checkAns("c"))
            self.optionC_button.place(x=20,y=260)
        elif self.stringData[5] == "d":
            self.optionD_button.destroy()
            self.optionD_button = Button(self.Window,text="  "+self.stringData[4],fg="black",bg="green",font=("Calibri",12),bd = 1,width=42,height=2,anchor="w",command=lambda:self.checkAns("d"))
            self.optionD_button.place(x=20,y=320)

    def showScore(self):
        app_label=Label(self.Window, text="Quiz Game", fg = "white", bg = "#252525", font=("Calibri", 20),bd=5,width=24)
        app_label.place(x=16, y=20)

        score_label=Label(self.Window, text="Your Score", fg = "white", bg = "#252525", font=("Calibri", 12),bd=3,width=42)
        score_label.place(x=20, y=120)

        score = Label(self.Window,bd=2,text=self.score,bg = "#252525",fg="white",font=("Calibri",20))
        score.place(x=177,y=160)

        button = Button(self.Window,text="Quit",fg="black",bg="#868686",font=("Calibri",12),bd = 2,width=16,height=2,command=lambda:self.Window.destroy())
        button.place(x=122,y=220)

    def receive(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                print(message)
                if message == 'NICKNAME':
                    client.send(self.name.encode('utf-8'))
                elif message == "correct":
                    self.score = self.score + 1
                    self.setGreen()
                elif message == "incorrect":
                    self.setRed()
                elif message == "over":
                    self.showScore()
                else:
                    self.showQuestion(message)                    
            except:
                print("An error occured!")
                client.close()
                break

g = GUI()

#write_thread = Thread(target=write)
#write_thread.start()
