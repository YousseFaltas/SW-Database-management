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

# Insert operation for customer table
def insert_customer():
    ID = entry_cust_id.get()
    name = entry_cust_name.get()
    email = entry_cust_email.get()
    phone = entry_cust_phone.get()
    address = entry_cust_address.get()
    nationality = entry_cust_nationality.get()
    bank_acc = entry_bank_acc.get()
    credit_worthiness = entry_credit_worthiness.get()
    if name and phone and email and nationality:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO Customer (Cust_id , Cust_Name, Cust_email, Cust_phone, cust_address,Nationality , bank_acc , credit_worthiness)
                    VALUES (?, ?, ?, ?)""", (ID,name, email , phone,address , nationality , bank_acc , credit_worthiness ))
                conn.commit()
                messagebox.showinfo("Success", "Customer inserted successfully!")
                #fetch_customer_data()
            except pyodbc.Error as e:
                messagebox.showerror("Error", f"Error inserting customer: {e}")
            finally:
                conn.close()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields!")

root = tk.Tk()
root.title("database GUI")

#create a main frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH , expand =1)
    
#create a canvas
main_canvas = Canvas(main_frame)
main_canvas.pack(side= LEFT , fill = BOTH ,expand =1)
    
#add a scrollbar to the canvas
main_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=main_canvas.yview)
main_scrollbar.pack(side = RIGHT , fill = Y)
    
#configure the canvas
main_canvas.configure(yscrollcommand=main_scrollbar.set)
main_canvas.bind('<Configure>' , lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))
    
#create another frame in the canvas
second_frame = Frame(main_canvas)
    
# add that new frame to a window in the canvas
main_canvas.create_window((0,0), window=second_frame, anchor="nw")

# Adding the insert section for the customer table 
second_frame.pack(pady=10)

tk.Label(second_frame, text="Customer ID:").grid(row=0, column=0, padx=5, pady=5)
entry_cust_id = tk.Entry(second_frame)
entry_cust_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(second_frame, text="Customer name:").grid(row=0, column=2, padx=5, pady=5)
entry_cust_name = tk.Entry(second_frame)
entry_cust_name.grid(row=0, column=3, padx=5, pady=5)

tk.Label(second_frame, text="Customer Email:").grid(row=0, column=4, padx=5, pady=5)
entry_cust_email = tk.Entry(second_frame)
entry_cust_email.grid(row=0, column=5, padx=5, pady=5)

tk.Label(second_frame, text="Customer phone:").grid(row=0, column=6, padx=5, pady=5)
entry_cust_phone = tk.Entry(second_frame)
entry_cust_phone.grid(row=0, column=7, padx=5, pady=5)

tk.Label(second_frame, text="Customer address:").grid(row=1, column=0, padx=5, pady=5)
entry_cust_address = tk.Entry(second_frame)
entry_cust_address.grid(row=1, column=1, padx=5, pady=5)

tk.Label(second_frame, text="Nationality:").grid(row=1, column=2, padx=5, pady=5)
entry_cust_nationality = tk.Entry(second_frame)
entry_cust_nationality.grid(row=1, column=3, padx=5, pady=5)

tk.Label(second_frame, text="Bank account:").grid(row=1, column=4, padx=5, pady=5)
entry_bank_acc = tk.Entry(second_frame)
entry_bank_acc.grid(row=1, column=5, padx=5, pady=5)

tk.Label(second_frame, text="Credit worthiness:").grid(row=1, column=6, padx=5, pady=5)
entry_credit_worthiness = tk.Entry(second_frame)
entry_credit_worthiness.grid(row=1, column=7, padx=5, pady=5)

#tk.Button(second_frame, text="Add Customer", command=insert_customer).grid(row=1, column=4, padx=10, pady=10)

# Run the Application
root.mainloop()
