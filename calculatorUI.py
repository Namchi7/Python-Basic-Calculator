import tkinter as tk


root = tk.Tk()
root.title("Calculator")

e = tk.Entry(root, width=60, borderwidth=4)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def buttonClick(num):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(num))


def equalClick():
    exp = e.get()
    op = ["+", "-", "*", "/"]

    if exp.isdigit():
        value = exp
    else:
        # --------------------------------------
        checkOp = False
        checkDg = False
        i = 0
        for ch in exp:
            # print(ch)
            if exp[0] == '0':
                exp = exp[1:]

            if ch in op:
                checkOp = True

            if ch.isdigit() and ch == '0':
                checkDg = False

            if ch.isdigit() and ch != '0':
                checkDg = True
                checkOp = False

            if checkOp == True and checkDg == False:
                exp = exp[0:i] + exp[i+1:]
                i -= 1
            i += 1
        #----------------------------------------

        value = eval(exp)

    e.delete(0, tk.END)
    e.insert(0, value)


def buttonClear():
    e.delete(0, tk.END)


b1 = tk.Button(root, text="1", padx=40, pady=20,
               command=lambda: buttonClick("1"))
b2 = tk.Button(root, text="2", padx=40, pady=20,
               command=lambda: buttonClick("2"))
b3 = tk.Button(root, text="3", padx=40, pady=20,
               command=lambda: buttonClick("3"))
b4 = tk.Button(root, text="4", padx=40, pady=20,
               command=lambda: buttonClick("4"))
b5 = tk.Button(root, text="5", padx=40, pady=20,
               command=lambda: buttonClick("5"))
b6 = tk.Button(root, text="6", padx=40, pady=20,
               command=lambda: buttonClick("6"))
b7 = tk.Button(root, text="7", padx=40, pady=20,
               command=lambda: buttonClick("7"))
b8 = tk.Button(root, text="8", padx=40, pady=20,
               command=lambda: buttonClick("8"))
b9 = tk.Button(root, text="9", padx=40, pady=20,
               command=lambda: buttonClick("9"))
b0 = tk.Button(root, text="0", padx=40, pady=20,
               command=lambda: buttonClick("0"))

bAdd = tk.Button(root, text="+", padx=38, pady=52,
                 command=lambda: buttonClick("+"))
bSub = tk.Button(root, text="-", padx=39, pady=20,
                 command=lambda: buttonClick("-"))
bMul = tk.Button(root, text="*", padx=39, pady=20,
                 command=lambda: buttonClick("*"))
bDiv = tk.Button(root, text="/", padx=39, pady=20,
                 command=lambda: buttonClick("/"))
bEq = tk.Button(root, text="=", padx=137, pady=20,
                command=lambda: equalClick())
bClr = tk.Button(root, text="Clear", padx=78, pady=20,
                 command=buttonClear)


b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0)

bAdd.grid(row=4, column=3, rowspan=2)
bSub.grid(row=3, column=3)
bMul.grid(row=2, column=3)
bDiv.grid(row=1, column=3)
bEq.grid(row=5, column=0, columnspan=3)
bClr.grid(row=4, column=1, columnspan=2)


root.mainloop()
