from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
from connect_db import connect


def search_book(home, search_books):
    search_books.configure(background="black")
    text = Text(search_books, height=1, width=30, font=("Courier", 25))
    text.pack(pady=15)
    Button(
        search_books,
        text="search",
        command=lambda: book_query(text, search_books),
        bg="black",
        fg="white",
        font=("Courier", 25),
    ).pack(pady=18)
    search_books.pack(expand=1, fill=X)
    home.pack_forget()
    return None


def book_query(text, search_books):
    search_text = text.get(1.0, "end-1c")
    query = (
        f"select book_id,name,aut_name,cat_name,dept_name,t_count,avail_count from Books natural join (select * from Category natural join Dept) as cat_dept where (lower(name) like lower('%"
        + search_text
        + "%'))or(lower(aut_name) like lower('%"
        + search_text
        + "%')) or (lower(cat_name) like lower('%"
        + search_text
        + "%')) or (lower(dept_name) like lower('%"
        + search_text
        + "%'))"
    )

    try:
        q = connect(query)
        result_refactor(q, search_books)
    except (pymysql.Error, pymysql.Warning) as e:
        print(e)
    return None


def result_refactor(q, search_books):
    for i, widget in enumerate(search_books.winfo_children()):
        if i == 2:
            widget.destroy()
    table = ttk.Treeview(search_books)
    search_result = []

    for row in q:
        result = {}
        result["id"] = row[0]
        result["name"] = row[1]
        result["author"] = row[2]
        result["category"] = row[3]
        result["department"] = row[4]
        result["t_count"] = row[5]
        result["avail_count"] = row[6]
        search_result.append(result)

    show_result(search_books, search_result, table)


def show_result(search_books, search_result, table):
    if len(search_result) == 0:
        messagebox.showinfo("oops", "no result found")

    table["columns"] = (
        "book_id",
        "book name",
        "author",
        "category",
        "department",
        "total count",
        "available count",
    )
    table.column("#0", width=0, stretch=NO)
    table.column("book_id", anchor=CENTER, width=200)
    table.column("book name", anchor=CENTER, width=300)
    table.column("author", anchor=CENTER, width=200)
    table.column("category", anchor=CENTER, width=200)
    table.column("department", anchor=CENTER, width=200)
    table.column("total count", anchor=CENTER, width=200)
    table.column("available count", anchor=CENTER, width=200)

    table.heading("#0", text="", anchor=CENTER)
    table.heading("book_id", text="book_id", anchor=CENTER)
    table.heading("book name", text="book name", anchor=CENTER)
    table.heading("author", text="author", anchor=CENTER)
    table.heading("category", text="category", anchor=CENTER)
    table.heading("department", text="department", anchor=CENTER)
    table.heading("total count", text="total count", anchor=CENTER)
    table.heading("available count", text="available count", anchor=CENTER)
    i = 0
    for each in search_result:
        table.insert(
            parent="",
            index="end",
            iid=i,
            text="",
            values=(
                each["id"],
                each["name"],
                each["author"],
                each["category"],
                each["department"],
                each["t_count"],
                each["avail_count"],
            ),
        )
        i += 1

    table.pack()

    return None


# for widget in search_books.winfo_children():
#             widget.destroy()
#     Label(search_books,text="id",bg='black', fg='white', font=('Courier',25)).pack(pady=5)
#     Label(search_books,text=id,bg='black', fg='white', font=('Courier',25)).pack(pady=5)
#     Label(search_books,text="name",bg='black', fg='white', font=('Courier',25)).pack(pady=5)
#     Label(search_books,text=name,bg='black', fg='white', font=('Courier',25)).pack(pady=5)
#     Label(search_books,text="author",bg='black', fg='white', font=('Courier',25)).pack(pady=5)
#     Label(search_books,text=author,bg='black', fg='white', font=('Courier',25)).pack(pady=5)
#     Label(search_books,text="category",bg='black', fg='white', font=('Courier',25)).pack(pady=5)
#     Label(search_books,text=category,bg='black', fg='white', font=('Courier',25)).pack(pady=5)
#     Label(search_books,text="department",bg='black', fg='white', font=('Courier',25)).pack(pady=5)
#     Label(search_books,text=dept,bg='black', fg='white', font=('Courier',25)).pack(pady=5)
#     Label(search_books,text="total count",bg='black', fg='white', font=('Courier',25)).pack(pady=5)
#     Label(search_books,text=t_count,bg='black', fg='white', font=('Courier',25)).pack(pady=5)
#     Label(search_books,text="available count",bg='black', fg='white', font=('Courier',25)).pack(pady=5)
#     Label(search_books,text=avail_count,bg='black', fg='white', font=('Courier',25)).pack(pady=5)
