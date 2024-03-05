from tkinter import *

from tkinter import messagebox
import datetime
from connect_db import connect
import pymysql


def issue_books(home, issue_book):
    issue_book.configure(background="black")
    Label(
        issue_book, text="Issue Book", bg="black", fg="white", font=("Courier", 35)
    ).pack(pady=15)
    Label(
        issue_book, text="Book Id", bg="black", fg="white", font=("Courier", 25)
    ).pack(pady=5)
    book_id = Text(issue_book, height=1, width=30, font=("Courier", 25))
    book_id.pack(pady=5)
    Label(
        issue_book, text="Student Id", bg="black", fg="white", font=("Courier", 25)
    ).pack(pady=5)
    Student_id = Text(issue_book, height=1, width=30, font=("Courier", 25))
    Student_id.pack(pady=5)
    issue_book.pack(expand=1, fill=X)
    Button(
        issue_book,
        text="Submit",
        command=lambda: issue(book_id, Student_id),
        bg="black",
        fg="white",
        font=("Courier", 25),
    ).pack(pady=12)
    home.pack_forget()


def issue(book_id, Student_id):
    book_id = book_id.get(1.0, "end-1c")
    Student_id = Student_id.get(1.0, "end-1c")
    try:
        query_avail = "select avail_count from Books where Book_id=" + book_id
        availability = connect(query_avail)
        if len(availability) == 0:
            messagebox.showinfo("Error", "Invalid Book ID")
            return None
        elif availability[0][0] == 0:
            messagebox.showinfo("Sorry", "Book is not available")
            return None
    except (pymysql.Error, pymysql.Warning) as e:
        print(e)
    today = datetime.date.today()

    issue_date = str(today)
    r_d = today + datetime.timedelta(days=30)
    return_date = str(r_d)

    try:
        query_max = "select max(issue_id) from Issue"
        max_issue_id = connect(query_max)

        if max_issue_id[0][0] == None:
            issue_id = 1
        else:
            issue_id = max_issue_id[0][0] + 1
        query_issue = (
            "insert into Issue values("
            + str(issue_id)
            + ","
            + Student_id
            + ","
            + book_id
            + ",'"
            + issue_date
            + "','"
            + return_date
            + "',NULL)"
        )
        connect(query_issue)
        messagebox.showinfo("Success", "Issue ID = " + str(issue_id))
    except (pymysql.Error, pymysql.Warning) as e:
        messagebox.showinfo("Error", "Invalid Student_id")
    finally:
        return None
