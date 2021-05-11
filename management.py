import time
from tkinter import *
import tkinter.messagebox

master=Tk()
master.geometry('1350x650+0+0')
master.title("EMPLOYEE PAYROLL SYSTEM")
Tops=Frame(master,width=1350,height=50,bd=8,bg="powder blue")
Tops.pack(side=TOP)

f1=Frame(master,width=800,height=600,bd=8,bg="powder blue")
f1.pack(side=LEFT)
f2=Frame(master,width=400,height=700,bd=8,bg="powder blue")
f2.pack(side=RIGHT)

fla=Frame(f1,width=600,height=200,bd=8,bg="powder blue")
fla.pack(side=TOP)
flb=Frame(f1,width=300,height=600,bd=8,bg="powder blue")
flb.pack(side=TOP)

lblinfo=Label(Tops,font=('arial',45,'bold'),text="Employee Payment Management system",bd=20,fg="green")
lblinfo.grid(row=0,column=0)

def exit():
    exit = tkinter.messagebox.askyesno("Employee system", "Do you want to exit the system")
    if exit > 0:
        master.destroy()
        return

def enterinfo():
  txtpayslip.delete("1.0",END)
  txtpayslip.insert(END,"\t\tPay Slip\n\n")
  txtpayslip.insert(END,"Name :\t\t"+Name.get()+"\n\n")
  txtpayslip.insert(END,"Address :\t\t"+Address.get()+"\n\n")
  txtpayslip.insert(END,"Employee_ID :\t\t"+Employee_ID.get()+"\n\n")
  txtpayslip.insert(END,"Mobile Number :\t\t"+Mobile_Number.get()+"\n\n")
  txtpayslip.insert(END,"Hours Worked :\t\t"+HoursWorked.get()+"\n\n")
  txtpayslip.insert(END,"Hourly Rate :\t\t"+Hourly_Rate.get()+"\n\n")
  txtpayslip.insert(END,"Tax Paid :\t\t"+Taxable.get()+"\n\n")
  txtpayslip.insert(END, "Gross Payable :\t\t" +GrossPayable.get() + "\n\n")
  txtpayslip.insert(END,"Net Payable :\t\t"+NetPayable.get()+"\n\n")

#___________________________________________________________________________________________________________________________________
Name=StringVar()
Address=StringVar()
HoursWorked=StringVar()
Hourly_Rate=StringVar()
Payable=StringVar()
Taxable=StringVar()
NetPayable=StringVar()
GrossPayable=StringVar()
OverTimeBonus=StringVar()
Employee_ID=StringVar()
Mobile_Number=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()

DateOfOrder.set(time.strftime("%d/%m/%Y"))

def reset():
  Name.set("")
  Address.set("")
  HoursWorked.set("")
  Hourly_Rate.set("")
  Payable.set("")
  Taxable.set("")
  NetPayable.set("")
  GrossPayable.set("")
  OverTimeBonus.set("")
  Employee_ID.set("")
  Mobile_Number.set("")
  txtpayslip.delete("1.0",END)

def weeklysalary():
  txtpayslip.delete("1.0",END)
  hoursworkedperweek=float(HoursWorked.get())
  wagesperhours=float(Hourly_Rate.get())

  paydue=wagesperhours*hoursworkedperweek
  paymentdue="INR",str('%.2f'%(paydue))
  Payable.set(paymentdue)

  tax=paydue*0.2
  taxable="INR",str('%.2f'%(tax))
  Taxable.set(taxable)

  netpay=paydue-tax
  netpays="INR",str('%.2f'%(netpay))
  NetPayable.set(netpays)

  if hoursworkedperweek > 40:
    overtimehours=(hoursworkedperweek-40)+wagesperhours*1.5
    overtime="INR",str('%.2f'%(overtimehours))
    OverTimeBonus.set(overtime)
  elif hoursworkedperweek<=40:
    overtimepay=(hoursworkedperweek-40)+wagesperhours*1.5
    overtimehrs="INR",str('%.2f'%(overtimepay))
    OverTimeBonus.set(overtimehrs)
  return
#______________________________________________________________________________________________________________________________________________
a=Label(fla,text='Name',font=('arial',16,'bold'),bd=20,bg="powder blue").grid(row=0,column=0)
g=Label(fla,text='Address',font=('arial',16,'bold'),bd=20,bg="powder blue").grid(row=0,column=2)
b=Label(fla,text='Employee Id',font=('arial',16,'bold'),bd=20,bg="powder blue").grid(row=1,column=0)
h=Label(fla,text='Mobile Number',font=('aria0l',16,'bold'),bd=20,bg="powder blue").grid(row=1,column=2)
c=Label(fla,text='Hours Worked',font=('arial',16,'bold'),bd=20,bg="powder blue").grid(row=2,column=0)
j=Label(fla,text="Hourly Rate",font=('arial',16,'bold'),bd=20,bg="powder blue").grid(row=2,column=2)
d=Label(fla,text='Tax',font=('arial',16,'bold'),bd=20,bg="powder blue").grid(row=3,column=0)
e=Label(fla,text='Overtime',font=('arial',16,'bold'),bd=20,bg="powder blue").grid(row=3,column=2)
i=Label(fla,text='Gross Pay',font=('arial',16,'bold'),bd=20,bg="powder blue").grid(row=4,column=0)
k=Label(fla,text='Net Pay',font=('arial',16,'bold'),bd=20,bg="powder blue").grid(row=4,column=2)
#___________________________________________________________________________________________________________________________________________

lb=Entry(fla,textvariable=Name,font=('arial',16,'bold'),bd='16',width=22,justify='left').grid(row=0, column=1)
lb1=Entry(fla,textvariable=Address,font=('arial',16,'bold'),bd='16',width=22,justify='left').grid(row=0, column=4)
lb2=Entry(fla,textvariable=Employee_ID,font=('arial',16,'bold'),bd='16',width=22,justify='left').grid(row=1, column=1)
lb3=Entry(fla,textvariable=Mobile_Number,font=('arial',16,'bold'),bd='16',width=22,justify='left').grid(row=1, column=4)
lb4=Entry(fla,textvariable=HoursWorked,font=('arial',16,'bold'),bd='16',width=22,justify='left').grid(row=2, column=1)
lb5=Entry(fla,textvariable=Hourly_Rate,font=('arial',16,'bold'),bd='16',width=22,justify='left').grid(row=2, column=4)
lb6=Entry(fla,textvariable=Payable,font=('arial',16,'bold'),bd='16',width=22,justify='left').grid(row=3, column=1)
lb7=Entry(fla,textvariable=OverTimeBonus,font=('arial',16,'bold'),bd='16',width=22,justify='left').grid(row=3, column=4)
lb8=Entry(fla,textvariable=GrossPayable,font=('arial',16,'bold'),bd='16',width=22,justify='left').grid(row=4, column=1)
lb9=Entry(fla,textvariable=NetPayable,font=('arial',16,'bold'),bd='16',width=22,justify='left').grid(row=4, column=4)

#______________________________________________________________________________________________________________________________

Button(flb, text='Weekly Salary',font=('arial',10,'bold'),padx='40',pady='10',bd=8,width=14,fg="red",bg="powder blue",command=weeklysalary).grid(row=8,column=0)
Button(flb, text='Reset',font=('arial',10,'bold'),padx='40',pady='10',bd=8,width=14,fg="red",bg="powder blue",command=reset).grid(row=8,column=1)
Button(flb, text='View PaySlip',font=('arial',10,'bold'),padx='40',pady='10',bd=8,width=14,fg="red",bg="powder blue",command=enterinfo).grid(row=8,column=2)
Button(flb, text='Exit System',font=('arial',10,'bold'),padx='40',pady='10',bd=8,width=14,fg="red",bg="powder blue",command=exit).grid(row=8,column=3)

#_________________________________________________________________________________________________________________________________

payslip=Label(f2,textvariable=DateOfOrder,font=('arial',21,'bold'),fg="red",bg="powder blue").grid(row=0,column=0)
txtpayslip=Text(f2,height=22,width=34,bd=16,font=('arial',13,'bold'),fg="green",bg="powder blue")
txtpayslip.grid(row=1,column=0)


master.mainloop()
