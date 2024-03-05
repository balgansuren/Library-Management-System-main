from tkinter import *
from add_book import add_books
from update_book import update_books
from delete_book import delete_books
from issue_book import issue_books
from return_book import return_books
from search_book import search_book


def home():
    main = Tk()
    main.title("Library")
    main.geometry("600x500")
    main.configure(background="black")
    head = Label(
        main,
        text="Library Management System",
        bg="black",
        fg="white",
        font=("Courier", 25),
    )

    def goback():
        for widget in search_books.winfo_children():
            widget.destroy()
        for widget in add_book.winfo_children():
            widget.destroy()
        for widget in update_book.winfo_children():
            widget.destroy()
        for widget in delete_book.winfo_children():
            widget.destroy()
        for widget in issue_book.winfo_children():
            widget.destroy()
        for widget in return_book.winfo_children():
            widget.destroy()
        home.pack(expand=1, fill=X)
        add_book.pack_forget()
        update_book.pack_forget()
        delete_book.pack_forget()
        issue_book.pack_forget()
        return_book.pack_forget()
        search_books.pack_forget()

    Button(
        main, text="back", bg="black", fg="white", font=("Courier", 25), command=goback
    ).pack(pady=12, side=TOP, anchor=NW)
    head.pack(pady=20)
    home = Frame(main)
    search_books = Frame(main)
    add_book = Frame(main)
    update_book = Frame(main)
    delete_book = Frame(main)
    issue_book = Frame(main)
    return_book = Frame(main)

    def landing():
        home.configure(background="black")
        Button(
            home,
            text="search",
            command=lambda: search_book(home, search_books),
            bg="black",
            fg="white",
            font=("Courier", 25),
        ).pack(pady=18)
        Button(
            home,
            text="add book",
            command=lambda: add_books(home, add_book),
            bg="black",
            fg="white",
            font=("Courier", 25),
        ).pack(pady=18)
        Button(
            home,
            text="update book",
            command=lambda: update_books(home, update_book),
            bg="black",
            fg="white",
            font=("Courier", 25),
        ).pack(pady=18)
        Button(
            home,
            text="delete book",
            command=lambda: delete_books(home, delete_book),
            bg="black",
            fg="white",
            font=("Courier", 25),
        ).pack(pady=18)
        Button(
            home,
            text="issue book",
            command=lambda: issue_books(home, issue_book),
            bg="black",
            fg="white",
            font=("Courier", 25),
        ).pack(pady=18)
        Button(
            home,
            text="return book",
            command=lambda: return_books(home, return_book),
            bg="black",
            fg="white",
            font=("Courier", 25),
        ).pack(pady=18)
        home.pack(expand=1, fill=X)

    landing()
    main.mainloop()


home()
