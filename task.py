from tkinter import *
root = Tk()
root.title("calc")
root.geometry("200x300+300+100")
def clear():
    my_entry.delete(0 ,END)
    
def button_click(number):
    my_entry.insert(END,str(number))
   
def DEL():
    DELETE = my_entry.get()
    if DELETE:
        my_entry.delete(len(DELETE) -1 ,END)
def equal():
    try:
        
        expression = my_entry.get()
        
       
        result = eval(expression)
        
        
        my_entry.delete(0, END)
        my_entry.insert(0, str(result))
        
    except Exception:
        
        my_entry.delete(0, END)
        my_entry.insert(0, "Error")
    
my_entry = Entry(root, font=("Consolas",16,"bold"))
my_entry.place(x = 25 , y = 10, width= 150, height = 30)
button_0 = Button(root, text = "0", padx = 10 , pady = 2,command = lambda: button_click(0))
button_0.place(x = 0 , y = 52)
button_1 = Button(root,text = "1", padx = 10 ,pady = 2,command = lambda: button_click(1))
button_1.place(x = 0 , y = 80)
button_2 =Button (root, text = "2",padx = 10 , pady = 2,command = lambda: button_click(2))
button_2.place(x = 35 , y = 80)
button_3 = Button(root, text = "3",padx = 10 , pady = 2,command = lambda: button_click(3) )
button_3.place(x = 70 , y = 80 )
button_4 = Button(root, text= "4",padx = 10 ,pady = 2,command = lambda: button_click(4))
button_4.place(x = 0 , y = 108)
button_5 = Button(root, text = 5 , padx = 10 ,pady =2,command = lambda: button_click(5))
button_5.place(x = 35 , y = 108)
button_6 = Button(root , text = "6", padx = 10, pady =2,command = lambda: button_click(6))
button_6.place(x = 70 , y = 108)
button_7 = Button (root, text = "7",padx = 10, pady = 2,command = lambda: button_click(7))
button_7.place(x = 0 , y =136)
button_8 = Button (root , text = "8" ,padx = 10 , pady = 2,command = lambda: button_click(8))
button_8.place(x = 35 , y = 136)
button_9 =Button(root,text = "9",padx = 10 ,pady = 2,command = lambda: button_click(9))
button_9.place(x = 70 , y = 136)
button_clear =Button(root , text = "clear" , padx = 10 , pady = 2,command = clear)
button_clear.place(x = 150, y = 136)
button_del = Button (root ,text = "DEL", padx = 10 ,pady = 2 , command = DEL )
button_del.place(x = 155 , y = 108)
button_x =Button(root, text ="X", padx = 10 ,pady = 2,command = lambda: button_click("*"))
button_x.place(x = 170 , y = 80)
button_add = Button(root, text = "+", padx = 10 , pady = 2,command = lambda: button_click("+"))
button_add.place(x = 170 , y = 52)
button_sub =Button(root , text = "-" , padx = 10 ,pady = 2 ,command = lambda: button_click("-"))
button_sub.place(x = 137 , y = 52 )
button_eqal = Button(root , text = "=", padx = 20 ,pady = 5,command = equal)
button_eqal.place(x = 150 , y = 165)
root.mainloop()