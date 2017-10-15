from Tkinter import *
import os
import tkMessageBox
import tkFont
import MySQLdb
import getpass
db=MySQLdb.connect("localhost","root","","quiz")
cursor=db.cursor()
#cursor.execute("create table question (qnum int (2),type varchar(10),ques varchar(80),op1 varchar(85),op2 varchar(85),op3 varchar(85),op4 varchar(85),corA varchar(85),qid int(5),"
#               "_cour varchar(45))")


"""
    ***         Description         ***
    : The program works in a way that there are 2 parts of it.
    The first part comprises of an instructor entity who has been stored as roll "Instructor"
    with his password "12345". The instructor his credentials and he is shown a compact menu where he has 
    got 3 choices:
    1) MCQs 2) T/F 3)NUMERIC
    Now, the type of question being stored depends upon the button clicked by instructor.
    After selecting the appropriate question type, the teacher then enters,
    1) Quiz ID= A unique id is given to ever quiz
    2) Course Name= The name of course from where quiz is being created 
     *These 2 entities are required to track a particular quiz
    3) Question Number
    4) Question Statement
    5) Available options
    6) Correct Answer
    On pressing the Submit button, Quiz is stored and if there is any issue regarding the submission of quiz, the Message
    box shows the error
    
    
    On the other hand, the student entity is stored as a roll="Student" and has password="12345"
    After login, the student is shown with the available list of quiz where he can select his desired Quiz
    by entering the Course name and quiz id. The quiz is retreived and after the student attempts the quiz,
    his marks are shown to him in Message Box and his marks are stored in database.
    
    
    Lets move on to see how the code works !!
"""

status=0
#variable to hold the status of query to submit the quiz.
#if the quiz is submitted successfully, it returns 1 else returns 0
def NUMERIC():
    master = Tk()
    master.configure(bg='#1e90ff')
    #Configuration of GUI screen for the question form for Numeric type questions
    global e0,e1,e2,e3,e4,e5,e6,e7,e8,e9
    Label(master,text="Question Number: ",font="arial",bg="white").grid(row=0,column=0)
    #Input box for taking input from instructor to store question number
    e0=Entry(master,bg="#87cefa",bd=4,fg="black",width=30)
    e0.grid(row=0,column=1)
    e1="NUMERIC"
    #Question type NUMERIC is stored in a variable e1
    Label(master,text="Quiz Id: ",font="arial",bg="white").grid(row=0,column=5)
    e2=Entry(master,bg="#87cefa",bd=4,fg="black",width=10)
    e2.grid(row=0,column=6)
    #Input box for taking input from instructor to store unique quiz id which is unique with every quiz
    Label(master,text="Course Name: ",font="arial",bg="white").grid(row=0,column=7)
    e3=Entry(master,bg="#87cefa",bd=4,fg="black",width=50)
    e3.grid(row=0,column=8)
    #Input box for taking input from instructor to store Course Name
    Label(master,text="Question Statment: ",font="arial",bg="white").grid(row=1,column=0)
    e4=Entry(master,bg="#87cefa",bd=4,fg="black",width=30)
    e4.grid(row=1,column=1)
    #Input box for taking input from instructor to store Question Statement
    Label(master,text="Correct Answer: ",font="arial",bg="white").grid(row=5,column=0)
    e9=Entry(master,bg="#87cefa",bd=4,fg="black",width=30)
    e9.grid(row=5,column=1)
    #Input box for taking input from instructor to store correct answer
    Button(master,text="SAVE",command=stor_data,font="arial",bg="white").grid(row=4,column=4)
    #Button to store variable values through a function call stor_data
    Button(master,text="Submit",command=sub_data,font="arial",bg="green").grid(row=4,column=5)
    #Button to store question in database in table QUIZ through function call sub_data
    return True
def TF():
    #The function definition goes same as mentioned in NUMERIC function except
    #2 more input boxes are on the screen since now we have to define options
    #for true and false statement
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
        return True
def MCQ():
     #The function definition goes same as mentioned in NUMERIC function except
     #3 more input boxes are on the screen since now we have to define options
    #for 4 Multiple Choices
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
    return True
def sub_data():
    """
    the function takes the value set in the variable status as 1 if the query for the submission of
    quiz is rendered successfully and 0 for a failure
    """
    if (status):
        """
        The tkMessageBox is a built-in function in tkMessage library for showing dialog boxes 
        """
        tkMessageBox.showinfo("Title","Quiz Submitted Successfully !!")
    else:
        tkMessageBox.showinfo("Title","Quiz Submission Failed!!")
    return True
def stor_data():
    """
        The function here takes values for all of the columns defined in database
        Quiz-Id, Question Number, Course Name, Question Statement, Possible Answers, Correct Answer
        These are all tuples defined in database to store relevant Quiz data

    """
    global status
    quNum=int(e0.get())
    #quNum: type-casts or converts a string returned by input box and converts into an Integer
    quType=e1
    quId=int(e2.get())
    #quId: type-casts or converts a string returned by input box and converts into an Integer
    corName=e3.get()
    quStat=e4.get()
    if quType=="MCQ":
        """
    Checking the type of question: If it is a MCQ, then the following code works !!
    """
        op1=e5.get()    #Option 1 for MCQ
        op2=e6.get()    #Option 2 for MCQ
        op3=e7.get()    #Option 3 for MCQ
        op4=e8.get()    #Option 4 for MCQ
        corA=e9.get()   #Correct answer for MCQ
        sql="insert into question values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #Sql query to store a MCQ into database table
        status=cursor.execute(sql,(quNum,quType,quStat,op1,op2,op3,op4,corA,quId ,corName))
    elif quType=="T/F":
        op1=e5.get()    #Option 1 for True/False
        op2=e6.get()    #Option 2 for True/False
        corA=e9.get()   #Correct Answer for True/False
        op3=None
        op4=None
        sql="insert into question values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #Sql query to store a MCQ into database table
        status=cursor.execute(sql,(quNum,quType,quStat,op1,op2,op3,op4,corA,quId ,corName))
    elif quType=="NUMERIC":
        op1=None    #Setting all tuples of answers to NULL(SQL)=None(python)
        op2=None
        op3=None
        op4=None
        corA=e9.get()
        sql="insert into question values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #Sql query to store a NUMERIC into database table
        status=cursor.execute(sql,(quNum,quType,quStat,op1,op2,op3,op4,corA,quId ,corName))
    return True
def make_quiz():
    master = Tk()
    master.configure(bg='#1e90ff')
    """
        Window and function definition above for the function which shows the appropriate window for
    selecting the type of qustion
    
    """
    Button(master,text="MCQ",command=MCQ,font="arial",bg="green").grid(row=3,column=5)
    Button(master,text="T/F",command=TF,font="arial",bg="green").grid(row=3,column=6)
    Button(master,text="NUMERIC",command=NUMERIC,font="arial",bg="green").grid(row=3,column=7)
def atmt_quiz():
    """
    Following is the function definition which fetches the quiz on selection made by the student
    Student enters the quiz-id and course name and presses Submit. After pressing the submit button, fet_quiz() function
    is called and it shows a screen where student attempts quiz

    """
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
    """
    Following is the function definition for storing the marks in database
    x1= is the argument passed by fet_quiz and its value is equal to the marks of student

    """
    s1="insert into student values ('Student',120168,1,%s)"
    cursor.execute(s1,x1)

def fet_quiz(test1,q0,q1):
    """
    fet_quiz is the actual function for student where he gets to see the
    quiz for him. Now it proceeds as:

    """
    marks=0 #Marks of student will be stored in this variable
    master = Tk()
    master.configure(bg='#1e90ff')
    master.minsize(300,300)
    #Window definition for displaying the quiz

    id=int(q0)
    cn=str(q1).upper()
    #id: Storing the Quiz Id provided by the student
    #cn: Storing the course name provided by the student

    try:
        sql="select * from question where qid=%s and _cour=%s"
        #sql query to fetch all of the rows from database where qid=id and _cour=cn
        cursor.execute(sql,(id,cn))
        results=cursor.fetchall()
        #fetchall function is predefined in MySQLdb where it converts a row into an associate array
        x=[0,0] #index 0 of list is the row index rows from database. Index 1: marks of student will be stored here
        answer=[0,0] #at index 0: answer given by student will be stored
        #at index 1: correct answer from database will be stored. Afterwards, both will be compared and decision about
        #correction will be taken
        def nex():
            """
            Function definition to fetch rows of questions 1 after another
            As the student presses "Submit", the very next question with its answers will be shown to him
            """
            if x[0]>0: #If : The rows of questions are not ended
                print x[1] #Console check to see the marks
                if answer[0].get()==answer[1]: #If the answer submitted is equal to correct answer
                    x[1]+=1 #Student gets 1 mark
                    print x[1]
            if x[0]>(len(results)-1):
                #Dialog box showing the marks to the student
                tkMessageBox.showinfo("Title",("Marks Obtained: %s" % x[1]))
                typ=str(x[1])
                add_marks(typ) #Passing the marks as arguments to the function where marks will be added to the database
                return
            """
                Showing the questions to student with their respective possible answers fetched from the rows
            """

            y=Label(master,text="Question: %s " %results[x[0]][2],bg='#1e90ff',justify=LEFT,anchor=W,font=("arial",12))
            y.pack()
            if (results[x[0]][3]!=None):
                z=Label(master,text="1) %s" %results[x[0]][3],bg='#1e90ff')
                z.pack()
            if (results[x[0]][4]!=None):
                a=Label(master,text="2) %s" %results[x[0]][4],bg='#1e90ff')
                a.pack()
            if (results[x[0]][5]!=None):
                b=Label(master,text="3) %s" %results[x[0]][5],bg='#1e90ff')
                b.pack()
            if (results[x[0]][6]!=None):
                c=Label(master,text="4) %s" %results[x[0]][6],bg='#1e90ff')
                c.pack()
            var=StringVar()
            ans=Entry(master,textvariable=var)
            ans.pack()
            answer[0]=ans
            answer[1]=results[x[0]][7]
            sub=Button(master,text="Submit",command=nex,bg="white",font="arial")
            sub.pack()
            x[0]+=1 #Jumping to the next questions



        nex()

        test1.destroy() #Closing the previous windows

    except:
         print "Cannot locate data"
    return True
def slct_quiz():
    """
    function definition to show the quiz list available for student
    :return:
    """
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
    return True
def _log(ref):
    """
    Login function where student and instructor entities are stored with credentionals
    :param ref:
    :return:
    """
    val1=str(r0.get())
    val2=int(r1.get())
    roll=(val1.upper())
    ref.destroy()
    if (roll=="INSTRUCTOR") and (val2==12345):
        make_quiz()
        return True
    elif (roll=="STUDENT") and (val2==12345):
        slct_quiz()
        return True




        #Main function starts here


if __name__ == '__main__':

    master = Tk()
    master.minsize(500,500)
    master.geometry("500x100")
    Label(master,text="Enter Roll: ",font="arial",bg="white").grid(row=5,column=0)
    r0=Entry(master,bg="white",width=30)
    r0.grid(row=5,column=3)
    Label(master,text="Enter Password: ",font="arial",bg="white").grid(row=15,column=0)
    r1=Entry(master,bg="white",show="*",width=30)
    r1.grid(row=15,column=3)
    #Lamba: keyword or more a function to pass parameters to function on a button called
    Button(master,text="Log-in",command=lambda : _log(master),font="arial",bg="white").grid(row=10,column=9)
    mainloop()


