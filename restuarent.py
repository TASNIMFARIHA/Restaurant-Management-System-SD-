#creat tkinte,r moduel

from tkinter import*
import os
from tkinter import messagebox
import PIL
from PIL import ImageTk
from PIL import Image




#creat bill class
class bill:
    #--init-- ta constructor r moto jeta initialize korbe object r state ke
    def __init__(self,root):   #self perameter ta python provide kore,r root ekta perameter niyechi
        self.root=root          #obj niyechi and self.root ta ekhane parent window
        self.root.geometry("1550x900")
        self.root.title("ORDER SYSTEM")


        #backgroung color r jonno ekta variable niyechi
        bg="dark blue"
        #Label ekta tkinter r class jeta use kora hoy text or image display korte
        title=Label(self.root,text="ORDER",bd=2,relief="groove",font=("ariel",30,"bold"),bg=bg,fg="white",pady=2).pack(fill=X)


        #................................variable.............................................................................

        #snacks
        self.pasta = IntVar()
        self.burger= IntVar()
        self.spaghetti = IntVar()
        self.noodles = IntVar()
        self.fazita = IntVar()
        self.chicken_fries= IntVar()
        self.nachos = IntVar()
        self.french_fries = IntVar()

        #drinks
        self.oreo_shake= IntVar()
        self.mint_lemon= IntVar()
        self.cold_drinks= IntVar()
        self.cold_coffee= IntVar()
        self.latte = IntVar()
        self.espresso= IntVar()
        self.tea= IntVar()
        self.water= IntVar()

        #price and vat

        self.m1=StringVar()
        self.m2=StringVar()
        self.m3 = StringVar()


        self.x = StringVar()

        #customer

        self.cname=StringVar()
        self.cphn=StringVar()
        self.cdate=StringVar()
        self.cadd=StringVar()

#........................................customer detailes............................................................

        #frame korar jonno Frame class use kora hoy
        f1=LabelFrame(self.root,text="CUSTOMER DETAILES",font=("ariel",18,"bold"),bg=bg,fg="white")
        #place use kora hoy label r x axis and y axis borabor joto ghor nibo oita place korte
        f1.place(x=0,y=55,width=1370,height=90)

        cname_lbl = Label(f1, text="NAME", bg=bg, fg="white", font=("ariel", 15, "bold")).grid(row=0, column=0, padx=20,
                                                                                               pady=5)
        # kono kichu entry korte entry class use kora hoy
        # textvariable sets the entry text to variavle
        cname_txt = Entry(f1, width=18, textvariable=self.cname, font=("ariel", 13), bd=2, relief=SUNKEN).grid(row=0,
                                                                                                               column=1,
                                                                                                               pady=5,
                                                                                                               padx=10)

        cphn_lbl = Label(f1, text=" PHONE NUMBER", bg=bg, fg="white", font=("ariel", 15, "bold")).grid(row=0, column=2,
                                                                                                       padx=20, pady=5)
        cphn_txt = Entry(f1, width=18, textvariable=self.cphn, font=("ariel", 13), bd=2, relief=SUNKEN).grid(row=0,
                                                                                                             column=3,
                                                                                                             pady=5,
                                                                                                             padx=10)

        cdate_lbl = Label(f1, text="DATE", bg=bg, fg="white", font=("ariel", 15, "bold")).grid(row=0, column=4, padx=20,
                                                                                               pady=5)
        cdate_txt = Entry(f1, width=18, textvariable=self.cdate, font=("ariel", 13), bd=2, relief=SUNKEN).grid(row=0,
                                                                                                               column=5,
                                                                                                               pady=5,
                                                                                                               padx=10)

        cadd_lbl = Label(f1, text="ADDRESS", bg=bg, fg="white", font=("ariel", 15, "bold")).grid(row=0, column=6, padx=20,
                                                                                               pady=5)
        cadd_txt = Entry(f1, width=18, textvariable=self.cadd, font=("ariel", 13), bd=2, relief=SUNKEN).grid(row=0,
                                                                                                               column=7,
                                                                                                               pady=20,
                                                                                                               padx=10)

        #.......................................snacks frame.......................................................................
        f2=LabelFrame(self.root,bd=3,relief="groove",text="SNACKS",font=("ariel",15,"bold"),bg=bg,fg="white")
        f2.place(x=220,y=146,width=300,height=330)

        pasta_lbl=Label(f2,text="PASTA",font=("ariel",12,"bold"),bg=bg,fg="white").grid(row=0,column=0,padx=10,pady=5)
        pasta_txt=Entry(f2,width=10,textvariable=self.pasta,font=("ariel",10,"bold"),bd=2,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
        burger_lbl = Label(f2,text="BURGER",font=("ariel",12,"bold"),bg=bg,fg="white").grid(row=1,column=0,padx=10,pady=5)
        burger_txt=Entry(f2,width=10,textvariable=self.burger,font=("ariel",10,"bold"),bd=2,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)
        spaghetti_lbl = Label(f2,text="SPAGHETTI",font=("ariel",12,"bold"),bg=bg,fg="white").grid(row=2,column=0,padx=10,pady=5)
        spaghetti_txt=Entry(f2,width=10,textvariable=self.spaghetti,font=("ariel",10,"bold"),bd=2,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=5)
        noodles_lbl = Label(f2,text="NOODLES",font=("ariel",12,"bold"),bg=bg,fg="white").grid(row=3,column=0,padx=10,pady=5)
        noodles_txt=Entry(f2,width=10,textvariable=self.noodles,font=("ariel",10,"bold"),bd=2,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=5)
        fazita_lbl =Label (f2,text="FAZITA",font=("ariel",12,"bold"),bg=bg,fg="white").grid(row=4,column=0,padx=10,pady=5)
        fazita_txt=Entry(f2,width=10,textvariable=self.fazita,font=("ariel",10,"bold"),bd=2,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=5)
        chicken_fries_lbl =Label(f2,text="CHICKEN FRIES",font=("ariel",12,"bold"),bg=bg,fg="white").grid(row=5,column=0,padx=10,pady=5)
        chicken_fries_txt=Entry(f2,width=10,textvariable=self.chicken_fries,font=("ariel",10,"bold"),bd=2,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=5)
        nachos_lbl=Label(f2,text="NACHOS",font=("ariel",12,"bold"),bg=bg,fg="white").grid(row=6,column=0,padx=10,pady=5)
        nachos_txt=Entry(f2,width=10,textvariable=self.nachos,font=("ariel",10,"bold"),bd=2,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=5)
        french_fries_lbl=Label (f2,text="FRENCH FRIES",font=("ariel",12,"bold"),bg=bg,fg="white").grid(row=7,column=0,padx=10,pady=5)
        french_fries_txt=Entry(f2,width=10,textvariable=self.french_fries,font=("ariel",10,"bold"),bd=2,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=5)

 #...............................................drinks frame.......................................................................
        f3 = LabelFrame(self.root, bd=3, relief="groove", text="DRINKS", font=("ariel", 15, "bold"), bg=bg,fg="white")
        f3.place(x=520, y=146,width=300,height=330)

        oreo_shake_lbl=Label(f3,text="OREO SHAKE",font=("ariel",12,"bold"),bg=bg,fg="white").grid(row=0,column=0,padx=10,pady=5)
        oreo_shake_txt=Entry(f3,width=10,textvariable=self.oreo_shake,font=("ariel",10,"bold"),bd=2,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
        mint_lemon_lbl=Label(f3,text="MINT LEMON",font=("ariel",12,"bold"),bg=bg,fg="white").grid(row=1,column=0,padx=10,pady=5)
        mint_lemon_txt=Entry(f3,width=10,textvariable=self.mint_lemon,font=("ariel",10,"bold"),bd=2,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)
        cold_drinks_lbl=Label(f3,text="COLD DRINKS",font=("ariel",12,"bold"),bg=bg,fg="white").grid(row=2,column=0,padx=10,pady=5)
        cold_drinks_txt=Entry(f3,width=10,textvariable=self.cold_drinks,font=("ariel",10,"bold"),bd=2,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=5)
        cold_coffee_lbl=Label(f3,text="COLD COFFEE",font=("ariel",12,"bold"),bg=bg,fg="white").grid(row=3,column=0,padx=10,pady=5)
        cold_coffee_txt=Entry(f3,width=10,textvariable=self. cold_coffee,font=("ariel",10,"bold"),bd=2,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=5)
        latte_lbl=Label(f3,text="LATTE",font=("ariel",12,"bold"),bg=bg,fg="white").grid(row=4,column=0,padx=10,pady=5)
        latte_txt=Entry(f3,width=10,textvariable=self.latte,font=("ariel",10,"bold"),bd=2,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=5)
        espresso_lbl=Label(f3,text="ESPRESSO",font=("ariel",12,"bold"),bg=bg,fg="white").grid(row=5,column=0,padx=10,pady=5)
        espresso_txt=Entry(f3,width=10,textvariable=self. espresso,font=("ariel",10,"bold"),bd=2,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=5)
        tea_lbl=Label(f3,text="TEA",font=("ariel",12,"bold"),bg=bg,fg="white").grid(row=6,column=0,padx=10,pady=5)
        tea_txt=Entry(f3,width=10,textvariable=self. tea,font=("ariel",10,"bold"),bd=2,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=5)
        water_lbl=Label(f3,text="WATER",font=("ariel",12,"bold"),bg=bg,fg="white").grid(row=7,column=0,padx=10,pady=5)
        water_txt=Entry(f3,width=10,textvariable=self. water,font=("ariel",10,"bold"),bd=2,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=5)

#.............................................bill frame....................................................................
        f4 = Frame(self.root,bd=1,relief="groove")
        f4.place(x=820, y=147, width=320, height=329)

        bill_title=Label(f4,text="ORDER CONFERMATION",font=("ariel",15,"bold"),bg=bg,fg="white",bd=2,relief="groove").pack(fill=X)
        #scrollbar
        scrol_y=Scrollbar(f4,orient=VERTICAL)       #scrollbar r syntax
        self.txtarea= Text(f4, yscrollcommand=scrol_y.set)   #txtbox niyechi,set ta connect kore scrollbark another widget r sathe
        #pack method tekk tk to fill the window
        scrol_y.pack(side=RIGHT, fill=Y)                     #scrollbar k pack kore diyechi
        scrol_y.config(command=self.txtarea.yview)           #config is used to access an object's attributes after its initialisation
        self.txtarea.pack(side=RIGHT)                        #txtbox k pack kore diyechi

#...................................cost frame.............................................................................
        f5 = LabelFrame(self.root, bd=3, relief="groove", text="BILL", font=("ariel", 15, "bold"), bg=bg, fg="white")
        f5.place(x=220, y=480, width=920, height=220)

        m1_lbl=Label(f5,text="SERVICE CHARGE",font=("ariel", 15, "bold"), bg=bg, fg="white").grid(row=0,column=0,padx=50,pady=10)
        m1_txt=Entry(f5,width=10,textvariable=self.m2,font=("ariel", 12, "bold"),bd=2,relief=SUNKEN ).grid(row=0,column=1,padx=1)

        m2_lbl =Label(f5, text="PRICE", font=("ariel", 15, "bold"), bg=bg, fg="white").grid(row=1, column=0, padx=50,)
        m2_txt =Entry(f5, width=10 ,textvariable=self.m1, font=("ariel", 12, "bold"), bd=2, relief=SUNKEN).grid(row=1,column=1,padx=1)

        m3_lbl = Label(f5, text="TOTAL", font=("ariel", 15, "bold"), bg=bg, fg="white").grid(row=2, column=0,
                                                                                                      padx=5, pady=5)
        m3_txt = Entry(f5, width=10, textvariable=self.m3, font=("ariel", 12, "bold"), bd=2, relief=SUNKEN).grid(row=2,
                                                                                                                 column=1,
                                                                                                                 padx=1)
        m4_lbl=Radiobutton(f5,text="Cash on delivery", font=("ariel", 15, "bold"),bg=bg,value="Cash on delivery",variable=self.x)\
            .grid(row=3, column=0,padx=5, pady=5)



        m5_lbl =Radiobutton(f5, text="Bkash", font=("ariel", 15, "bold"), bg=bg,value="Bkash",variable=self.x) \
            .grid(row=3, column=1, padx=5, pady=5)

        m6_lbl = Radiobutton(f5, text="Cash", font=("ariel", 15, "bold"), bg=bg, value="cash", variable=self.x) \
            .grid(row=3, column=2, padx=5, pady=5)

        #............................................button frame......................................................................

        btn_F= Frame(f5,bg=bg,relief="groove")
        btn_F.place(x=395, width=500, height=70)


        #button create korte Button class use kora hoy
        total_btn = Button(btn_F, text="TOTAL",command=self.total, bg=bg, fg="white", bd=2, width=8,font=("ariel", 12, "bold")).grid(row=0,column=0,padx=15,pady=20)
        bill_btn = Button(btn_F, text="CONFIRM",command=self.bill, bg=bg, fg="white", bd=2, width=10,font=("ariel", 12, "bold")).grid(row=0, column=2,padx=15,pady=20)
        clear_btn = Button(btn_F, text="CLEAR",command=self.clear, bg=bg, fg="white", bd=2, width=8,font=("ariel", 12, "bold")).grid(row=0, column=1,padx=15,pady=20)
        exit_btn = Button(btn_F, text="EXIT",command=self.exit, bg=bg, fg="white", bd=2, width=8,font=("ariel", 12, "bold")).grid(row=0, column=3,padx=15,pady=20)
        self.welcome()


    #total button r moddhe shob gular price jog kore ashbe
    def total(self):
        #snacks.price new ekta obj niyechi and oita = shb snacks r price r total
        #pasta=200,burger=180,chowmien=150,noodles=120,fazita=130,chicken fries=220,nachos=160,french fries=100


        self.pa_price=(self.pasta.get()*200)
        self.bu_price=(self.burger.get()*180)
        self.sp_price=(self.spaghetti.get()*150)
        self.no_price=(self.noodles.get()*120)
        self.fa_price=(self.fazita.get()*130)
        self.cf_price=(self.chicken_fries.get()*220)
        self.na_price=(self.nachos.get()*160)
        self.ff_price=(self.french_fries.get()*100)

        # oreo shake=180,mint lemon=100,cold drinks=25,cold coffee=120,latta=150,espresso=60,tea=40,water=20
        # snacks.price new ekta obj niyechi and oita = shb snacks r price r total

        self.os_price = (self.oreo_shake.get() * 180)
        self.ml_price = (self.mint_lemon.get() * 100)
        self.cd_price = (self.cold_drinks.get() * 25)
        self.cc_price = (self.cold_coffee.get() * 120)
        self.l_price = (self.latte.get() * 150)
        self.e_price = (self.espresso.get() * 60)
        self.t_price = (self.tea.get() * 40)
        self.w_price = (self.water.get() * 20)

        #total price
        self.price=((self.pa_price)+
                         (self.bu_price)+
                         (self.sp_price)+
                         (self.no_price)+
                         (self.fa_price)+
                         (self.cf_price)+
                         (self.na_price)+
                         (self.ff_price)+
                         (self.os_price) +
                         (self.ml_price) +
                         (self.cd_price) +
                         (self.cc_price) +
                         (self.l_price) +
                         (self.e_price) +
                         (self.t_price) +
                         (self.w_price)
                         )

        self.m1.set("TK "+str(self.price))

        self.service_charge=(60)
        self.m2.set("TK "+str(self.service_charge))

        self.total_price=(self.price+self.service_charge)
        self.m3.set("TK "+str(self.total_price))


    def welcome(self):
        #line 1 thekke end line porjonto delete kore debe
        self.txtarea.delete("1.0",END)
        #insert kore string k ekta specified location/index e,end ta ekhane index
        self.txtarea.insert(END, "\t WELCOME TO SNACK ATTACK")
        self.txtarea.insert(END, f"\n CUSTOMER NAME :{self.cname.get()}")
        self.txtarea.insert(END, f"\n PHONE NUMBER :{self.cphn.get()}")
        self.txtarea.insert(END, f"\n DATE :{self.cdate.get()}")
        self.txtarea.insert(END, f"\n ADDRESS :{self.cadd.get()}")
        self.txtarea.insert(END, f"\n PAY VIA :{self.x.get()}")
        self.txtarea.insert(END, f"\n=====================================")
        self.txtarea.insert(END, f"\n Product\t\tQTY\tPrice")
        self.txtarea.insert(END, f"\n=====================================")

    def bill(self):
        if self.cname.get()=="" or self.cphn.get()=="" or self.cdate.get()=="" or self.cadd.get()=="":
            messagebox.showerror("Error","Customer details are must")
        else:
            self.welcome()

            if self.pasta.get()!=0:
                self.txtarea.insert(END, f"\n Pasta\t\t{self.pasta.get()}\t{self.pa_price}")
            if self.burger.get()!=0:
                self.txtarea.insert(END, f"\n Burger\t\t{self.burger.get()}\t{self.bu_price}")
            if self.spaghetti.get()!=0:
                self.txtarea.insert(END, f"\n Spaghetti\t\t{self.spaghetti.get()}\t{self.sp_price}")
            if self.noodles.get()!=0:
                self.txtarea.insert(END, f"\n Noodles\t\t{self.noodles.get()}\t{self.no_price}")
            if self.fazita.get() != 0:
                self.txtarea.insert(END, f"\n Fazita\t\t{self.fazita.get()}\t{self.fa_price}")
            if self.chicken_fries.get() != 0:
                    self.txtarea.insert(END, f"\n Chicken fries\t\t{self.chicken_fries.get()}\t{self.cf_price}")
            if self.nachos.get()!=0:
                self.txtarea.insert(END, f"\n Nachos\t\t{self.nachos.get()}\t{self.na_price}")
            if self.french_fries.get() != 0:
                self.txtarea.insert(END, f"\n French fries\t\t{self.french_fries.get()}\t{self.ff_price}")

            if self.oreo_shake.get() != 0:
                self.txtarea.insert(END, f"\n Oreo shake\t\t{self.oreo_shake.get()}\t{self.os_price}")
            if self.mint_lemon.get() != 0:
                self.txtarea.insert(END, f"\n Mint lemon\t\t{self.mint_lemon.get()}\t{self.ml_price}")
            if self.cold_drinks.get() != 0:
                self.txtarea.insert(END, f"\n Cold drinks\t\t{self.cold_drinks.get()}\t{self.cd_price}")
            if self.cold_coffee.get() != 0:
                self.txtarea.insert(END, f"\n Cold coffee\t\t{self.cold_coffee.get()}\t{self.cf_price}")
            if self.latte.get() != 0:
                self.txtarea.insert(END, f"\n Latte\t\t{self.latte.get()}\t{self.l_price}")
            if self.espresso.get() != 0:
                self.txtarea.insert(END, f"\n Espresso\t\t{self.espresso.get()}\t{self.e_price}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t{self.t_price}")
            if self.water.get() != 0:
                self.txtarea.insert(END, f"\n Water\t\t{self.water.get()}\t{self.w_price}")

            self.txtarea.insert(END, f"\n-------------------------------------")
            if self.m2.get!="TK 0.0":
                self.txtarea.insert(END, f"\n Service Charge\t\t\t{self.m2.get()}")
            self.txtarea.insert(END, f"\n-------------------------------------")
            self.txtarea.insert(END, f"\n \tConfirm Your Order")
            self.save()

    def clear(self):
        # snacks
        self.pasta.set(0)
        self.burger .set(0)
        self.spaghetti.set(0)
        self.noodles.set(0)
        self.fazita .set(0)
        self.chicken_fries .set(0)
        self.nachos .set(0)
        self.french_fries.set(0)

        # drinks
        self.oreo_shake .set(0)
        self.mint_lemon .set(0)
        self.cold_drinks .set(0)
        self.cold_coffee.set(0)
        self.latte .set(0)
        self.espresso.set(0)
        self.tea .set(0)
        self.water.set(0)

        #price

        self.m1.set(0)
        self.m2.set(0)
        self.m3.set(0)

        self.x.set("")
        # customer

        self.cname.set("")
        self.cphn .set("")
        self.cdate.set("")
        self.cadd .set("")


    def exit(self):
        #destroy method destroy kore dey
        self.root.destroy()
    #data gula save korbo phone number diye
    def save(self):
        #1ta object niyechi bill,index number 1 line theke end porjonto data get korbe
        self.bill=self.txtarea.get("1.0",END)
        # bill folder e new file baniyechi,phone number ta txt e nibo r w=write mode e
        f1=open("bill/"+str(self.cphn.get())+"txt","w")
        #f1 e write function k call kore bill object pass kore diyechi
        f1.write(self.bill)
        #close kore diyechi
        f1.close()

root=Tk()         #initialize tkinter


obj=bill(root)

canvas=Canvas(width=216,height=200)
canvas.place(x=0,y=146)
photo= PhotoImage(file="C:\\Users\\user\\buttonpython\\buttonpython\\image.png")
canvas.create_image(0,0,image=photo,anchor="nw")

canvas=Canvas(width=216,height=200)
canvas.place(x=0,y=330)
photo1= PhotoImage(file="C:\\Users\\user\\buttonpython\\buttonpython\\image1.png")
canvas.create_image(0,0,image=photo1,anchor="nw")

canvas=Canvas(width=216,height=200)
canvas.place(x=0,y=530)
photo2= PhotoImage(file="C:\\Users\\user\\buttonpython\\buttonpython\\image4.png")
canvas.create_image(0,0,image=photo2,anchor="nw")

canvas=Canvas(width=216,height=200)
canvas.place(x=1140,y=146)
photo3= PhotoImage(file="C:\\Users\\user\\buttonpython\\buttonpython\\image.png")
canvas.create_image(0,0,image=photo3,anchor="nw")


canvas=Canvas(width=216,height=200)
canvas.place(x=1140,y=330)
photo4= PhotoImage(file="C:\\Users\\user\\buttonpython\\buttonpython\\image1.png")
canvas.create_image(0,0,image=photo4,anchor="nw")

canvas=Canvas(width=216,height=200)
canvas.place(x=1140,y=530)
photo5= PhotoImage(file="C:\\Users\\user\\buttonpython\\buttonpython\\image4.png")
canvas.create_image(0,0,image=photo5,anchor="nw")
root.mainloop()