from tkinter import *
from tkinter import messagebox
import random, os
root = Tk()
root.title('Billing System')
root.geometry('1275x508')
root.iconbitmap('bill.ico')

#Functions Part
if not os.path.exists('bills'):
    os.mkdir('bills')

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billEntry.get():
            f= open(f'bills/{i}', 'r')
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror('Error', 'Bill not found')
def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirmation','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0, END)
        file=open(f'bills/{billnumber}.txt', 'w')
        file.write(bill_content)
        file.close
        messagebox.showinfo('Saved',f'Bill Number {billnumber} is saved successfully')
        billnumber = random.randint(500, 1000)

billnumber = random.randint(500, 1000)
def bill_area():
    if nameEntry.get()=='':
        messagebox.showerror('Error', 'Customer name is required!')
    elif vegpriceEntry.get()=='' and grocerypriceEntry.get()=='':
        messagebox.showerror('Error','No products are entered.')
    elif vegpriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs':
        messagebox.showerror('Error','No products are entered.')
    else:
        textarea.delete(1.0, END)
        textarea.insert(END, '\t\t\t\t\t***** Thank You For Shopping With Us! *****\n')
        textarea.insert(END, f'Bill Number: {billnumber}\n')
        textarea.insert(END, f'Customer Name: {nameEntry.get()}\n')
        textarea.insert(END, f'Email: {emailEntry.get()}\n')
        textarea.insert(END, f'Phone: {phoneEntry.get()}\n')
        textarea.insert(END,'\n==============================================================================================================')
        textarea.insert(END, 'Product\t\t\t\t\tQuantity\t\t\t\t\tPrice')
        textarea.insert(END,'\n==============================================================================================================\n')
        if tomatoEntry.get()!='0':
            textarea.insert(END,f'Tomato \t\t\t\t\t {tomatoEntry.get()}\t\t\t\t\t{tomatoprice} Rs\n')
        if potatoEntry.get()!='0':
            textarea.insert(END,f'Potato \t\t\t\t\t {potatoEntry.get()}\t\t\t\t\t{potatoprice} Rs\n')
        if carrotEntry.get()!='0':
            textarea.insert(END,f'Carrot \t\t\t\t\t {carrotEntry.get()}\t\t\t\t\t{carrotprice} Rs\n')
        if broccoliEntry.get()!='0':
            textarea.insert(END,f'Broccoli \t\t\t\t\t {broccoliEntry.get()}\t\t\t\t\t{broccoliprice} Rs\n')
        if lettuceEntry.get()!='0':
            textarea.insert(END,f'Lettuce \t\t\t\t\t {lettuceEntry.get()}\t\t\t\t\t{lettuceprice} Rs\n')
        if riceEntry.get()!='0':
            textarea.insert(END,f'Rice \t\t\t\t\t {riceEntry.get()}\t\t\t\t\t{riceprice} Rs\n')
        if wheatEntry.get()!='0':
            textarea.insert(END,f'Wheat \t\t\t\t\t {wheatEntry.get()}\t\t\t\t\t{wheatprice} Rs\n')
        if flourEntry.get()!='0':
            textarea.insert(END,f'Flour \t\t\t\t\t {flourEntry.get()}\t\t\t\t\t{flourprice} Rs\n')
        if eggEntry.get()!='0':
            textarea.insert(END,f'Eggs \t\t\t\t\t {eggEntry.get()}\t\t\t\t\t{eggprice} Rs\n')
        if teaEntry.get()!='0':
            textarea.insert(END,f'Tea \t\t\t\t\t {teaEntry.get()}\t\t\t\t\t{teaprice} Rs\n')
            textarea.insert(END,'--------------------------------------------------------------------------------------------------------------\n')
        if vegtaxEntry.get()!= '0.0 Rs':
            textarea.insert(END, f'\nVegetables Tax\t\t\t{vegtaxEntry.get()}')
        if grocerytaxEntry.get()!= '0.0 Rs':
            textarea.insert(END, f'\nGroceries Tax\t\t\t{grocerytaxEntry.get()}')

        textarea.insert(END,f'\nYour Total Bill is:\t\t\t{totalbill} Rs\n')
        textarea.insert(END,'==============================================================================================================\n')
        textarea.insert(END, '\t\t\t\t\t***** Visit Us Again Soon *****\n')

def total():
    global tomatoprice, potatoprice, carrotprice, broccoliprice, lettuceprice, riceprice, wheatprice, flourprice, eggprice, teaprice
    global totalbill
    tomatoprice=int(tomatoEntry.get())*30
    potatoprice=int(potatoEntry.get())*20
    carrotprice=int(carrotEntry.get())*25
    broccoliprice=int(broccoliEntry.get())*15
    lettuceprice=int(lettuceEntry.get())*25

    totalvegprice= tomatoprice+potatoprice+carrotprice+broccoliprice+lettuceprice
    vegpriceEntry.delete(0,END)
    vegpriceEntry.insert(0,f'{totalvegprice} Rs')
    vegtax=totalvegprice*0.12
    vegtaxEntry.delete(0, END)
    vegtaxEntry.insert(0, str(round(vegtax,2))+ ' Rs')

    riceprice = int(riceEntry.get()) * 50
    wheatprice = int(wheatEntry.get()) * 70
    flourprice = int(flourEntry.get()) * 120
    eggprice = int(eggEntry.get()) * 30
    teaprice = int(teaEntry.get()) * 110

    totalgroceryprice = riceprice + wheatprice + flourprice + eggprice + teaprice
    grocerypriceEntry.delete(0, END)
    grocerypriceEntry.insert(0, f'{totalgroceryprice} Rs')
    grocerytax=totalgroceryprice*0.20
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, str(round(grocerytax,2)) + ' Rs')

    totalbill = totalvegprice + totalgroceryprice + vegtax + grocerytax

def clear():
    tomatoEntry.delete(0, END)
    potatoEntry.delete(0, END)
    carrotEntry.delete(0, END)
    broccoliEntry.delete(0, END)
    lettuceEntry.delete(0, END)
    riceEntry.delete(0, END)
    wheatEntry.delete(0, END)
    flourEntry.delete(0, END)
    eggEntry.delete(0, END)
    teaEntry.delete(0, END)
    tomatoEntry.insert(0, 0)
    potatoEntry.insert(0, 0)
    carrotEntry.insert(0, 0)
    broccoliEntry.insert(0, 0)
    lettuceEntry.insert(0, 0)
    riceEntry.insert(0, 0)
    wheatEntry.insert(0, 0)
    flourEntry.insert(0, 0)
    eggEntry.insert(0, 0)
    teaEntry.insert(0, 0)
    grocerytaxEntry.delete(0, END)
    vegtaxEntry.delete(0,END)
    vegpriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    nameEntry.delete(0,END)
    emailEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billEntry.delete(0,END)
    textarea.delete(1.0,END)

#GUI Part
headingLabel = Label(root, text='Billing System', font=('Helvetica', 30, 'bold'),
                     bg = 'gray20', fg = 'gold', bd = 12, relief= RAISED)
headingLabel.pack(fill = X)
customer_details_frame = LabelFrame(root, text='Customer Details', font=('Helvetica', 15, 'bold'),
                  bg = 'gray20', fg = 'gold', bd = 8, relief= RAISED)


nameLabel = Label(customer_details_frame, text = 'Name', font=('Helvetica', 11, 'bold'),
                  bg = 'gray20', fg = 'white')
nameLabel.grid(row = 0, column = 0, padx = 10)
customer_details_frame.pack(fill = X)

nameEntry = Entry(customer_details_frame, font = ('Arial', 10), bd = 2, width=25)
nameEntry.grid(row = 0, column = 1, padx = 10)

phoneLabel = Label(customer_details_frame, text = 'Phone', font=('Helvetica', 11, 'bold'),
                  bg = 'gray20', fg = 'white')
phoneLabel.grid(row = 0, column = 2, padx = 10)

phoneEntry = Entry(customer_details_frame, font = ('Arial', 10), bd = 2, width=25)
phoneEntry.grid(row = 0, column = 3, padx = 10)

emailLabel = Label(customer_details_frame, text = 'Email', font=('Helvetica', 11, 'bold'),
                  bg = 'gray20', fg = 'white')
emailLabel.grid(row = 0, column = 4, padx = 10)

emailEntry = Entry(customer_details_frame, font = ('Arial', 10), bd = 2, width=25)
emailEntry.grid(row = 0, column = 5, padx = 10)

billLabel = Label(customer_details_frame, text = 'Bill Number', font=('Helvetica', 11, 'bold'),
                  bg = 'gray20', fg = 'white')
billLabel.grid(row = 0, column = 6, padx = 10, pady = 5)

billEntry = Entry(customer_details_frame, font = ('Arial', 10), bd = 2, width=25)
billEntry.grid(row = 0, column = 7, padx = 10)

searchButton=Button(customer_details_frame, text = 'Find the bill',
                    font=('Helvetica', 10, 'bold'), bd = 7, width=11, command =search_bill)
searchButton.grid(row = 0, column = 8, padx =15)

productsFrame = Frame(root)
productsFrame.pack()

vegFrame = LabelFrame(productsFrame, text = 'Vegetables', font=('Helvetica', 12, 'bold'),
                  bg = 'gray20', fg = 'gold')
vegFrame.grid(row = 0, column = 0, padx= 1, pady = 5)

tomatoLabel=Label(vegFrame, text='Tomato', font=('Helvetica', 10, 'bold'),
                  bg = 'gray20', fg = 'white')
tomatoLabel.grid(row = 0, column = 0, padx= 10)

tomatoEntry=Entry(vegFrame, font=('Arial', 10), bd=2, width=10)
tomatoEntry.grid(row=0, column=1, padx=10, pady=10)
tomatoEntry.insert(0,0)

potatoLabel=Label(vegFrame, text='Potato', font=('Helvetica', 10, 'bold'),
                  bg = 'gray20', fg = 'white')
potatoLabel.grid(row = 1, column = 0, padx= 10)

potatoEntry=Entry(vegFrame, font=('Arial', 10), bd=2, width=10)
potatoEntry.grid(row=1, column=1, padx=10, pady=10)
potatoEntry.insert(0,0)

carrotLabel=Label(vegFrame, text='Carrot', font=('Helvetica', 10, 'bold'),
                  bg = 'gray20', fg = 'white')
carrotLabel.grid(row = 2, column = 0, padx= 10)

carrotEntry=Entry(vegFrame, font=('Arial', 10), bd=2, width=10)
carrotEntry.grid(row=2, column=1, padx=10, pady=10)
carrotEntry.insert(0,0)

broccoliLabel=Label(vegFrame, text='Broccoli', font=('Helvetica', 10, 'bold'),
                  bg = 'gray20', fg = 'white')
broccoliLabel.grid(row = 3, column = 0, padx= 10)

broccoliEntry=Entry(vegFrame, font=('Arial', 10), bd=2, width=10)
broccoliEntry.grid(row=3, column=1, padx=10, pady=10)
broccoliEntry.insert(0,0)

lettuceLabel=Label(vegFrame, text='Lettuce', font=('Helvetica', 10, 'bold'),
                  bg = 'gray20', fg = 'white')
lettuceLabel.grid(row = 4, column = 0, padx= 10)

lettuceEntry=Entry(vegFrame, font=('Arial', 10), bd=2, width=10)
lettuceEntry.grid(row=4, column=1, padx=10, pady=10)
lettuceEntry.insert(0,0)

groceryFrame = LabelFrame(productsFrame, text = 'Grocery', font=('Helvetica', 12, 'bold'),
                  bg = 'gray20', fg = 'gold')
groceryFrame.grid(row = 0, column = 1, pady= 5, padx= 8)

riceLabel=Label(groceryFrame, text='Rice', font=('Helvetica', 10, 'bold'),
                  bg = 'gray20', fg = 'white')
riceLabel.grid(row = 1, column = 1, padx= 10)

riceEntry=Entry(groceryFrame, font=('Arial', 10), bd=2, width=10)
riceEntry.grid(row=1, column=2, padx=10, pady=10)
riceEntry.insert(0,0)

wheatLabel=Label(groceryFrame, text='Wheat', font=('Helvetica', 10, 'bold'),
                  bg = 'gray20', fg = 'white')
wheatLabel.grid(row = 2, column = 1, padx= 10)

wheatEntry=Entry(groceryFrame, font=('Arial', 10), bd=2, width=10)
wheatEntry.grid(row=2, column=2, padx=10, pady=10)
wheatEntry.insert(0,0)

flourLabel=Label(groceryFrame, text='Flour', font=('Helvetica', 10, 'bold'),
                  bg = 'gray20', fg = 'white')
flourLabel.grid(row = 3, column = 1, padx= 10)

flourEntry=Entry(groceryFrame, font=('Arial', 10), bd=2, width=10)
flourEntry.grid(row=3, column=2, padx=10, pady=10)
flourEntry.insert(0,0)

eggLabel=Label(groceryFrame, text='Egg', font=('Helvetica', 10, 'bold'),
                  bg = 'gray20', fg = 'white')
eggLabel.grid(row = 4, column = 1, padx= 10)

eggEntry=Entry(groceryFrame, font=('Arial', 10), bd=2, width=10)
eggEntry.grid(row=4, column=2, padx=10, pady=10)
eggEntry.insert(0,0)

teaLabel=Label(groceryFrame, text='Tea', font=('Helvetica', 10, 'bold'),
                  bg = 'gray20', fg = 'white')
teaLabel.grid(row = 5, column = 1, padx= 10)

teaEntry=Entry(groceryFrame, font=('Arial', 10), bd=2, width=10)
teaEntry.grid(row=5, column=2, padx=10, pady=10)
teaEntry.insert(0,0)

billframe=Frame(productsFrame, bd=8, relief=GROOVE)
billframe.grid(row = 0, column = 3)

billareaLabel=Label(billframe, text='Preview', font=('Helvetica', 15, 'bold'), bd=7, relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
textarea=Text(billframe, height=11, width=110, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root, text='Bill Menu', font=('Helvetica',15,'bold'),
                         fg='gold', bd=8, relief=GROOVE,bg='gray20')
billmenuFrame.pack()


vegpriceLabel=Label(billmenuFrame, text='Vegetables Price', font=('Helvetica', 10, 'bold'),
                  bg = 'gray20', fg = 'white')
vegpriceLabel.grid(row = 0, column = 0, padx= 10)

vegpriceEntry=Entry(billmenuFrame, font=('Arial', 10), bd=2, width=10)
vegpriceEntry.grid(row=0, column=1, padx=10, pady=10)

grocerypriceLabel=Label(billmenuFrame, text='Grocery Price', font=('Helvetica', 10, 'bold'),
                  bg = 'gray20', fg = 'white')
grocerypriceLabel.grid(row = 1, column = 0, padx= 10)

grocerypriceEntry=Entry(billmenuFrame, font=('Arial', 10), bd=2, width=10)
grocerypriceEntry.grid(row=1, column=1, padx=10, pady=10)

vegtaxLabel=Label(billmenuFrame, text='Vegetable Tax', font=('Helvetica', 10, 'bold'),
                  bg = 'gray20', fg = 'white')
vegtaxLabel.grid(row = 0, column = 2, padx= 10)

vegtaxEntry=Entry(billmenuFrame, font=('Arial', 10), bd=2, width=10)
vegtaxEntry.grid(row=0, column=3, padx=10, pady=10)

grocerytaxLabel=Label(billmenuFrame, text='Grocery Tax', font=('Helvetica', 10, 'bold'),
                  bg = 'gray20', fg = 'white')
grocerytaxLabel.grid(row = 1, column = 2, padx= 10)

grocerytaxEntry=Entry(billmenuFrame, font=('Arial', 10), bd=2, width=10)
grocerytaxEntry.grid(row=1, column=3, padx=10, pady=10)

buttonFrame=Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=2)

totalButton=Button(buttonFrame, text='Total', font=('arial', 16, 'bold'),
                   bg='red',fg='white', bd=5, width=8, command=total)
totalButton.grid(row=0, column=0, pady= 10, padx=20)

billButton=Button(buttonFrame, text='Create Bill', font=('arial', 16, 'bold'),
                   bg='blue',fg='white', bd=5, width=8, command=bill_area)
billButton.grid(row=0, column=1, pady= 10, padx=20)

saveButton=Button(buttonFrame, text='Save', font=('arial', 16, 'bold'),
                   bg='gold2',fg='white', bd=5, width=8, command=save_bill)
saveButton.grid(row=0, column=3, pady= 10, padx=20)

emailButton=Button(buttonFrame, text='Email', font=('arial', 16, 'bold'),
                   bg='green2',fg='white', bd=5, width=8)
emailButton.grid(row=0, column=4, pady= 10, padx=20)

clearButton=Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'),
                   bg='gray20',fg='white', bd=5, width=8, command=clear)
clearButton.grid(row=0, column=5, pady= 10, padx=20)

root.mainloop()