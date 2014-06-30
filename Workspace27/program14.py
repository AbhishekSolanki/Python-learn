#GUI Programming

#PY inbuilt GUI Class
import Tkinter as tk

#Creating window
window = tk.Tk()

#creating textBox
text_box = tk.Entry(window)

#Function to call on button click event
def saveText():
    file_obj = open("program14.txt","w")
    file_obj.write(text_box.get())
    file_obj.close()

#Creating Button and display "save" on button, command specifies the function to call on button click
btn1 = tk.Button(window,text="Save",command = saveText)

# add widget to window,pack() method organizes the widget in window
text_box.pack() 
btn1.pack()

#main window loop
window.mainloop()
