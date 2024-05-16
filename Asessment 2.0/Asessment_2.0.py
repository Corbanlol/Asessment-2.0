from sys import exit 
import pyodbc
import tkinter as tk

 # this is just a comment

 # comment made Branch1 

# Backend pyodbc starts here

def show_entries():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Shantelle\Downloads\Movie_list.accdb;') 
    
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Moive_list5')

    for row in cursor.fetchall():
        print (row)
    
        

def add_entries():
    ID = e0.get()
    Movie_name = e1.get()
    Release_date = e2.get()
    Genre = e3.get()
    Age_rating = e4.get() 
    Review = e5.get()
  
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Shantelle\Downloads\Movie_list.accdb;')

    cursor = conn.cursor()


    cursor.execute('INSERT INTO Movie_list VALUES (?,?,?,?,?,?)', (ID, Movie_name, Release_date, Genre, Age_rating, Review,))
    conn.commit()



def quit_program():
    '''Exits the program, including the frontend and backend'''
    root.destroy() 
    exit()

root = tk.Tk()

# Frontend tkinter starts here


# labels for textboxes
tk.Label(root, text="ID").grid(row=0)
tk.Label(root, text="Movie name").grid(row=1)
tk.Label(root, text="Release date").grid(row=2)
tk.Label(root, text="Genre").grid(row=3)
tk.Label(root, text="Age raiting").grid(row=4)
tk.Label(root, text="Review").grid(row=5)

# textboxes
e0=tk.Entry(root)
e1=tk.Entry(root)
e2=tk.Entry(root)
e3=tk.Entry(root)
e4=tk.Entry(root) 
e5=tk.Entry(root)


e0.grid(row=0, column=1)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1) 
e5.grid(row=5, column=1)

# button group

tk.Button(root, text='Show', command=show_entries).grid(row=7, column =0)
tk.Button(root, text='Submit', command=add_entries).grid(row=7, column =1)
tk.Button(root, text='Quit', command=quit_program).grid(row=7, column =2)

tk.mainloop() 








