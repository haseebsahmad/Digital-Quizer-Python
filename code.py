from Tkinter import *
from Tkinter import Tk,Frame,BOTH
from PIL import Image,ImageTk
from PIL import ImageTk, Image
import ImageTk
import os
import tkMessageBox
import tkFont
import MySQLdb
import getpass
db=MySQLdb.connect("localhost","root","","quiz")
cursor=db.cursor()
#cursor.execute("create table question (qnum int (2),type varchar(10),ques varchar(80),op1 varchar(85),op2 varchar(85),op3 varchar(85),op4 varchar(85),corA varchar(85),qid int(5),"
#               "_cour varchar(45))")

status=0

def NUMERIC():
    master = Tk()
    master.configure(bg='#1e90ff')
    global e0,e1,e2,e3,e4,e5,e6,e7,e8,e9
    Label(master,text="Question Number: ",font="arial",bg="white").grid(row=0,column=0)
    e0=Entry(master,bg="#87cefa",bd=4,fg="black",width=30)
    e0.grid(row=0,column=1)
    e1="NUMERIC"
    Label(master,text="Quiz Id: ",font="arial",bg="white").grid(row=0,column=5)
    e2=Entry(master,bg="#87cefa",bd=4,fg="black",width=10)
    e2.grid(row=0,column=6)
    Label(master,text="Course Name: ",font="arial",bg="white").grid(row=0,column=7)
    e3=Entry(master,bg="#87cefa",bd=4,fg="black",width=50)
    e3.grid(row=0,column=8)
    Label(master,text="Question Statment: ",font="arial",bg="white").grid(row=1,column=0)
    e4=Entry(master,bg="#87cefa",bd=4,fg="black",width=30)
    e4.grid(row=1,column=1)
    Label(master,text="Correct Answer: ",font="arial",bg="white").grid(row=5,column=0)
    e9=Entry(master,bg="#87cefa",bd=4,fg="black",width=30)
    e9.grid(row=5,column=1)
    Button(master,text="SAVE",command=stor_data,font="arial",bg="white").grid(row=4,column=4)
    Button(master,text="Submit",command=sub_data,font="arial",bg="green").grid(row=4,column=5)
def TF():
        master = Tk()
        master.configure(bg='#1e90ff')
        global e0,e1,e2,e3,e4,e5,e6,e7,e8,e9
        Label(master,text="Question Number: ",font="arial",bg="white").grid(row=0,column=0)
        e0=Entry(master,bg="#87cefa",bd=4,fg="black",width=30)
        e0.grid(row=0,column=1)
        e1="T/F"
        Label(master,text="Quiz Id: ",font="arial",bg="white").grid(row=0,column=5)
        e2=Entry(master,bg="#87cefa",bd=4,fg="black",width=10)
        e2.grid(row=0,column=6)
        Label(master,text="Course Name: ",font="arial",bg="white").grid(row=0,column=7)
        e3=Entry(master,bg="#87cefa",bd=4,fg="black",width=50)
        e3.grid(row=0,column=8)
        Label(master,text="Question Statment: ",font="arial",bg="white").grid(row=1,column=0)
        e4=Entry(master,bg="#87cefa",bd=4,fg="black",width=30)
        e4.grid(row=1,column=1)
        Label(master,text="Option 1: ",font="arial",bg="white").grid(row=2,column=0)
        e5=Entry(master,bg="#87cefa",bd=4,fg="black",width=30)
        e5.grid(row=2,column=1)
        Label(master,text="Option 2: ",font="arial",bg="white").grid(row=3,column=0)
        e6=Entry(master,bg="#87cefa",bd=4,fg="black",width=30)
        e6.grid(row=3,column=1)
        Label(master,text="Correct Answer: ",font="arial",bg="white").grid(row=6,column=0)
        e9=Entry(master,bg="#87cefa",bd=4,fg="black",width=30)
        e9.grid(row=6,column=1)
        Button(master,text="SAVE",command=stor_data,font="arial",bg="white").grid(row=3,column=4)
        Button(master,text="Submit",command=sub_data,font="arial",bg="green").grid(row=3,column=5)
def MCQ():
    master = Tk()
    master.configure(bg='#1e90ff')
    global e0,e1,e2,e3,e4,e5,e6,e7,e8,e9
    Label(master,text="Question Number: ",font="arial",bg="white").grid(row=0,column=0)
    e0=Entry(master,bg="#87cefa",bd=4,fg="black",width=30)
    e0.grid(row=0,column=1)
    e1="MCQ"
    Label(master,text="Quiz Id: ",font="arial",bg="white").grid(row=0,column=5)
    e2=Entry(master,bg="#87cefa",bd=4,fg="black",width=10)
    e2.grid(row=0,column=6)
    Label(master,text="Course Name: ",font="arial",bg="white").grid(row=0,column=7)
    e3=Entry(master,bg="#87cefa",bd=4,fg="black",width=50)
    e3.grid(row=0,column=8)
    Label(master,text="Question Statment: ",font="arial",bg="white").grid(row=1,column=0)
    e4=Entry(master,bg="#87cefa",bd=4,fg="black",width=30)
    e4.grid(row=1,column=1)
    Label(master,text="Option 1: ",font="arial",bg="white").grid(row=2,column=0)
    e5=Entry(master,bg="#87cefa",bd=4,fg="black",width=30)
    e5.grid(row=2,column=1)
    Label(master,text="Option 2: ",font="arial",bg="white").grid(row=3,column=0)
    e6=Entry(master,bg="#87cefa",bd=4,fg="black",width=30)
    e6.grid(row=3,column=1)
    Label(master,text="Option 3: ",font="arial",bg="white").grid(row=4,column=0)
    e7=Entry(master,bg="#87cefa",bd=4,fg="black",width=30)
    e7.grid(row=4,column=1)
    Label(master,text="Option 4: ",font="arial",bg="white").grid(row=5,column=0)
    e8=Entry(master,bg="#87cefa",bd=4,fg="black",width=30)
    e8.grid(row=5,column=1)
    Label(master,text="Correct Answer: ",font="arial",bg="white").grid(row=6,column=0)
    e9=Entry(master,bg="#87cefa",bd=4,fg="black",width=30)
    e9.grid(row=6,column=1)
    Button(master,text="SAVE",command=stor_data,font="arial",bg="white").grid(row=3,column=4)
    Button(master,text="Submit",command=sub_data,font="arial",bg="green").grid(row=3,column=5)
def sub_data():
    if (status):
        tkMessageBox.showinfo("Title","Quiz Submitted Successfully !!")
    else:
        tkMessageBox.showinfo("Title","Quiz Submission Failed!!")
def stor_data():
    global status
    quNum=int(e0.get())
    quType=e1
    quId=int(e2.get())
   # qId.append(quId)
    corName=e3.get()
   # corN.append(corName)
   # print corN,qId
    quStat=e4.get()

    if quType=="MCQ":
        op1=e5.get()
        op2=e6.get()
        op3=e7.get()
        op4=e8.get()
        corA=e9.get()
        sql="insert into question values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        status=cursor.execute(sql,(quNum,quType,quStat,op1,op2,op3,op4,corA,quId ,corName))
    elif quType=="T/F":
        op1=e5.get()
        op2=e6.get()
        corA=e9.get()
        op3=None
        op4=None
        sql="insert into question values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        status=cursor.execute(sql,(quNum,quType,quStat,op1,op2,op3,op4,corA,quId ,corName))
    elif quType=="NUMERIC":
        op1=None
        op2=None
        op3=None
        op4=None
        corA=e9.get()
        sql="insert into question values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        status=cursor.execute(sql,(quNum,quType,quStat,op1,op2,op3,op4,corA,quId ,corName))
def make_quiz():
    master = Tk()
    master.configure(bg='#1e90ff')
    Button(master,text="MCQ",command=MCQ,font="arial",bg="green").grid(row=3,column=5)
    Button(master,text="T/F",command=TF,font="arial",bg="green").grid(row=3,column=6)
    Button(master,text="NUMERIC",command=NUMERIC,font="arial",bg="green").grid(row=3,column=7)
def atmt_quiz():
    root = Tk()
    root.configure(bg='#1e90ff')
    root.minsize(200,50)
    global q0,q1
    Label(root,text="Quiz ID: ",font="arial",bg="white").grid(row=0,column=0)
    q0=Entry(root,bg="#87cefa",bd=4,fg="black",width=10)
    q0.grid(row=0,column=1)
    Label(root,text="Course Name: ",font="arial",bg="white").grid(row=0,column=3)
    q1=Entry(root,bg="#87cefa",bd=4,fg="black",width=40)
    q1.grid(row=0,column=4)
    Button(root,text="Submit",command=lambda : fet_quiz(root,q0.get(),q1.get()),font="arial",bg="green").grid(row=1,column=0)
def add_marks(x1):
    s1="insert into student values ('Student',120168,1,%s)"
    cursor.execute(s1,x1)
def chk(i,j):
    print i,j
#def mar():
 #   print
def fet_quiz(test1,q0,q1):
    marks=0
    master = Tk()
    master.configure(bg='#1e90ff')
    master.minsize(100,100)
    #scrollbar = Scrollbar(master)
    #scrollbar.pack(side=RIGHT, fill=Y)
    ##listbox = Listbox(master, yscrollcommand=scrollbar.set)
    #for i in range(1000):
    #    listbox.insert(END, str(i))
    #    listbox.pack(side=LEFT, fill=BOTH)

    id=int(q0)
    cn=str(q1).upper()

    try:
        sql="select * from question where qid=%s and _cour=%s"
        cursor.execute(sql,(id,cn))
        results=cursor.fetchall()
        x=[0,0]
        answer=[0,0]
        def nex():
            if x[0]>0:
                print x[1]
                if answer[0].get()==answer[1]:
                    x[1]+=1
                    print x[1]
            if x[0]>(len(results)-1):
                tkMessageBox.showinfo("Title",("Marks Obtained: %s" % x[1]))
                typ=str(x[1])
                add_marks(typ)
                return
            y=Label(master,text="Question: %s " %results[x[0]][2],bg='#1e90ff',justify=LEFT,anchor=W,font=("arial",12))
            y.pack()
            z=Label(master,text="1) %s" %results[x[0]][3],bg='#1e90ff')
            z.pack()
            a=Label(master,text="2) %s" %results[x[0]][4],bg='#1e90ff')
            a.pack()
            b=Label(master,text="3) %s" %results[x[0]][5],bg='#1e90ff')
            b.pack()
            c=Label(master,text="4) %s" %results[x[0]][6],bg='#1e90ff')
            c.pack()
            var=StringVar()
            ans=Entry(master,textvariable=var)
            ans.pack()
            answer[0]=ans
            answer[1]=results[x[0]][7]
            # print type(int(ans.get()))
            #if (ans.get()==results[x[0]][7]):
             #   x[1]+=1
            #print var.get()
           # sub=Button(master,text="Submit",command=sequence(nex,mar))
            sub=Button(master,text="Submit",command=nex,bg="white",font="arial")
            sub.pack()
            #chk(results[x[0][7]],var.get())

            x[0]+=1



        nex()
        #scrollbar.config(command=listbox.yview)
        test1.destroy()
        #marks=112
        #tkMessageBox.showinfo("Title",marks)

        # while(x<len(results)):
    except:
         print "Cannot locate data"
def slct_quiz():
    master=Tk()
    master.configure(bg="#f0e68c")
    master.minsize(600,600)
    master.geometry("500x100")
    master.title("Quiz Choices")
    op=Label(text="Following are the quizzez available for you", font=("arial",20), bg="white")
    op.pack()


    try:
        cursor.execute("select distinct qid,_cour from question")
        res=cursor.fetchall()
        for row in res:
            opt=Label(master,text="%s\t%s" %row,bg="#f0e68c", font=("arial",15))
            opt.pack()
    except:
        print "Cannot locate data"

    atmt_quiz()




    mainloop()
def _log(ref):

    val1=str(r0.get())
    val2=int(r1.get())
    roll=(val1.upper())
    ref.destroy()
    if (roll=="INSTRUCTOR") and (val2==12345):
        make_quiz()
    elif (roll=="STUDENT") and (val2==12345):
        slct_quiz()







if __name__ == '__main__':

    #_log()
    #make_quiz()
    #slct_quiz()
    #atmt_quiz()
    master = Tk()
    master.minsize(500,500)
    master.geometry("500x100")
    """path = "aaa.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    img = ImageTk.PhotoImage(Image.open(path))
    #master.configure(bg=img)
    #master.configure(bg='#cd5c5c')"""
    Label(master,text="Enter Roll: ",font="arial",bg="white").grid(row=5,column=0)
    r0=Entry(master,bg="white",width=30)
    r0.grid(row=5,column=3)
    Label(master,text="Enter Password: ",font="arial",bg="white").grid(row=15,column=0)
    r1=Entry(master,bg="white",show="*",width=30)
    r1.grid(row=15,column=3)
    Button(master,text="Log-in",command=lambda : _log(master),font="arial",bg="white").grid(row=10,column=9)


    mainloop()



########
