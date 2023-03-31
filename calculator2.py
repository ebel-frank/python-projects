from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(equation.get()))
        equation.set(total)
        expression = ""
    except:
        equation.set("ERROR")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


def but(source, side, text, command=None):
    store = Button(source, text=text, fg="black", bg="red", relief=RAISED, command=command)
    store.pack(side=side, expand=YES, fill=BOTH)
    return store


def cal(source, side):
    steve = Frame(source, borderwidth=4, bd=4, bg="blue")
    steve.pack(side=side, expand=YES, fill=BOTH)


if __name__ == "__main__":
    gui = Tk()
    gui.configure(bg="blue")
    gui.option_add('*Font', 'arial 14 bold')
    gui.title("My Calculator")
    equation = StringVar()
    expression_field = Entry(gui, relief=RIDGE, textvariable=equation, justify='left', bd=20, bg="dark red")
    expression_field.pack(side=TOP, expand=YES, fill=BOTH)
    equation.set("enter your expression")

    but(gui, TOP, "CE", command=clear)
    but(gui, TOP, "C", command=clear)

    equal = but(gui, TOP, "=", command=equalpress)

    for Num in ("789/", "456*", "123-", "0.+()"):
        tim = cal(gui, TOP)
        for But in Num:
            but(tim, LEFT, But,
                lambda store=equation, q=But: store.set(store.get() + q))

    gui.mainloop()
