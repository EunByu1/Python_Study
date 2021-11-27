from tkinter import *

def cry():
    print("♥ Meow ♥")

# 창 설정 
root = Tk()
root.title("Eunji's first GUI test")
root.geometry("540x380+600+250")
root.resizable(False,False)


# text로 된 버튼 생성 
btn1 = Button(root, padx = 5.5, pady = 7.5, fg="white", bg="black", text = "Button_1")
btn2 = Button(root, width = 8, height = 2,fg = "red", bg="black", text = "Button_2")
btn1.pack()
btn2.pack()


# image로 된 버튼 생성
photo = PhotoImage(file = "C:\\Users\\82105\\Desktop\\GUI\\Cat.png")
btn3 = Button(root, image = photo, command = cry)
btn3.pack()


root.mainloop()
    