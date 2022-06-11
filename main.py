from tkinter import *
from pymongo import MongoClient
import time
import os

root = Tk()
root.title("Kütüphane Yönetim Sistemi v0.1")
root.geometry("700x500+450+150")
root.iconbitmap("icon.ico")
backgroundColor = "#4D4A4D"
background = Label(bg=backgroundColor, width=700, height=500)
background.place(x=0, y=0)
root.resizable(width=False, height=False)

# Burada kendi MongoDB'nize bağlamanız gerekiyor.

DATABASE_LINK = "mongodb+srv://<username>:<password>@fazztech.zpsm83s.mongodb.net/?retryWrites=true&w=majority" # Kendi link adresiniz olmalıdır.

client = MongoClient(DATABASE_LINK)
database = client["Database"]
kitaplar = database["Books"]
verilenler = database["Gives"]

def YENI_KAYIT():
    data = {
        "Kitap":entry1.get(),
        "KitapNo":entry2.get(),
        "Yazar":entry3.get(),
        "Türü":entry4.get(),
        "Stok":entry5.get(),
        "Alıcı":entry6.get()
    }

    kitaplar.insert_one(data)
    root.destroy()
    os.system("main.py")

def KAYIT_SIL():
    ISLEM_LABEL["text"] = "İşlem : Kayıt Sil"
    try:
        v = entry1.get()
        sorgu = {"Kitap":v}
        for i in kitaplar.find(sorgu, {}):
            kitaplar.delete_one(i)
            root.destroy()
            os.system("main.py")
    except:
        ISLEM_LABEL["fg"] = "white"
        ISLEM_LABEL["font"] = "Arial 12"
        ISLEM_LABEL["text"] = "Silmek istediğiniz kitabın ismini giriniz."

def KAYIT_GUNCELLE():
    try:
        v1 = entry1.get()
        v2 = entry2.get()
        v3 = entry3.get()
        v4 = entry4.get()
        v5 = entry5.get()
        v6 = entry6.get()
        sorgu = {"Kitap":v1}
        sorguyap = kitaplar.find_one(sorgu, {})
        if sorguyap != None:
            ISLEM_LABEL["text"] = "İşlem : Kayıt Düzenle"
            for i in kitaplar.find(sorgu, {}):
                data5 = {
                    "Kitap":v1,
                    "KitapNo":v2,
                    "Yazar":v3,
                    "Türü":v4,
                    "Stok":v5,
                    "Alıcı":v6,
                }
                kitaplar.delete_one(i)
                kitaplar.insert_one(data5)
                root.destroy()
                os.system("main.py")
        else:
            ISLEM_LABEL["fg"] = "white"
            ISLEM_LABEL["font"] = "Arial 10"
            ISLEM_LABEL["text"] = "Düzenlemek istediğiniz kitabın bilgilerini giriniz"
            ISLEM_LABEL.place(x=400, y=315)
            ISLEM_LABEL2 = Label(text="Kitap ismi değişemez.", bg=backgroundColor, fg="white", font="Arial 10")
            ISLEM_LABEL2.place(x=430, y=350)
    except:
        ISLEM_LABEL["fg"] = "white"
        ISLEM_LABEL["font"] = "Arial 12"
        ISLEM_LABEL["text"] = "Düzenlemek istediğiniz kitabın bilgilerini giriniz"



ISLEM_LABEL = Label(text="işlem : Yeni Kayıt", bg=backgroundColor, fg="yellow", font="Arial 18")
ISLEM_LABEL.place(x=430, y=315)

label1 = Label(text="Fazz | Kütüphane Sistemi v0.1", bg=backgroundColor, fg="white", font="Arial 16")
label1.place(x=10, y=20)

buton1 = Button(text="Yeni Kayıt", font="Arial 18", bg="green", fg="white", command=YENI_KAYIT)
buton1.place(x=10, y=50)

buton2 = Button(text="Kayıt Sil", font="Arial 18", bg="green", fg="white", command=KAYIT_SIL)
buton2.place(x=150, y=50)

buton3 = Button(text="Kayıt Düzenle", font="Arial 18", bg="green", fg="white", command=KAYIT_GUNCELLE)
buton3.place(x=270, y=50)

buton4 = Button(text="Kitap Ver", font="Arial 18", bg="green", fg="white")
buton4.place(x=450, y=50)

label2 = Label(text="Kitap :", bg=backgroundColor, fg="white", font="Arial 18")
label2.place(x=10, y=270)

entry1 = Entry(bg="lightgray", fg="black", font="Arial 18")
entry1.place(x=100, y=270)
entry1.focus()

label3 = Label(text="Kitap No :", bg=backgroundColor, fg="white", font="Arial 18")
label3.place(x=10, y=320)

entry2 = Entry(bg="lightgray", fg="black", font="Arial 18")
entry2.place(x=130, y=320)

label4 = Label(text="Yazar :", bg=backgroundColor, fg="white", font="Arial 18")
label4.place(x=10, y=370)

entry3 = Entry(bg="lightgray", fg="black", font="Arial 18")
entry3.place(x=100, y=370)

label5 = Label(text="Türü :", bg=backgroundColor, fg="white", font="Arial 18")
label5.place(x=10, y=420)

entry4 = Entry(bg="lightgray", fg="black", font="Arial 18")
entry4.place(x=100, y=420)

label6 = Label(text="Stok :", bg=backgroundColor, fg="white", font="Arial 18")
label6.place(x=10, y=465)

entry5 = Entry(bg="lightgray", fg="black", font="Arial 18")
entry5.place(x=100, y=465)

label7 = Label(text="Alıcı :", bg=backgroundColor, fg="white", font="Arial 18")
label7.place(x=370, y=465)

entry6 = Entry(bg="lightgray", fg="black", font="Arial 16")
entry6.place(x=450, y=465)

books = Listbox(bg="lightgray",width=110)
books.place(x=10, y=100)

sb = Scrollbar(orient=HORIZONTAL)
sb.pack(fill=X)

books.configure(xscrollcommand=sb.set)
sb.config(command=books.xview)

for i in kitaplar.find({},{"_id":0}):
    books.insert(0, i)


root.mainloop()