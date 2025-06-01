from tkinter import *
import random
from tkinter import messagebox
import sys

class Supermarket:
    def __init__(self, root):
        self.root = root
        self.root.title("MOATH_Supermarket")
        self.root.geometry("1300x700+30+10")
        self.root.resizable(False, False)
        self.root.iconbitmap("3695283.ico")
        self.root.config(bg="white")

        # Title
        title = Label(self.root, text="Customer Purchase & Billing System", font=("Arial", 20, 'bold'), fg="white",
                      bg="#0B2F3A")
        title.pack(fill=X)

        # =========== Variables ===========
        self.name = StringVar()
        self.phone = StringVar()
        self.bill = StringVar()
        self.DryFoodItems = StringVar()
        self.Cleaning = StringVar()
        self.Beverages = StringVar()
        self.All = StringVar()

        self.items_food = [IntVar() for _ in range(10)]
        self.items_cleaning = [IntVar() for _ in range(10)]
        self.items_beverages = [IntVar() for _ in range(10)]

        self.bill.set(str(random.randint(1000, 9999)))

        # Customer Info Frame
        self.create_customer_frame()

        # Bill Area
        self.create_bill_area()

        # Buttons and Totals
        self.create_buttons_totals()

        # Items Area
        self.create_items_frames()

        self.q1=IntVar()
        self.q2=IntVar()
        self.q3=IntVar()
        self.q4=IntVar()
        self.q5=IntVar()
        self.q6=IntVar()
        self.q7=IntVar()
        self.q8=IntVar()
        self.q9=IntVar()
        self.q10=IntVar()
        #========== Variables for CleaningCleaning  ===========
        self.qq1=IntVar()
        self.qq2=IntVar()
        self.qq3=IntVar()
        self.qq4=IntVar()
        self.qq5=IntVar()
        self.qq6=IntVar()
        self.qq7=IntVar()
        self.qq8=IntVar()
        self.qq9=IntVar()
        self.qq10=IntVar()
        #========== Variables for  Beverages  ===========
        self.qqq1=IntVar()
        self.qqq2=IntVar()
        self.qqq3=IntVar()
        self.qqq4=IntVar()
        self.qqq5=IntVar()
        self.qqq6=IntVar()
        self.qqq7=IntVar()
        self.qqq8=IntVar()
        self.qqq9=IntVar()
        self.qqq10=IntVar()
        FF1=Frame(self.root,bd=2,width=319,height=557,bg="#0B4C5F")
        FF1.place(x=0,y=35)
        FF2=Frame(self.root,bd=2,width=319,height=557,bg="#0B4C5F")
        FF2.place(x=321,y=35)
        FF3=Frame(self.root,bd=2,width=318,height=557,bg="#0B4C5F")
        FF3.place(x=642,y=35)
        t1=Label(FF1,text="Food Items",font=("Arial", 16 ,'bold'),fg="white" , bg="#0B4C5F")
        t1.place(x=100,y=10)
        bq1=Label(FF1,text="Rice" , font=("Arial", 12 ),fg="white" , bg="#0B4C5F")
        bq1.place(x=10,y=60)
        bq2=Label(FF1,text="Sugar" , font=("Arial", 12 ),fg="white" , bg="#0B4C5F")
        bq2.place(x=10,y=100)
        bq3=Label(FF1,text="Flour" , font=("Arial", 12 ),fg="white" , bg="#0B4C5F")
        bq3.place(x=10,y=140)
        bq4=Label(FF1,text="Lentils" , font=("Arial", 12 ),fg="white" , bg="#0B4C5F")
        bq4.place(x=10,y=180)
        bq5=Label(FF1,text="Beans" , font=("Arial", 12 ),fg="white" , bg="#0B4C5F")
        bq5.place(x=10,y=220)
        bq6=Label(FF1,text="Pasta" , font=("Arial", 12 ),fg="white" , bg="#0B4C5F")
        bq6.place(x=10,y=260)
        bq7=Label(FF1,text="Vermicelli" , font=("Arial", 12 ),fg="white" , bg="#0B4C5F")
        bq7.place(x=10,y=300)
        bq8=Label(FF1,text="Oats" , font=("Arial", 12 ),fg="white" , bg="#0B4C5F")
        bq8.place(x=10,y=340)
        bq9=Label(FF1,text="Salt" , font=("Arial", 12 ),fg="white" , bg="#0B4C5F")
        bq9.place(x=10,y=380)
        bq10=Label(FF1,text="Cocoa" , font=("Arial", 12 ),fg="white" , bg="#0B4C5F")
        bq10.place(x=10,y=420)
        bqint1=Entry(FF1,width=10,textvariable=self.q1,font=("Arial", 12 ,'bold'),justify="center")
        bqint1.place(x=120,y=60)
        bqint2=Entry(FF1,width=10,textvariable=self.q2,font=("Arial", 12 ,'bold'),justify="center")
        bqint2.place(x=120,y=100)
        bqint3=Entry(FF1,width=10,textvariable=self.q3,font=("Arial", 12 ,'bold'),justify="center")
        bqint3.place(x=120,y=140)
        bqint4=Entry(FF1,width=10,textvariable=self.q4,font=("Arial", 12 ,'bold'),justify="center")
        bqint4.place(x=120,y=180)
        bqint5=Entry(FF1,width=10,textvariable=self.q5,font=("Arial", 12 ,'bold'),justify="center")
        bqint5.place(x=120,y=220)
        bqint6=Entry(FF1,width=10,textvariable=self.q6,font=("Arial", 12 ,'bold'),justify="center")
        bqint6.place(x=120,y=260)
        bqint7=Entry(FF1,width=10,textvariable=self.q7,font=("Arial", 12 ,'bold'),justify="center")
        bqint7.place(x=120,y=300)
        bqint8=Entry(FF1,width=10,textvariable=self.q8,font=("Arial", 12 ,'bold'),justify="center")
        bqint8.place(x=120,y=340)
        bqint9=Entry(FF1,width=10,textvariable=self.q9,font=("Arial", 12 ,'bold'),justify="center")
        bqint9.place(x=120,y=380)
        bqint10=Entry(FF1,width=10,textvariable=self.q10,font=("Arial", 12 ,'bold'),justify="center")
        bqint10.place(x=120,y=420)
        #===============================================
        t3=Label(FF3,text="Cleaning",font=("Arial", 16 ,'bold'),fg="white" , bg="#0B4C5F")
        t3.place(x=100,y=10)
        bq11 = Label(FF3, text="Laundry Detergent", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq11.place(x=10, y=60)
        bq12 = Label(FF3, text="Dishwashing Liquid", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq12.place(x=10, y=100)
        bq13 = Label(FF3, text="Floor Disinfectant", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq13.place(x=10, y=140)
        bq14 = Label(FF3, text="Air freshener", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq14.place(x=10, y=180)
        bq15 = Label(FF3, text="Trash Bags", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq15.place(x=10, y=220)
        bq16 = Label(FF3, text="Cleaning Sponges", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq16.place(x=10, y=260)
        bq17 = Label(FF3, text="Cleaning Powder", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq17.place(x=10, y=300)
        bq18 = Label(FF3, text="Paper Towels", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq18.place(x=10, y=340)
        bq19 = Label(FF3, text="Wet Cleaning", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq19.place(x=10, y=380)
        bq110 = Label(FF3, text="Glass Cleaner", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq110.place(x=10, y=420)
        bqint11 = Entry(FF3, width=10, textvariable=self.qq1,font=("Arial", 12, 'bold'), justify="center")
        bqint11.place(x=160, y=60)
        bqint12 = Entry(FF3, width=10,textvariable=self.qq2, font=("Arial", 12, 'bold'), justify="center")
        bqint12.place(x=160, y=100)
        bqint13 = Entry(FF3, width=10,textvariable=self.qq3, font=("Arial", 12, 'bold'), justify="center")
        bqint13.place(x=160, y=140)
        bqint14 = Entry(FF3, width=10,textvariable=self.qq4, font=("Arial", 12, 'bold'), justify="center")
        bqint14.place(x=160, y=180)
        bqint15 = Entry(FF3, width=10,textvariable=self.qq5, font=("Arial", 12, 'bold'), justify="center")
        bqint15.place(x=160, y=220)
        bqint16 = Entry(FF3, width=10, textvariable=self.qq6,font=("Arial", 12, 'bold'), justify="center")
        bqint16.place(x=160, y=260)
        bqint17 = Entry(FF3, width=10, textvariable=self.qq7,font=("Arial", 12, 'bold'), justify="center")
        bqint17.place(x=160, y=300)
        bqint18 = Entry(FF3, width=10,textvariable=self.qq8, font=("Arial", 12, 'bold'), justify="center")
        bqint18.place(x=160, y=340)
        bqint19 = Entry(FF3, width=10,textvariable=self.qq9, font=("Arial", 12, 'bold'), justify="center")
        bqint19.place(x=160, y=380)
        bqint110 = Entry(FF3, width=10, textvariable=self.qq10,font=("Arial", 12, 'bold'), justify="center")
        bqint110.place(x=160, y=420)
        #=====================================================
        t2=Label(FF2,text="Beverages",font=("Arial", 16 ,'bold'),fg="white" , bg="#0B4C5F")
        t2.place(x=100,y=10)
        bq111 = Label(FF2, text="Plain Yogurt", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq111.place(x=10, y=60)
        bq112 = Label(FF2, text="Butter milk", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq112.place(x=10, y=100)
        bq113 = Label(FF2, text="White Cheese", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq113.place(x=10, y=140)
        bq114 = Label(FF2, text="Cheddar Cheese", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq114.place(x=10, y=180)
        bq115 = Label(FF2, text="Triangle Cheese", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq115.place(x=10, y=220)
        bq116 = Label(FF2, text="Cream", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq116.place(x=10, y=260)
        bq117 = Label(FF2, text="Milk Powder", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq117.place(x=10, y=300)
        bq118 = Label(FF2, text="Condensed Milk", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq118.place(x=10, y=340)
        bq119 = Label(FF2, text="Butter", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq119.place(x=10, y=380)
        bq1110 = Label(FF2, text="Milk", font=("Arial", 12), fg="white", bg="#0B4C5F")
        bq1110.place(x=10, y=420)
        bqint111 = Entry(FF2, width=10,textvariable=self.qqq1, font=("Arial", 12, 'bold'), justify="center")
        bqint111.place(x=160, y=60)
        bqint112 = Entry(FF2, width=10,textvariable=self.qqq2, font=("Arial", 12, 'bold'), justify="center")
        bqint112.place(x=160, y=100)
        bqint113 = Entry(FF2, width=10,textvariable=self.qqq3, font=("Arial", 12, 'bold'), justify="center")
        bqint113.place(x=160, y=140)
        bqint114 = Entry(FF2, width=10,textvariable=self.qqq4, font=("Arial", 12, 'bold'), justify="center")
        bqint114.place(x=160, y=180)
        bqint115 = Entry(FF2, width=10,textvariable=self.qqq5, font=("Arial", 12, 'bold'), justify="center")
        bqint115.place(x=160, y=220)
        bqint116 = Entry(FF2, width=10,textvariable=self.qqq6, font=("Arial", 12, 'bold'), justify="center")
        bqint116.place(x=160, y=260)
        bqint117 = Entry(FF2, width=10,textvariable=self.qqq7, font=("Arial", 12, 'bold'), justify="center")
        bqint117.place(x=160, y=300)
        bqint118 = Entry(FF2, width=10,textvariable=self.qqq8, font=("Arial", 12, 'bold'), justify="center")
        bqint118.place(x=160, y=340)
        bqint119 = Entry(FF2, width=10,textvariable=self.qqq9, font=("Arial", 12, 'bold'), justify="center")
        bqint119.place(x=160, y=380)
        bqint1110 = Entry(FF2, width=10,textvariable=self.qqq10, font=("Arial", 12, 'bold'), justify="center")
        bqint1110.place(x=160, y=420)


    def total(self):
        self.Rice = self.q1.get() * 5000
        self.Sugar = self.q2.get() * 4000
        self.Flour = self.q3.get() * 13000
        self.Lentils = self.q4.get() * 500
        self.Beans = self.q5.get() * 600
        self.Pasta = self.q6.get() * 300
        self.Vermicelli = self.q7.get() * 250
        self.Oats = self.q8.get() * 1000
        self.Salt = self.q9.get() * 200
        self.Cocoa = self.q10.get() * 1000
        self.Total = float(
            self.Rice +
            self.Sugar +
            self.Flour +
            self.Lentils +
            self.Beans +
            self.Pasta +
            self.Vermicelli +
            self.Oats +
            self.Salt +
            self.Cocoa
        )
        self.Laundry_Detergent = self.qq1.get() * 1000
        self.Dishwashing_Liquid = self.qq2.get() * 1500
        self.Floor_Disinfectant = self.qq3.get() * 1300
        self.Air_freshener = self.qq4.get() * 700
        self.TrashBags = self.qq5.get() * 400
        self.CleaningSponges = self.qq6.get() * 300
        self.CarpetCleaningPowder = self.qq7.get() * 2000
        self.PaperTowels = self.qq8.get() * 1000
        self.WetCleaning = self.qq9.get() * 1200
        self.GlassCleaner = self.qq10.get() * 1000
        self.Total1 = float(
            self.Laundry_Detergent +
            self.Dishwashing_Liquid +
            self.Floor_Disinfectant +
            self.Air_freshener +
            self.TrashBags +
            self.CleaningSponges +
            self.CarpetCleaningPowder +
            self.PaperTowels +
            self.WetCleaning +
            self.GlassCleaner
        )
        self.PlainYogurt = self.qqq1.get() * 350
        self.Buttermilk = self.qqq2.get() * 800
        self.WhiteCheese = self.qqq3.get() * 500
        self.CheddarCheese = self.qqq4.get() * 1200
        self.TriangleCheese = self.qqq5.get() * 1100
        self.Cream = self.qqq6.get() * 300
        self.MiPowder = self.qq7.get() * 2000
        self.CondensedMilk = self.qqq8.get() * 1000
        self.Butter = self.qqq9.get() * 1200
        self.Milk = self.qqq10.get() * 300
        self.Total2 = float(
            self.PlainYogurt +
            self.Buttermilk +
            self.WhiteCheese +
            self.CheddarCheese +
            self.TriangleCheese +
            self.Cream +
            self.CarpetCleaningPowder +
            self.CondensedMilk +
            self.Butter +
            self.Milk
        )
        self.DryFoodItems.set(str(self.Total) + ' Riyal')
        self.Cleaning.set(str(self.Total1) + ' Riyal')
        self.Beverages.set(str(self.Total2) + ' Riyal')
        self.all = float(
            self.Total +
            self.Total1 +
            self.Total2
        )
        self.All.set(self.all)

    def create_customer_frame(self):
        F1 = Frame(self.root, bd=2, width=338, height=240, bg="#0B4C5F")
        F1.place(x=961, y=35)

        Label(F1, text="Customer's data :", font=("Arial", 13, 'bold'), fg="white", bg="#0B4C5F").place(x=10, y=10)
        Label(F1, text="Name :", font=("Arial", 12, 'bold'), fg="white", bg="#0B4C5F").place(x=10, y=50)
        Entry(F1, width=20, textvariable=self.name, font=("Arial", 12, 'bold'), justify="center").place(x=120, y=50)
        Label(F1, text="Phone :", font=("Arial", 12, 'bold'), fg="white", bg="#0B4C5F").place(x=10, y=90)
        Entry(F1, width=20, textvariable=self.phone, font=("Arial", 12, 'bold'), justify="center").place(x=120, y=90)
        Label(F1, text="Bill number :", font=("Arial", 12, 'bold'), fg="white", bg="#0B4C5F").place(x=10, y=130)
        Entry(F1, width=20, textvariable=self.bill, font=("Arial", 12, 'bold'), justify="center").place(x=120, y=130)
        Button(F1, text="Search", width=10, fg="white", font=("Arial", 12, 'bold'), bg="#1878F2").place(x=120, y=170)

    def create_bill_area(self):
        Label(self.root, text=" Bill ", font=("tajawal", 16, 'bold'), fg="white", bg="#0B4C5F").place(x=1110, y=250)
        F3 = Frame(self.root, bd=2, width=338, height=390, bg="white")
        F3.place(x=961, y=290)
        scrol_y = Scrollbar(F3, orient=VERTICAL)
        self.text_area = Text(F3, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=LEFT, fill=Y)
        scrol_y.config(command=self.text_area.yview)
        self.text_area.pack(fill=BOTH, expand=1)

    def create_buttons_totals(self):
        F4 = Frame(self.root, bd=2, width=1300, height=240, bg="#0B4C5F")
        F4.place(x=0, y=595)

        Button(F4, text="Calculate", width=10, height=1, font="Arial", bg="green", command=self.total).place(x=530,
                                                                                                             y=10)
        Button(F4, text="Bill", width=10, height=1, font="Arial", bg="green", command=self.generate_bill).place(x=530,
                                                                                                                y=60)
        Button(F4, text="Clear", width=10, height=1, font="Arial", bg="green", command=self.clear).place(x=402, y=10)
        Button(F4, text="Exit", width=10, height=1, font="Arial", bg="green", command=self.root.quit).place(x=402, y=60)

        Label(F4, text="Total price of Food Items :", font=("Arial", 12, 'bold'), fg="white", bg="#0B4C5F").place(x=10,
                                                                                                                  y=10)
        Entry(F4, width=15, textvariable=self.DryFoodItems, font=("Arial", 12, 'bold'), justify="center").place(x=220,
                                                                                                                y=10)

        Label(F4, text="Total price of Beverages :", font=("Arial", 12, 'bold'), fg="white", bg="#0B4C5F").place(x=10,
                                                                                                                 y=40)
        Entry(F4, width=15, textvariable=self.Beverages, font=("Arial", 12, 'bold'), justify="center").place(x=220,
                                                                                                             y=40)

        Label(F4, text="Total price of Cleaning :", font=("Arial", 12, 'bold'), fg="white", bg="#0B4C5F").place(x=10,
                                                                                                                y=75)
        Entry(F4, width=15, textvariable=self.Cleaning, font=("Arial", 12, 'bold'), justify="center").place(x=220, y=75)

        Label(F4, text=" Total :", font=("Arial", 20, 'bold'), fg="white", bg="#0B4C5F").place(x=680, y=35)
        self.total_all_entry = Entry(F4, width=20,textvariable=self.All, font=("Arial", 20, 'bold'), justify="center")
        self.total_all_entry.place(x=800, y=35)

    def create_items_frames(self):
        # Placeholder for FF1, FF2, FF3
        pass

    # def total(self):
    #     # food_total = sum([v.get() * 10 for v in self.items_food])
    #     # cleaning_total = sum([v.get() * 8 for v in self.items_cleaning])
    #     # beverages_total = sum([v.get() * 5 for v in self.items_beverages])
    #     #
    #     # total_all = food_total + cleaning_total + beverages_total
    #     self.DryFoodItems.set(str(self.DryFoodItems))
    #     self.Cleaning.set(str(self.Cleaning))
    #     self.Beverages.set(str(self.Beverages))
    #     self.total_all_entry.delete(0, END)
    #     self.total_all_entry.insert(END, str(self.All))

    def generate_bill(self):
        self.text_area.delete('1.0', END)
        self.text_area.insert(END, f"Customer Name: {self.name.get()}\n")
        self.text_area.insert(END, f"Phone Number: {self.phone.get()}\n")
        self.text_area.insert(END, f"Bill Number: {self.bill.get()}\n")
        self.text_area.insert(END, "----------------------------------------\n")
        self.text_area.insert(END, f"Total Food: {self.DryFoodItems.get()}\n")
        self.text_area.insert(END, f"Total Cleaning: {self.Cleaning.get()}\n")
        self.text_area.insert(END, f"Total Beverages: {self.Beverages.get()}\n")
        self.text_area.insert(END, f"Grand Total: {self.total_all_entry.get()}\n")

    def clear(self):
        # for var_list in [self.DryFoodItems, self.Cleaning, self.Beverages]:
        #     for var in var_list:
        #         var.set("0")
        self.name.set("")
        self.phone.set("")
        self.bill.set(str(random.randint(1000, 9999)))
        self.DryFoodItems.set("0")
        self.Cleaning.set("0")
        self.Beverages.set("0")
        self.total_all_entry.delete(0, END)
        self.text_area.delete('1.0', END)

def run():
    root = Tk()
    app = Supermarket(root)
    root.mainloop()
    from sopermarkt import exit_1
    exit_1()

