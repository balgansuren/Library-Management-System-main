from tkinter import *
from tkinter import messagebox
import datetime
from connect_db import connect
import pymysql


def return_books(home, return_book):
    return_book.configure(background="black")
    Label(
        return_book, text="Return Book", bg="black", fg="white", font=("Courier", 35)
    ).pack(pady=15)
    Label(
        return_book, text="Issue Id", bg="black", fg="white", font=("Courier", 25)
    ).pack(pady=5)
    issue_id = Text(return_book, height=1, width=30, font=("Courier", 25))
    issue_id.pack(pady=5)
    return_book.pack(expand=1, fill=X)
    Button(
        return_book,
        text="Submit",
        command=lambda: returnbook(issue_id),
        bg="black",
        fg="white",
        font=("Courier", 25),
    ).pack(pady=12)
    home.pack_forget()


def returnbook(issue_id):
    issue_id = issue_id.get(1.0, "end-1c")
    today = datetime.date.today()
    returned_date = str(today)
    query = f'update Issue set returned_date="{str(returned_date)}" where issue_id={issue_id}'
    print(query)
    try:
        connect(query)
        messagebox.showinfo("Success", "Book returned")
    except (pymysql.Error, pymysql.Warning) as e:
        messagebox.showinfo("Error", str(e))
