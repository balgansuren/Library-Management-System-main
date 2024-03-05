from tkinter import *

from black import out
from connect_db import connect
from tkinter import messagebox
import pymysql


def update_books(home, update_book):
    update_book.configure(background="black")
    Label(
        update_book, text="Update Book", bg="black", fg="white", font=("Courier", 35)
    ).pack(pady=15)
    Label(
        update_book, text="Enter Book Id", bg="black", fg="white", font=("Courier", 25)
    ).pack(pady=5)
    id = Text(update_book, height=1, width=30, font=("Courier", 25))
    id.pack(pady=5)
    update_book.pack(expand=1, fill=X)
    Button(
        update_book,
        text="Submit",
        command=lambda: queryby_id(id, update_book),
        bg="black",
        fg="white",
        font=("Courier", 25),
    ).pack(pady=12)
    home.pack_forget()


def detailed_update(update_book, output):
    Label(update_book, text="Name", bg="black", fg="white", font=("Courier", 25)).pack(
        pady=5
    )
    name = Text(update_book, height=1, width=30, font=("Courier", 25))
    name.pack(pady=5)
    Label(
        update_book, text="Author", bg="black", fg="white", font=("Courier", 25)
    ).pack(pady=5)
    author = Text(update_book, height=1, width=30, font=("Courier", 25))
    author.pack(pady=5)
    Label(
        update_book, text="Category", bg="black", fg="white", font=("Courier", 25)
    ).pack(pady=5)
    category = Text(update_book, height=1, width=30, font=("Courier", 25))
    category.pack(pady=5)
    Label(
        update_book, text="Total Count", bg="black", fg="white", font=("Courier", 25)
    ).pack(pady=5)
    t_count = Text(update_book, height=1, width=30, font=("Courier", 25))
    t_count.pack()
    display_details(name, author, category, t_count, output)
    Button(
        update_book,
        text="update",
        command=lambda: update_submit(name, author, category, t_count, output),
        bg="black",
        fg="white",
        font=("Courier", 25),
    ).pack(pady=12)


def queryby_id(id, update_book):
    book_id = id.get(1.0, "end-1c")
    query = "select * from Books where book_id=" + book_id
    try:
        result = connect(query)
        if len(result) > 0:
            output = fetch_detail(result)
            detailed_update(update_book, output)
        else:
            messagebox.showinfo("Error", "Enter valid book_id")
    except (pymysql.Error, pymysql.Warning) as e:
        err = str(e)
        messagebox.showinfo("Error", "Can't add data into Database " + err)


def display_details(name, author, category, t_count, output):
    name.insert(INSERT, output[1])
    author.insert(INSERT, output[2])
    category.insert(INSERT, output[3])
    t_count.insert(INSERT, output[4])


def fetch_detail(result):
    for row in result:
        id = row[0]
        name = row[1]
        author = row[2]
        cat_id = row[3]
        t_count = row[4]
        avail_count = row[5]
    return [id, name, author, cat_id, t_count, avail_count]


def update_submit(name, author, category, t_count, output):
    name = name.get(1.0, "end-1c")
    author = author.get(1.0, "end-1c")
    category = category.get(1.0, "end-1c")
    t_count = t_count.get(1.0, "end-1c")
    d = int(t_count) - output[4]
    avail_count = output[5]
    avail_count += d
    if d < 0:
        messagebox.showinfo("Error", "New count is less than available ")
    else:
        query = (
            "update Books set name='"
            + name
            + "',aut_name='"
            + author
            + "',cat_id="
            + category
            + ",t_count="
            + t_count
            + ",avail_count="
            + str(avail_count)
            + " where book_id="
            + str(output[0])
        )
        try:
            connect(query)
            messagebox.showinfo("Success", "Details updated successfully")

        except (pymysql.Error, pymysql.Warning) as e:
            err = str(e)
            messagebox.showinfo("Error", "Can't update the details of book " + err)
