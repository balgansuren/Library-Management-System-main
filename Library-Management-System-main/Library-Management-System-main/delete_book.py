from tkinter import *
from connect_db import connect
import pymysql
from tkinter import messagebox


def delete_books(home, delete_book):
    delete_book.configure(background="black")
    Label(
        delete_book, text="Delete Book", bg="black", fg="white", font=("Courier", 35)
    ).pack(pady=15)
    Label(
        delete_book, text="Enter Book Id", bg="black", fg="white", font=("Courier", 25)
    ).pack(pady=5)
    id = Text(delete_book, height=1, width=30, font=("Courier", 25))
    id.pack(pady=5)
    delete_book.pack(expand=1, fill=X)
    Button(
        delete_book,
        text="Submit",
        command=lambda: delete(id),
        bg="black",
        fg="white",
        font=("Courier", 25),
    ).pack(pady=12)
    home.pack_forget()


def delete(id):
    Book_id = id.get(1.0, "end-1c")
    delete = f"delete from Books where book_id={Book_id}"
    try:
        connect(delete)
        messagebox.showinfo("Success", "Book Deleted Successfully")
    except (pymysql.Error, pymysql.Warning) as e:
        err = str(e)
        messagebox.showinfo("Error", "Can't delete book from  Database " + err)

    return None
