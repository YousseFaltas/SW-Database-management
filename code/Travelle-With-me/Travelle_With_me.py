from ast import Attribute
import email
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from turtle import update, width
from venv import create
import pyodbc
import csv
from tkinter import filedialog
import math

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

def configure_treeview_fetch_columns(columns):
    tree_fetch["columns"] = columns
    for col in columns:
        tree_fetch.heading(col, text=col)
        tree_fetch.column(col)
       
 
def fetch_table_data():
    table_name = table_var1.get()
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = [list(row) for row in cursor.fetchall() ] 
            column_names = [column[0] for column in cursor.description]
            for row in tree_fetch.get_children():
                tree_fetch.delete(row)
            configure_treeview_fetch_columns(column_names)
            for row in rows:
                tree_fetch.insert("", tk.END, values=row)
        except pyodbc.Error as e:
            messagebox.showerror("Error", f"Error fetching data: {e}")
        finally:
            conn.close()
    else:
        messagebox.showwarning("Input Error", "Please select a table")
            
def update_room () :
    int_arr = ["H_id, R_id , R_Price"]
    set_att = entry_set_att.get()
    set_val = entry_set_val.get()
    where_att=entry_where_att.get()
    where_val = entry_where_val.get()
    if set_att not in int_arr:
        set_val = f"'{entry_set_val}'"
    if where_att not in int_arr:
        where_val= f"'{entry_where_val}'"
    if set_att and set_val and where_att and where_val:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            try:
                if where_att and where_val:
                    cursor.execute(f'UPDATE Room SET {set_att} = {set_val} WHERE {where_att} = {where_val}')
                    conn.commit()
                else:
                    cursor.execute("""
                    UPDATE Room
                    SET ? = ?""", (set_att, set_val))
                    conn.commit()
                messagebox.showinfo("Success", "Room updated successfully!")
            except pyodbc.Error as e:
                messagebox.showerror("Error", f"Error updating Room: {e}")
            finally:
                conn.close()
    else:
        messagebox.showwarning("Input Error", "Please enter all fields!")
        
def update_customer () :
    int_arr = ["Cust_id","Date_birth"]
    set_att = entry_cust_set_att.get()
    set_val = entry_cust_set_val.get()
    where_att = entry_cust_where_att.get()
    where_val = entry_cust_where_val.get()
    if set_att in int_arr:
        set_val = f"'{entry_cust_set_val}'"
    if where_att in int_arr:
        where_val= f"'{entry_cust_where_val}'"
    if set_att and set_val and where_att and where_val:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            try:
                if where_att and where_val:
                    cursor.execute(f'UPDATE Customer SET {set_att} = {set_val} WHERE {where_att} = {where_val}')
                    conn.commit()
                else:
                    cursor.execute("""
                    UPDATE Customer
                    SET ? = ?""", (set_att, set_val))
                    conn.commit()
                messagebox.showinfo("Success", "Customer updated successfully!")
            except pyodbc.Error as e:
                messagebox.showerror("Error", f"Error updating Customer: {e}")
            finally:
                conn.close()
    else:
        messagebox.showwarning("Input Error", "Please enter all fields!")
        
# Add this function to handle join queries
def execute_join_query():
    table1 = entry_join_table1.get()
    table2 = entry_join_table2.get()
    join_condition = entry_join_condition.get()
    columns = entry_join_columns.get()

    if table1 and table2 and join_condition and columns:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            try:
                # Construct the SQL query dynamically
                query = f"""
                SELECT {columns}
                FROM {table1}
                INNER JOIN {table2} ON {join_condition};
                """
                cursor.execute(query)
                rows = [list(row) for row in cursor.fetchall() ] 

                # Clear the existing data in the treeview
                for row in tree_join.get_children():
                    tree_join.delete(row)

                # Insert the new data into the treeview
                for row in rows:
                    tree_join.insert("", tk.END, values=row)

                messagebox.showinfo("Success", "Join query executed successfully!")
            except pyodbc.Error as e:
                messagebox.showerror("Error", f"Error executing join query: {e}")
            finally:
                conn.close()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields for the join query!")


# Configure the Treeview columns dynamically based on the query results
def configure_treeview_columns(columns):
    tree_join["columns"] = columns
    for col in columns:
        tree_join.heading(col, text=col)
        tree_join.column(col, width=150 , stretch= False)

# Modify the execute_join_query function to configure the Treeview columns
def execute_join_query():
    table1 = entry_join_table1.get()
    table2 = entry_join_table2.get()
    join_condition = entry_join_condition.get()
    columns = entry_join_columns.get()

    if table1 and table2 and join_condition and columns:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            try:
                # Construct the SQL query dynamically
                query = f"""
                SELECT {columns}
                FROM {table1}
                INNER JOIN {table2} ON {join_condition};
                """
                cursor.execute(query)
                rows = cursor.fetchall()

                # Get column names from the query result
                column_names = [column[0] for column in cursor.description]

                # Clear the existing data in the treeview
                for row in tree_join.get_children():
                    tree_join.delete(row)

                # Configure the Treeview columns dynamically
                configure_treeview_columns(column_names)

                # Insert the new data into the treeview
                for row in rows:
                    tree_join.insert("", tk.END, values=row)

                messagebox.showinfo("Success", "Join query executed successfully!")
            except pyodbc.Error as e:
                messagebox.showerror("Error", f"Error executing join query: {e}")
            finally:
                conn.close()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields for the join query!")


# Fetch table names from the database
def get_table_names():
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';")
            tables = [row[0] for row in cursor.fetchall()]
            return tables
        except pyodbc.Error as e:
            messagebox.showerror("Error", f"Error fetching table names: {e}")
            return []
        finally:
            conn.close()

# Export data to CSV
def export_to_csv():
    table_name = table_var.get()
    if not table_name:
        messagebox.showwarning("Input Error", "Please select a table to export.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return  # User cancelled the dialog
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            if not rows:
                messagebox.showinfo("Info", "No data to export.")
                return
            # Get column names
            columns = [column[0] for column in cursor.description]
            # Write to CSV
            with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(columns)
                for row in rows:
                    writer.writerow(row)
            messagebox.showinfo("Success", f"Data from {table_name} has been exported to {file_path}.")
        except pyodbc.Error as e:
            messagebox.showerror("Error", f"Error exporting data: {e}")
        finally:
            conn.close()
    else:
        messagebox.showwarning("Database Error", "Could not connect to the database.")
        
root = tk.Tk()
root.title("database GUI")
root.geometry("1200x600")
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
second_frame = Frame(main_canvas , width= 500 , height=1100)
second_frame.pack_propagate(False)

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
tk.Label(second_frame , text= "delete from the table room ").grid(row = base_row , column = 4 , padx =5 ,pady =5)
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

#Adding the update section for the room table
update_base_row = 14
tk.Label(second_frame , text= "update from the table room").grid(row = update_base_row , column = 4 , padx =5 ,pady =5)
tk.Label(second_frame , text= "column to update").grid(row=update_base_row+2 , column = base_col_del_room ,padx=5 ,pady=5)
tk.Label(second_frame , text= "(attribute)").grid(row=update_base_row+1 , column = base_col_del_room+1 ,padx=5 ,pady=5)
entry_set_att = tk.Entry(second_frame)
entry_set_att.grid(row = update_base_row+2 , column = base_col_del_room+1 , padx = 5 , pady=5)
tk.Label(second_frame , text= "=").grid(row = update_base_row+2 , column = base_col_del_room+2 , padx =5 ,pady =5)
tk.Label(second_frame , text= "(value)").grid(row=update_base_row+1 , column =base_col_del_room+3 ,padx=5 ,pady=5)
entry_set_val = tk.Entry(second_frame)
entry_set_val.grid(row = update_base_row+2 , column = base_col_del_room+3 , padx = 5 , pady=5)
tk.Label(second_frame , text= "=").grid(row = update_base_row+3 , column = base_col_del_room+2 , padx =5 ,pady =5)
#condition
tk.Label(second_frame , text= "condition").grid(row=update_base_row+3 , column = base_col_del_room ,padx=5 ,pady=5)
entry_where_val = tk.Entry(second_frame)
entry_where_val.grid(row = update_base_row+3 , column = base_col_del_room+3 , padx = 5 , pady=5)
tk.Label(second_frame , text= "=").grid(row = update_base_row+3 , column = base_col_del_room+2 , padx =5 ,pady =5)
entry_where_att = tk.Entry(second_frame)
entry_where_att.grid(row = update_base_row+3 , column = base_col_del_room+1 , padx = 5 , pady=5)

tk.Button(second_frame , text = "update room" , command=update_room).grid(row = update_base_row+3 , column = base_col_del_room+4 , padx=10 ,pady=5)

#Adding the update section for the customer table 
update_customer_row = 20
tk.Label(second_frame , text= "update from the Customer room").grid(row = update_customer_row , column = 4 , padx =5 ,pady =5)
tk.Label(second_frame , text= "column to update").grid(row=update_customer_row+2 , column = base_col_del_room ,padx=5 ,pady=5)
tk.Label(second_frame , text= "(attribute)").grid(row=update_customer_row+1 , column = base_col_del_room+1 ,padx=5 ,pady=5)
entry_cust_set_att = tk.Entry(second_frame)
entry_cust_set_att.grid(row = update_customer_row+2 , column = base_col_del_room+1 , padx = 5 , pady=5)
tk.Label(second_frame , text= "=").grid(row = update_customer_row+2 , column = base_col_del_room+2 , padx =5 ,pady =5)
tk.Label(second_frame , text= "(value)").grid(row=update_customer_row+1 , column =base_col_del_room+3 ,padx=5 ,pady=5)
entry_cust_set_val = tk.Entry(second_frame)
entry_cust_set_val.grid(row = update_customer_row+2 , column = base_col_del_room+3 , padx = 5 , pady=5)
tk.Label(second_frame , text= "=").grid(row = update_customer_row+3 , column = base_col_del_room+2 , padx =5 ,pady =5)
#condition
tk.Label(second_frame , text= "condition").grid(row=update_customer_row+3 , column = base_col_del_room ,padx=5 ,pady=5)
entry_cust_where_val = tk.Entry(second_frame)
entry_cust_where_val.grid(row = update_customer_row+3 , column = base_col_del_room+3 , padx = 5 , pady=5)
tk.Label(second_frame , text= "=").grid(row = update_customer_row+3 , column = base_col_del_room+2 , padx =5 ,pady =5)
entry_cust_where_att = tk.Entry(second_frame)
entry_cust_where_att.grid(row = update_customer_row+3 , column = base_col_del_room+1 , padx = 5 , pady=5)

tk.Button(second_frame , text = "update customer" , command=update_customer).grid(row = update_customer_row+3 , column = base_col_del_room+4 , padx=10 ,pady=5)


# Adding the Treeview widget 
tables = get_table_names()
if tables:
    table_var1 = StringVar()
    table_combobox1 = ttk.Combobox(second_frame, textvariable=table_var1, values=tables)
    table_combobox1.set("Select a table")
    table_combobox1.grid(row=27, column=4, padx=5, pady=5)
else:
    messagebox.showwarning("No Tables", "No tables found in the database.")
    
starting_row_tree = 27

tk.Label(second_frame , text= "select table to display data").grid(row = 26 , column = 4 , padx =5 ,pady =5)

tree_frame = tk.Frame(second_frame, width=800 , height=400)
tree_frame.grid(row=starting_row_tree + 1, column=0, columnspan=8, padx=10, pady=10, sticky="nsew")
tree_frame.grid_propagate(False)


tree_fetch = ttk.Treeview(tree_frame, columns=("Column1", "Column2", "Column3"), show="headings")
tree_fetch.grid(row=0, column=0, sticky="nsew")

# Add a horizontal scrollbar
tree_horizontal_scroll = ttk.Scrollbar(tree_frame, orient="horizontal", command=tree_fetch.xview)
tree_horizontal_scroll.grid(row=1, column=0, sticky="ew")

# Configure the Treeview to use the horizontal scrollbar
tree_fetch.configure(xscrollcommand=tree_horizontal_scroll.set)

# Ensure the Treeview expands to fill the frame
tree_frame.grid_rowconfigure(0, weight=1)
tree_frame.grid_columnconfigure(0, weight=1)

# Add a vertical scrollbar 
tree_vertical_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=tree_fetch.yview)
tree_vertical_scroll.grid(row=0, column=1, sticky="ns")
tree_fetch.configure(yscrollcommand=tree_vertical_scroll.set)

tk.Button(second_frame , text="Fetch tabel Data", command=fetch_table_data).grid(row = starting_row_tree , column = 5 , padx=10 ,pady=10)


# GUI for join queries
join_base_row = 30
tk.Label(second_frame, text="Join Query Section").grid(row=join_base_row, column=4, padx=10, pady=10)

tk.Label(second_frame, text="Table 1:").grid(row=join_base_row + 1, column=0, padx=5, pady=5)
entry_join_table1 = tk.Entry(second_frame)
entry_join_table1.grid(row=join_base_row + 1, column=1, padx=5, pady=5)

tk.Label(second_frame, text="Table 2:").grid(row=join_base_row + 1, column=2, padx=5, pady=5)
entry_join_table2 = tk.Entry(second_frame)
entry_join_table2.grid(row=join_base_row + 1, column=3, padx=5, pady=5)

tk.Label(second_frame, text="Join Condition:").grid(row=join_base_row + 1, column=4, padx=5, pady=5)
entry_join_condition = tk.Entry(second_frame)
entry_join_condition.grid(row=join_base_row + 1, column=5, padx=5, pady=5)

tk.Label(second_frame, text="Columns to Select:").grid(row=join_base_row + 2, column=0, padx=5, pady=5)
entry_join_columns = tk.Entry(second_frame)
entry_join_columns.grid(row=join_base_row + 2, column=1, padx=5, pady=5)

tk.Button(second_frame, text="Execute Join Query", command=execute_join_query).grid(row=join_base_row + 2, column=4, padx=10, pady=10)

# Add a Treeview to display join query results
tree_frame_join = tk.Frame(second_frame, width=800 , height=400)
tree_frame_join.grid(row=join_base_row+3 , column=0, columnspan=8, padx=10, pady=10, sticky="nsew")
tree_frame_join.grid_propagate(False)


tree_join = ttk.Treeview(tree_frame_join, columns=("Column1", "Column2", "Column3"), show="headings")
tree_join.grid(row=0, column=0, columnspan=8, padx=10, pady=10, sticky="nsew")


# Add a horizontal scrollbar
tree_horizontal_scroll_1 = ttk.Scrollbar(tree_frame_join, orient="horizontal", command=tree_join.xview)
tree_horizontal_scroll_1.grid(row=1, column=0, sticky="ew")

# Configure the Treeview to use the horizontal scrollbar
tree_join.configure(xscrollcommand=tree_horizontal_scroll_1.set)

# Ensure the Treeview expands to fill the frame
tree_frame_join.grid_rowconfigure(0, weight=1)
tree_frame_join.grid_columnconfigure(0, weight=1)

# Add a vertical scrollbar 
tree_vertical_scroll_1 = ttk.Scrollbar(tree_frame_join, orient="vertical", command=tree_join.yview)
tree_vertical_scroll_1.grid(row=0, column=1, sticky="ns")
tree_join.configure(yscrollcommand=tree_vertical_scroll_1.set)

# GUI to include export functionality

if tables:
    table_var = StringVar()
    table_combobox = ttk.Combobox(second_frame, textvariable=table_var, values=tables)
    table_combobox.set("Select a table")
    table_combobox.grid(row=40, column=1, padx=5, pady=5)
else:
    messagebox.showwarning("No Tables", "No tables found in the database.")

Button(second_frame, text="Export to CSV", command=export_to_csv).grid(row=40, column=2, padx=10, pady=10)

root.resizable(False, False)
# Run the Application
root.mainloop()
