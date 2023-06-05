import tkinter as tk
import re

usern_pattern = re.compile(r'^\w{4,8}$')

root=tk.Tk()
root.geometry('400x250+700+500') # размеры окна и его положение
root.resizable(False, False) # нельзя менять размер окна (справа и слева)

def signin():
    signin = usern_entry.get()
    if usern_pattern.search(signin):
        usern_entry.config(bg='green')
    else:
        usern_entry.config(bg='red')



usern_label = tk.Label(root, text = 'Sign in', font=('Arial', 14), padx=50)

usern_entry = tk.Entry(root, font=('Arial', 12), width=20)

registr_button = tk.Button(root, text='SIGN IN', font=('Arial', 16), width=12, command=signin)

root.grid_columnconfigure(0, minsize=150)
root.grid_rowconfigure(0, minsize=90)
registr_button.grid(columnspan=2)

usern_label.grid(column=0, row=0, sticky='w')

usern_entry.grid(column=1, row=0, sticky='w')
registr_button.grid(column=0, row=2)
root.mainloop()

# код выше нужно поместить в login.py


'''def sayUserHello(user): # охоплююча функция
    msg = 'Hello ' + user
    def showMsg():
        nonlocal msg
        msg = 'Student'
        print(msg+', let`s start!') # вкладена функция
    showMsg()
    print(msg)


sayUserHello('Admin')'''

'''def sayhello(user):
    msg = 'Hi!, ' + user
    def show():
        print(msg + ' and world')
    return show
case1 = sayhello('admin')
case1()'''

def doExercise1(var1):
    var2 = 5
    def doExercise2(var2):
        return var1**var2
    return doExercise2

case1 = doExercise1(2)
print(case1(5))
print(case1(10))


