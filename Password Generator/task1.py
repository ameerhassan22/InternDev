# Libraries
import tkinter as tk
from tkinter import messagebox as ms
import random

# create tkinker window 
window = tk.Tk()
window.title('Password Generator')
window.geometry('800x600')
window.config(background='#006666')

# method to Generate Password
def generate_password():
    # user input for password length
    password_length = int(password_entry.get())
    if password_length <= 0 or password_length > 76:
        ms.showerror("Error", "Please enter a valid password length (1 to 76)")
    else:
        characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$^&*()?|/;"
        password = "".join(random.sample(characters, password_length))
        ms.showinfo("Password", password)
        password_show.config(text='Password: ' + password, font=('Helvetica', 15, 'bold'))

   
#labels
heading = tk.Label(window , text='Password Generator',background='#006666', fg='white',font=('Helvetica', 35,'bold'))
heading.place(x=10,y=350)

password_label = tk.Label(window,text='Length of Password',background='#006666',fg='white',font=('Helvetica', 20,'bold'))
password_label.place(x=600,y=200)

password_entry = tk.Entry(window, background='#a45b80',fg='white',font=('Helvetica', 20,'bold'))
password_entry.place(x=600,y=250)
  
password_button = tk.Button(window,text='Generate Password',command=generate_password,background='yellow',fg='black',font=('Helvetica', 10,'bold'))
password_button.place(x=600,y=300)

password_show= tk.Message(window,width=900,text="",background='#006666',fg='yellow',font=('Helvetica', 10,'bold'))
password_show.place(x=600,y=400)

# link of tkinker
window.mainloop()
