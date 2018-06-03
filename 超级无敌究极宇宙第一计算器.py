import math
from tkinter import *

u = ""
uu=""
L = []
L1 =[]
r = ""

def press(n, m,label1):
    global L
    global u
    global uu
    global L1
    L += (str(n))
    L1 +=(str(m))
    u = "".join(L)
    uu = "".join(L1)
    print(u)
    label1["text"] = uu
    
def AC(label1, label2):
    global u
    global L
    global L1
    global uu
    L.clear()
    L1.clear()
    u = "".join(L)
    print(u)
    print("归零")
    label1["text"] = ""
    label2["text"] = ""
# def jiechen():
#   global u
#  u+="math.factorial("+u+")"
# print(u)   阶乘未实现
# 差一个y的x次方根

def dele(label1, label2):
    global L
    global u
    global L1
    global uu
    L.pop()
    L1.pop()
    u = "".join(L)
    uu = "".join(L1)
    print(u)
    label1["text"] = uu
    label2["text"] = ""

def over(label2):
    global u
    global L
    global r
    global L1
    global uu
    u = "".join(L)
    r = eval(u)
    print(r)
    print("运算完毕")
    label2["text"] = str(r)

def StandardC():
    global u
    global r
    global L
    global L1
    global uu
    app = Toplevel()
    app.geometry("400x525")
    app.title("小霸王牌计算器---油嘎哇嘎跌ki我苦辣呜")
    label1 = Label(app, fg="#828282", bg="black", anchor='se', font=('微软雅黑', 30))
    label1.place(x=0, y=0, width=400, height=55)
    label2 = Label(app, fg="white", bg="black", anchor='se', font=('微软雅黑', 60))
    label2.place(x=0, y=55, width=400, height=95)
    # b11=Button(app,text="MC", font=('微软雅黑', 20)).place(x=0,y=150,width=100,height=75)
    # b12=Button(app,text="M+", font=('微软雅黑', 20)).place(x=100,y=150,width=100,height=75)
    # b13=Button(app,text="M-", font=('微软雅黑', 20)).place(x=200,y=150,width=100,height=75)
    # b14=Button(app,text="MR", font=('微软雅黑', 20)).place(x=300,y=150,width=100,height=75)
    b21 = Button(app, text="    AC", fg="orange", command=lambda: AC(label1, label2), anchor="w", font=('微软雅黑', 20)).place(x=0, y=150,width=200,height=75)
    b22 = Button(app, text="←", fg="orange", font=('微软雅黑', 20), command=lambda: dele(label1, label2)).place(x=200,y=150, width=100,height=75)
    # b23=Button(app,text="+/-", font=('微软雅黑', 20)).place(x=200,y=225,width=100,height=75)
    b24 = Button(app, text="÷", command=lambda: press("/","÷", label1), font=('微软雅黑', 20)).place(x=300, y=150, width=100,height=75)
    b31 = Button(app, text="7", command=lambda: press("7","7",label1), font=('微软雅黑', 20)).place(x=0, y=225, width=100,height=75)
    b32 = Button(app, text="8", command=lambda: press("8","8", label1), font=('微软雅黑', 20)).place(x=100, y=225, width=100,height=75)
    b33 = Button(app, text="9", command=lambda: press("9", "9",label1), font=('微软雅黑', 20)).place(x=200, y=225, width=100,height=75)
    b34 = Button(app, text="×", command=lambda: press("*","×", label1), font=('微软雅黑', 20)).place(x=300, y=225, width=100,height=75)
    b41 = Button(app, text="4", command=lambda: press("4", "4",label1), font=('微软雅黑', 20)).place(x=0, y=300, width=100,height=75)
    b42 = Button(app, text="5", command=lambda: press("5","5", label1), font=('微软雅黑', 20)).place(x=100, y=300, width=100,height=75)
    b43 = Button(app, text="6", command=lambda: press("6", "6",label1), font=('微软雅黑', 20)).place(x=200, y=300, width=100,height=75)
    b44 = Button(app, text="-", command=lambda: press("-","-", label1), font=('微软雅黑', 20)).place(x=300, y=300, width=100,height=75)
    b51 = Button(app, text="1", command=lambda: press("1", "1",label1), font=('微软雅黑', 20)).place(x=0, y=375, width=100,height=75)
    b52 = Button(app, text="2", command=lambda: press("2", "2",label1), font=('微软雅黑', 20)).place(x=100, y=375, width=100,height=75)
    b53 = Button(app, text="3", command=lambda: press("3", "3",label1), font=('微软雅黑', 20)).place(x=200, y=375, width=100,height=75)
    b54 = Button(app, text="+", command=lambda: press("+", "+",label1), font=('微软雅黑', 20)).place(x=300, y=375, width=100,height=75)
    b61 = Button(app, text="    0", command=lambda: press("0", "0",label1), font=('微软雅黑', 20), anchor="w").place(x=0, y=450,width=200,height=75)
    b62 = Button(app, text=".", command=lambda: press(".", ".",label1), font=('微软雅黑', 20)).place(x=200, y=450, width=100,height=75)
    b63 = Button(app, text="=", command=lambda: over(label2), fg="white", bg="orange", font=('微软雅黑', 20)).place(x=300, y=450,width=100,height=75)
    app.update()

def ScientificC():
    global u
    global r
    global L
    global L1
    global uu
    window = Toplevel()
    window.geometry("800x400")
    window.title("小霸王牌超级计算器---竜が我が敌を喰らう")
    label1 = Label(window,bg = "black",fg='#828282', anchor='se', font=('微软雅黑', 30))
    label1.place(x = 0,y = 0, width= 800,height =50)
    label2 = Label(window,fg= "white", bg = "black", anchor='se', font=('微软雅黑', 60))
    label2.place(x = 0,y = 50, width= 800,height =100)
    imgb1=PhotoImage(file="1.gif")
    imgb2=PhotoImage(file="2.gif") 
    b21 = Button(window, text="1/x", command=lambda: press("**(-1)","^(-1)", label1)).place(x=0, y=150, width=100, height=50)
    b22 = Button(window, text="x^2", command=lambda: press("**2", "^2",label1)).place(x=100, y=150, width=100, height=50)
    b23 = Button(window, text="x^3", command=lambda: press("**3", "^3",label1)).place(x=200, y=150, width=100, height=50)
    b24 = Button(window, text="y^x", command=lambda: press("**","^", label1)).place(x=300, y=150, width=100, height=50)
    b25 = Button(window, text="AC", fg="orange", command=lambda: AC(label1, label2)).place(x=400, y=150, width=100,height=50)
    b26 = Button(window, text="←", fg="orange", command=lambda: dele(label1, label2)).place(x=500, y=150, width=100,height=50)
    b27 = Button(window,text="",image=imgb1 ).place(x = 600,y = 150, width = 100, height = 50)
    b28 = Button(window, text="÷", command=lambda: press("/", "÷",label1)).place(x=700, y=150, width=100, height=50)
    b31 = Button(window, text="x!", command=lambda: press("math.factorial(","!(", label1)).place(x=0, y=200, width=100, height=50)
    b32 = Button(window, text="√", command=lambda: press("math.sqrt(","√(", label1)).place(x=100, y=200, width=100, height=50)
    b33 = Button(window,text="",image=imgb2 ).place(x = 200,y = 200, width = 100, height = 50)
    b34 = Button(window, text="lg", command=lambda: press("math.log10(", "lg(",label1)).place(x=300, y=200, width=100, height=50)
    b35 = Button(window, text="7", fg="white", bg="grey", command=lambda: press("7","7", label1)).place(x=400, y=200,width=100,height=50)
    b36 = Button(window, text="8", fg="white", bg="grey", command=lambda: press("8","8", label1)).place(x=500, y=200,width=100,height=50)
    b37 = Button(window, text="9", fg="white", bg="grey", command=lambda: press("9", "9",label1)).place(x=600, y=200, width=100,height=50)
    b38 = Button(window, text="×", command=lambda: press("*", "×",label1)).place(x=700, y=200, width=100, height=50)
    b41 = Button(window, text="sin", command=lambda: press("math.sin(", "sin(",label1)).place(x=0, y=250, width=100, height=50)
    b42 = Button(window, text="cos", command=lambda: press("math.cos(", "cos(",label1)).place(x=100, y=250, width=100, height=50)
    b43 = Button(window, text="tan", command=lambda: press("math.tan(", "tan(",label1)).place(x=200, y=250, width=100, height=50)
    b44 = Button(window, text="ln", command=lambda: press("math.log(", "ln(",label1)).place(x=300, y=250, width=100, height=50)
    b45 = Button(window, text="4", fg="white", bg="grey", command=lambda: press("4","4", label1)).place(x=400, y=250,width=100,height=50)
    b46 = Button(window, text="5", fg="white", bg="grey", command=lambda: press("5", "5",label1)).place(x=500, y=250,width=100,height=50)
    b47 = Button(window, text="6", fg="white", bg="grey", command=lambda: press("6", "6",label1)).place(x=600, y=250,width=100,height=50)
    b48 = Button(window, text="-", command=lambda: press("-","-", label1)).place(x=700, y=250, width=100, height=50)
    b51 = Button(window, text="sinh", command=lambda: press("math.sinh(", "sinh(",label1)).place(x=0, y=300, width=100,height=50)
    b52 = Button(window, text="cosh", command=lambda: press("math.cosh(", "cosh(",label1)).place(x=100, y=300, width=100,height=50)
    b53 = Button(window, text="tanh", command=lambda: press("math.tanh(", "tanh(",label1)).place(x=200, y=300, width=100, height=50)
    b54 = Button(window, text="e^x", command=lambda: press("math.exp(","e^(", label1)).place(x=300, y=300, width=100, height=50)
    b55 = Button(window, text="1", fg="white", bg="grey", command=lambda: press("1","1", label1)).place(x=400, y=300,width=100,height=50)
    b56 = Button(window, text="2", fg="white", bg="grey", command=lambda: press("2", "2",label1)).place(x=500, y=300,width=100,height=50)
    b57 = Button(window, text="3", fg="white", bg="grey", command=lambda: press("3","3", label1)).place(x=600, y=300,width=100, height=50)
    b58 = Button(window, text="+", command=lambda: press("+", "+",label1)).place(x=700, y=300, width=100, height=50)
    b61 = Button(window, text="e", command=lambda: press("math.e", "e",label1)).place(x = 0,y = 350, width = 100, height = 50)
    b62 = Button(window, text="π", command=lambda: press("math.pi","π", label1)).place(x=100, y=350, width=100, height=50)
    b63 = Button(window, text="(", command=lambda: press("(", "(",label1)).place(x=200, y=350, width=100, height=50)
    b64 = Button(window, text=")", command=lambda: press(")", ")",label1)).place(x=300, y=350, width=100, height=50)
    b65 = Button(window, text="0", fg="white", bg="grey", command=lambda: press("0","0", label1)).place(x=400, y=350,width=200,height=50)
    b67 = Button(window, text=".", fg="white", bg="grey", command=lambda: press(".","." ,label1)).place(x=600, y=350,width=100,height=50)
    b68 = Button(window, text="＝", fg="white", bg="orange", command=lambda: over(label2)).place(x=700, y=350, width=100,height=50)
    window.update()
    
windows = Tk()
windows.geometry("400x300")
windows.title("Σ(っ °Д °;)っ一个按键99999")
img1=PhotoImage(file="半藏.gif") 
Label(windows, text="请谨慎选择，你的选择将会影响到你这几秒钟之后的人生", image=img1,fg="black", bg="white",).place(x=0, y=0, width=400, height=200)
Button(windows, text="油嘎哇嘎跌ki我苦辣呜", command=StandardC, bg="lightblue").place(x=0, y=200, width=200, height=100)
Button(windows, text="竜が我が敌を喰らう", command=ScientificC, bg="lightgrey").place(x=200, y=200, width=200, height=100)
windows.mainloop()
