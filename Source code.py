import os
import time

import tkinter.messagebox
import pywinstyles
import customtkinter
from customtkinter import *

customtkinter.set_appearance_mode("System")


type_action = None


win = CTk()

chasi_var = customtkinter.IntVar()
minuti_var = customtkinter.IntVar()
secundi_var = customtkinter.IntVar()

rgb = True

win.iconbitmap(default="favicon.ico")
win.title("Computer offer")
win.geometry("500x500")
win.resizable(False,False)

tabview = customtkinter.CTkTabview(master=win, width=500, height=500)
tabview.pack(padx=20, pady=20)

tabview.add("Тип")  # add tab at the end
tabview.add("Время")  # add tab at the end
tabview.add("Запуск")
tabview.set("Тип")  # set currently visible tab

def test(value):
    global type_action
    type_action = value

segemented_button = customtkinter.CTkSegmentedButton(tabview.tab("Тип"), values=["Перезагрузка", "Выключение", "Выход"], command=test)
segemented_button.pack()

pywinstyles.py_win_style.change_title_color(win, "white")
pywinstyles.change_border_color(win, "#8cc6ff")
pywinstyles.change_header_color(win, "#8cc6ff")
pywinstyles.py_win_style.apply_style(win, "mica")

def tick(hours: int, minutes: int, seckonds: int):
    times = 0
    if int(hours) > 0:
        times += int(hours) * 3600
    if int(minutes) > 0:
        times += int(minutes) * 60
    if int(seckonds) > 0:
        times += int(seckonds)
    time.sleep(times)
    if type_action == "Выключение":
        os.system("shutdown /s /t 0")
    elif type_action == "Перезагрузка":
        os.system("shutdown /r")  # исправлено на /r для перезагрузки
    elif type_action == "Выход":
        os.system("shutdown /l")
    else:
        tkinter.messagebox.showerror(title="ERROR!", message="Error when starting timer", detail="Не указан тип действия")




def on_mousewheel1(event):
    if event.delta == 120:
        if chasi_var.get() < 9:
            chasi_var.set(chasi_var.get() + 1)
        else:
            pass
    elif event.delta == -120:
        if chasi_var.get() == 0:
            pass
        else:
            chasi_var.set(chasi_var.get() - 1)

def on_mousewheel2(event):
    if event.delta == 120:
        if minuti_var.get() < 60:
            minuti_var.set(minuti_var.get() + 1)
        else:
            pass
    elif event.delta == -120:
        if minuti_var.get() == 0:
            pass
        else:
            minuti_var.set(minuti_var.get() - 1)

def on_mousewheel3(event):
    if event.delta == 120:
        if secundi_var.get() < 60:
            secundi_var.set(secundi_var.get() + 1)
        else:
            pass
    elif event.delta == -120:
        if secundi_var.get() == 0:
            pass
        else:
            secundi_var.set(secundi_var.get() - 1)



frame1 = CTkFrame(tabview.tab("Время"))
frame1.pack(fill="x")

CTkLabel(master=frame1, text="Выключить через:", font=CTkFont("Arial", 20)).pack()

frame2 = CTkFrame(tabview.tab("Время"))
frame2.pack(fill="x")

CTkLabel(master=frame2, text="Часы", font=CTkFont("Arial", 20)).pack(side="left", padx="40", pady="20")
CTkLabel(master=frame2, text="Минуты", font=CTkFont("Arial", 20)).pack(side="left", padx="40", pady="20")
CTkLabel(master=frame2, text="Секунды", font=CTkFont("Arial", 20)).pack(side="left", padx="40", pady="20")


frame3 = CTkFrame(tabview.tab("Время"))
frame3.pack(fill="x")

chasi = customtkinter.CTkEntry(master=frame3, textvariable=chasi_var, width=100, height=100, font=CTkFont("Arial", 50))
chasi.pack(side="left", padx="20")

chasi.bind('<MouseWheel>', on_mousewheel1)


minuti = customtkinter.CTkEntry(master=frame3, textvariable=minuti_var, width=100, height=100, font=CTkFont("Arial", 50))
minuti.pack(side="left", padx="20")

minuti.bind('<MouseWheel>', on_mousewheel2)

secundi = customtkinter.CTkEntry(master=frame3, textvariable=secundi_var, width=100, height=100, font=CTkFont("Arial", 50))
secundi.pack(side="left", padx="20")

secundi.bind('<MouseWheel>', on_mousewheel3)



startbtn = CTkButton(master=tabview.tab("Запуск"), text="START!", command=lambda: tick(chasi.get(), minuti.get(), secundi.get()))
startbtn.pack()



win.mainloop()