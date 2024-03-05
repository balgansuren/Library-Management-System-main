from tkinter import *
import pymysql
from tkinter import messagebox
from connect_db import connect


def add_books(home, add_book):
    add_book.configure(background="black")
    Label(add_book, text="Add Book", bg="black", fg="white", font=("Courier", 35)).pack(
        pady=15
    )
    Label(add_book, text="Book Id", bg="black", fg="white", font=("Courier", 25)).pack(
        pady=5
    )
    id = Text(add_book, height=1, width=30, font=("Courier", 25))
    id.pack(pady=5)
    Label(add_book, text="Name", bg="black", fg="white", font=("Courier", 25)).pack(
        pady=5
    )
    name = Text(add_book, height=1, width=30, font=("Courier", 25))
    name.pack(pady=5)
    Label(add_book, text="Author", bg="black", fg="white", font=("Courier", 25)).pack(
        pady=5
    )
    author = Text(add_book, height=1, width=30, font=("Courier", 25))
    author.pack(pady=5)
    Label(add_book, text="Category", bg="black", fg="white", font=("Courier", 25)).pack(
        pady=5
    )
    category = Text(add_book, height=1, width=30, font=("Courier", 25))
    category.pack(pady=5)
    Label(add_book, text="Count", bg="black", fg="white", font=("Courier", 25)).pack(
        pady=5
    )
    count = Text(add_book, height=1, width=30, font=("Courier", 25))
    count.pack()
    Button(
        add_book,
        text="Submit",
        command=lambda: add_book_query(id, name, category, author, count),
        bg="black",
        fg="white",
        font=("Courier", 25),
    ).pack(pady=12)
    add_book.pack(expand=1, fill=X)
    home.pack_forget()


def add_book_query(id, name, category, author, count):
    book_id = id.get(1.0, "end-1c")
    name = name.get(1.0, "end-1c")
    category = category.get(1.0, "end-1c")
    author = author.get(1.0, "end-1c")
    count = count.get(1.0, "end-1c")
    print(book_id, name, category, author, count)
    insert = (
        "insert into Books values("
        + book_id
        + ",'"
        + name
        + "','"
        + author
        + "', '"
        + category
        + "',"
        + count
        + ","
        + count
        + ");"
    )

    try:
        connect(insert)
        messagebox.showinfo("Success", "Book added successfully")
    except (pymysql.Error, pymysql.Warning) as e:
        err = str(e)
        messagebox.showinfo("Error", "Can't add data into Database " + err)
