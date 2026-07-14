
#Tkinter instance
root = tk.TK()

#Title of app in the top left banner of window
root.title("Hello World!!")

#The size of the window
root.geometry('500x350')


#Creating a global switch variable to convert 1 button from F to C and back
global temp_change
temp_change = True
#Function that changes text
def conversion():
    global temp_change
    if temp_change == True:
        my_label.config(text='GOODBYE WORLD!!!')
        temp_change = False
    else:
        my_label.config(text='Hello World!!!')
        temp_change = True



#Creating a Label widget. root is a window
my_label = ttk.Label(root, text='Hello World', font=('Helvetica', 24))

#Packing a window. pady is placing padding 20 above and below. Always pack a widget
my_label.pack(pady=20)

#You can only use on of these (mostly):
#Pack puts widget at top of screen, and next one right underneath.
#Grid creates rows and collumns. 
#Place specifies a coordinate, which gets tricky with apps.


#Creating a button. It has attributes
my_button = ttk.Button(root, text='CLICK ME!!!', font=('Helvetica', 24), command=conversion)
my_button.pack(pady=40)



#Have method for converting Celcius to Farenheit

#Have method for converting Farenheit to Celcius

#If button 1 is pressed, run C to F. If button 2 is pressed, run F to C

#Print the most recently used conversion at bottom of window

#Creating a loop of tkinter instance
root.mainloop()