import socket
from threading import Thread
import random as random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000


server.bind((ip_address, port))
server.listen()

list_of_clients = []
list_of_nicknames = []

print("Server has started...")

def clientthread(conn, addr):
    
    questions = [
        "Where did the Mahabharata war took place ? \na.Ayodhya \nb.Kurukshetra \nc.Lanka \nd.Dwarika",
        "Who is one of the Chiranjeevis ? \na.Raja Bali \nb.Jambvant \nc.Bhishma \nd.Dronacharya",
        "Who is referred as Radheya in Mahabharata ? \na.Krishna \nb.Arjun \nc.Bheem \nd.Karna",
        "Name of Shree Krishna's conch shell was . \na.Paundra \nb.Panchajanya \nc.Devdutta \nd.Sugosh",
        "Who will be the Last Avatar of Shree Hari ? \na.Nar \nb.Parshuram \nc.Kalki \nd.Matsya",
        "Who is considered as the king of demigods ? \na.Vayu \nb.Yam \nc.Varun \nd.Indra",
        "For how many days was the Mahabharata War fought ? \na.108 \nb.10 \nc.18 \nd.100",
        "Who wiped out the entire Kshatriya Bloodline from the earth for 21 times ? \na.Parshuram \nb.Bharat \nc.Duryodhan \nd.Indra"
    ]

    answers = ["b","a","d","b","c","d","c","a"]
    indices = [0,1,2,3,4,5,6,7]
    def getQnA(conn):
      index = random.randint(0,len(questions)-1)
      question = questions[index]
      answer = answers[index]
      question = f"{question}\n{answer}\n{index}"
      conn.send(question.encode('utf-8'))
      return question,answer,index

    def removeQuestion(index):
      print("done")
      questions.pop(index)
      answers.pop(index)

    question,answer,index = getQnA(conn)
    removeQuestion(index)
    score = 0
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
              if message.lower() == "a" or message.lower() == "b" or message.lower() == "c" or message.lower() == "d":
                print(message)
                if message == answer:
                   conn.send("correct".encode('utf-8'))
                   score = score + 1
                else:
                   conn.send("incorrect".encode('utf-8'))
              elif message == "next":
                if len(questions) == 0:
                  conn.send("over".encode('utf-8'))
                else:
                  question,answer,index = getQnA(conn)
                  removeQuestion(index)
            else:
              remove(conn)
        except:
            continue


def remove(unwanted_client):
    for i in list_of_clients:
        if i == unwanted_client:
            list_of_clients.remove(i)

while True:
    conn, addr = server.accept()
    conn.send("NICKNAME".encode('utf-8'))
    nickname = conn.recv(2048).decode('utf-8')
    list_of_clients.append(conn)
    list_of_nicknames.append(nickname)
    print(nickname + " has connected")
    new_thread = Thread(target= clientthread,args=(conn,addr))
    new_thread.start()
