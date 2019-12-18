from tkinter import *
import sqlite3
from tkinter import messagebox

def viewall():
    text.config(state=NORMAL)
    text.delete(1.0,END)

    conn = sqlite3.connect('bookstore.sqlite3')
    cur = conn.cursor()
    cur.execute('select title,author,year,isbn from books')
    all = cur.fetchall()
    
    for books in all:
        store = '('
        for book in list(books):
            store = store + str(book)+' , '
        text.insert(END,store+')'+'\n')
    text.config(state=DISABLED)
    conn.close()

def search_entry():
    text.config(state=NORMAL)
    text.delete(1.0,END)

    conn = sqlite3.connect('bookstore.sqlite3')
    cur = conn.cursor()

    title_ = title_entry.get()
    author_ = author_entry.get()
    year_ = year_entry.get()
    isbn_ = isbn_entry.get()

    if len(title_) > 0 and len(year_) > 0 and len(author_) > 0 and len(isbn_) > 0:
        cur.execute('SELECT title,author,year,isbn from books WHERE title=? and author=? and year = ? and isbn = ?',(title_,author_,year_,isbn_,))
        all = cur.fetchall()

        if len(all) > 0:
            for books in all:
                store = '('
                for book in list(books):
                    store = store + str(book)+' , '
                text.insert(END,store+')'+'\n')
        else:
            messagebox.showinfo('NOT FOUND','NO BOOKS EXIST WITH THOSE DETAILS')

    elif len(title_) > 0 and len(year_) > 0 and len(author_) > 0:
        cur.execute('SELECT title,author,year,isbn from books WHERE title=? and author=? and year = ?',(title_,author_,year_,))
        all = cur.fetchall()

        if len(all) > 0:
            for books in all:
                store = '('
                for book in list(books):
                    store = store + str(book)+' , '
                text.insert(END,store+')'+'\n')
        else:
            messagebox.showinfo('NOT FOUND','NO BOOKS EXIST WITH THOSE DETAILS')

    elif len(title_) > 0 and len(author_) > 0:
        cur.execute('SELECT title,author,year,isbn from books WHERE title=? and author=?',(title_,author_,))
        all = cur.fetchall()

        if len(all) > 0:
            for books in all:
                store = '('
                for book in list(books):
                    store = store + str(book)+' , '
                text.insert(END,store+')'+'\n')
        else:
            messagebox.showinfo('NOT FOUND','NO BOOKS EXIST WITH THOSE DETAILS')
    
    elif len(title_) > 0 and len(year_) > 0:
        cur.execute('SELECT title,author,year,isbn from books WHERE title=? and year = ?',(title_,year_,))
        all = cur.fetchall()

        if len(all) > 0:
            for books in all:
                store = '('
                for book in list(books):
                    store = store + str(book)+' , '
                text.insert(END,store+')'+'\n')
        else:
            messagebox.showinfo('NOT FOUND','NO BOOKS EXIST WITH THOSE DETAILS')
    
    elif len(year_) > 0 and len(author_) > 0:
        cur.execute('SELECT title,author,year,isbn from books WHERE year=? and author=?',(year_,author_,))
        all = cur.fetchall()

        if len(all) > 0:
            for books in all:
                store = '('
                for book in list(books):
                    store = store + str(book)+' , '
                text.insert(END,store+')'+'\n')
        else:
            messagebox.showinfo('NOT FOUND','NO BOOKS EXIST WITH THOSE DETAILS')    
            
    elif len(title_) > 0:
        cur.execute('SELECT title,author,year,isbn from books WHERE title=?',(title_,))
        all = cur.fetchall()

        if len(all) > 0:
            for books in all:
                store = '('
                for book in list(books):
                    store = store + str(book)+' , '
                text.insert(END,store+')'+'\n')
        else:
            messagebox.showinfo('NOT FOUND','NO BOOKS EXIST WITH THOSE DETAILS')

    elif len(author_) > 0:
        cur.execute('select title,author,year,isbn from books WHERE author=?',(author_,))
        all = cur.fetchall()

        if len(all) > 0:
            for books in all:
                store = '('
                for book in list(books):
                    store = store + str(book)+' , '
                text.insert(END,store+')'+'\n')
        else:
            messagebox.showinfo('NOT FOUND','NO BOOKS EXIST WITH THOSE DETAILS')


    elif len(year_) > 0:
        cur.execute('select title,author,year,isbn from books WHERE year=?',(year_,))
        all = cur.fetchall()

        if len(all) > 0:
            for books in all:
                store = '('
                for book in list(books):
                    store = store + str(book)+' , '
                text.insert(END,store+')'+'\n')
        else:
            messagebox.showinfo('NOT FOUND','NO BOOKS EXIST WITH THOSE DETAILS')
        
    elif len(isbn_) > 0:
        cur.execute('select title,author,year,isbn from books WHERE isbn=?',(isbn_,))
        all = cur.fetchall()

        if len(all) > 0:
            for books in all:
                store = '('
                for book in list(books):
                    store = store + str(book)+' , '
                text.insert(END,store+')'+'\n')
        else:
            messagebox.showinfo('NOT FOUND','NO BOOKS EXIST WITH THOSE DETAILS')

    conn.close()
    text.config(state=DISABLED)

def add_entry():
    t = messagebox.askyesno('Question','Do you want to Add the Book')
    if t:
        conn = sqlite3.connect('bookstore.sqlite3')
        cur = conn.cursor()
        title_ = title_entry.get()
        author_ = author_entry.get()
        year_ = year_entry.get()
        isbn_ = isbn_entry.get()

        cur.execute('insert into books(title,author,year,isbn) values(?,?,?,?)',(title_,author_,year_,isbn_))
        conn.commit()
        conn.close()
    else:
        return None

def delete_selected():
    title_ = title_entry.get()
    author_ = author_entry.get()
    year_ = year_entry.get()
    isbn_ = isbn_entry.get()

    conn = sqlite3.connect('bookstore.sqlite3')
    cur = conn.cursor()

    cur.execute('select * from books')
    all = cur.fetchall()
    
    if ((title_) or (author_) or (year_) or (isbn_) in all) and len(all) > 0:
        if (len(title_) > 0) and (len(author_) > 0) and (len(year_) > 0) and (len(isbn_) > 0):
            t = messagebox.askyesno('Question','Do you want to delete the selected Book')
            if t:
                cur.execute('DELETE from books WHERE title = ? and author=? and year=? and isbn=?',(title_,author_,year_,isbn_,))
                messagebox.showinfo('SUCCESS','DELETE SUCCESSFUL')

        elif (len(title_) > 0) and (len(author_) > 0):
            t = messagebox.askyesno('Question','Do you want to delete the selected Book')
            if t:
                cur.execute('DELETE from books WHERE title = ? and author=?',(title_,author_,))
                messagebox.showinfo('SUCCESS','DELETE SUCCESSFUL')

        elif (len(title_) > 0) and (len(year_) > 0):
            t = messagebox.askyesno('Question','Do you want to delete the selected Book')
            if t:
                cur.execute('DELETE from books WHERE title = ? and year=?',(title_,year_,))
                messagebox.showinfo('SUCCESS','DELETE SUCCESSFUL')

        elif (len(author_) > 0) and (len(year_) > 0):
            t = messagebox.askyesno('Question','Do you want to delete the selected Book')
            if t:
                cur.execute('DELETE from books WHERE year = ? and author=?',(year_,author_,))
                messagebox.showinfo('SUCCESS','DELETE SUCCESSFUL')

        elif len(title_) > 0:
            t = messagebox.askyesno('Question','Do you want to delete the selected Book')
            if t:
                cur.execute('DELETE from books WHERE title = ?',(title_,))
                messagebox.showinfo('SUCCESS','DELETE SUCCESSFUL')

        elif len(author_) > 0:
            t = messagebox.askyesno('Question','Do you want to delete the selected Book')
            if t:
                cur.execute('DELETE from books WHERE author = ?',(author_,))
                messagebox.showinfo('SUCCESS','DELETE SUCCESSFUL')
            
        elif len(year_) > 0:
            t = messagebox.askyesno('Question','Do you want to delete the selected Book')
            if t:
                cur.execute('DELETE from books WHERE year = ?',(year_,))
                messagebox.showinfo('SUCCESS','DELETE SUCCESSFUL')

        elif len(isbn_) > 0:
            t = messagebox.askyesno('Question','Do you want to delete the selected Book')
            if t:            
                cur.execute('DELETE from books WHERE isbn = ?',(isbn_,))
                messagebox.showinfo('SUCCESS','DELETE SUCCESSFUL')
    else:
        messagebox.showerror('ERROR',"BOOK WITH THAT DETAIL DOESN'T EXIST")

    conn.commit()
    conn.close()

def view_select():
    var = text.get(1.0,'2.0')
    var = var.split(',')
    if len(var) > 1:
        var[0] = var[0].replace('(','')
        title_var.set(var[0].strip())
        author_var.set(var[1].strip())
        year_var.set(var[2].strip())
        isbn_var.set(var[3].strip())

def update_selected():
    conn = sqlite3.connect('bookstore.sqlite3')
    cur = conn.cursor()

    var = text.get(1.0,'2.0')
    var = var.split(',')

    if len(var) > 1:
        title_ = title_entry.get()
        author_ = author_entry.get()
        year_ = year_entry.get()
        isbn_ = isbn_entry.get()

        cur.execute('update books set title=?,author=?,year=?,isbn=? where title=? or author=? or year=? or isbn=? ',(title_,author_,year_,isbn_,var[0],var[1],var[2],var[3],))
        messagebox.showinfo('SUCCESS','Book Updated Successfully')
    conn.commit()
    conn.close()
    

app = Tk()
app.geometry('500x300')
app.resizable(width=FALSE,height=FALSE)
app.title('Bookstore')

title_var = StringVar()
author_var = StringVar()
year_var = StringVar()
isbn_var = StringVar()

title_label = Label(app,text='Title',font=('arial black',10))
title_label.place(relx=0.05,rely=0.02)

title_entry = Entry(app,textvariable=title_var,font=('arial',10))
title_entry.place(relx=0.15,rely=0.03,relwidth=0.3)

author_label = Label(app,text='Author',font=('arial black',10))
author_label.place(relx=0.5,rely=0.02)

author_entry = Entry(app,textvariable=author_var,font=('arial',10))
author_entry.place(relx=0.62,rely=0.03,relwidth=0.3)

year_label = Label(app,text='Year',font=('arial black',10))
year_label.place(relx=0.05,rely=0.09)

year_entry = Entry(app,textvariable=year_var,font=('arial',10))
year_entry.place(relx=0.15,rely=0.1,relwidth=0.3)

isbn_label = Label(app,text='ISBN',font=('arial black',10))
isbn_label.place(relx=0.5,rely=0.09)

isbn_entry = Entry(app,textvariable=isbn_var,font=('arial',10))
isbn_entry.place(relx=0.62,rely=0.1,relwidth=0.3)

text_frame = Frame(app,bg='black')
text_frame.place(relx=0.004,rely=0.29,relwidth=0.56,relheight=0.62)

text = Text(app,bd=1,relief=FLAT,bg='white',font=('Times New Roman',11))
text.place(relx=0.01,rely=0.3,relwidth=0.55,relheight=0.6)

scroll = Scrollbar(app)
scroll.place(relx=0.56,rely=0.3,relheight=0.6)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

frame = Frame(app,bg='white')
frame.place(relx=0.68,rely=0.22,relwidth=0.3,relheight=0.65)

for i in range(50):
    Grid.columnconfigure(frame,i,weight=1)
    Grid.rowconfigure(frame,i,weight=1)

view = Button(frame,text='View all',font=('arial black',10),activebackground='lightgray',command = lambda : viewall())
view.grid(row=0,column=0,columnspan=6,ipadx=60,ipady=2)

search = Button(frame,text='Search entry',font=('arial black',10),activebackground='lightgray',command=lambda : search_entry())
search.grid(row=1,column=0,columnspan=6,ipadx=60,ipady=2)

add = Button(frame,text='Add entry',font=('arial black',10),activebackground='lightgray',command=lambda : add_entry())
add.grid(row=2,column=0,columnspan=6,ipadx=60,ipady=2)

view_selected = Button(frame,text='View searched',font=('arial black',10),activebackground='lightgray',command=lambda :view_select())
view_selected.grid(row=3,column=0,columnspan=6,ipadx=60,ipady=2)

update = Button(frame,text='Update selected',font=('arial black',10),activebackground='lightgray',command=lambda : update_selected())
update.grid(row=4,column=0,columnspan=6,ipadx=60,ipady=2)

delete = Button(frame,text='Delete selected',font=('arial black',10),activebackground='lightgray',command=lambda : delete_selected())
delete.grid(row=5,column=0,columnspan=6,ipadx=60,ipady=2)

close = Button(frame,text='close',font=('arial black',10),activebackground='lightgray',command=app.quit)
close.grid(row=6,column=0,columnspan=6,ipadx=60,ipady=2)

app.mainloop()