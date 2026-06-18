import tkinter as tk
from tkinter import ttk, messagebox

# Data storage
inventory = []  # List to store inventory (medicine details)
sales = []  # List to store sales transactions

# Add Medicine Function
def add_medicine():
    def save_medicine():
        name = name_entry.get()
        quantity = quantity_entry.get()
        price = price_entry.get()
        expiry_date = expiry_entry.get()
        if name and quantity and price and expiry_date:
            inventory.append({"Name": name, "Quantity": int(quantity), "Price": float(price), "Expiry": expiry_date})
            messagebox.showinfo("Success", f"Medicine '{name}' added successfully!")
            add_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Please fill all fields.")

    add_window = tk.Toplevel(root)
    add_window.title("Add Medicine")
    add_window.geometry("400x300")
    add_window.configure(bg="light blue")

    tk.Label(add_window, text="Add Medicine", font=("Arial", 16, "bold"), bg="light blue").pack(pady=10)
    tk.Label(add_window, text="Name:", bg="light blue").pack()
    name_entry = tk.Entry(add_window, width=30)
    name_entry.pack()
    tk.Label(add_window, text="Quantity:", bg="light blue").pack()
    quantity_entry = tk.Entry(add_window, width=30)
    quantity_entry.pack()
    tk.Label(add_window, text="Price:", bg="light blue").pack()
    price_entry = tk.Entry(add_window, width=30)
    price_entry.pack()
    tk.Label(add_window, text="Expiry Date:", bg="light blue").pack()
    expiry_entry = tk.Entry(add_window, width=30)
    expiry_entry.pack()
    tk.Button(add_window, text="Save", command=save_medicine, bg="green", fg="white").pack(pady=10)

# View Inventory Function
def view_inventory():
    inventory_window = tk.Toplevel(root)
    inventory_window.title("View Inventory")
    inventory_window.geometry("600x400")
    inventory_window.configure(bg="light blue")

    tk.Label(inventory_window, text="Inventory", font=("Arial", 16, "bold"), bg="light blue").pack(pady=10)
    columns = ("Name", "Quantity", "Price", "Expiry")
    tree = ttk.Treeview(inventory_window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
    tree.pack(fill="both", expand=True)

    # Populate inventory data
    for item in inventory:
        tree.insert("", tk.END, values=(item["Name"], item["Quantity"], item["Price"], item["Expiry"]))

# View Sales Function
def view_sales():
    sales_window = tk.Toplevel(root)
    sales_window.title("View Sales")
    sales_window.geometry("600x400")
    sales_window.configure(bg="light blue")

    tk.Label(sales_window, text="Sales", font=("Arial", 16, "bold"), bg="light blue").pack(pady=10)
    columns = ("Name", "Quantity", "Price", "Total")
    tree = ttk.Treeview(sales_window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
    tree.pack(fill="both", expand=True)

    # Populate sales data
    for sale in sales:
        total = float(sale["Price"]) * int(sale["Quantity"])
        tree.insert("", tk.END, values=(sale["Name"], sale["Quantity"], sale["Price"], f"{total:.2f}"))

# Sell Medicine Function
def sell_medicine():
    def process_sale():
        name = name_entry.get()
        quantity = quantity_entry.get()

        if not name or not quantity:
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return

        quantity = int(quantity)
        for item in inventory:
            if item["Name"] == name:
                if item["Quantity"] >= quantity:
                    item["Quantity"] -= quantity
                    sales.append({"Name": name, "Quantity": quantity, "Price": item["Price"]})
                    messagebox.showinfo("Success", f"Sold {quantity} of '{name}' successfully!")
                    sell_window.destroy()
                    return
                else:
                    messagebox.showwarning("Stock Error", "Not enough stock available.")
                    return

        messagebox.showwarning("Not Found", f"Medicine '{name}' not found in inventory.")

    sell_window = tk.Toplevel(root)
    sell_window.title("Sell Medicine")
    sell_window.geometry("400x200")
    sell_window.configure(bg="light blue")

    tk.Label(sell_window, text="Sell Medicine", font=("Arial", 16, "bold"), bg="light blue").pack(pady=10)
    tk.Label(sell_window, text="Name:", bg="light blue").pack()
    name_entry = tk.Entry(sell_window, width=30)
    name_entry.pack()
    tk.Label(sell_window, text="Quantity:", bg="light blue").pack()
    quantity_entry = tk.Entry(sell_window, width=30)
    quantity_entry.pack()
    tk.Button(sell_window, text="Sell", command=process_sale, bg="green", fg="white").pack(pady=10)

# Main UI
root = tk.Tk()
root.title("KHADIJA RASHID (FA24-BSE-032)")
root.geometry("900x700")
root.configure(bg="green")

# Title
title_frame = tk.Frame(root, bg="white", relief="raised", bd=3)
title_frame.pack(pady=20)
title_label = tk.Label(
    title_frame,
    text="PHARMACY MANAGEMENT SYSTEM",
    font=("Arial", 24, "bold"),
    bg="white",
    fg="black",
    padx=10,
    pady=10
)
title_label.pack()

# Quote
quote_frame = tk.Frame(root, bg="light green", relief="sunken", bd=2)
quote_frame.pack(pady=10, fill="x")
quote_label = tk.Label(
    quote_frame,
    text="Your health is our priority, and we care for every detail of your needs.",
    font=("Arial", 16, "italic"),
    bg="light green",
    padx=20,
    pady=10
)
quote_label.pack()

# Buttons
button_frame = tk.Frame(root, bg="green")
button_frame.pack(pady=30)

button_style = {
    "font": ("Arial", 18),
    "bg": "light blue",
    "fg": "black",
    "width": 25,
    "height": 2,
    "relief": "raised",
    "bd": 3
}

tk.Button(button_frame, text="ADD A MEDICINE", command=add_medicine, **button_style).pack(pady=10)
tk.Button(button_frame, text="VIEW INVENTORY", command=view_inventory, **button_style).pack(pady=10)
tk.Button(button_frame, text="SELL MEDICINE", command=sell_medicine, **button_style).pack(pady=10)
tk.Button(button_frame, text="VIEW SALES", command=view_sales, **button_style).pack(pady=10)

# Run the application
root.mainloop()

