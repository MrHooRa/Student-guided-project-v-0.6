#                               #
#       KSU Student guided      #
#          Version 0.6          #
#       By: Salman Alessa       #
#       KSU ID: 439100011       #
#           7/17/2019           #
#       Last update: 7/23/19    #
#                               #

from tkinter import *
from sklearn import tree
import importlib
import csv

## I use these arrays because there is no database  ##
settings = ["KSU Student guided v0.6", "white", "0.6", 'uploads/icon5.ico']
user = ['Admin0', 'pass102', 'سلمان آل عيسى', '439100011@student.ksu.edu.sa', 1, 'السنة التحضيرية - المسار العلمي', 'لا يوجد']

# Summon lable with specifc options || How to use? => textIn(screen id, text, x, y, background color, font color, width, height, font, size, var name[DO NOT CHANGE IT IF YOU ARE NOT KNOW HOW IT IS WORK!])
def lableT(lDef = "",textDef = "", xDef = 0, yDef = 0, bgDef = "#57606f", fgDef = "#ffffff", widthDef = "50", heightDef = "2", fontDef = "Calibri", sizeDef = "13", varName = "lable"):
        varName = Label(lDef,
                text=textDef, 
                bg=bgDef, 
                fg=fgDef, 
                width=widthDef, 
                height=heightDef,
                bd = 3,
                font=(fontDef, sizeDef))
        varName.place(x=xDef , y=yDef)

# Summon buttn with specifc options || How to use? => btnIn(screen id, text, x, y, command, height, width, font, font color, background color, bold[just type "bold"], border[0,1,2,3,4], font size)
def btnT(bDef = "", textDef = "", xDef = 0, yDef = 0, commandDef = "", heightDef = "2", widthDef = "30", fontDef = "Calibri", fgDef = "#2f3542", bgDef = "#f1f2f6", bold = "", border = 3, size = 13):
        button = Button(bDef,
                text=textDef, 
                height=heightDef, 
                width=widthDef, 
                font=(fontDef, size, bold), 
                fg=fgDef, 
                bg=bgDef,
                borderwidth=border, 
                command = commandDef)
        button.place(x=xDef , y=yDef)

def first_screen():
        def goto_main_screen():
                first_screen.destroy()
                main_screen()
        first_screen = Tk()
        first_screen.configure(bg=settings[1] ,bd=2 , relief= GROOVE)
        first_screen.resizable(0,0)
        first_screen.title(settings[0])
        first_screen.geometry("690x468+350+300")
        first_screen.iconbitmap(settings[3])

        background_path = PhotoImage(file = "uploads/background6.png")
        background_img = Label(first_screen, image=background_path)
        background_img.place(x=-11, y=-2)
        # btnT(first_screen, "بدء", 247, 325, goto_main_screen, 2, 20, "calibri", "#dfe4ea", "#596275", "bold", 2)
        enter = Button(first_screen, text = "دخول", height = 1, width = 16, font = ("Calibri", 17, "bold"), fg = "#dfe4ea", bg = "#748995", border = 3, command = goto_main_screen)
        enter.place(x = 243, y = 334)
        
        first_screen.mainloop()

def main_screen(logout = 0):
        def login():
                userEG = userE.get()
                passEG = passE.get()
                if userEG == user[0] and passEG == user[1]:
                        if user[4] == 0:
                                main_screen.destroy()
                                accountNotComplete_screen()
                        else:
                                main_screen.destroy()
                                loginSuccessful_screen()
                else:
                        errorMsgLogin.configure(text = "إسم المستخدم وكلمة المرور غير صحيحة")
        def register():
                main_screen.destroy()
                register_screen()

        main_screen = Tk()
        main_screen.configure(bg=settings[1] ,bd=2 , relief= GROOVE)
        main_screen.resizable(0,0)
        main_screen.title(settings[0])
        main_screen.geometry("462x378+400+300")
        main_screen.iconbitmap(settings[3])

        lableT(main_screen, "دليل الطالب في جامعة الملك سعود", 0, 0, "#57606f", settings[1], 50, 2, "Calibri bold")
        lableT(main_screen, " مرحبا بك في برنامج دليل الطالب لجامعة الملك السعود\nللحصول على أفضل تجربة، رجاءً سجل دخولك", 5, 51, settings[1], "#222f3e", 49, 3, "Calibri", 13)
        lableT(main_screen, "═══════════════════════════", 0, 116, "White", "#57606f", 50, 1)
        lableT(main_screen, " :  اسم المستخدم", 310, 140, settings[1], "#227093", 12, 2, "Calibri bold", 13)
        lableT(main_screen, " :       كلمة المرور", 311, 190, settings[1], "#227093", 12, 2, "Calibri bold", 13)

        userE = StringVar()
        username = Entry(main_screen, textvariable = userE, bg = "#f1f2f6", width = 30, font = ("Calibri", 12), justify='center')
        username.place(x= 50, y =156)
    
        passE = StringVar()
        password = Entry(main_screen, textvariable = passE, bg = "#f1f2f6", width = 30, font = ("Calibri", 12), justify='center', show = "*")
        password.place(x= 50, y =206)

        btnT(main_screen, "تسجيل الدخول", 51, 261, login, 1, 26, "Calibri" ,settings[1], "#747d8c", "bold")
        lableT(main_screen, "ليس لديك حساب؟", 160, 300, settings[1], "#576574", 12, 2, "Calibri bold", 11)
        # lableT(main_screen, "انشاء حساب", 90, 300, settings[1], "#2e86de", 8, 2, "Calibri bold", 11)
        btnT(main_screen, "!انشاء حساب", 75, 305, register, 1, 9, 'Calibri', '#2e86de', settings[1], 'bold', 0)
        errorMsgLogin = Label(main_screen,
                text="", 
                bg=settings[1], 
                fg="#c0392b", 
                width=30, 
                height=1,
                bd = 3,
                font=("Calibri bold", 13))
        errorMsgLogin.place(x=32 , y=230)

        lableT(main_screen, "By: Salman Alessa\nVersion {}".format(settings[2]), 2, 347, settings[1], "#576574", 13, 1, "Calibri bold", 6)

        main_screen.mainloop()

def accountNotComplete_screen():
        accountNotComplete_screen = Tk()
        accountNotComplete_screen.configure(bg=settings[1] ,bd=2 , relief= GROOVE)
        accountNotComplete_screen.resizable(0,0)
        accountNotComplete_screen.title(settings[0])
        accountNotComplete_screen.geometry("462x278+400+300")
        accountNotComplete_screen.iconbitmap(settings[3])

def register_screen():
        def createNewAccount():
                userEG = userE.get()
                passEG = passE.get()
                emailEG = emailE.get()
                first_nameEG = first_nameE.get()
                last_nameEG = last_nameE.get()
                print("Create new account\n Username: ", userEG, "\nPassword: ", passEG, "\nEmail: ", emailEG, "\nFirst name: ", first_nameEG, "\nLast name: ", last_nameEG)

        register_screen = Tk()
        register_screen.configure(bg=settings[1] ,bd=2 , relief= GROOVE)
        register_screen.resizable(0,0)
        register_screen.title(settings[0])
        register_screen.geometry("462x378+400+300")
        register_screen.iconbitmap(settings[3])

        lableT(register_screen, "دليل الطالب في جامعة الملك سعود", 0, 0, "#57606f", settings[1], 50, 2, "Calibri bold")
        lableT(register_screen, " :  اسم المستخدم", 310, 60, settings[1], "#227093", 12, 2, "Calibri bold", 13)
        lableT(register_screen, " :     كــلــمة الـمـرور", 311, 110, settings[1], "#227093", 12, 2, "Calibri bold", 13)
        lableT(register_screen, " :  البريد الإلكتروني", 311, 160, settings[1], "#227093", 12, 2, "Calibri bold", 13)
        lableT(register_screen, " :         الاسم الاول", 311, 210, settings[1], "#227093", 12, 2, "Calibri bold", 13)
        lableT(register_screen, " :         الاسم الثاني", 311, 260, settings[1], "#227093", 12, 2, "Calibri bold", 13)

        userE = StringVar()
        username = Entry(register_screen, textvariable = userE, bg = "#f1f2f6", width = 30, font = ("Calibri", 12), justify='center')
        username.place(x= 50, y =76)
    
        passE = StringVar()
        password = Entry(register_screen, textvariable = passE, bg = "#f1f2f6", width = 30, font = ("Calibri", 12), justify='center', show = "*")
        password.place(x= 50, y =126)

        emailE = StringVar()
        email = Entry(register_screen, textvariable = emailE, bg = "#f1f2f6", width = 30, font = ("Calibri", 12), justify='center')
        email.place(x= 50, y =176)

        first_nameE = StringVar()
        fname = Entry(register_screen, textvariable = first_nameE, bg = "#f1f2f6", width = 30, font = ("Calibri", 12), justify='center')
        fname.place(x= 50, y =226)

        last_nameE = StringVar()
        lname = Entry(register_screen, textvariable = last_nameE, bg = "#f1f2f6", width = 30, font = ("Calibri", 12), justify='center')
        lname.place(x= 50, y =276)

        btnT(register_screen, "انشاء حساب جديد", 50, 320, createNewAccount, 1, 26, "Calibri" ,settings[1], "#747d8c", "bold")

        register_screen.mainloop()

def loginSuccessful_screen():
        def logout():
                loginSuccessful_screen.destroy()
                main_screen(1)
        def personalTest():
                loginSuccessful_screen.destroy()
                personalTest_screen(1)
        def jobDecisionTest():
                loginSuccessful_screen.destroy()
                jobDecision_screen()
        loginSuccessful_screen = Tk()
        loginSuccessful_screen.configure(bg=settings[1] ,bd=2 , relief= GROOVE)
        loginSuccessful_screen.resizable(0,0)
        loginSuccessful_screen.title(settings[0])
        loginSuccessful_screen.geometry("912x600+400+200")
        loginSuccessful_screen.iconbitmap(settings[3])

        lableT(loginSuccessful_screen, "دليل الطالب في جامعة الملك سعود", 0, 0, "#57606f", settings[1], 100, 2, "Calibri bold")
        lableT(loginSuccessful_screen, "أهلا وسهلا بك يا", 640, 62, "white", "black", 12, 1, "Calibri", 12)
        lableT(loginSuccessful_screen, user[2], 513, 61, 'white', 'black', 14, 1)
        lableT(loginSuccessful_screen, 'التخصص', 265, 63, 'white', 'black', 12, 1)
        if user[4] == 1:
                lableT(loginSuccessful_screen, user[5], 98, 63, 'white', 'green', 21, 1)
        elif user[4] == 0:
                lableT(loginSuccessful_screen, user[6], 214, 63, 'white', 'red', 8, 1)
        lableT(loginSuccessful_screen, "════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", 0, 92, "White", "#57606f", 100, 0)

        # btnT(loginSuccessful_screen, "اختبار تحديد التخصص", 110, 202, personalTest_screen, 4, 18, 'Calibri', '#ffffff', '#34495e', 'bold', 3, 16)
        btnT(loginSuccessful_screen, "اختبار تحديد الوظيفة", 110, 202, jobDecisionTest, 4, 18, 'Calibri', '#ffffff', '#34495e', 'bold', 3, 16)
        btnT(loginSuccessful_screen, "شؤون الطلاب", 571, 202, '', 4, 18, 'Calibri', '#ffffff', '#34495e', 'bold', 3, 16)
        btnT(loginSuccessful_screen, "السنة التحضيرية", 110, 404, '', 4, 18, 'Calibri', '#ffffff', '#34495e', 'bold', 3, 16)
        btnT(loginSuccessful_screen, "خروج", 571, 404, logout, 4, 18, 'Calibri', '#ffffff', '#c0392b', 'bold', 3, 16)

        lableT(loginSuccessful_screen, "By: Salman Alessa\nVersion {}".format(settings[2]), 2, 574, settings[1], "#576574", 13, 1, "Calibri bold", 6)

def personalTest_screen():
        personalTest_screen = Tk()
        personalTest_screen.configure(bg=settings[1] ,bd=2 , relief= GROOVE)
        personalTest_screen.resizable(0,0)
        personalTest_screen.title(settings[0])
        personalTest_screen.geometry("516x500+400+200")
        personalTest_screen.iconbitmap(settings[3])
        
        lableT(personalTest_screen, "دليل الطالب في جامعة الملك سعود", 0, 0, "#57606f", settings[1], 56, 2, "Calibri bold")
        lableT(personalTest_screen, "أهلا وسهلا بك يا", 640, 62, "white", "black", 12, 1, "Calibri", 12)

        personalTest_screen.mainloop()

def jobDecision_screen():
        def decision():
                heightV = heightJ.get()
                weightV = weightJ.get()
                sleepRateV = sleepRateJ.get()
                shoeSizeV = shoeSizeJ.get()
                ageV = ageJ.get()
                
                if heightV == "" or weightV == "" or sleepRateV == "" or shoeSizeV == "" or ageV == "":
                        errorMsgDecision.configure(text = "!جميع الحقول مطلوبة")
                else:
                        errorMsgDecision.configure(text = "")
                        def insertDecisionData(action, files=0):
                                if files == 1:
                                        f = open("logs/decisions.log", "a+")
                                        f.write(action + "\r\n")
                                        f.close()
                                if files == 2:
                                        f = open("uploads/csv/x_Vars.csv", "a+")
                                        f.write("\n" + action)
                                        f.close()
                                if files == 3:
                                        f = open("uploads/csv/y_Vars.csv", "a+")
                                        f.write("\n" + action)
                                        f.close()
                        def correctGuess():
                                insertDecisionData("{0}, {1}, {2}, {3}, {4}".format(heightV, weightV, sleepRateV, shoeSizeV, ageV), 2)
                                insertDecisionData("{0}".format(guess_format), 3)
                                jobDecision_screen.destroy()
                                loginSuccessful_screen()
                        def notCorrectGuess():
                                jobDecision_screen.destroy()
                                loginSuccessful_screen()
                                
                        makeGuess.configure("text")
                        
                        clf = tree.DecisionTreeClassifier()
                
                        with open('uploads/csv/x_Vars.csv', newline='') as csvfile:
                                X = list(csv.reader(csvfile))
                        with open('uploads/csv/y_Vars.csv', newline='') as csvfile:
                                Y = list(csv.reader(csvfile))

                        # train them on our data
                        clf = clf.fit(X, Y)
                        bestGuess = clf.predict([[heightV, weightV, sleepRateV, shoeSizeV, ageV]])

                        # compare their reusults and print the best one!
                        if bestGuess == "nota":
                                bestGuess = "غير ذلك"
                                guess_format = "nota"
                        elif bestGuess == "ge":
                                bestGuess = "موظف حكومي"
                                guess_format = "ge"
                        elif bestGuess == "pse":
                                bestGuess = "موظف في القطاع الخاص"
                                guess_format = "pse"
                        elif bestGuess == "st":
                                bestGuess = "طالب"
                                guess_format = "st"

                        guessLable.configure(text = "أفضل تخمين هو : {}".format(bestGuess))
                        btnT(jobDecision_screen, "تخمين صحيح", 50, 410, correctGuess, 1, 11, "Calibri" ,settings[1], "green", "bold")
                        btnT(jobDecision_screen, "تخمين خطأ", 190, 410, notCorrectGuess, 1, 11, "Calibri" ,settings[1], "red", "bold")

        jobDecision_screen = Tk()
        jobDecision_screen.configure(bg=settings[1] ,bd=2 , relief= GROOVE)
        jobDecision_screen.resizable(0,0)
        jobDecision_screen.title(settings[0])
        jobDecision_screen.geometry("400x470+400+200")
        jobDecision_screen.iconbitmap(settings[3])

        lableT(jobDecision_screen, "دليل الطالب في جامعة الملك سعود", 0, 0, "#57606f", settings[1], 43, 2, "Calibri bold")
        lableT(jobDecision_screen, " :           العمر", 202, 60, settings[1], "#227093", 16, 2, "Calibri bold", 13)
        lableT(jobDecision_screen, " :           الطول", 202, 110, settings[1], "#227093", 16, 2, "Calibri bold", 13)
        lableT(jobDecision_screen, " :            الوزن", 202, 160, settings[1], "#227093", 16, 2, "Calibri bold", 13)
        lableT(jobDecision_screen, " :  متوسط ساعات النوم", 228, 210, settings[1], "#227093", 16, 2, "Calibri bold", 13)
        lableT(jobDecision_screen, " :        مقاس الحذاء", 216, 260, settings[1], "#227093", 16, 2, "Calibri bold", 13)

        ageJ = StringVar()
        age = Entry(jobDecision_screen, textvariable = ageJ, bg = "#f1f2f6", width = 20, font = ("Calibri", 12), justify='center')
        age.place(x= 50, y =76)
        
        heightJ = StringVar()
        height = Entry(jobDecision_screen, textvariable = heightJ, bg = "#f1f2f6", width = 20, font = ("Calibri", 12), justify='center')
        height.place(x= 50, y =126)

        weightJ = StringVar()
        weight = Entry(jobDecision_screen, textvariable = weightJ, bg = "#f1f2f6", width = 20, font = ("Calibri", 12), justify='center')
        weight.place(x= 50, y =176)

        sleepRateJ = StringVar()
        sleepRate = Entry(jobDecision_screen, textvariable = sleepRateJ, bg = "#f1f2f6", width = 20, font = ("Calibri", 12), justify='center')
        sleepRate.place(x= 50, y =226)

        shoeSizeJ = StringVar()
        shoeSize = Entry(jobDecision_screen, textvariable = shoeSizeJ, bg = "#f1f2f6", width = 20, font = ("Calibri", 12), justify='center')
        shoeSize.place(x= 50, y =276)
        
        makeGuess = Button(jobDecision_screen,
                text="تـــخـــمــيــن", 
                height=1, 
                width=26, 
                font=("Calibri", 13, "bold"), 
                fg="white", 
                bg="#747d8c",
                borderwidth=3, 
                command = decision)
        makeGuess.place(x=50 , y=330)

        guessLable = Label(jobDecision_screen,
                text="", 
                bg=settings[1], 
                fg="#227093", 
                width=32, 
                height=1,
                bd = 3,
                font=("Calibri bold", 13))
        guessLable.place(x=35 , y=375)

        errorMsgDecision = Label(jobDecision_screen,
                text="", 
                bg=settings[1], 
                fg="#c0392b", 
                width=32, 
                height=1,
                bd = 3,
                font=("Calibri bold", 13))
        errorMsgDecision.place(x=40 , y=305)

        jobDecision_screen.mainloop()

first_screen()