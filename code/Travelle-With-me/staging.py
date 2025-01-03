import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc

# Database connection
def connect_to_database():
    try:
        conn = pyodbc.connect(f'Driver={{ODBC Driver 17 for SQL Server}};Server=YOUSSEF-LAPTOP\SQLEXPRESS;Database=Faith;Trusted_Connection=yes;')
        print("connected successfully")
        return conn
    except pyodbc.Error as e:
        messagebox.showerror("Database Error", f"Error connecting to database: {e}")
        return None
    
# Delete operations
def delete_room():
    room_id = entry_room_id.get()
    if room_id:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM Room WHERE Room_ID = ?", (room_id,))
                conn.commit()
                messagebox.showinfo("Success", "Room deleted successfully!")
            except pyodbc.Error as e:
                messagebox.showerror("Error", f"Error deleting room: {e}")
            finally:
                conn.close()
    else:
        messagebox.showwarning("Input Error", "Please enter the Room ID!")

def delete_car():
    car_id = entry_car_id.get()
    if car_id:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM Car WHERE Car_ID = ?", (car_id,))
                conn.commit()
                messagebox.showinfo("Success", "Car deleted successfully!")
            except pyodbc.Error as e:
                messagebox.showerror("Error", f"Error deleting car: {e}")
            finally:
                conn.close()
    else:
        messagebox.showwarning("Input Error", "Please enter the Car ID!")

# Update operations
def update_customer():
    cust_id = entry_update_cust_id.get()
    address = entry_update_cust_address.get()
    if cust_id and address:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    UPDATE Customer
                    SET Cust_Address = ?
                    WHERE Cust_ID = ?""", (address, cust_id))
                conn.commit()
                messagebox.showinfo("Success", "Customer updated successfully!")
            except pyodbc.Error as e:
                messagebox.showerror("Error", f"Error updating customer: {e}")
            finally:
                conn.close()
    else:
        messagebox.showwarning("Input Error", "Please enter all fields!")

def update_hotel():
    hotel_id = entry_update_hotel_id.get()
    phone = entry_update_hotel_phone.get()
    if hotel_id and phone:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    UPDATE Hotel
                    SET H_PhoneNum = ?
                    WHERE H_ID = ?""", (phone, hotel_id))
                conn.commit()
                messagebox.showinfo("Success", "Hotel updated successfully!")
            except pyodbc.Error as e:
                messagebox.showerror("Error", f"Error updating hotel: {e}")
            finally:
                conn.close()
    else:
        messagebox.showwarning("Input Error", "Please enter all fields!")

# Select operations
def fetch_customer_data():
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM customer")
            rows = cursor.fetchall()
            tree_customer.delete(*tree_customer.get_children())  # Clear existing rows
            for row in rows:
                row_values = []
                for value in row:
                    row_values.append(value)
                tree_customer.insert("", tk.END, values=row_values)
        except pyodbc.Error as e:
            messagebox.showerror("Error", f"Error fetching customer data: {e}")
        finally:
            conn.close()


def fetch_hotel_data():
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM Hotel")
            rows = cursor.fetchall()
            tree_hotel.delete(*tree_hotel.get_children())  # Clear existing rows
            for row in rows:
                row_values = []
                for value in row:
                    row_values.append(value)
                tree_hotel.insert("", tk.END, values=row_values)
        except pyodbc.Error as e:
            messagebox.showerror("Error", f"Error fetching hotel data: {e}")
        finally:
            conn.close()

# GUI setup
root = tk.Tk()
root.title("Hotel Management System")

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=canvas.yview)

canvas.config(scrollregion=canvas.bbox(tk.ALL))

# Delete Section
frame_delete = tk.Frame(canvas)
frame_delete.pack(pady=10)

tk.Label(frame_delete, text="Room ID to Delete:").grid(row=0, column=0, padx=5, pady=5)
entry_room_id = tk.Entry(frame_delete)
entry_room_id.grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_delete, text="Delete Room", command=delete_room).grid(row=0, column=2, padx=5, pady=5)

tk.Label(frame_delete, text="Car ID to Delete:").grid(row=0, column=3, padx=5, pady=5)
entry_car_id = tk.Entry(frame_delete)
entry_car_id.grid(row=0, column=4, padx=5, pady=5)
tk.Button(frame_delete, text="Delete Car", command=delete_car).grid(row=0, column=5, padx=5, pady=5)

# Update Section
frame_update = tk.Frame(canvas)
frame_update.pack(pady=10)

tk.Label(frame_update, text="Customer ID to Update:").grid(row=0, column=0, padx=5, pady=5)
entry_update_cust_id = tk.Entry(frame_update)
entry_update_cust_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_update, text="New Address:").grid(row=0, column=2, padx=5, pady=5)
entry_update_cust_address = tk.Entry(frame_update)
entry_update_cust_address.grid(row=0, column=3, padx=5, pady=5)

tk.Button(frame_update, text="Update Customer", command=update_customer).grid(row=0, column=4, padx=5, pady=5)

tk.Label(frame_update, text="Hotel ID to Update:").grid(row=1, column=0, padx=5, pady=5)
entry_update_hotel_id = tk.Entry(frame_update)
entry_update_hotel_id.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_update, text="New Phone:").grid(row=1, column=2, padx=5, pady=5)
entry_update_hotel_phone = tk.Entry(frame_update)
entry_update_hotel_phone.grid(row=1, column=3, padx=5, pady=5)

tk.Button(frame_update, text="Update Hotel", command=update_hotel).grid(row=1, column=4, padx=5, pady=5)


# Fetch Customer Data Section
frame_customer = tk.Frame(canvas)
frame_customer.pack(pady=10)

tk.Label(frame_customer, text="Customer Data").pack(pady=5)

columns_customer = ( "Cust_ID" , "Cust_Name" , "Cust_email" , "Cust_phone" , "Cust_address" , "nationality" , "Bank_acc" , "Date_Birth" , "Credit_Worthiness")
tree_customer = ttk.Treeview(frame_customer, columns=columns_customer, show="headings", height=5)
tree_customer.pack()

scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree_customer.yview)
tree_customer.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

for col in columns_customer:
    tree_customer.heading(col, text=col)

tk.Button(frame_customer, text="Fetch Customer Data", command=fetch_customer_data).pack(pady=5)

# Fetch Hotel Data Section
frame_hotel = tk.Frame(canvas)
frame_hotel.pack(pady=10)

tk.Label(frame_hotel, text="Hotel Data").pack(pady=5)

columns_hotel = ("H_Name", "H_Loc", "H_Policy")
tree_hotel = ttk.Treeview(frame_hotel, columns=columns_hotel, show="headings", height=5)
tree_hotel.pack()

for col in columns_hotel:
    tree_hotel.heading(col, text=col)

tk.Button(frame_hotel, text="Fetch Hotel Data", command=fetch_hotel_data).pack(pady=5)

# Run the Application
root.mainloop()

