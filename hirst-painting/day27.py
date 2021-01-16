


from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)
def button_clicked():
    print("I got the clicked")
    new_text = input.get()
    km_text = str(round((int(new_text)*1.609344), 2))
    outputKm.config(text=km_text)
    
my_label = Label(text="is equal to", font=("Arial",24,"bold"))
my_label.grid(column=0, row=1)
miles_label = Label(text="Miles", font=("Arial",24,"bold"))
km_label= Label(text="Km", font=("Arial",24,"bold"))
outputKm= Label(text="0",font=("Arial",24,"bold"))
outputKm.grid(column=1, row=1)
miles_label.grid(column=2, row=0)
km_label.grid(column=2, row=1)
button = ttk.Button(text="Calculate", command=button_clicked)
button.grid(column= 1, row = 2)



# entry
input = Entry(width=10)
input.grid(column=1, row=0)
print(input.get())





window.mainloop()