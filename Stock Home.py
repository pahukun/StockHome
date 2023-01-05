import sqlite3 as sql3
from tkinter import *
from tkinter import ttk, tkentrycomplete, messagebox


# Login Condition
def LoginClick():
    if EntUsername_Login.get() == "":
        WarningMSG("Please Enter Username", "#FBCCCC")
    else:
        conn = sql3.connect('stockhome.sqlite')
        cursor = conn.cursor()
        sql = 'select * from userdata where user="%s"' % EntUsername_Login.get().lower()
        cursor.execute(sql)
        check = cursor.fetchall()
        if check == []:
            WarningMSG("Username Not found", "#FBCCCC")
        elif check[0][1] != EntPassword_Login.get():
            WarningMSG("Invalid Password", "#FBCCCC")
        else:
            global name, admin, user
            user = check[0][0]
            name = check[0][2]
            admin = check[0][3]
            UsernameLogin.delete(0, END)
            PasswordLogin.delete(0, END)
            MainMenu()


# Menu Admin
def MainMenu():
    global windowMainMenu
    root.withdraw()
    windowMainMenu = Toplevel(root)
    windowMainMenu.title("Stock Home : MAIN MENU")
    windowMainMenu.geometry('%dx%d+%d+%d' % (w, h, x, y))
    windowMainMenu.columnconfigure(0, weight=1)
    windowMainMenu.columnconfigure(1, weight=1)
    for r in range(7):
        windowMainMenu.rowconfigure(r, weight=1)
    pos = 0
    if admin == 'T':
        bg = "#ADB0FF"
        for index, item in enumerate(colorListAdmin):
            Frame(windowMainMenu, bg=item).place(x=0, y=pos, width=root.winfo_screenwidth(), height=86)
            pos += 86
        ttk.Button(windowMainMenu, text=MainMenu_btnList[2], style='Main.TButton', command=ShowStock).grid(row=3,
                                                                                                           column=0,
                                                                                                           sticky="e",
                                                                                                           padx=20)
        ttk.Button(windowMainMenu, text=MainMenu_btnList[3], style='Main.TButton', command=add_newuser).grid(row=3,
                                                                                                             column=1,
                                                                                                             sticky="w",
                                                                                                             padx=20)
    else:
        bg = "#FFADD9"
        for index, item in enumerate(colorListUser):
            Frame(windowMainMenu, bg=item).place(x=0, y=pos, width=root.winfo_screenwidth(), height=86)
            pos += 86
        ttk.Button(windowMainMenu, text=MainMenu_btnList[2], style='Main.TButton', command=ShowStock).grid(row=3,
                                                                                                           columnspan=2,
                                                                                                           padx=20)

    ttk.Label(windowMainMenu, text="Welcome " + name, background=bg, foreground='#505050', style='16.TLabel') \
        .grid(row=0, column=1, sticky='ne')
    ttk.Label(windowMainMenu, text="Stock Home", style='Title.TLabel', background=bg).grid(row=0, columnspan=2)
    ttk.Button(windowMainMenu, text=MainMenu_btnList[0], style='Main.TButton', command=add_newproduct).grid(row=2,
                                                                                                            column=0,
                                                                                                            sticky="e",
                                                                                                            padx=20)
    ttk.Button(windowMainMenu, text=MainMenu_btnList[1], style='Main.TButton', command=withdraw).grid(row=2,
                                                                                                      column=1,
                                                                                                      sticky="w",
                                                                                                      padx=20)
    ttk.Button(windowMainMenu, image=logoutPhoto, style="Exit.TButton", command=Logout).grid(row=7, column=0,
                                                                                             sticky='w')
    ttk.Button(windowMainMenu, image=settingPhoto, style="Setting.TButton", command=Setting).grid(row=7, column=1,
                                                                                                  sticky='e')


# Add User
def add_newuser():
    windowMainMenu.destroy()
    global windowAdd
    windowAdd = Toplevel(root)
    windowAdd.title("Stock Home : ADD NEW USER")
    windowAdd.geometry('%dx%d+%d+%d' % (w, h, x, y))
    windowAdd.columnconfigure(0, weight=1)
    windowAdd.columnconfigure(1, weight=1)
    for r in range(7):
        windowAdd.rowconfigure(r, weight=1)
    pos = 0
    for index, item in enumerate(colorListAdmin):
        Frame(windowAdd, bg=item).place(x=0, y=pos, width=root.winfo_screenwidth(), height=86)
        pos += 86
    ttk.Label(windowAdd, text="Add New User", style='Title.TLabel', background="#ADB0FF").grid(row=0, columnspan=2)
    for i, item in enumerate(AddUser_textlist):
        ttk.Label(windowAdd, text=item, background=colorListAdmin[i + 1]).grid(row=i + 1, column=0, sticky="e", padx=10)
        if i < 4:
            if i == 1 or i == 2:
                ttk.Entry(windowAdd, textvariable=AddUser_var[i], width=40, show="*").grid(row=i + 1, column=1,
                                                                                           sticky='w', padx=10)
            else:
                ttk.Entry(windowAdd, textvariable=AddUser_var[i], width=40).grid(row=i + 1, column=1, sticky='w',
                                                                                 padx=10)
    ttk.Button(windowAdd, image=backPhoto, style="Back.TButton", command=lambda: BackToMenu("Add_User")).grid(row=7,
                                                                                                              column=0,
                                                                                                              sticky='w')
    ttk.Button(windowAdd, text="Register", style='Main.TButton', command=Adduser).grid(row=6, columnspan=2, padx=20)
    AddUser_var[4].set("F")
    Radiobutton(windowAdd, text="Admin", variable=AddUser_var[4], value="T", bg=colorListAdmin[5]).grid(row=5, column=1,
                                                                                                        sticky='w',
                                                                                                        padx=10)
    Radiobutton(windowAdd, text="User", variable=AddUser_var[4], value="F", bg=colorListAdmin[5]).grid(row=5, column=1,
                                                                                                       padx=10)


# SQL AddUser
def Adduser():
    if AddUser_var[0].get().lower() == "":
        WarningMSG("Please Enter Username", "#EDCCFB")
    elif AddUser_var[1].get() == "":
        WarningMSG("Please fill up this form", "#EDCCFB")
    elif AddUser_var[2].get() == "":
        WarningMSG("Please fill up this form", "#EDCCFB")
    elif AddUser_var[3].get() == "":
        WarningMSG("Please fill up this form", "#EDCCFB")
    elif AddUser_var[4].get() == "":
        WarningMSG("Please fill up this form", "#EDCCFB")
    else:
        if AddUser_var[2].get() != AddUser_var[1].get():
            WarningMSG("Please Enter Password Again", "#EDCCFB")
        else:
            conn = sql3.connect('stockhome.sqlite')
            cursor = conn.cursor()
            sql = 'select * from userdata where user="%s"' % AddUser_var[0].get().lower()
            cursor.execute(sql)
            check = cursor.fetchall()
            if check == []:
                CompleteMSG("Add New User", "#EDCCFB")
                param = [AddUser_var[i].get() for i in range(len(AddUser_var)) if i != 2]
                param[0] = param[0].lower()
                sql = " insert into userdata values (?,?,?,?);"
                cursor.execute(sql, param)
                conn.commit()
                conn.close()
                for i in AddUser_var:
                    i.set("")
                windowAdd.destroy()
                MainMenu()
            else:
                WarningMSG("Username's already exist!!", "#EDCCFB")


#  Show Stock
def ShowStock():
    global windowshowstock, frame_data, search_cat, cat_box
    windowMainMenu.destroy()
    windowshowstock = Toplevel(root)
    windowshowstock.title("Stock Home : SHOW STOCK")
    windowshowstock.geometry('%dx%d+%d+%d' % (w, 430, x, y))
    search_cat = StringVar()
    search_cat.set("Filter by Category")
    conn = sql3.connect("stockhome.sqlite")
    cursor = conn.cursor()
    sql = 'select NameCategory from category '
    cursor.execute(sql)
    categorylist = cursor.fetchall()
    for r in range(5):
        windowshowstock.rowconfigure(r, weight=1)
    for c in range(4):
        windowshowstock.columnconfigure(c, weight=1)
    pos = 0
    if admin == 'T':
        bg = "#ADB0FF"
        for index, item in enumerate(colorListAdmin):
            Frame(windowshowstock, bg=item).place(x=0, y=pos, width=root.winfo_screenwidth(), height=86)
            pos += 86
        ttk.Button(windowshowstock, text="Update", style="Main.TButton", command=UpdateStockMenu).grid(row=4, column=0,
                                                                                                       columnspan=2,
                                                                                                       sticky="e",
                                                                                                       pady=(200, 0),
                                                                                                       padx=(30, 20))
        ttk.Button(windowshowstock, text="Delete", style="Main.TButton", command=DeleteStockMenu).grid(row=4, column=2,
                                                                                                       columnspan=2,
                                                                                                       sticky="w",
                                                                                                       pady=(200, 0),
                                                                                                       padx=(10, 200))
        ttk.Label(windowshowstock, text=showtitle[0], background=bg, style="30.TLabel").grid(row=0, column=0,
                                                                                             padx=(50, 0),
                                                                                             pady=(15, 5))
        ttk.Label(windowshowstock, text=showtitle[1], background=bg, style="30.TLabel", anchor="c").grid(row=0,
                                                                                                         column=1,
                                                                                                         padx=(130, 0),
                                                                                                         pady=(15, 5),
                                                                                                         sticky="news")
        ttk.Label(windowshowstock, text=showtitle[2], background=bg, style="30.TLabel").grid(row=0, column=2,
                                                                                             padx=(60, 0),
                                                                                             pady=(15, 5))
        ttk.Label(windowshowstock, text=showtitle[3], background=bg, style="30.TLabel").grid(row=0, column=3,
                                                                                             padx=(25, 0), pady=(15, 5),
                                                                                             sticky="w")

    else:
        bg = "#FFADD9"
        for index, item in enumerate(colorListUser):
            Frame(windowshowstock, bg=item).place(x=0, y=pos, width=root.winfo_screenwidth(), height=86)
            pos += 86
        ttk.Label(windowshowstock, text=showtitle[0], background=bg, style="30.TLabel").grid(row=0, column=0,
                                                                                             padx=(20, 0),
                                                                                             pady=(15, 5))
        ttk.Label(windowshowstock, text=showtitle[1], background=bg, style="30.TLabel", anchor="c").grid(row=0,
                                                                                                         column=1,
                                                                                                         padx=(50, 0),
                                                                                                         pady=(15, 5),
                                                                                                         sticky="news")
        ttk.Label(windowshowstock, text=showtitle[2], background=bg, style="30.TLabel").grid(row=0, column=2,
                                                                                             padx=(20, 0),
                                                                                             pady=(15, 5))
        ttk.Label(windowshowstock, text=showtitle[3], background=bg, style="30.TLabel").grid(row=0, column=3,
                                                                                             padx=(25, 0), pady=(15, 5),
                                                                                             sticky="w")

    cat_box = tkentrycomplete.AutocompleteCombobox(windowshowstock, textvariable=search_cat, width=20)
    cat_box.grid(row=4, columnspan=2, column=2, pady=(200, 0), padx=(0, 50), sticky="e")
    cat_box.set_completion_list([cat[0] for cat in categorylist])

    Body = Frame(windowshowstock, bg="#f8beff")
    Body.place(x=30, y=85, width=690, height=260)
    Body.columnconfigure(0, weight=1)
    Body.rowconfigure(0, weight=1)
    canvas = Canvas(Body, bg="#F8BEFF")
    canvas.place(x=0, y=0, width=690, height=260)
    vsb = Scrollbar(Body, orient="vertical", command=canvas.yview)
    vsb.grid(row=0, column=1, sticky='ns')
    canvas.configure(yscrollcommand=vsb.set)
    frame_data = Frame(canvas, bg="#F8BEFF")
    canvas.create_window((0, 0), window=frame_data, anchor="nw")
    for c in range(4):
        frame_data.columnconfigure(c, weight=1)
    sql = "select * from productstock"
    cursor.execute(sql)
    productlist = cursor.fetchall()
    for i, data in enumerate(productlist):
        ttk.Label(frame_data, text=data[0], style="16.TLabel", background="#F8BEFF").grid(row=i, column=0,
                                                                                          padx=(30, 10),
                                                                                          pady=(15, 5))
        ttk.Label(frame_data, text=data[1], style="16.TLabel", background="#F8BEFF", anchor="c").grid(row=i, column=1,
                                                                                                      padx=(40, 0),
                                                                                                      pady=(15, 5),
                                                                                                      sticky="news")
        ttk.Label(frame_data, text=data[2], style="16.TLabel", background="#F8BEFF").grid(row=i, column=2, padx=(50, 0),
                                                                                          pady=(15, 5))
        ttk.Label(frame_data, text=data[3], style="16.TLabel", background="#F8BEFF").grid(row=i, column=3,
                                                                                          padx=(125, 0), pady=(15, 5))
    frame_data.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    ttk.Button(windowshowstock, image=backPhoto, style="Back.TButton", command=lambda: BackToMenu("Show_Stock")) \
        .grid(row=4, column=0, sticky='ws', pady=(200, 0))
    cat_box.bind("<<ComboboxSelected>>", setlabel)


def setlabel(e):
    conn = sql3.connect("stockhome.sqlite")
    cursor = conn.cursor()
    sql = 'select * from productstock where category="%s" ' % search_cat.get()
    cursor.execute(sql)
    newlabel = cursor.fetchall()
    for inx in frame_data.winfo_children():
        inx.destroy()
    for i, data in enumerate(newlabel):
        ttk.Label(frame_data, text=data[0], style="16.TLabel", background="#F8BEFF").grid(row=i, column=0, padx=(30, 0),
                                                                                          pady=(15, 5))
        ttk.Label(frame_data, text=data[1], style="16.TLabel", background="#F8BEFF", width=30, anchor="c").grid(row=i,
                                                                                                                column=1,
                                                                                                                padx=(
                                                                                                                    40,
                                                                                                                    0),
                                                                                                                pady=(
                                                                                                                    15,
                                                                                                                    5),
                                                                                                                sticky="news")
        ttk.Label(frame_data, text=data[2], style="16.TLabel", background="#F8BEFF").grid(row=i, column=2, padx=(50, 0),
                                                                                          pady=(15, 5))
        ttk.Label(frame_data, text=data[3], style="16.TLabel", background="#F8BEFF", anchor="c").grid(row=i, column=3,
                                                                                                      padx=(125, 0),
                                                                                                      pady=(15, 5))


def UpdateStockMenu():
    global EntID_update, EntAmount_update, EntName_update, EntPrice_update, windowUpdateStock
    EntSearch.set("")
    EntID_update = StringVar()
    EntAmount_update = StringVar()
    EntName_update = StringVar()
    EntPrice_update = StringVar()
    windowUpdateStock = Toplevel(windowshowstock)
    windowUpdateStock.title("Stock Home : UPDATE STOCK")
    windowUpdateStock.geometry('%dx%d+%d+%d' % (700, 430, windowshowstock.winfo_screenwidth() / 2 - (700 / 2), y))
    windowUpdateStock.configure(bg="#ADB0FF")
    for r in range(5):
        windowUpdateStock.rowconfigure(r, weight=1)
    windowUpdateStock.columnconfigure(0, weight=1)
    windowUpdateStock.columnconfigure(1, weight=1)
    ttk.Label(windowUpdateStock, text="Please Enter Product ID For Searching", background="#ADB0FF",
              style='30.TLabel').grid(row=0, columnspan=2)
    ttk.Label(windowUpdateStock, text="Enter Product ID :", background="#ADB0FF", style='16.TLabel').grid(row=1,
                                                                                                          column=0,
                                                                                                          columnspan=2,
                                                                                                          sticky="w",
                                                                                                          padx=(80, 0))
    ttk.Entry(windowUpdateStock, width=40, textvariable=EntSearch).grid(row=1, column=0, columnspan=2)
    ttk.Button(windowUpdateStock, text="Search", command=lambda: SearchStock("Update")).grid(row=1, column=0,
                                                                                             columnspan=2, sticky="e",
                                                                                             padx=(0, 100))
    ttk.Label(windowUpdateStock, text="ID :", background="#ADB0FF", style='16.TLabel').grid(row=2, column=0, sticky="w",
                                                                                            padx=(40, 0))
    ttk.Entry(windowUpdateStock, width=30, textvariable=EntID_update, state="disabled").grid(row=2, column=0,
                                                                                             sticky="e", padx=(0, 40))
    ttk.Label(windowUpdateStock, text="Amount :", background="#ADB0FF", style='16.TLabel').grid(row=2, column=1,
                                                                                                sticky="w",
                                                                                                padx=(40, 0))
    ttk.Entry(windowUpdateStock, width=30, textvariable=EntAmount_update).grid(row=2, column=1, sticky="e",
                                                                               padx=(0, 40))
    ttk.Label(windowUpdateStock, text="Name :", background="#ADB0FF", style='16.TLabel').grid(row=3, column=0,
                                                                                              sticky="w", padx=(40, 0))
    ttk.Entry(windowUpdateStock, width=30, textvariable=EntName_update).grid(row=3, column=0,
                                                                             sticky="e", padx=(0, 40))
    ttk.Label(windowUpdateStock, text="Price :", background="#ADB0FF", style='16.TLabel').grid(row=3, column=1,

                                                                                               sticky="w", padx=(40, 0))
    ttk.Entry(windowUpdateStock, width=30, textvariable=EntPrice_update).grid(row=3, column=1,
                                                                              sticky="e", padx=(0, 40))
    ttk.Button(windowUpdateStock, text="Update", style="Main.TButton", command=UpdateStock).grid(row=4, column=0,
                                                                                                 sticky="e", padx=10)
    ttk.Button(windowUpdateStock, text="Cancel", style="Main.TButton",
               command=lambda: CancelClick(windowUpdateStock)).grid(row=4, column=1, sticky="w", padx=10)


def DeleteStockMenu():
    global Bodydelete, datalist, windowDeleteStock
    EntSearch.set("")
    windowDeleteStock = Toplevel(windowshowstock)
    windowDeleteStock.title("Stock Home : DELETE STOCK")
    windowDeleteStock.geometry('%dx%d+%d+%d' % (700, 430, windowshowstock.winfo_screenwidth() / 2 - (700 / 2), y))
    windowDeleteStock.configure(bg="#ADB0FF")
    for r in range(5):
        windowDeleteStock.rowconfigure(r, weight=1)
    windowDeleteStock.columnconfigure(0, weight=1)
    windowDeleteStock.columnconfigure(1, weight=1)
    ttk.Label(windowDeleteStock, text="Please Enter Product ID For Searching", background="#ADB0FF",
              style='30.TLabel').grid(row=0, columnspan=2)
    ttk.Label(windowDeleteStock, text="Enter Product ID :", background="#ADB0FF", style='16.TLabel').grid(row=1,
                                                                                                          column=0,
                                                                                                          columnspan=2,
                                                                                                          sticky="w",
                                                                                                          padx=(80, 0))
    ttk.Entry(windowDeleteStock, width=40, textvariable=EntSearch).grid(row=1, column=0, columnspan=2)
    ttk.Button(windowDeleteStock, text="Search", command=lambda: SearchStock("Delete")).grid(row=1, column=0,
                                                                                             columnspan=2, sticky="e",
                                                                                             padx=(0, 100))
    Bodydelete = Frame(windowDeleteStock, bg="#f8beff")
    Bodydelete.place(x=20, y=200, width=660, height=100)
    for c in range(4):
        Bodydelete.columnconfigure(c, weight=1)
    datalist = [StringVar() for i in range(4)]
    for index, item in enumerate(showtitle):
        ttk.Label(Bodydelete, text=item, background="#f8beff", style="30.TLabel").grid(row=0, column=index)
        ttk.Label(Bodydelete, text="", textvariable=datalist[index], background="#f8beff").grid(row=1, column=index)
    ttk.Button(windowDeleteStock, text="Delete", style="Main.TButton", command=DeleteStock).grid(row=4, column=0,
                                                                                                 sticky="e", padx=10)
    ttk.Button(windowDeleteStock, text="Cancel", style="Main.TButton",
               command=lambda: CancelClick(windowDeleteStock)).grid(row=4, column=1, sticky="w", padx=10)


def SearchStock(page):
    if EntSearch.get() == "":
        WarningMSG("Plase Enter ID For Searching", "#EDCCFB")
    else:
        conn = sql3.connect("stockhome.sqlite")
        cursor = conn.cursor()
        sql = 'select * from productstock where id="%s"' % EntSearch.get()
        cursor.execute(sql)
        data = cursor.fetchall()
        if data == []:
            WarningMSG("Data Not Found!!", "#EDCCFB")
        else:
            for x in data:
                if page == "Update":
                    EntID_update.set(x[0])
                    EntAmount_update.set(x[2])
                    EntName_update.set(x[1])
                    EntPrice_update.set(x[3])
                else:
                    datalist[0].set(x[0])
                    datalist[1].set(x[1])
                    datalist[2].set(x[2])
                    datalist[3].set(x[3])


def DeleteStock():
    conn = sql3.connect("stockhome.sqlite")
    cursor = conn.cursor()
    cursor.execute('delete from productstock where ID="%s"' % EntSearch.get())
    conn.commit()
    CompleteMSG("Delete Product", "#EDCCFB")
    conn.close()
    windowDeleteStock.destroy()
    windowshowstock.destroy()
    ShowStock()


def UpdateStock():
    conn = sql3.connect("stockhome.sqlite")
    cursor = conn.cursor()
    cursor.execute('update productstock set name="%s", amount="%d", price="%.2f" where ID="%s"' % (
    EntName_update.get(), int(EntAmount_update.get()), float(EntPrice_update.get()), EntSearch.get()))
    conn.commit()
    CompleteMSG("Update Product", "#EDCCFB")
    conn.close()
    windowUpdateStock.destroy()
    windowshowstock.destroy()
    ShowStock()


# Add Product
def add_newproduct():
    global windowNewProduct, EntName_Add, EntAmount_Add, EntPrice_Add, EntCategory_Add, Entlist
    EntName_Add = StringVar()
    EntAmount_Add = StringVar()
    EntPrice_Add = StringVar()
    EntCategory_Add = StringVar()
    windowMainMenu.destroy()
    windowNewProduct = Toplevel(root)
    windowNewProduct.title("Stock Home : ADD PRODUCT")
    windowNewProduct.geometry('%dx%d+%d+%d' % (w, h, x, y))
    windowNewProduct.columnconfigure(0, weight=1)
    windowNewProduct.columnconfigure(1, weight=1)
    for r in range(7):
        windowNewProduct.rowconfigure(r, weight=1)
    conn = sql3.connect("stockhome.sqlite")
    cursor = conn.cursor()
    sql = "select NameCategory from category"
    cursor.execute(sql)
    categoryList = cursor.fetchall()
    pos = 0
    if admin == 'T':
        bg = "#ADB0FF"
        for index, item in enumerate(colorListAdmin):
            Frame(windowNewProduct, bg=item).place(x=0, y=pos, width=root.winfo_screenwidth(), height=86)
            pos += 86
        for index, item in enumerate(AddStock_textlist):
            ttk.Label(windowNewProduct, text=item, background=colorListAdmin[index + 2]).grid(row=index + 1, column=0,
                                                                                              sticky="e")
    else:
        bg = "#FFADD9"
        for index, item in enumerate(colorListUser):
            Frame(windowNewProduct, bg=item).place(x=0, y=pos, width=root.winfo_screenwidth(), height=86)
            pos += 86
            for index, item in enumerate(AddStock_textlist):
                ttk.Label(windowNewProduct, text=item, background=colorListUser[index + 2]).grid(row=index + 1,
                                                                                                 column=0, sticky="e")

    NameProduct = ttk.Entry(windowNewProduct, textvariable=EntName_Add, width=30)
    AmountProduct = ttk.Entry(windowNewProduct, textvariable=EntAmount_Add, width=30)
    PriceProduct = ttk.Entry(windowNewProduct, textvariable=EntPrice_Add, width=30)
    CategoryProduct = ttk.Combobox(windowNewProduct, width=28, values=[item[0] for item in categoryList],
                                   state="readonly", textvariable=EntCategory_Add)
    Entlist = [NameProduct, AmountProduct, PriceProduct, CategoryProduct]

    ttk.Label(windowNewProduct, text="Add Product", style='Title.TLabel', background=bg).grid(row=0, columnspan=2)

    for index, item in enumerate(Entlist):
        item.grid(row=index + 1, column=1, sticky="w", padx=20)

    ttk.Button(windowNewProduct, text="Add", style='Main.TButton', command=AddProduct).grid(row=6, columnspan=2,
                                                                                            padx=20)
    ttk.Button(windowNewProduct, image=backPhoto, style="Back.TButton", command=lambda: BackToMenu("Add_Product")) \
        .grid(row=6, column=0, sticky='ws')


def AddProduct():
    if admin == "T":
        bg = "#EDCCFB"
    else:
        bg = "#FBCCCC"

    if EntName_Add.get() == "":
        WarningMSG("Please fill up this form", bg)
    elif EntAmount_Add.get() == "":
        WarningMSG("Please fill up this form", bg)
    elif not EntAmount_Add.get().isdecimal():
        WarningMSG("Please use numeric only", bg)
    elif EntPrice_Add.get() == "":
        WarningMSG("Please fill up this form", bg)
    elif not EntPrice_Add.get().isdecimal():
        WarningMSG("Please use numeric only", bg)
    elif EntCategory_Add.get() == "":
        WarningMSG("Please fill up this form", bg)
    else:
        conn = sql3.connect('stockhome.sqlite')
        cursor = conn.cursor()
        sql = 'select name from productstock where name="%s"' % EntName_Add.get().lower()
        cursor.execute(sql)
        checkNameProduct = cursor.fetchall()
        if checkNameProduct != []:
            if checkNameProduct[0][0] == EntName_Add.get().lower():
                WarningMSG("This Product Name Already Exists!", bg)
        else:
            param = [EntName_Add.get().lower(), EntAmount_Add.get(), EntPrice_Add.get(), EntCategory_Add.get()]
            sql = 'insert into productstock values (NULL,?,?,?,?)'
            cursor.execute(sql, param)
            for i in Entlist:
                i["text"] = ""
            CompleteMSG("Add Product", bg)
            windowNewProduct.destroy()
            MainMenu()
            conn.commit()
            conn.close()


# Withdraw
def withdraw():
    global windowWithdraw, name_withdraw, category_withdraw, button
    windowMainMenu.destroy()
    windowWithdraw = Toplevel(root)
    windowWithdraw.title("Stock Home : WITHDRAW PRODUCT")
    windowWithdraw.geometry('%dx%d+%d+%d' % (w, h, x, y))
    windowWithdraw.columnconfigure(0, weight=1)
    windowWithdraw.columnconfigure(1, weight=1)
    for r in range(7):
        windowWithdraw.rowconfigure(r, weight=1)

    conn = sql3.connect("stockhome.sqlite")
    cursor = conn.cursor()
    sql = "SELECT * FROM productstock"
    cursor.execute(sql)
    stock = cursor.fetchall()
    cursor.execute("SELECT namecategory FROM category")
    category = cursor.fetchall()
    pos = 0
    if admin == 'T':
        bg = colorListAdmin
        for index, item in enumerate(colorListAdmin):
            Frame(windowWithdraw, bg=item).place(x=0, y=pos, width=root.winfo_screenwidth(), height=86)
            pos += 86
        for index, item in enumerate(Withdraw_textlist):
            ttk.Label(windowWithdraw, text=item, background=bg[index + 2]).grid(row=index + 1,
                                                                                column=0,
                                                                                sticky="e")
    else:
        bg = colorListUser
        for index, item in enumerate(colorListUser):
            Frame(windowWithdraw, bg=item).place(x=0, y=pos, width=root.winfo_screenwidth(), height=86)
            pos += 86
            for index, item in enumerate(Withdraw_textlist):
                ttk.Label(windowWithdraw, text=item, background=bg[index + 2]).grid(row=index + 1,
                                                                                    column=0,
                                                                                    sticky="e")

    category_withdraw = tkentrycomplete.AutocompleteCombobox(windowWithdraw, width=28, textvariable=Withdraw_var[1], )
    category_withdraw.grid(row=1, column=1, sticky="w", padx=20)
    category_withdraw.set_completion_list([item[0] for item in category])
    name_withdraw = tkentrycomplete.AutocompleteCombobox(windowWithdraw, width=28, textvariable=Withdraw_var[0])
    name_withdraw.grid(row=2, column=1, sticky="w", padx=20)
    name_withdraw.set_completion_list([item[1] for item in stock])
    ttk.Entry(windowWithdraw, textvariable=Withdraw_var[2], width=30, state="disabled").grid(row=3, column=1,
                                                                                             sticky="w", padx=20)
    ttk.Entry(windowWithdraw, textvariable=Withdraw_var[3], width=30, state="disabled").grid(row=4, column=1,
                                                                                             sticky="w", padx=20)
    ttk.Entry(windowWithdraw, textvariable=Withdraw_var[4], width=30).grid(row=5, column=1,
                                                                           sticky="w", padx=20)
    ttk.Label(windowWithdraw, text="Withdraw Product", style='Title.TLabel', background=bg[0]).grid(row=0, columnspan=2)
    button = ttk.Button(windowWithdraw, text="Withdraw", style='Main.TButton', command=WithdrawProduct)
    button.grid(row=6, columnspan=2, padx=20)
    ttk.Button(windowWithdraw, image=backPhoto, style="Back.TButton", command=lambda: BackToMenu("Withdraw_Product")) \
        .grid(row=6, column=0, sticky='ws')
    category_withdraw.bind("<<ComboboxSelected>>", change_name_onclick)
    name_withdraw.bind("<<ComboboxSelected>>", setentry)


def change_name_onclick(e):
    conn = sql3.connect("stockhome.sqlite")
    cursor = conn.cursor()
    sql = 'SELECT * FROM productstock where category ="%s"' % Withdraw_var[1].get()
    cursor.execute(sql)
    new_name = cursor.fetchall()
    name_withdraw.set_completion_list(x[1] for x in new_name)
    for inx, item in enumerate(Withdraw_var):
        if inx != 1 and inx != 4:
            item.set("")


def setentry(e):
    button["state"] = "normal"
    conn = sql3.connect("stockhome.sqlite")
    cursor = conn.cursor()
    sql = 'SELECT * FROM productstock where name ="%s"' % Withdraw_var[0].get()
    cursor.execute(sql)
    new_data = cursor.fetchall()
    Withdraw_var[2].set(new_data[0][2])
    Withdraw_var[3].set(new_data[0][3])
    if Withdraw_var[2].get() == "0":
        button["state"] = "disabled"


def WithdrawProduct():
    if admin == "T":
        bg = "#EDCCFB"
    else:
        bg = "#FBCCCC"

    conn = sql3.connect("stockhome.sqlite")
    cursor = conn.cursor()
    sql = 'SELECT * FROM productstock where name = "%s"' % Withdraw_var[0].get()
    cursor.execute(sql)
    check_data = cursor.fetchall()
    if Withdraw_var[0].get() != "":
        for x in check_data:
            if Withdraw_var[0].get() not in x or Withdraw_var[1].get() not in x:
                WarningMSG("Can't find Product or Category", bg)
            elif int(Withdraw_var[4].get()) > int(x[2]):
                WarningMSG("Amount is Not Enough", bg)
            else:
                total_withdraw = int(x[2] - int(Withdraw_var[4].get()))
                sql = """UPDATE productstock
                        SET amount = ?
                        WHERE name = ?"""
                cursor.execute(sql, [total_withdraw, Withdraw_var[0].get()])
                conn.commit()
                conn.close()
                CompleteMSG("Withdraw Product", bg)
                for i in Withdraw_var:
                    i.set("")
                windowWithdraw.destroy()
                MainMenu()
    else:
        WarningMSG("Please Enter Product Name", bg)


def WarningMSG(text, bg):
    windowMessage = Toplevel(root)
    windowMessage.title("Warning!!")
    windowMessage.geometry('%dx%d+%d+%d' % (500, 300, 720, 400))
    windowMessage.iconphoto(False, PhotoImage(file='Imgs/exclamation.png'))
    windowMessage.configure(bg=bg)
    ttk.Label(windowMessage, text=text, background=bg, style='30.TLabel').pack(
        pady=70)
    ttk.Button(windowMessage, text="OK", command=windowMessage.destroy, style='Small.TButton').pack()


def CompleteMSG(text, bg):
    windowMessage = Toplevel(root)
    windowMessage.title("Processing Complete")
    windowMessage.geometry('%dx%d+%d+%d' % (400, 300, 760, 400))
    windowMessage.configure(bg=bg)
    ttk.Label(windowMessage, text=text + " Complete", background=bg, style='30.TLabel').pack(
        pady=70)
    ttk.Button(windowMessage, text="OK", command=windowMessage.destroy, style='Small.TButton').pack()


# Logout
def Logout():
    windowMainMenu.destroy()
    root.deiconify()


def Setting():
    global windowSetting, bg
    windowSetting = Toplevel(root)
    windowSetting.title('Stock Home : SETTING')
    windowSetting.geometry('%dx%d+%d+%d' % (
        700, 590, windowMainMenu.winfo_screenwidth() / 2 - (700 / 2),
        windowMainMenu.winfo_screenheight() / 2 - (590 / 2)))
    windowSetting.iconphoto(False, settingPhoto)
    for c in range(3):
        windowSetting.columnconfigure(c, weight=1)
    for r in range(7):
        windowSetting.rowconfigure(r, weight=1)
    if admin == "T":
        bg = "#EDCCFB"
        CategoryMenu()
        menulist = ["Category", "Permission", "Profile"]
        commandlist = [CategoryMenu, PermissionMenu, Profile]
    else:
        bg = "#FBCCCC"
        Profile()
        menulist = ["Profile"]
        commandlist = [Profile]
    menubar = Menu(windowSetting)
    for index, item in enumerate(menulist):
        menubar.add_command(label=item, command=commandlist[index])
    windowSetting.configure(bg=bg, menu=menubar)


def Profile():
    global frmPro, fullname_profile, username_profile
    username_profile = StringVar()
    fullname_profile = StringVar()
    frmPro = Frame(windowSetting, bg=bg)
    frmPro.place(width=700, height=590)
    for i in range(2):
        frmPro.columnconfigure(i, weight=1)
    for i in range(5):
        frmPro.rowconfigure(i, weight=1)
    conn = sql3.connect("stockhome.sqlite")
    cursor = conn.cursor()
    sql = 'SELECT * FROM userdata where user = "%s"' % user
    cursor.execute(sql)
    user_data = cursor.fetchall()
    username_profile.set(user_data[0][0])
    fullname_profile.set(user_data[0][2])
    ttk.Label(frmPro, text="Profile", style='Title.TLabel', background=bg).grid(row=0, columnspan=2)
    ttk.Label(frmPro, text="Username : ", background=bg).grid(row=1, column=0, sticky="ne", padx=(0, 30))
    ttk.Label(frmPro, text="Full name : ", background=bg).grid(row=1, column=0, sticky="se", padx=(0, 30))
    ttk.Entry(frmPro, textvariable=username_profile, width=30, state="disabled").grid(row=1, column=1, sticky="nw",
                                                                                      padx=(30, 0))
    ttk.Entry(frmPro, textvariable=fullname_profile, width=30).grid(row=1, column=1, sticky="sw", padx=(30, 0))
    ttk.Button(frmPro, text="Edit Password", style='Small.TButton', command=changepassword).grid(row=3, column=0,
                                                                                                 sticky="e",
                                                                                                 padx=(10, 0))
    ttk.Button(frmPro, text="Confirm", style='Small.TButton', command=changingfullname).grid(row=3, column=1,
                                                                                             sticky="w",
                                                                                             padx=(60, 0))


def changepassword():
    global oldpassword, newpassword, changepassword_window
    changepassword_window = Toplevel(root)
    changepassword_window.geometry('%dx%d+%d+%d' % (
        400, 300, frmPro.winfo_screenwidth() / 2 - (400 / 2), frmPro.winfo_screenheight() / 2 - (300 / 2)))
    changepassword_window.configure(bg=bg)
    oldpassword = StringVar()
    newpassword = StringVar()
    for i in range(2):
        changepassword_window.columnconfigure(i, weight=1)
    for i in range(4):
        changepassword_window.rowconfigure(i, weight=1)

    ttk.Label(changepassword_window, text="Old Password : ", background=bg).grid(row=1, column=0, sticky="ne",
                                                                                 padx=(0, 10))
    ttk.Label(changepassword_window, text="New Password : ", background=bg).grid(row=1, column=0, sticky="se",
                                                                                 padx=(0, 10))
    ttk.Entry(changepassword_window, textvariable=oldpassword, width=30, show="*").grid(row=1, column=1, sticky="nw",
                                                                                        padx=(10, 0))
    ttk.Entry(changepassword_window, textvariable=newpassword, width=30, show="*").grid(row=1, column=1, sticky="sw",
                                                                                        padx=(10, 0))
    ttk.Button(changepassword_window, text="Ok", style='Small.TButton', command=changingpassword).grid(row=3, column=0,
                                                                                                       sticky="e",
                                                                                                       padx=(10, 0))
    ttk.Button(changepassword_window, text="Cancel", style='Small.TButton', command=changepassword_window.destroy).grid(
        row=3, column=1, sticky="w", padx=(60, 0))


def changingpassword():
    conn = sql3.connect("stockhome.sqlite")
    cursor = conn.cursor()
    sql = 'SELECT password,fullname FROM userdata where user = "%s"' % user
    cursor.execute(sql)
    old_password = cursor.fetchall()
    if old_password[0][0] != oldpassword.get():
        WarningMSG("Please enter your password again", bg)
    elif newpassword.get() == "" or oldpassword.get() == "":
        WarningMSG("Pasword can't be none", bg)
    elif oldpassword.get() == newpassword.get():
        WarningMSG("Cannot Use Old Password!!", bg)
    else:
        sql = 'UPDATE userdata SET password="%s" WHERE user="%s"' % (newpassword.get(), user)
        cursor.execute(sql)
        conn.commit()
        conn.close()
        CompleteMSG("Changing Password", bg)
        windowSetting.destroy()
        changepassword_window.destroy()
        Logout()


def changingfullname():
    global name
    conn = sql3.connect("stockhome.sqlite")
    cursor = conn.cursor()
    sql = 'UPDATE userdata SET fullname = "%s" where user = "%s"' % (fullname_profile.get(), user)
    cursor.execute(sql)
    conn.commit()
    cursor.execute('SELECT fullname from userdata WHERE user="%s"' % user)
    newname = cursor.fetchall()
    name = newname[0][0]
    conn.close()
    CompleteMSG("Edit Profile", bg)
    windowSetting.destroy()
    windowMainMenu.destroy()
    MainMenu()


def CategoryMenu():
    global EntAddCat, EntDeleteCat
    EntDeleteCat = StringVar()
    EntAddCat = StringVar()

    frmCat = Frame(windowSetting, bg=bg)
    frmCat.place(width=700, height=590)
    for c in range(2):
        frmCat.columnconfigure(c, weight=1)
    for r in range(7):
        frmCat.rowconfigure(r, weight=1)
    ttk.Label(frmCat, text='Category', style="Title.TLabel", background=bg).grid(row=0, column=0, columnspan=2)
    ttk.Label(frmCat, text="Category Name : ", background=bg, style='16.TLabel').grid(row=0, column=0,
                                                                                      columnspan=2, sticky="ws",
                                                                                      padx=(80, 0))
    ttk.Entry(frmCat, width=40, textvariable=EntAddCat).grid(row=0, column=0, columnspan=2, sticky="s")
    ttk.Button(frmCat, text="Add", command=AddCategory).grid(row=0, column=0, columnspan=2, sticky="es", padx=(0, 100))
    ttk.Label(frmCat, text="No.", style="30.TLabel", background=bg).grid(row=1, column=0, sticky='e', padx=100)
    ttk.Label(frmCat, text="Name", style="30.TLabel", background=bg).grid(row=1, column=1, sticky='w', padx=100)
    ttk.Label(frmCat, text="Category Number : ", background=bg, style='16.TLabel').grid(row=6, column=0,
                                                                                        columnspan=2, sticky="w",
                                                                                        padx=(80, 0))
    ttk.Entry(frmCat, width=40, textvariable=EntDeleteCat).grid(row=6, column=0, columnspan=2)
    ttk.Button(frmCat, text="Delete", command=DeleteCategory).grid(row=6, column=0, columnspan=2, sticky="e",
                                                                   padx=(0, 100))
    BodyCat = Frame(frmCat)
    BodyCat.place(x=50, y=250, width=600, height=260)
    BodyCat.columnconfigure(0, weight=1)
    BodyCat.rowconfigure(0, weight=1)
    canvas = Canvas(BodyCat, bg=bg)
    canvas.place(width=600, height=260)
    scroll = Scrollbar(BodyCat, orient="vertical", command=canvas.yview)
    scroll.grid(row=0, column=1, sticky='ns')
    canvas.configure(yscrollcommand=scroll.set)
    inCanvas = Frame(canvas, bg=bg)
    canvas.create_window((0, 0), window=inCanvas, anchor='nw')
    for c in range(2):
        inCanvas.columnconfigure(c, weight=1)
    conn = sql3.connect('stockhome.sqlite')
    cursor = conn.cursor()
    sql = "select * from category"
    cursor.execute(sql)
    categorylist = cursor.fetchall()
    for inx, item in enumerate(categorylist):
        ttk.Label(inCanvas, text=item[0], style="16.TLabel", background=bg).grid(row=inx, column=0,
                                                                                 padx=(150, 0),
                                                                                 pady=(15, 5))
        ttk.Label(inCanvas, text=item[1], style="16.TLabel", background=bg).grid(row=inx, column=1,
                                                                                 padx=(205, 0),
                                                                                 pady=(15, 5))
    inCanvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


def AddCategory():
    if EntAddCat.get() == "":
        WarningMSG("Please Enter Category Name", bg)
    else:
        conn = sql3.connect("stockhome.sqlite")
        cursor = conn.cursor()
        cursor.execute('select NameCategory from category where NameCategory="%s"' % EntAddCat.get().lower())
        nameCat = cursor.fetchall()
        if nameCat == []:
            cursor.execute('insert into category values (null,"%s")' % EntAddCat.get().lower())
            CompleteMSG("Add Category", bg)
            conn.commit()
            conn.close()
            CategoryMenu()
        else:
            WarningMSG("Category Name Already Exist!!", bg)


def DeleteCategory():
    if EntDeleteCat.get() == "":
        WarningMSG("Please Enter Category Number", bg)
    else:
        conn = sql3.connect("stockhome.sqlite")
        cursor = conn.cursor()
        cursor.execute('select * from category where ID="%s"' % EntDeleteCat.get())
        check = cursor.fetchall()
        if check == []:
            WarningMSG("Category not found", bg)
        else:
            cursor.execute('delete from category where ID="%s"' % EntDeleteCat.get())
            CompleteMSG("Delete Category", bg)
            conn.commit()
            conn.close()
            CategoryMenu()


def PermissionMenu():
    global EntNamePer, frmPer
    EntNamePer = StringVar()
    frmPer = Frame(windowSetting, bg=bg)
    frmPer.place(width=700, height=590)
    for c in range(2):
        frmPer.columnconfigure(c, weight=1)
    for r in range(7):
        frmPer.rowconfigure(r, weight=1)

    ttk.Label(frmPer, text='Permission', style='Title.TLabel', background=bg).grid(row=0, column=0, columnspan=2)
    ttk.Label(frmPer, text="User", style="30.TLabel", background=bg).grid(row=0, column=0, sticky='s',
                                                                          padx=(45, 0))
    ttk.Label(frmPer, text="Fullname", style="30.TLabel", background=bg).grid(row=0, column=1, sticky='ws',
                                                                              padx=(10, 0))
    ttk.Label(frmPer, text="Permission", style="30.TLabel", background=bg).grid(row=0, column=1, sticky='es',
                                                                                padx=(0, 90))
    ttk.Label(frmPer, text="Enter Username : ", background=bg, style="16.TLabel").grid(row=5, column=0,
                                                                                       sticky="es")
    ttk.Entry(frmPer, textvariable=EntNamePer, width=40).grid(row=5, column=1, sticky="ws")
    ttk.Button(frmPer, text="Update", style="Main.TButton", command=UpdatePermission).place(x=150, y=540)
    ttk.Button(frmPer, text="Delete", style="Main.TButton", command=DeleteUser).place(x=360, y=540)
    BodyPer = Frame(frmPer)
    BodyPer.place(x=50, y=200, width=600, height=260)
    BodyPer.columnconfigure(0, weight=1)
    BodyPer.rowconfigure(0, weight=1)
    canvas = Canvas(BodyPer, bg=bg)
    canvas.place(width=600, height=260)
    scroll = Scrollbar(BodyPer, orient="vertical", command=canvas.yview)
    scroll.grid(row=0, column=1, sticky='ns')
    canvas.configure(yscrollcommand=scroll.set)
    inCanvas = Frame(canvas, bg=bg)
    canvas.create_window((0, 0), window=inCanvas, anchor='nw')
    for c in range(3):
        inCanvas.columnconfigure(c, weight=1)
    conn = sql3.connect('stockhome.sqlite')
    cursor = conn.cursor()
    sql = "select * from userdata order by admin desc"
    cursor.execute(sql)
    permissionlist = cursor.fetchall()
    for inx, item in enumerate(permissionlist):
        ttk.Label(inCanvas, text=item[0], style="16.TLabel", background=bg).grid(row=inx, column=0,
                                                                                 padx=(90, 0),
                                                                                 pady=(15, 5))
        ttk.Label(inCanvas, text=item[2], style="16.TLabel", background=bg).grid(row=inx, column=1,
                                                                                 padx=(90, 0),
                                                                                 pady=(15, 5))
        if item[3] == "T":
            ttk.Label(inCanvas, text="Admin", style="16.TLabel", background=bg).grid(row=inx, column=2,
                                                                                     padx=(90, 0),
                                                                                     pady=(15, 5))
        elif item[3] == "F":
            ttk.Label(inCanvas, text="User", style="16.TLabel", background=bg).grid(row=inx, column=2,
                                                                                    padx=(90, 0),
                                                                                    pady=(15, 5))
    inCanvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


def UpdatePermission():
    global windowUpdatePer, UsernameSQL
    if EntNamePer.get().lower() == "":
        WarningMSG("Please Enter Username", bg)
    else:
        conn = sql3.connect("stockhome.sqlite")
        cursor = conn.cursor()
        cursor.execute('select user, admin from userdata where user="%s"' % EntNamePer.get().lower())
        UsernameSQL = cursor.fetchall()
        if UsernameSQL == []:
            WarningMSG("Username not Found!", bg)
        else:
            windowUpdatePer = Toplevel(frmPer)
            windowUpdatePer.title('Stock Home : PERMISSION')
            windowUpdatePer.geometry('%dx%d+%d+%d' % (
                400, 300, frmPer.winfo_screenwidth() / 2 - (400 / 2), frmPer.winfo_screenheight() / 2 - (300 / 2)))
            windowUpdatePer.configure(bg=bg)
            windowUpdatePer.columnconfigure(0, weight=1)
            windowUpdatePer.columnconfigure(1, weight=1)
            ttk.Label(windowUpdatePer, text=UsernameSQL[0][0], background=bg).grid(row=0, column=0, pady=80,
                                                                                   padx=(20, 0))
            if UsernameSQL[0][1] == "T":
                PermissionCBB.set("Admin")
            else:
                PermissionCBB.set("User")
            CCB = ttk.Combobox(windowUpdatePer, textvariable=PermissionCBB, state="readonly")
            CCB['values'] = ('Admin', 'User')
            CCB.grid(row=0, column=1, pady=80)
            ttk.Button(windowUpdatePer, text="OK", command=ConfirmUpdatePermission).grid(row=1, column=0, sticky="e",
                                                                                         padx=(50, 0))
            ttk.Button(windowUpdatePer, text="Cancel", command=lambda: CancelClick(windowUpdatePer)).grid(row=1,
                                                                                                          column=1,
                                                                                                          sticky="w",
                                                                                                          padx=50)


def ConfirmUpdatePermission():
    conn = sql3.connect("stockhome.sqlite")
    cursor = conn.cursor()
    if PermissionCBB.get() == "Admin":
        cursor.execute('update userdata set admin = "%s" where user = "%s"' % ("T", UsernameSQL[0][0]))
        CompleteMSG("Change Permission", bg)
        conn.commit()
        conn.close()
        windowUpdatePer.destroy()
        PermissionMenu()
    else:
        cursor.execute('update userdata set admin = "%s" where user = "%s"' % ("F", UsernameSQL[0][0]))
        CompleteMSG("Change Permission", bg)
        conn.commit()
        cursor.execute('select admin from userdata where user="%s"' % user)
        checkAdmin = cursor.fetchall()
        if checkAdmin[0][0] == "F":
            windowUpdatePer.destroy()
            windowSetting.destroy()
            Logout()
            conn.close()
        else:
            conn.close()
            windowUpdatePer.destroy()
            PermissionMenu()


def DeleteUser():
    if EntNamePer.get().lower() == "":
        WarningMSG("Please Enter Username", bg)
    else:
        conn = sql3.connect("stockhome.sqlite")
        cursor = conn.cursor()
        cursor.execute('select * from userdata where user="%s"' % EntNamePer.get().lower())
        check = cursor.fetchall()
        if check == []:
            WarningMSG("User not found!!", bg)
        else:
            Confirm = messagebox.askyesno("Confirm", "Are you sure to Delete this User?")
            if Confirm == True:
                cursor.execute('delete from userdata where user="%s"' % EntNamePer.get().lower())
                CompleteMSG("Delete User", bg)
                conn.commit()
                conn.close()
                PermissionMenu()


def BackToMenu(check):
    if check == "Show_Stock":
        windowshowstock.destroy()
    elif check == "Add_User":
        windowAdd.destroy()
        for i in AddUser_var:
            i.set("")
    elif check == "Add_Product":
        windowNewProduct.destroy()
    elif check == "Withdraw_Product":
        windowWithdraw.destroy()
        for i in Withdraw_var:
            i.set("")
    elif check == "Setting":
        windowSetting.destroy()
    MainMenu()


def CancelClick(check):
    check.destroy()


# ROOT
root = Tk()
root.title("Welcome to Stock Home : LOGIN")
w = 750
h = 600
x = root.winfo_screenwidth() / 2 - (w / 2)
y = root.winfo_screenheight() / 2 - (h / 2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.iconphoto(True, PhotoImage(file='Imgs/stock.png'))
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
for r in range(7):
    root.rowconfigure(r, weight=1)

# TTK
style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', font=('DB Adman X', 20))
style.configure('16.TLabel', font=('DB Adman X', 16))
style.configure('30.TLabel', font=('DB Adman X', 30))
style.configure('Title.TLabel', font=('DB Adman X', 80))
style.configure('TEntry', font=('DB Adman X', 20), padding=5)
style.configure('TCombobox', font=('DB Adman X', 20), padding=5)
style.configure('Small.TButton', font=('DB Adman X', 20), width=10, padding=5)
style.configure('Main.TButton', font=('DB Adman X', 20), width=15, padding=5)
style.configure('Exit.TButton', background='#EF3940')
style.configure('Back.TButton', background="#ffffff")
style.configure('Setting.TButton', background="#757575")
style.map("Small.TButton", foreground=[('pressed', '#ffffff'), ('active', '#ffffff')],
          font=[('pressed', ('DB Adman X', 20)), ('active', ('DB Adman X', 20))],
          background=[('pressed', '#3DD862'), ('active', '#49FC73')])
style.map("Main.TButton", foreground=[('pressed', '#F8369D'), ('active', '#F8369D')],
          font=[('pressed', ('DB Adman X', 20)), ('active', ('DB Adman X', 20))],
          background=[('pressed', '#BCA66F'), ('active', '#FFE29B')])
style.map("Exit.TButton", background=[('pressed', '#B5282E'), ('active', '#EF3940')])
style.map("Back.TButton", background=[('pressed', '#868687'), ('active', '#ffffff')])
style.map("TButton", foreground=[('pressed', '#40E5FF'), ('active', '#40E5FF')],
          background=[('pressed', '#BF6699'), ('active', '#FF8BCD')])

# Data
exitPhoto = PhotoImage(file="Imgs/exit.png")
logoutPhoto = PhotoImage(file="Imgs/logout.png")
backPhoto = PhotoImage(file="Imgs/back.png")
settingPhoto = PhotoImage(file="Imgs/setting.png")
colorListUser = ['#FFADD9', '#FFADD2', '#FFADCB', '#FFADC4', '#FFADBD', '#FFADB6', '#FFADB0']
colorListAdmin = ['#ADB0FF', '#B1ADFF', '#B8ADFF', '#BFADFF', '#C6ADFF', '#CDADFF', '#D4ADFF']
MainMenu_btnList = ['Add Stock', 'Withdraw', 'Show Stock', 'Add new User']
AddUser_textlist = ["Username : ", "Password : ", "Confirm Password : ", "Full name : ", "Permission : "]
AddStock_textlist = ["Product Name : ", "Amount : ", "Price : ", "Category : "]
Withdraw_textlist = ["Category : ", "Product Name : ", "Amount : ", "Price : ", "Withdraw : "]
AddUser_var = [StringVar() for num in range(len(AddUser_textlist))]
Withdraw_var = [StringVar() for i in range(5)]
showtitle = ["ID", "Name", "Amount", "Price"]
EntSearch = StringVar()
PermissionCBB = StringVar()

# Login
EntUsername_Login = StringVar()
EntPassword_Login = StringVar()
pos = 0
for index, item in enumerate(colorListUser):
    Frame(root, bg=item).place(x=0, y=pos, width=root.winfo_screenwidth(), height=86)
    pos += 86

TextTitle = ttk.Label(root, text="Stock Home", style='Title.TLabel', background='#FFADD9')
UsernameLogin = ttk.Entry(root, textvariable=EntUsername_Login, width=30)
PasswordLogin = ttk.Entry(root, textvariable=EntPassword_Login, show="*", width=30)
btnLogin = ttk.Button(root, text="Login", style='Small.TButton', command=LoginClick)

TextTitle.grid(row=0, columnspan=2)
ttk.Label(root, text='Username : ', background='#FFADCB').grid(row=1, column=0, sticky='e')
UsernameLogin.grid(row=1, column=1, sticky='w', padx=20)
ttk.Label(root, text='Password : ', background='#FFADC4').grid(row=2, column=0, sticky='e')
PasswordLogin.grid(row=2, column=1, sticky='w', padx=20)
btnLogin.grid(row=3, columnspan=2)
ttk.Button(root, image=exitPhoto, style='Exit.TButton', command=exit).grid(row=7, column=0, sticky='w')
root.mainloop()
