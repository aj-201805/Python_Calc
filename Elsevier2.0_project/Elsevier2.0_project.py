while(True):
    from tkinter import*
    inp=int(input("PASSWORD :"))

    if inp==1234567890:
        try:
            # all imports
            from tkinter import*
            from tkinter import messagebox
            from python_math import *
            from PIL import Image, ImageTk
            # from tkcalendar import Calendar
            import datetime
            import phonenumbers
            from phonenumbers import geocoder, carrier, timezone

        except Exception as e:
            print(e)



        print("HELLO WORLD")

        try:
            # making main window
            root = Tk()
            root.geometry("323x477")
            root.title("Elsevier2.0_Project",)

        # all images
            img = ImageTk.PhotoImage(Image.open('download (2).gif'))
            img1 = ImageTk.PhotoImage(Image.open('calculating.png').resize((40, 40), ))
            img2 = ImageTk.PhotoImage(Image.open(
                'scientific-calculator (1).png').resize((40, 40), ))
            img3 = ImageTk.PhotoImage(Image.open('binary-code.png').resize((40, 40),))
            img4 = ImageTk.PhotoImage(Image.open('maths.png').resize((40, 40),))
            img6 = ImageTk.PhotoImage(Image.open('rectangle.png').resize((40, 40),))
            img7 = ImageTk.PhotoImage(Image.open('frame.png').resize((40, 40),))
            img8 = ImageTk.PhotoImage(Image.open('circle.png').resize((40, 40),))
            img9 = ImageTk.PhotoImage(Image.open('download.jpg').resize((40, 40),))
            img10 = ImageTk.PhotoImage(Image.open(
                'smartphone.png').resize((120, 120), ))

        # inputs
            data = StringVar()
            datanew = StringVar()
            data_for_s1 = " "
            data_for_s2 = " "
            data_for_s3 = " "
            area = " "

            val = ""
            A = 0
            operator = ""

        # functions for numbers and operators

            def btn1fn():
                global val
                val = val+"1"
                data.set(val)
                # datanew.set(val)

            def btn2fn():
                global val
                val = val+"2"
                data.set(val)
                # datanew.set(val)

            def btn3fn():
                global val
                val = val+"3"
                data.set(val)
                # datanew.set(val)

            def btn4fn():
                global val
                val = val+"4"
                data.set(val)
                # datanew.set(val)

            def btn5fn():
                global val
                val = val+"5"
                data.set(val)
                # datanew.set(val)

            def btn6fn():
                global val
                val = val+"6"
                data.set(val)
                # datanew.set(val)

            def btn7fn():
                global val
                val = val+"7"
                data.set(val)
                # datanew.set(val)

            def btn8fn():
                global val
                val = val+"8"
                data.set(val)
                # datanew.set(val)

            def btn9fn():
                global val
                val = val+"9"
                data.set(val)
                # datanew.set(val)

            def btn0fn():
                global val
                val = val+"0"
                data.set(val)
                # datanew.set(val)

            def btnaddfn():
                global val
                global operator
                global A
                A = int(val)
                operator = "+"
                val = val + "+"
                data.set(val)

            def btnminusfn():
                global val
                global operator
                global A
                A = int(val)
                operator = "-"
                val = val + "-"
                data.set(val)

            def btnmultfn():
                global val
                global operator
                global A
                A = int(val)
                operator = "x"
                val = val + "x"
                data.set(val)

            def btndivfn():
                global val
                global operator
                global A
                A = int(val)
                operator = "/"
                val = val + "/"
                data.set(val)

            def btncfn():
                global A
                global operator
                global val
                val = ""
                A = 0
                operator = ""
                data.set(val)

                # datanew.set(val)

            def btnsqrtfn():
                global val
                global operator
                global A
                A = int(val)
                operator = "√"
                val = "√"+val
                data.set(val)

            def btnsqrfn():
                global val
                global operator
                global A
                A = int(val)
                operator = "²"
                val = val+"²"
                data.set(val)

            def btnsqrtfn():
                global val
                global operator
                global A
                A = int(val)
                operator = "√"
                val = "√"+val
                data.set(val)

            def btncosfn():
                global val
                global operator
                global A
                A = int(val)
                operator = "cos"
                val = math.cos(int(val))
                data.set(val)

            def btntanfn():
                global val
                global operator
                global A
                A = int(val)
                operator = "tan"
                val = math.tan(int(val))
                data.set(val)

            def btnsinfn():
                global val
                global operator
                global A
                A = int(val)
                operator = "sin"
                val = math.sin(int(val))
                data.set(val)

            def btnpyfn():
                global val
                global operator
                global A
                A = float(val)
                operator = "π"
                val = (int(val))*3.14159265359
                data.set(val)

            def btnlnfn():
                global val
                global operator
                global A
                A = int(val)
                operator = "ln"
                val = math.log10(int(val))
                data.set(val)

            def btnlogfn():
                global val
                global operator
                global A
                A = int(val)
                operator = "log"
                val = math.log(int(val))
                data.set(val)

            def btnexpfn():
                global val
                global operator
                global A
                A = int(val)
                operator = "exp"
                val = math.exp(int(val))
                data.set(val)

            def btnsquarefn():
                global val
                global operator
                global A
                A = int(val)
                operator = "x²"
                val = int(val)*int(val)
                data.set(val)

            def result2():
                global val
                val = int(val)
                val = bin(val)[2:]
                datanew.set(val)

            # def result2():
            #     global val
            #     val = int(val)
            #     val = bin(val)[2:]
            #     datanew.set(val)
            #     str(val)

            def result():
                global A
                global operator
                global val
                val2 = val
                if operator == "+":
                    x = int((val2.split("+")[1]))
                    C = A+x
                    data.set(C)
                    val = str(C)

                elif operator == "-":
                    x = int((val2.split("-")[1]))
                    C = A-x
                    data.set(C)
                    val = str(C)

                elif operator == "x":
                    x = int((val2.split("x")[1]))
                    C = A*x
                    data.set(C)
                    val = str(C)

                elif operator == "√":
                    x = int(val2.split("√")[1])
                    C = math.sqrt(x)
                    data.set(C)
                    val = str(C)

                elif operator == "²":
                    x = int(val2.split("²")[0])
                    C = x*x
                    data.set(C)
                    val = str(C)

                elif operator == "/":
                    x = int((val2.split("/")[1]))
                    if x == 0:
                        messagebox.showerror("Error", "divison by 0 is not allowed")
                        A = ""
                        val = ""
                        data.set(val)

                    else:
                        C = int(A/x)
                        data.set(C)
                        val = str(C)

        # func for other windows

            def open_scientific_calc():
                win1 = Toplevel(root)
                win1.geometry("500x500")
                win1.title("Scientific Calculator ")
                img2 = ImageTk.PhotoImage(Image.open('scientific-calculator (1).png'))
                win1.iconphoto(False, img2)
                # img2l = Label(root, image=img2)

                nl2 = Label(win1, font="century 15", text="Scientific Calculator ")
                nl2.pack()

                nl = Label(win1,
                        font=('century', 25, 'bold'),
                        text="Label",
                        textvariable=data,
                        anchor=SE,
                        bg="White",
                        fg="black",
                        pady=40)
                nl.pack(expand=True, fill="both")

                nf1 = Frame(win1)
                nf1.pack(expand=True, fill="both")

                nf2 = Frame(win1)
                nf2.pack(expand=True, fill="both")

                nf3 = Frame(win1)
                nf3.pack(expand=True, fill="both")

                nf4 = Frame(win1)
                nf4.pack(expand=True, fill="both")

                btn_in = Button(nf1,
                                text="ln",
                                background="black",
                                foreground="white",

                                activebackground="black",
                                activeforeground="white",
                                font="century 20",
                                borderwidth=0,
                                relief=FLAT, command=btnlnfn)
                btn_in.pack(side="left", fill="both", expand=True)

                btn_sin = Button(nf1,
                                text="sin",
                                background="black",
                                foreground="white",

                                activebackground="black",
                                activeforeground="white",
                                font="century 20",
                                borderwidth=0,
                                relief=FLAT, command=btnsinfn)
                btn_sin.pack(expand=True, fill="both", side="left")
                btn_exp = Button(nf1,
                                text="exp",

                                background="black",
                                foreground="white",

                                activebackground="black",
                                activeforeground="white",
                                font="century 20",
                                borderwidth=0,
                                relief=FLAT, command=btnexpfn)
                btn_exp.pack(expand=True, fill="both", side="left")

                btn7 = Button(nf1,
                            text="7",

                            background="black",
                            foreground="white",

                            activebackground="black",
                            activeforeground="white",
                            font="century 20",
                            borderwidth=0,
                            relief=FLAT,
                            command=btn7fn)

                btn7.pack(expand=True, fill="both", side="left")
                btn8 = Button(nf1,
                            text="8",

                            background="black",
                            foreground="white",

                            activebackground="black",
                            activeforeground="white",
                            font="century 20",
                            borderwidth=0,
                            relief=FLAT,
                            command=btn8fn)
                btn8.pack(expand=True, fill="both", side="left")
                btn9 = Button(nf1,
                            text="9",

                            background="black",
                            foreground="white",

                            activebackground="black",
                            activeforeground="white",
                            font="century 20",
                            borderwidth=0,
                            relief=FLAT,
                            command=btn9fn)
                btn9.pack(expand=True, fill="both", side="left")
                btnmult = Button(nf1,
                                text="x",

                                background="black",
                                foreground="white",

                                activebackground="black",
                                activeforeground="white",
                                font="century 20",
                                borderwidth=0,
                                relief=FLAT,
                                command=btnmultfn)
                btnmult.pack(expand=True, fill="both", side="left")
                btn_log = Button(nf2,
                                text="log",

                                background="black",
                                foreground="white",

                                activebackground="black",
                                activeforeground="white",
                                font="century 20",
                                borderwidth=0,
                                relief=FLAT, command=btnlogfn)
                btn_log.pack(expand=True, fill="both", side="left")
                btn_cos = Button(nf2,
                                text="cos",

                                background="black",
                                foreground="white",

                                activebackground="black",
                                activeforeground="white",
                                font="century 20",
                                borderwidth=0,
                                relief=FLAT, command=btncosfn)
                btn_cos.pack(expand=True, fill="both", side="left")
                btn_py = Button(nf2,
                                text="π",
                                background="black",
                                foreground="white",

                                activebackground="black",
                                activeforeground="white",
                                font="algerian 20",
                                borderwidth=0,
                                relief=FLAT, command=btnpyfn)
                btn_py.pack(side="left", expand=True, fill="both", )

                btn4 = Button(nf2,
                            text="4",

                            background="black",
                            foreground="white",

                            activebackground="black",
                            activeforeground="white",
                            font="century 20",
                            borderwidth=0,
                            relief=FLAT, command=btn4fn)
                btn4.pack(expand=True, fill="both", side="left")
                btn5 = Button(nf2,
                            text="5",

                            background="black",
                            foreground="white",

                            activebackground="black",
                            activeforeground="white",
                            font="century 20",
                            borderwidth=0,
                            relief=FLAT, command=btn5fn)
                btn5.pack(expand=True, fill="both", side="left")
                btn6 = Button(nf2,
                            text="6",

                            background="black",
                            foreground="white",

                            activebackground="black",
                            activeforeground="white",
                            font="century 20",
                            borderwidth=0,
                            relief=FLAT, command=btn6fn)
                btn6.pack(expand=True, fill="both", side="left")
                btnminus = Button(nf2,
                                text="-",

                                background="black",
                                foreground="white",

                                activebackground="black",
                                activeforeground="white",
                                font="century 20",
                                borderwidth=0,
                                relief=FLAT, command=btnminusfn)
                btnminus.pack(expand=True, fill="both", side="left")
                btn_root = Button(nf3,
                                text="√",

                                background="black",
                                foreground="white",

                                activebackground="black",
                                activeforeground="white",
                                font="century 20",
                                borderwidth=0,
                                relief=FLAT, command=btnsqrtfn, padx=8)
                btn_root.pack(expand=True, fill="both", side="left")
                btn_tan = Button(nf3,
                                text="tan",

                                background="black",
                                foreground="white",

                                activebackground="black",
                                activeforeground="white",
                                font="century 20",
                                borderwidth=0,
                                relief=FLAT, command=btntanfn)
                btn_tan.pack(expand=True, fill="both", side="left")
                # btn_e = Button(nf3,
                #                text="e",
                #                background="black",
                #                foreground="white",

                #                activebackground="black",
                #                activeforeground="white",
                #                font="century 20",
                #                borderwidth=0,
                #                relief=FLAT, command=btnefn)
                # btn_e.pack(side="left", expand=True, fill="both")

                btn_xsqr = Button(nf3,
                                text="x²",
                                background="black",
                                foreground="white",

                                activebackground="black",
                                activeforeground="white",
                                font="century 20",
                                borderwidth=0,
                                relief=FLAT, command=btnsquarefn)
                btn_xsqr.pack(side="left", expand=True, fill="both", )

                btn1 = Button(nf3, text="1",
                            background="black",

                            foreground="white",

                            activebackground="black",
                            activeforeground="white",
                            font="century 20",
                            borderwidth=0,
                            relief=FLAT, command=btn1fn)
                btn1.pack(expand=True, fill="both", side="left")
                btn2 = Button(nf3,
                            text="2",

                            background="black",
                            foreground="white",

                            activebackground="black",
                            activeforeground="white",
                            font="century 20",
                            borderwidth=0,
                            relief=FLAT, command=btn2fn)
                btn2.pack(expand=True, fill="both", side="left")
                btn3 = Button(nf3,
                            text="3",

                            background="black",
                            foreground="white",
                            activebackground="black",
                            activeforeground="white",
                            font="century 20",
                            borderwidth=0,
                            relief=FLAT, command=btn3fn)
                btn3.pack(expand=True, fill="both", side="left")
                btnsum = Button(nf3,
                                text="+",
                                background="black",
                                foreground="white",

                                activebackground="black",
                                activeforeground="white",
                                font="century 20",
                                borderwidth=0,
                                relief=FLAT, command=btnaddfn)
                btnsum.pack(side="left", expand=True, fill="both", )

                # btn_exp = Button(nf4,
                #                  text="EXP",
                #                  background="black",
                #                  foreground="white",

                #                  activebackground="black",
                #                  activeforeground="white",
                #                  font="century 20",
                #                  borderwidth=0,
                #                  relief=FLAT, command=btnexpfn)
                # btn_exp.pack(side="left", expand=True, fill="both")

                btnequal = Button(nf4,
                                text="=",

                                background="black",
                                foreground="white",
                                activebackground="black",
                                activeforeground="white",
                                font="century 20",
                                borderwidth=0,
                                relief=FLAT, command=result)
                btnequal.pack(expand=True, fill="both", side="left")
                btn0 = Button(nf4,
                            text="0",

                            background="black",
                            foreground="white",

                            activebackground="black",
                            activeforeground="white",
                            font="century 20",
                            borderwidth=0,
                            relief=FLAT, command=btn0fn, )
                btn0.pack(expand=True, fill="both", side="left")

                btnc = Button(nf4,
                            text="c",

                            background="black",
                            foreground="white",

                            activebackground="black",
                            activeforeground="white",
                            font="century 20",
                            borderwidth=0,
                            relief=FLAT, command=btncfn)
                btnc.pack(expand=True, fill="both", side="left")

                btnndiv = Button(nf4,
                                text="/",

                                background="black",
                                foreground="white",

                                activebackground="black",
                                activeforeground="white",
                                font="century 20",
                                borderwidth=0,
                                relief=FLAT, command=btndivfn)
                btnndiv.pack(expand=True, fill="both", side="left")
                btnsquare = Button(nf4,
                                text="",

                                background="black",
                                foreground="white",

                                activebackground="black",
                                activeforeground="white",
                                font="century 20",
                                borderwidth=0,
                                relief=FLAT, command=btnsquarefn)
                btnsquare.pack(expand=True, fill="both", side="left")

                # label = Label(root, text="NEW HELLO WORLD")
                # label.pack(pady=10)
                # btn = Button(root, text="click me", command=openroot)
                # btn.pack()

            # def open_datecalc():
            #     win4 = Toplevel(root)
            #     win4.geometry("500x477")
            #     img = ImageTk.PhotoImage(Image.open('calculating.png'))
            #     win4.iconphoto(False, img)
            #     nl = Label(win4, text="Date Calculator",
            #                font="century 15", background="white", bd=1)
            #     nl.pack()
            #     cal = Calendar(win4, selectmode='day', year=2021, month=10, day=29, )
            #     cal.pack(pady=20,)
            #     # method fro add days

            #     def add_days():
            #         date_1 = datetime.datetime.strptime(cal.get_date(), "%m/%d/%y")
            #         end_date = date_1 + datetime.timedelta(days=int(days.get()))
            #         converted_date.config(
            #             text=f"Date: {end_date.strftime('%m/%d/%Y')}")
            #     # method to subtract days

            #     def subtract_days():
            #         date_1 = datetime.datetime.strptime(cal.get_date(), "%m/%d/%y")
            #         end_date = date_1 - datetime.timedelta(days=int(days.get()))
            #         converted_date.config(
            #             text=f"Date: {end_date.strftime('%m/%d/%Y')}")
            #     f1 = Frame(win4, )
            #     f1.pack()
            #     f2 = Frame(win4, )
            #     f2.pack()
            #     ldays = Label(f1,
            #                   text="Days",
            #                   bd=1,
            #                   bg="white",
            #                   fg="black",
            #                   width=20,
            #                   font="century ",
            #                   )
            #     ldays.pack(side="left", padx=5, expand=True, fill="both")
            #     days = Spinbox(f1,
            #                    from_=0, to=100000000000000000000000000000000,
            #                    font="century ",
            #                    bd=0,
            #                    background="white",
            #                    foreground="black",
            #                    relief=FLAT)
            #     days.pack(expand=True, fill="both")
            #     btn1 = Button(f2,
            #                   text="Add Days",
            #                   font="century",
            #                   bd=0,
            #                   relief=FLAT,
            #                   background="white",
            #                   foreground="black", command=add_days)
            #     btn1.pack(side="left", pady=12, expand=True, fill="both")
            #     btn2 = Button(f2,
            #                   text="Subtract Days",
            #                   font="century",
            #                   background="white",
            #                   foreground="black",
            #                   bd=0,
            #                   relief=FLAT, command=subtract_days)
            #     btn2.pack(padx=10, pady=12, expand=True, fill="both")
            #     converted_date = Label(win4, text="Date: ",
            #                            bd=0,
            #                            foreground="black",
            #                            relief=SOLID,
            #                            font="century",
            #                            width=30, )
            #     converted_date.pack(expand=True, fill="both")

            def open_binarycalc():
                win6 = Toplevel(root)
                win6.title("Binary Calculator")
                win6.geometry("323x477")
                img = ImageTk.PhotoImage(Image.open('binary-code.png'))
                win6.iconphoto(False, img)
                # denary setup
                f_for_denary = Frame(win6, background="black",)
                f_for_denary.pack(expand=True, fill="both", side="top")

                denarylabel = Label(f_for_denary, text="Denary",
                                    background="black", foreground="white", font="century 15")
                denarylabel.pack(expand=True, fill="both", side="left")

                binary_q_label = Label(f_for_denary, textvariable=data,
                                    background="black", foreground="white", font="century 15")
                binary_q_label.pack(expand=True, fill="both", side="left")
                # binary setup
                f_for_binary = Frame(win6, background="black",)
                f_for_binary.pack(expand=True, fill="both", side="top")

                binarylabel = Label(f_for_binary, text="Binary",
                                    background="black", foreground="white", font="century 15")
                binarylabel.pack(expand=True, fill="both", side="left")

                binary_q_label = Label(f_for_binary, textvariable=datanew,
                                    background="black", foreground="white", font="century 15")
                binary_q_label.pack(expand=True, fill="both", side="left")

                # Buttons Setup
                f_for_btns = Frame(win6, background="black",)
                f_for_btns.pack(expand=True, fill="both")

                f_for_btnr1 = Frame(f_for_btns, background="black")
                f_for_btnr1.pack(expand=True, fill="both")

                f_for_btnr2 = Frame(f_for_btns, background="black")
                f_for_btnr2.pack(expand=True, fill="both")

                f_for_btnr3 = Frame(f_for_btns, background="black")
                f_for_btnr3.pack(expand=True, fill="both")

                f_for_btnr4 = Frame(f_for_btns, background="black")
                f_for_btnr4.pack(expand=True, fill="both")

                btn1 = Button(f_for_btnr1,
                            text="1",
                            background="black",
                            foreground="white",
                            font="century 20", borderwidth=0, relief=FLAT, activebackground="black", activeforeground="white", command=btn1fn)
                btn1.pack(side="left", expand=True, fill="both")

                btn2 = Button(f_for_btnr1,
                            text="2",
                            background="black",
                            foreground="white",
                            font="century 20", borderwidth=0, relief=FLAT, activebackground="black", activeforeground="white", command=btn2fn)
                btn2.pack(side="left", expand=True, fill="both")

                btn3 = Button(f_for_btnr1,
                            text="3",
                            background="black",
                            foreground="white",
                            font="century 20", borderwidth=0, relief=FLAT, activebackground="black", activeforeground="white", command=btn3fn)
                btn3.pack(side="left", expand=True, fill="both")

                btn4 = Button(f_for_btnr2,
                            text="4",
                            background="black",
                            foreground="white",
                            font="century 20", borderwidth=0, relief=FLAT, activebackground="black", activeforeground="white", command=btn4fn)
                btn4.pack(side="left", expand=True, fill="both")

                btn5 = Button(f_for_btnr2,
                            text="5",
                            background="black",
                            foreground="white",
                            font="century 20", borderwidth=0, relief=FLAT, activebackground="black", activeforeground="white", command=btn5fn)
                btn5.pack(side="left", expand=True, fill="both")

                btn6 = Button(f_for_btnr2,
                            text="6",
                            background="black",
                            foreground="white",
                            font="century 20", borderwidth=0, relief=FLAT, activebackground="black", activeforeground="white", command=btn6fn)
                btn6.pack(side="left", expand=True, fill="both")

                btn7 = Button(f_for_btnr3,
                            text="7",
                            background="black",
                            foreground="white",
                            font="century 20", borderwidth=0, relief=FLAT, activebackground="black", activeforeground="white", command=btn7fn)
                btn7.pack(side="left", expand=True, fill="both")

                btn8 = Button(f_for_btnr3,
                            text="8",
                            background="black",
                            foreground="white",
                            font="century 20", borderwidth=0, relief=FLAT, activebackground="black", activeforeground="white", command=btn8fn)
                btn8.pack(side="left", expand=True, fill="both")

                btn9 = Button(f_for_btnr3,
                            text="9",
                            background="black",
                            foreground="white",
                            font="century 20", borderwidth=0, relief=FLAT, activebackground="black", activeforeground="white", command=btn9fn)
                btn9.pack(side="left", expand=True, fill="both")

                btnc = Button(f_for_btnr4,
                            text="CE",
                            background="black",
                            foreground="white",
                            font="century 20", borderwidth=0, relief=FLAT, activebackground="black", activeforeground="white", command=btncfn)
                btnc.pack(side="left", expand=True, fill="both")

                btn0 = Button(f_for_btnr4,
                            text="0",
                            background="black",
                            foreground="white",
                            font="century 20", borderwidth=0, relief=FLAT, activebackground="black", activeforeground="white", command=btn0fn)
                btn0.pack(side="left", expand=True, fill="both")

                btnequal = Button(f_for_btnr4,
                                text="=",
                                background="black",
                                foreground="white",
                                font="century 20", borderwidth=0, relief=FLAT, activebackground="black", activeforeground="white", command=result2)
                btnequal.pack(side="left", expand=True, fill="both")

            def open_rectanglecalc():
                win8 = Toplevel(root)
                win8.title("Rectangle Calculator")
                win8.geometry("323x477")
                img = ImageTk.PhotoImage(Image.open('rectangle.png'))
                win8.iconphoto(False, img)
                win8.configure(bg="black")

                def areaans():
                    l = length.get()
                    b = breadth.get()
                    l = int(l)
                    b = int(b)

                    result = l*b
                    area.set(result)

                f = Frame(win8)
                f.pack()
                f1 = Frame(f, background="black", pady=60)
                f1.pack(fill="both",)

                f2 = Frame(f, background="black", pady=60)
                f2.pack(fill="both")

                f3 = Frame(f, background="black", pady=60)
                f3.pack(fill="both")

                lngthlbl = Label(f1, text="Length", background="black",
                                foreground="white", borderwidth=0, relief=FLAT, font="century 15")
                lngthlbl.pack(fill="both", side="left")
                length = StringVar()
                lngthentry = Entry(f1, textvariable=length, font="century 15")
                lngthentry.pack(fill="both", side="right")

                brdthlbl = Label(f2, text="Breadth",
                                background="black", foreground="white", borderwidth=0, relief=FLAT, font="century 15")
                brdthlbl.pack(fill="both", side="left",)

                breadth = StringVar()
                brdthentry = Entry(f2, textvariable=breadth, font="century 15")
                brdthentry.pack(fill="both", side="right")

                area = StringVar()
                arealbl = Label(f3, font="century 15", textvariable=area,
                                background="black", foreground="white", borderwidth=0, relief=FLAT)
                arealbl.pack(fill="both", side="right")

                areabtn = Button(f3, font="century 12", text="Area", background="black",
                                foreground="white", borderwidth=4, relief=SUNKEN, command=areaans)
                areabtn.pack(fill="both", side="left")

            def open_Circlecalc():
                win7 = Toplevel(root)
                win7.title("Circle Calculator")
                win7.geometry("323x400")
                img = ImageTk.PhotoImage(Image.open('circle.png'))
                win7.iconphoto(False, img)
                win7.configure(bg="black")
                # win7.configure("black")

                fnw = Frame(win7, background="white")
                fnw.pack()

                ltitle = Label(fnw,
                            text="Circle Calculator",
                            font="century 13",
                            )
                ltitle.pack()

                f = Frame(win7, background="black")
                f.pack(pady=75, expand=True, fill="both")

                f1 = Frame(f, background="black")
                f1.pack(pady=10, expand=True, fill="both")

                # f2=Frame(f,background="black")
                # f2.pack(pady=10,expand=True,fill="both")

                # f3=Frame(f,background="black")
                # f3.pack(pady=10,expand=True,fill="both")

                f2 = Frame(f, background="black")
                f2.pack(pady=20, expand=True, fill="both")

                def ar():
                    r = radius.get()
                    r = int(r)

                    rslt = (22/7)*r
                    rslt = str(rslt)
                    area.set(rslt)

                radius = StringVar()
                area = StringVar()

                radiuslbl = Label(f1, text="Radius", font="century 12", borderwidth=0,
                                relief=FLAT, background="black", foreground="white")
                radiuslbl.pack(fill="both", expand=True)

                radiusentry = Entry(f1, textvariable=radius, font="century 12")
                radiusentry.pack(fill="both", expand=True)

                areabtn = Button(f2, text="Area", font="century 12", borderwidth=4,
                                relief=GROOVE, background="black", foreground="white", command=ar)
                areabtn.pack(fill="both", expand=True)

                arealbl = Label(f2, textvariable=area, font="century 12", padx=2)
                arealbl.pack(fill="both", expand=True)

            def open_squarecalc():
                win7 = Toplevel(root)
                win7.title("Square Calculator")
                win7.geometry("300x320")
                win7.resizable(0, 0)
                img = ImageTk.PhotoImage(Image.open('frame.png'))
                win7.iconphoto(False, img)

                side = StringVar()

                def areaans():
                    s = side.get()
                    # s = int(side)
                    result = 4*int(s)
                    area.set(result)

                f = Frame(win7)
                f.pack(expand=True, fill="both")
                f1 = Frame(f, background="black", pady=60)
                f1.pack(fill="both", expand=True)

                f2 = Frame(f, background="black", pady=60)
                f2.pack(fill="both")

                f3 = Frame(f, background="black", pady=60)
                f3.pack(fill="both")

                sidelbl = Label(f1, text="Length", background="black",
                                foreground="white", borderwidth=0, relief=FLAT, font="century 15")
                sidelbl.pack(fill="both", side="left")

                sideentry = Entry(f1, textvariable=side, font="century 15")
                sideentry.pack(fill="both", side="right")

                # brdthlbl = Label(f2, text="Breadth",
                #  background="black", foreground="white", borderwidth=0, relief=FLAT, font="century 15")
                # brdthlbl.pack(fill="both", side="left",)

                # breadth = StringVar()
                # brdthentry = Entry(f2, textvariable=breadth, font="century 15")
                # brdthentry.pack(fill="both", side="right")

                area = StringVar()
                arealbl = Label(f3, font="century 15", textvariable=area,
                                background="black", foreground="white", borderwidth=0, relief=FLAT)
                arealbl.pack(fill="both", side="right")

                areabtn = Button(f3, font="century 12", text="Area", background="black",
                                foreground="white", borderwidth=4, relief=SUNKEN, command=areaans)
                areabtn.pack(fill="both", side="left")

            def open_trianglecalc():
                win7 = Toplevel(root)
                win7.title("Triangle Calculator")
                win7.geometry("327x425")
                img = ImageTk.PhotoImage(Image.open('maths.png'))
                win7.iconphoto(False, img)
                win7.configure(bg="black")
                win7.resizable(0, 0)

                fnw = Frame(win7, background="white")
                fnw.pack()

                f = Frame(win7, background="black")
                f.pack(pady=75, expand=True, fill="both")

                f1 = Frame(f, background="black")
                f1.pack(pady=10, expand=True, fill="both")

                f2 = Frame(f, background="black")
                f2.pack(pady=10, expand=True, fill="both")

                f3 = Frame(f, background="black")
                f3.pack(pady=10, expand=True, fill="both")

                f4 = Frame(f, background="black")
                f4.pack(pady=20, expand=True, fill="both")

                side1 = StringVar()
                side2 = StringVar()
                side3 = StringVar()

                def new():
                    a = side1.get()
                    b = side2.get()
                    c = side3.get()
                    # while (True):
                    a == int(a)
                    b == int(b)
                    c == int(c)

                    a11 = int(a)
                    b2 = int(b)
                    c3 = int(c)

                    a11 = a
                    a11 = int(a)
                    b2 = b
                    b2 = int(b)
                    c3 = c
                    c3 = int(c)

                    print("a=", a11)
                    print("b=", b2)
                    print("c=", c3)

                    p = int(a11+b2+c3)
                    p == int(p)
                    print(p)

                    s = int(p/2)
                    print(s)
                    s == int(s)

                    if int(a) > int(s):
                        messagebox.showerror("Error", "HELLO WORLD")
                        # continue

                    elif int(b) > int(s):
                        messagebox.showerror("Error", "HELLO WORLD")
                        # continue

                    elif int(c) > int(s):
                        messagebox.showerror("Error", "HELLO WORLD")
                        # continue

                        # ans = (int(s)*(int(s)-int(a))(int(s)-int(b))(int(s)-int(c)))
                        # print(ans)
                        # ans = math.sqrt(ans)
                        # print(ans)
                        # > greater
                        # < lesser
                        # if a > s or p or b > s or p or c > s or p:
                        #     messagebox.showerror(
                        #         "Error", "A side can't be equal to or greater than it's perimeter")

                        # elif a < s or b < s or c < s:
                    a1 = int((int(s)-int(a)))
                    print(a1)
                    a2 = int((int(s)-int(b)))
                    print(a2)
                    a3 = int((int(s)-int(c)))
                    print(a3)

                    result = int(s)*(int(a1)*int(a2)*int(a3))
                    print(result)

                    mainresult = math.sqrt(result)
                    print(mainresult)

                    mainresult = str(mainresult)
                    area.set(mainresult)

                # ttllbl=Label(win7,text="Triangle calculator",background="white",foreground="black")
                # ttllbl.pack()

                ltitle = Label(fnw,
                            text="Triangle Calculator",
                            font="cambria 13",
                            )
                ltitle.pack()

                s1_label = Label(f1, text="Side 1 ", font="century 15", borderwidth=0,
                                relief=FLAT, background="black", foreground="white")
                s1_label.pack(fill="both", side="left", padx=25)
                s1_entry = Entry(f1, textvariable=side1, font="century 12",
                                borderwidth=0, relief=FLAT, foreground="black")
                s1_entry.pack(expand=True, fill="both")

                s2_label = Label(f2, text="Side 2 ", font="century 15", borderwidth=0,
                                relief=FLAT, background="black", foreground="white")
                s2_label.pack(fill="both", side="left", padx=25)
                s2_entry = Entry(f2, textvariable=side2, font="century 12",
                                borderwidth=0, relief=FLAT, foreground="black")
                s2_entry.pack(expand=True, fill="both")

                s3_label = Label(f3, text="Side 3 ", font="century 15", borderwidth=0,
                                relief=FLAT, background="black", foreground="white")
                s3_label.pack(fill="both", side="left", padx=25)
                s3_entry = Entry(f3, textvariable=side3, font="century 12",
                                borderwidth=0, relief=FLAT, foreground="black")
                s3_entry.pack(expand=True, fill="both")

                areabtn = Button(f4, text="Area", font="century 12", borderwidth=4, relief=SUNKEN, background="black",
                                foreground="white", command=new, activebackground="black", activeforeground="black", padx=25)
                areabtn.pack(expand=True, fill="both",)

                area = StringVar()
                arealbl = Label(f4, textvariable=area, font="century 15", borderwidth=0,
                                relief=FLAT, background="white", foreground="black", pady=20)
                arealbl.pack(side="left", expand=True, fill="both",)

            def open_mlttbl():
                win8 = Toplevel(root)
                win8.geometry("323x500")
                win8.title("Table")

                inp = StringVar()
                outp1 = StringVar()
                outp2 = StringVar()
                outp3 = StringVar()
                outp4 = StringVar()
                outp5 = StringVar()
                outp6 = StringVar()
                outp7 = StringVar()
                outp8 = StringVar()
                outp9 = StringVar()
                outp10 = StringVar()

                def new():

                    n = inp.get()
                    print(n)

                    a = n, "x", "1", "=", 1*int(n)
                    outp1.set(a)
                    print(a)
                    b = n, "x", "2", "=", 2*int(n)
                    outp2.set(b)
                    print(b)
                    c = n, "x", "3", "=", 3*int(n)
                    outp3.set(c)
                    print(c)
                    d = n, "x", "4", "=", 4*int(n)
                    outp4.set(d)
                    print(d)
                    e = n, "x", "5", "=", 5*int(n)
                    outp5.set(e)
                    print(e)
                    f = n, "x", "6", "=", 6*int(n)
                    outp6.set(f)
                    print(f)
                    g = n, "x", "7", "=", 7*int(n)
                    outp7.set(g)
                    print(g)
                    h = n, "x", "8", "=", 8*int(n)
                    outp8.set(h)
                    print(h)
                    i = n, "x", "9", "=", 9*int(n)
                    outp9.set(i)
                    print(i)
                    j = n, "x", "10", "=", 10*int(n)
                    outp10.set(j)
                    print(j)

                f = Frame(win8, background="black")
                f.pack(expand=True, fill="both")

                f1 = Frame(win8, background="black")
                f1.pack(expand=True, fill="both")

                f2 = Frame(win8, background="black")
                f2.pack(expand=True, fill="both")

                f3 = Frame(win8, background="black")
                f3.pack(expand=True, fill="both")

                nl = Label(f1, text="Multipilication Table!", background="white",
                        foreground="black", font="century 12")
                nl.pack(expand=True, fill="both", side="top")

                nl = Label(f1, text="Enter Your Digit", background="black",
                        foreground="white", font="century 15")
                nl.pack(expand=True, fill="both", pady=20)

                num = Entry(f1, textvariable=inp, background="white",
                            foreground="black", font="century 12")
                num.pack(expand=True, fill="both")

                l = Label(f2, textvariable=outp1, background="black",
                        foreground="white", font="century 17")
                l.pack(expand=True, anchor="w", padx=30)
                l = Label(f2, textvariable=outp2, background="black",
                        foreground="white", font="century 17")
                l.pack(expand=True, anchor="w", padx=30)
                l = Label(f2, textvariable=outp3, background="black",
                        foreground="white", font="century 17")
                l.pack(expand=True, anchor="w", padx=30)
                l = Label(f2, textvariable=outp4, background="black",
                        foreground="white", font="century 17")
                l.pack(expand=True, anchor="w", padx=30)
                l = Label(f2, textvariable=outp5, background="black",
                        foreground="white", font="century 17")
                l.pack(expand=True, anchor="w", padx=30)
                l = Label(f2, textvariable=outp6, background="black",
                        foreground="white", font="century 17")
                l.pack(expand=True, anchor="w", padx=30)
                l = Label(f2, textvariable=outp7, background="black",
                        foreground="white", font="century 17")
                l.pack(expand=True, anchor="w", padx=30)
                l = Label(f2, textvariable=outp8, background="black",
                        foreground="white", font="century 17")
                l.pack(expand=True, anchor="w", padx=30)
                l = Label(f2, textvariable=outp9, background="black",
                        foreground="white", font="century 17")
                l.pack(expand=True, anchor="w", padx=30)
                l = Label(f2, textvariable=outp10, background="black",
                        foreground="white", font="century 17")
                l.pack(expand=True, anchor="w", padx=30)

                btn = Button(f3, text="Get!", command=new,
                            background="black", font="century 17", foreground="white", borderwidth=0, relief=FLAT, activebackground="black", activeforeground="white")
                btn.pack(expand=True, fill="both")

            def open_standardcalc():
                win9 = Toplevel(root)
                win9.geometry("323x477")
                win9.title("CALCULATOR",)
                win9.iconphoto(False, img)

                # standard calc
                fnw = Frame(win9, background="white",)
                fnw.pack()

                ltitle = Label(fnw,
                            text="Standard Calculator",
                            font="cambria 13",
                            )
                ltitle.pack()

                l = Label(win9,
                        font=('century', 25, 'bold'),
                        text="Label",
                        textvariable=data,
                        anchor=SE,
                        bg="White",
                        fg="black",
                        pady=40
                        )
                l.pack(expand=True, fill="both")

                nfrm = Frame(win9, background="black")
                nfrm.pack(fill="both", anchor="e", expand=True)

                nfrm2 = Frame(win9, background="black", )
                nfrm2.pack(fill="both", side="left", )

                btnrow5 = Frame(win9, background="black")
                btnrow5.pack(expand=True, fill="both")

                btnrow1 = Frame(win9, background="black")
                btnrow1.pack(expand=True, fill="both",)

                btnrow2 = Frame(win9, background="black")
                btnrow2.pack(expand=True, fill="both")

                btnrow3 = Frame(win9, background="black")
                btnrow3.pack(expand=True, fill="both")

                btnrow4 = Frame(win9, background="black")
                btnrow4.pack(expand=True, fill="both")

                # img1 = ImageTk.PhotoImage(Image.open('calculator.png').resize((40, 40), ))
                # b1 = Button(nfrm, image=img1, background="black", foreground="white",
                #             activebackground="black", activeforeground="white", borderwidth=0, relief=FLAT, )
                # b1.pack(side="right", padx=10, expand=True, fill="both")
                # ______________________________________________________________________________________________________________________________________________________________________________________________

                # Image For Date calc

                # Button For Date Calc

                # b1 = Button(nfrm, image=img1, background="black", foreground="black",
                            # activebackground="black", activeforeground="black", borderwidth=0, relief=FLAT, command=open_datecalc, )
                # b1.pack(side="left",   fill="both")

                # ______________________________________________________________________________________________________________________________________________________________________________________________

                # Image For Scientific Calc

                # Button For Scientific Calc
                b2 = Button(nfrm, image=img2, background="black", foreground="black",
                            activebackground="black", activeforeground="black", borderwidth=0, relief=FLAT, command=open_scientific_calc)
                b2.pack(side="right", expand=True, fill="both")
                # ______________________________________________________________________________________________________________________________________________________________________________________________

                # Button For Binary calc
                b3 = Button(nfrm, image=img3,  background="black", foreground="black", activebackground="black",
                            activeforeground="black", borderwidth=0, relief=FLAT, command=open_binarycalc)
                b3.pack(expand=True, fill="both", side="right")

                # ______________________________________________________________________________________________________________________________________________________________________________________________

                b4 = Button(nfrm, image=img4,  background="black", foreground="black", activebackground="black",
                            activeforeground="black", borderwidth=0, relief=FLAT, command=open_trianglecalc)
                b4.pack(expand=True, fill="both", side="left")
                # ______________________________________________________________________________________________________________________________________________________________________________________________

                # img5 = ImageTk.PhotoImage(Image.open(
                #     'maths.png').resize((40, 40),))
                # b5 = Button(nfrm2, image=img5,  background="white", foreground="white", activebackground="white",
                #             activeforeground="white", borderwidth=0, relief=FLAT, command=open_squarecalc)
                # b5.pack(expand=True, fill="both", side="top")
                # _____________________________________________________________________________________________________________________________________________________________________________________

                b6 = Button(nfrm2, image=img6,  background="black", foreground="black", activebackground="black",
                            activeforeground="black", borderwidth=0, relief=FLAT, command=open_rectanglecalc)
                b6.pack(expand=True, fill="both", side="bottom")
                # ______________________________________________________________________________________________________________________________________________________________________________________________

                b7 = Button(nfrm2, image=img7,  background="black", foreground="black", activebackground="black",
                            activeforeground="black", borderwidth=0, relief=FLAT, command=open_squarecalc)
                b7.pack(expand=True, fill="both", side="top")
                # ______________________________________________________________________________________________________________________________________________________________________________________________

                b8 = Button(nfrm2, image=img8,  background="black", foreground="black", activebackground="black",
                            activeforeground="black", borderwidth=0, relief=FLAT, command=open_Circlecalc)
                b8.pack(expand=True, fill="both", side="bottom")

                b9 = Button(nfrm2, image=img9,  background="black", foreground="black", activebackground="black",
                            activeforeground="black", borderwidth=0, relief=FLAT, command=open_mlttbl)
                b9.pack(expand=True, fill="both", side="bottom")

                btnsqrt = Button(btnrow5,
                                text="√x",
                                bd=0,
                                font="century 20",
                                background="black",
                                foreground="white",
                                activebackground="black",
                                activeforeground="white",
                                command=btnsqrtfn)
                btnsqrt.pack(side=RIGHT, expand=True)

                btnsqr = Button(btnrow5,
                                text="x²",
                                bd=0,
                                font="century 20",
                                background="black",
                                foreground="white",
                                activebackground="black",
                                activeforeground="white",
                                command=btnsqrfn)

                btnsqr.pack(side=LEFT, expand=True)
                # row1
                btn7 = Button(btnrow1,
                            text="7",
                            bd=0,
                            font="century 20",
                            background="black",
                            fg="White",
                            activebackground="black",
                            activeforeground="white",
                            command=btn7fn,
                            )

                btn7.pack(side=LEFT, expand=True, )

                btn8 = Button(btnrow1,
                            text="8",
                            bd=0,
                            font="Century 20",
                            background="black",
                            fg="White",
                            activebackground="black",
                            activeforeground="white",
                            command=btn8fn)

                btn8.pack(side=LEFT, expand=True)

                btn9 = Button(btnrow1,
                            text="9",
                            bd=0,
                            font="Century 20",
                            background="black",
                            fg="White",
                            activebackground="black",
                            activeforeground="white",
                            command=btn9fn)

                btn9.pack(side=LEFT, expand=True)

                btnmult = Button(btnrow1,
                                text="x",
                                bd=0,
                                font="Century 20",
                                background="black",
                                fg="White",
                                activebackground="black",
                                activeforeground="white",
                                command=btnmultfn)
                btnmult.pack(side=LEFT, expand=True)

                # row2
                btn4 = Button(btnrow2, text="4",
                            bd=0,
                            font="Century 20",
                            background="black",
                            fg="White",
                            activebackground="black",
                            activeforeground="white",
                            command=btn4fn)

                btn4.pack(side=LEFT, expand=True)

                btn5 = Button(btnrow2,
                            text="5",
                            bd=0,
                            font="Century 20",
                            background="black",
                            fg="White",
                            activebackground="black",
                            activeforeground="white",
                            command=btn5fn)

                btn5.pack(side=LEFT, expand=True)

                btn6 = Button(btnrow2,
                            text="6",
                            bd=0,
                            font="Century 20",
                            background="black",
                            fg="White",
                            activebackground="black",
                            activeforeground="white",
                            command=btn6fn)

                btn6.pack(side=LEFT, expand=True)

                btnmin = Button(btnrow2,
                                text="-",
                                bd=0,
                                font="Century 20",
                                background="black",
                                fg="White",
                                activebackground="black",
                                activeforeground="white",
                                command=btnminusfn)

                btnmin.pack(side=LEFT, expand=True)

                # row 3
                btn1 = Button(btnrow3,
                            text="1",
                            bd=0,
                            font="Century 20",
                            background="black",
                            fg="White",
                            activebackground="black",
                            activeforeground="white",
                            command=btn1fn)

                btn1.pack(side=LEFT, expand=True)

                btn2 = Button(btnrow3,
                            text="2",
                            bd=0,
                            font="Century 20",
                            background="black",
                            fg="White",
                            activebackground="black",
                            activeforeground="white",
                            command=btn2fn)

                btn2.pack(side=LEFT, expand=True)

                btn3 = Button(btnrow3,
                            text="3",
                            bd=0,
                            font="Century 20",
                            background="black",
                            fg="White",
                            activebackground="black",
                            activeforeground="white",
                            command=btn3fn)

                btn3.pack(side=LEFT, expand=True)

                btnadd = Button(btnrow3,
                                text="+",
                                bd=0,
                                font="Century 20",
                                background="black",
                                fg="White",
                                activebackground="black",
                                activeforeground="white",
                                command=btnaddfn)
                btnadd.pack(side=LEFT, expand=True)

                # row 4

                btnequal = Button(btnrow4,
                                text="=",
                                bd=0,
                                font="Century 20",
                                background="black",
                                fg="White",
                                activebackground="black",
                                activeforeground="white",
                                command=result)
                btnequal.pack(side=LEFT, expand=True)

                btn0 = Button(btnrow4,
                            text="0",
                            bd=0,
                            font="Century 20",
                            background="black",
                            fg="White",
                            activebackground="black",
                            activeforeground="white",
                            command=btn0fn)

                btn0.pack(side=LEFT, expand=True)

                btnc = Button(btnrow4,
                            text="C",
                            bd=0,
                            font="Century 20",
                            background="black",
                            fg="white",
                            activebackground="black",
                            activeforeground="white",
                            command=btncfn)

                btnc.pack(side=LEFT, expand=True)

                btndiv = Button(btnrow4,
                                text="/",
                                bd=0,
                                font="Century 20",
                                background="black",
                                fg="White",
                                activebackground="black",
                                activeforeground="white",
                                command=btndivfn)
                btndiv.pack(side=LEFT, expand=True)

            def open_num_dtl_fndr():
                win10 = Toplevel(root)
                win10.geometry("600x550")
                win10.configure()
                win10.title("Phone Number Details Founder")

                img = ImageTk.PhotoImage(Image.open(
                    'smartphone.png').resize((40, 40), ))
                win10.iconphoto(False, img)

                def ans():
                    print("HELLO WORLD")
                    new = n.get()
                    # phonenumbers.parse(new, "CH")
                    # test = phonenumbers.is_valid_number(new)

                    num = phonenumbers.parse(new, "CH")
                    cntry = geocoder.description_for_number(num, "en")
                    num = phonenumbers.parse(new, "CH")
                    # lctn = phonenumbers.length_of_geographical_area_code(num, )
                    # lctn = phonenumbers.
                    num = phonenumbers.parse(new, "CH")
                    crrier = carrier.name_for_number(num, "RO")
                    num = phonenumbers.parse(new, "CH")
                    tzone = timezone.time_zones_for_geographical_number(num)
                    glctn= phonenumbers.length_of_geographical_area_code(num,)
                    cn.set(cntry)
                    # dn.set(lctn)
                    en.set(crrier)
                    fn.set(tzone)
                    gn.set(glctn)


                f_for_img = Frame(win10, background="#1f1d83")
                f_for_img.pack(fill="both", expand=True)

                l = Label(f_for_img, image=img10, background="#1f1d83")
                l.pack(expand=True, fill="both")

                ftitle = Frame(win10, background="#1f1d83")
                ftitle.pack(expand=True, fill="both")

                ttllbl = Label(win10, text="(:__Phone Number Details Founder__:)", background="black",
                            foreground="white", font="century 15 bold")
                ttllbl.pack(expand=True, fill="both")

                f = Frame(win10, background="#1f1d83")
                f.pack(fill="both", expand=True)

                f1 = Frame(f, background="#1f1d83")
                f1.pack(fill="both", expand=True)

                f2 = Frame(f, background="#1f1d83")
                f2.pack(fill="both", expand=True)

                f3 = Frame(f, background="#1f1d83")
                f3.pack(fill="both", expand=True)

                f4 = Frame(f, background="#1f1d83")
                f4.pack(fill="both", expand=True)

                f5 = Frame(f, background="#1f1d83")
                f5.pack(fill="both", expand=True)

                
                f51 = Frame(f, background="#1f1d83")
                f51.pack(fill="both", expand=True)

                f6 = Frame(f, background="#1f1d83")
                f6.pack(fill="both", expand=True)

                numberlbl = Label(f1, background="#1f1d83", foreground="white",
                                font="century 15", text="Enter any Number :")
                numberlbl.pack(fill="both", side="left", expand=True)

                n = StringVar()
                number = Entry(f1, textvariable=n, font="century 12 ")
                number.pack(fill="both", side="right", pady=20, expand=True)

                cn = StringVar()
                countrylbl = Label(f2, background="#1f1d83", foreground="white",
                                font="century 15", text="Country :")
                countrylbl.pack(fill="both", side="left", expand=True, pady=20,)

                countryname = Label(f2, background="white", foreground="#1f1d83",
                                    font="century 12", textvariable=cn)
                countryname.pack(fill="both", side="right", expand=True, pady=20,)

                # countrylbl = Label(f3, background="#1f1d83", foreground="white",
                #                    font="century 15", text="Location")
                # countrylbl.pack(fill="both", side="left", expand=True, pady=20,)

                # dn = StringVar()
                # countryname = Label(f3, background="white", foreground="#1f1d83",
                #                     font="century 12", textvariable=dn)
                # countryname.pack(fill="both", side="right", expand=True, pady=20,)

                en = StringVar()
                serviceproviderlbl = Label(f4, background="#1f1d83", foreground="white",
                                        font="century 15", text="Service Provider :")
                serviceproviderlbl.pack(
                    fill="both", side="left", expand=True, pady=20,)

                serviceprovider = Label(f4, background="white", foreground="#1f1d83",
                                        font="century 12", textvariable=en)
                serviceprovider.pack(fill="both", side="right", expand=True, pady=20,)

                fn = StringVar()
                timeznelbl = Label(f5, background="#1f1d83", foreground="white",
                                font="century 15", text="Timezone :")
                timeznelbl.pack(fill="both", side="left", expand=True, pady=20,)

                timezne = Label(f5, background="white", foreground="#1f1d83",
                                font="century 12", textvariable=fn)
                timezne.pack(fill="both", side="right", expand=True, pady=20,)

                
                gn = StringVar()
                timeznelbl = Label(f51, background="#1f1d83", foreground="white",
                                font="century 15", text="GEOLOCATION :")
                timeznelbl.pack(fill="both", side="left", expand=True, pady=20,)

                timezne = Label(f51, background="white", foreground="#1f1d83",
                                font="century 12", textvariable=fn)
                timezne.pack(fill="both", side="right", expand=True, pady=20,)

                getbtn = Button(f6, background="#1f1d83", foreground="white",
                                text="Get!", font="century 15", relief=FLAT, borderwidth=0, command=ans, activebackground="#1f1d83", activeforeground="white")
                getbtn.pack(expand=True, fill="both", pady=20,)

        # desigining first Window
            f0 = Frame(root, background="black")
            f0.pack(fill="both", expand=True)

            l1 = Label(f0,  font="cambria 12", background="black")
            l1.pack(fill="both", expand=True)

            f = Frame(root, background="black")
            f.pack(fill="both", expand=True)

            f1 = Frame(root,)
            f1.pack(fill="both", expand=True)

            f2 = Frame(root,)
            f2.pack(fill="both", expand=True)

            f3 = Frame(root,)
            f3.pack(fill="both", )

            l1 = Label(f, text="Welcome To My Program", font="cambria 15",
                    background="black", foreground="white")
            l1.pack(fill="both", expand=True)

            l1 = Label(f, text="This is my Elsevier2.0 Project ",
                    font="cambria 15", background="black", foreground="white")
            l1.pack(fill="both", expand=True)

            l1 = Label(f, text="Here I have Made Two things", font="cambria 15",
                    background="black", foreground="white")
            l1.pack(fill="both", expand=True)

            # l1 = Label(f, text="")
            # l1.pack()

            btn1 = Button(f1, text="Calculator!",
                        command=open_standardcalc,  borderwidth=3, relief=SUNKEN, font="cambria 12", background="black", foreground="white", activeforeground="black", activebackground="black")
            btn1.pack(fill="both", expand=True,)

            l = Label(f2, text="And", font="cambria 15")
            l.pack()
            btn2 = Button(f2, text="Numbers Details Founder!",
                        command=open_num_dtl_fndr,  borderwidth=3, relief=SUNKEN, font="cambria 12", background="black", foreground="white", activeforeground="black", activebackground="black")
            btn2.pack(fill="both",  expand=True,)

            l = Label(root, text="Made by - UMBRA!", font="magneto 12 bold")
            l.pack(fill="both")

            root.mainloop()

        except Exception as e:
            print(e)
            

        # a = input("Enter a number")
        # a = input("Enter a number")
        # a = input("Enter a number")
        # a = input("Enter a number")
        # a = input("Enter a number")
        # a = input("Enter a number")
        # a = input("Enter a number")
        # a = input("Enter a number")
        # a = input("Enter a number")

    elif inp!=1234567890:
        print("WRONG PASSWORD")
        inp2=input("""For exit type "exit" and if want to try again press enter button: """)
        if inp2=="exit":
            break
    
    # else:
        # pass