from tkinter import *

root = Tk()
root.title("JUST FOR FUN")

frame = Frame(root, borderwidth=10, bd=10,bg="blue")
frame.pack(side=TOP, expand=YES, fill=BOTH)
frame.option_add('*Font', 'arial 20 bold')

Entry(root, relief=RIDGE, text="You are a boy",justify='left', bd=25, bg="light green").pack(side=TOP, expand=YES, fill=BOTH)
Label(frame, text="HELP", relief=RAISED, bg="red", fg='gold').pack(side=TOP, fill=BOTH)

button = Button(frame, text="QUIT", command=root.destroy, bg='green', relief=RAISED, fg='white')
button.pack(side=TOP, fill=BOTH)

if __name__ == '__main__':
    root.mainloop()


