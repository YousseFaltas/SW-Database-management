from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from venv import create
import pyodbc

def connect_to_database ():
    try :
        conn = pyodbc.connect (f'Driver={{ODBC Driver 17 for SQL Server}};Server=YOUSSEF-LAPTOP\SQLEXPRESS;Database=Faith;Trusted_Connection=yes;')
        print("connected successfully")
        return conn
    except  pyodbc.Error as e:
        messagebox.showerror("Database Error", f"Error connecting to database: {e}")
        return None
    
def main():
    root = tk.Tk()
    root.title("database GUI")

    #create a main frame
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH , expand =1)
    
    #create a canvas
    canvas = Canvas(main_frame)
    canvas.pack(side= LEFT , fill = BOTH ,expand =1)
    
    #add a scrollbar to the canvas
    scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side = RIGHT , fill = Y)
    
    #configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>' , lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    #create another frame in the canvas
    second_frame = Frame(canvas)
    
    # add that new frame to a window in the canvas
    canvas.create_window((0,0), window=second_frame, anchor="nw")

    # Add content to the content frame
    for i in range(50):  # Example content
        tk.Button(second_frame, text=f"Item {i}").grid(row=i,column=0,padx=10,pady=10)


    # Run the Application
    root.mainloop()

if __name__ == "__main__":
    main()