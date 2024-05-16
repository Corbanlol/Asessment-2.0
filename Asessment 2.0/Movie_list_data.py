import pyodbc
import tkinter as tk


# Backend pyodbc starts here

def show_entries():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\2022000130\Downloads\Movie_list_data.accdb"')
    
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Moive_list_data')

    for row in cursor.fetchall():
        print (row)

        
def add_entries():
    ID = e0.get()
    Movie_name = e1.get()
    Release_date = e2.get()
    Genre = e3.get()
    Age_rating = e4.get() 
    Reviews = e5.get()
    
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\"C:\Users\2022000130\Downloads\Movie_list_data.accdb;')

    cursor = conn.cursor()

    cursor.execute('INSERT INTO Movie_list_data VALUES (?,?,?,?,?,?)', (ID, Movie_name, Release_date, Genre, Age_rating, Reviews,))
    connection.commit()

# Frontend tkinter starts here

master = tk.Tk()

# labels for textboxes
tk.Label(master, text="ID").grid(row=0)
tk.Label(master, text="Movie name").grid(row=1)
tk.Label(master, text="Release date").grid(row=2)
tk.Label(master, text="Genre").grid(row=3)
tk.Label(master, text="Age raiting").grid(row=4)
tk.Label(master, text="Reviews").grid(row=5)

# textboxes
e0=tk.Entry(master)
e2=tk.Entry(master)
e2=tk.Entry(master)
e3=tk.Entry(master)
e4=tk.Entry(master) 
e5=tk.Entry(master)


e0.grid(row=0, column=1)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1) 
e5.grid(row=5, column=1)

# button group

tk.Button(master, text='Show', command=show_entries).grid(row=7, column =0)
tk.Button(master, text='Submit', command=add_entries).grid(row=7, column =1)
tk.Button(master, text='Quit', command=add_entries).grid(row=7, column =2)

tk.mainloop()





