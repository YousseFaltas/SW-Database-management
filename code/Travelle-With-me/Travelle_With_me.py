from ast import Attribute
import email
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
    date_birth = entry_date_birth.get()
    credit_worthiness = entry_credit_worthiness.get()
    if name and phone and email and nationality:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO Customer (Cust_id , Cust_Name, Cust_email, Cust_phone, cust_address,Nationality , bank_acc, date_birth , credit_worthiness)
                    VALUES (?, ?, ?, ?, ? , ? , ? , CONVERT(DATE, ?, 105), ? )""", (ID,name, email , phone,address , nationality , bank_acc, date_birth , credit_worthiness ))
                conn.commit()
                messagebox.showinfo("Success", "Customer inserted successfully!")
                #fetch_customer_data()
            except pyodbc.Error as e:
                messagebox.showerror("Error", f"Error inserting customer: {e}")
            finally:
                conn.close()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields!")


def insert_hotel():
    ID = entry_hotel_id.get()
    name = entry_hotel_name.get()
    location = entry_hotel_loc.get()
    email=entry_hotel_email.get()
    phone=entry_hotel_phone.get()
    policy = entry_hotel_policy.get()
    website=entry_hotel_website.get()
    
    if name and location and policy:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO Hotel (H_id , H_Name, H_Loc, H_Policy, H_email , H_phone , H_website)
                    VALUES (?, ?, ?, ?, ?, ?, ?)""", (ID,name, location, policy,email,phone,website))
                conn.commit()
                messagebox.showinfo("Success", "Hotel inserted successfully!")
                #fetch_hotel_data()
            except pyodbc.Error as e:
                messagebox.showerror("Error", f"Error inserting hotel: {e}")
            finally:
                conn.close()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields!")
        
def delete_room():
    Attribute = entry_att_room.get()
    value = entry_value_room.get()
    if Attribute and value:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM Room WHERE ? = ?",(Attribute , value))
                conn.commit()
                messagebox.showinfo("Success", "statement excuted successfully!")
            except pyodbc.Error as e:
                messagebox.showerror("Error", f"Error deleting Room: {e}")
            finally:
                conn.close()
    else:
        messagebox.showwarning("Input Error", "Please enter a valid condition")

def delete_ticket():
    Attribute = entry_att_room.get()
    value = entry_value_room.get()
    if Attribute and value:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM Room WHERE ? = ?",(Attribute , value))
                conn.commit()
                messagebox.showinfo("Success", "statement excuted successfully!")
            except pyodbc.Error as e:
                messagebox.showerror("Error", f"Error deleting Room: {e}")
            finally:
                conn.close()
    else:
        messagebox.showwarning("Input Error", "Please enter a valid condition")

# Select operations
def fetch_table_data():
    table_name = entry_table_name.get()
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = ?",(table_name))
            tabel_columns=cursor.fetchall()
            
            tree_room_booked = ttk.Treeview(second_frame, columns=tabel_columns, show="headings")
            tree_room_booked.grid(row=starting_row_tree+1, column=1, columnspan=8, padx=10, pady=10, sticky="nsew")
            tree_room_booked.delete(*tree_room_booked.get_children())  # Clear existing rows
            
            for col in tabel_columns:
                tree_room_booked.heading(col, text=col)
            
            for row in rows:
                row_values = []
                for value in row:
                    row_values.append(value)
                tree_room_booked.insert("", tk.END, values=row_values)
            
        except pyodbc.Error as e:
            messagebox.showerror("Error", f"Error fetching customer data: {e}")
        finally:
            conn.close()
    else:
        messagebox.showwarning("Input Error", "Please enter a table")
            
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

tk.Label(second_frame,text="Add new customer section").grid(row=0 ,column=4 , padx=10 , pady=10)
add_cust_base_row =1
tk.Label(second_frame, text="Customer ID:").grid(row=add_cust_base_row, column=0, padx=5, pady=5)
entry_cust_id = tk.Entry(second_frame)
entry_cust_id.grid(row=add_cust_base_row, column=1, padx=5, pady=5)

tk.Label(second_frame, text="Customer name:").grid(row=add_cust_base_row, column=2, padx=5, pady=5)
entry_cust_name = tk.Entry(second_frame)
entry_cust_name.grid(row=add_cust_base_row, column=3, padx=5, pady=5)

tk.Label(second_frame, text="Customer Email:").grid(row=add_cust_base_row, column=4, padx=5, pady=5)
entry_cust_email = tk.Entry(second_frame)
entry_cust_email.grid(row=add_cust_base_row, column=5, padx=5, pady=5)

tk.Label(second_frame, text="Customer phone:").grid(row=add_cust_base_row, column=6, padx=5, pady=5)
entry_cust_phone = tk.Entry(second_frame)
entry_cust_phone.grid(row=add_cust_base_row, column=7, padx=5, pady=5)

tk.Label(second_frame, text="Customer address:").grid(row=add_cust_base_row+1, column=0, padx=5, pady=5)
entry_cust_address = tk.Entry(second_frame)
entry_cust_address.grid(row=add_cust_base_row+1, column=1, padx=5, pady=5)

tk.Label(second_frame, text="Nationality:").grid(row=add_cust_base_row+1, column=2, padx=5, pady=5)
entry_cust_nationality = tk.Entry(second_frame)
entry_cust_nationality.grid(row=add_cust_base_row+1, column=3, padx=5, pady=5)

tk.Label(second_frame, text="Bank account:").grid(row=add_cust_base_row+1, column=4, padx=5, pady=5)
entry_bank_acc = tk.Entry(second_frame)
entry_bank_acc.grid(row=add_cust_base_row+1, column=5, padx=5, pady=5)

tk.Label(second_frame, text="Date of birth:").grid(row=add_cust_base_row+1, column=6, padx=5, pady=5)
entry_date_birth = tk.Entry(second_frame)
entry_date_birth.grid(row=add_cust_base_row+1, column=7, padx=5, pady=5)

tk.Label(second_frame, text="Credit worthiness:").grid(row=add_cust_base_row+2, column=2, padx=5, pady=5)
entry_credit_worthiness = tk.Entry(second_frame)
entry_credit_worthiness.grid(row=add_cust_base_row+2, column=3, padx=5, pady=5)

tk.Button(second_frame, text="Add Customer", command=insert_customer).grid(row=add_cust_base_row+2, column=4, padx=10, pady=10)

tk.Label(second_frame,text="Add new hotel section").grid(row=add_cust_base_row+3 ,column=4 , padx=10 , pady=10)
#Adding the insert section for the hotel table
add_hotel_base_row =5
tk.Label(second_frame, text="Hotel ID:").grid(row=add_hotel_base_row , column=0, padx=5, pady=5)
entry_hotel_id = tk.Entry(second_frame)
entry_hotel_id.grid(row=add_hotel_base_row, column=1, padx=5, pady=5)

tk.Label(second_frame, text="Hotel name:").grid(row=add_hotel_base_row, column=2, padx=5, pady=5)
entry_hotel_name = tk.Entry(second_frame)
entry_hotel_name.grid(row=add_hotel_base_row, column=3, padx=5, pady=5)

tk.Label(second_frame, text="Hotel loaction:").grid(row=add_hotel_base_row, column=4, padx=5, pady=5)
entry_hotel_loc = tk.Entry(second_frame)
entry_hotel_loc.grid(row=add_hotel_base_row, column=5, padx=5, pady=5)

tk.Label(second_frame, text="Hotel Policy:").grid(row=add_hotel_base_row, column=6, padx=5, pady=5)
entry_hotel_policy = tk.Entry(second_frame)
entry_hotel_policy.grid(row=add_hotel_base_row, column=7, padx=5, pady=5)

tk.Label(second_frame, text="Hotel email:").grid(row=add_hotel_base_row+1, column=0, padx=5, pady=5)
entry_hotel_email = tk.Entry(second_frame)
entry_hotel_email.grid(row=add_hotel_base_row+1, column=1, padx=5, pady=5)

tk.Label(second_frame, text="Hotel Phone:").grid(row=add_hotel_base_row+1, column=2, padx=5, pady=5)
entry_hotel_phone = tk.Entry(second_frame)
entry_hotel_phone.grid(row=add_hotel_base_row+1, column=3, padx=5, pady=5)

tk.Label(second_frame, text="Hotel website:").grid(row=add_hotel_base_row+1, column=4, padx=5, pady=5)
entry_hotel_website = tk.Entry(second_frame)
entry_hotel_website.grid(row=add_hotel_base_row+1, column=5, padx=5, pady=5)

tk.Button(second_frame, text="Add Hotel", command=insert_hotel).grid(row=add_hotel_base_row+1, column=6, padx=10, pady=10)

#Adding the delete section for the room table
base_row=7
base_col_del_room =2
tk.Label(second_frame , text= "delete from the table customer").grid(row = base_row , column = 4 , padx =5 ,pady =5)
tk.Label(second_frame , text= "condition").grid(row=base_row+2 , column = base_col_del_room ,padx=5 ,pady=5)
tk.Label(second_frame , text= "(attribute)").grid(row=base_row+1 , column = base_col_del_room+1 ,padx=5 ,pady=5)
entry_att_room = tk.Entry(second_frame)
entry_att_room.grid(row = base_row+2 , column = base_col_del_room+1 , padx = 5, pady=5)
tk.Label(second_frame , text= "=").grid(row = base_row+2 , column = base_col_del_room +2 , padx =5 ,pady =5)
tk.Label(second_frame , text= "(value)").grid(row=base_row+1 , column =base_col_del_room +3 ,padx=5 ,pady=5)
entry_value_room = tk.Entry(second_frame)
entry_value_room.grid(row = base_row+2 , column = base_col_del_room +3 , padx = 5 , pady=5)

tk.Button(second_frame , text = "delete room" , command=delete_room).grid(row = base_row+2 , column = base_col_del_room +4 , padx=5 ,pady=5)

#Adding the delete section for the ticket table
del_table_base_row = 10
tk.Label(second_frame , text= "delete from the table ticket").grid(row = del_table_base_row , column = 4 , padx =5 ,pady =5)
tk.Label(second_frame , text= "condition").grid(row=del_table_base_row+2 , column = base_col_del_room ,padx=5 ,pady=5)
tk.Label(second_frame , text= "(attribute)").grid(row=del_table_base_row+1 , column = base_col_del_room+1 ,padx=5 ,pady=5)
entry_att_table = tk.Entry(second_frame)
entry_att_table.grid(row = del_table_base_row+2 , column = base_col_del_room+1 , padx = 5 , pady=5)
tk.Label(second_frame , text= "=").grid(row = del_table_base_row+2 , column = base_col_del_room+2 , padx =5 ,pady =5)
tk.Label(second_frame , text= "(value)").grid(row=del_table_base_row+1 , column =base_col_del_room+3 ,padx=5 ,pady=5)
entry_value_table = tk.Entry(second_frame)
entry_value_table.grid(row = del_table_base_row+2 , column = base_col_del_room+3 , padx = 5 , pady=5)

tk.Button(second_frame , text = "delete ticket" , command=delete_room).grid(row = del_table_base_row+2 , column = base_col_del_room+4 , padx=10 ,pady=5)


# Adding the Treeview widget 
starting_row_tree = 15

tk.Label(second_frame , text= "select table to display data").grid(row = 14 , column = 4 , padx =5 ,pady =5)

tk.Label(second_frame , text= "table name").grid(row=starting_row_tree , column = 3 ,padx=5 ,pady=5)
entry_table_name = tk.Entry(second_frame)
entry_table_name.grid(row = starting_row_tree , column = 4 , padx = 5 , pady=5)

tk.Button(second_frame , text="Fetch tabel Data", command=fetch_table_data).grid(row = starting_row_tree , column = 5 , padx=10 ,pady=10)


   

# Run the Application
root.mainloop()
