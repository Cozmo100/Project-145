from tkinter import *

root = Tk()
root.geometry('300x200')
root.title("Driver's License")

label_id = Label(root,text='ID: ')
label_name = Label(root,text='NAME: ')
label_dob = Label(root,text='DATE OF BIRTH: ')
label_pin = Label(root,text='PIN NO: ')
label_Adr = Label(root,text='ADDRESS: ')
label_adfv = Label(root,text='AUTHORIZATION TO DRIVE: ')

label_id.pack()
label_name.pack()
label_dob.pack()
label_pin.pack()
label_Adr.pack()
label_adfv.pack()

def updtlab():
    dli = "1234567890"
    label_id["text"]+= dli
    print(type(dli))
    name = "Pengu"
    label_name["text"]+= name
    print(type(name))
    dob = "December 31 2000"
    label_dob["text"]+= dob
    print(type(dob))
    pin = "010101"
    label_pin["text"]+= pin
    print(type(pin))
    adr = "Penguin World"
    label_Adr["text"]+= adr
    print(type(adr))
    atd = "unicycle (1)"
    label_adfv["text"]+= atd
    print(type(atd))
    
b1 = Button(root, text = 'veiw drivers license', command = updtlab)
b1.pack()

root.mainloop()