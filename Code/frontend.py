import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import requests
import os

# Function to handle POST requests to the Flask server
def send_data_to_server(data, url='http://127.0.0.1:8080/'):
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Invoice sent successfully!")
        else:
            messagebox.showerror("Error", "Failed to send invoice!")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error communicating with server: {e}")

# Function to upload a template file
def upload_template():
    file_path = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                template_content = file.read()
            # Send the template to the server
            send_data_to_server({'template_content': template_content}, url='http://127.0.0.1:8080/uploadtemplate')
        except Exception as e:
            messagebox.showerror("Error", f"Error uploading template: {e}")

# Function to create the invoice
def create_invoice():
    # Collect all data from the Tkinter fields and send it to the Flask backend
    data = {
        'customer_company': customer_company.get(),
        'customer_handler_name': customer_handler_name.get(),
        'customer_handler_email': customer_handler_email.get(),
        'customer_address_line1': customer_address_line1.get(),
        'customer_address_line2': customer_address_line2.get(),
    }

    # Add Product Items
    product_items = []
    for i in range(len(item_titles)):
        product_items.append({
            'product_title': item_titles[i].get(),
            'product_charge': item_charges[i].get(),
            'product_number': item_numbers[i].get(),
            'product_tax': item_taxes[i].get(),
        })
    data['product_items'] = product_items

    # Add Service Items
    service_items = []
    for i in range(len(service_titles)):
        service_items.append({
            'service_title': service_titles[i].get(),
            'service_charge': service_charges[i].get(),
            'service_number': service_numbers[i].get(),
            'service_tax': service_taxes[i].get(),
        })
    data['service_items'] = service_items

    # Send data to the server to create the invoice
    send_data_to_server(data)

# Function to add a new product item row
def add_product_item():
    item_titles.append(tk.Entry(tab_home))
    item_charges.append(tk.Entry(tab_home))
    item_numbers.append(tk.Entry(tab_home))
    item_taxes.append(tk.Entry(tab_home))

    row = len(item_titles)
    tk.Label(tab_home, text="Item Title").grid(row=row, column=0)
    item_titles[-1].grid(row=row, column=1)
    tk.Label(tab_home, text="Charge Per Item").grid(row=row, column=2)
    item_charges[-1].grid(row=row, column=3)
    tk.Label(tab_home, text="Item Quantity").grid(row=row, column=4)
    item_numbers[-1].grid(row=row, column=5)
    tk.Label(tab_home, text="Tax (%)").grid(row=row, column=6)
    item_taxes[-1].grid(row=row, column=7)

# Function to add a new service item row
def add_service_item():
    service_titles.append(tk.Entry(tab_home))
    service_charges.append(tk.Entry(tab_home))
    service_numbers.append(tk.Entry(tab_home))
    service_taxes.append(tk.Entry(tab_home))

    row = len(service_titles)
    tk.Label(tab_home, text="Service Title").grid(row=row, column=0)
    service_titles[-1].grid(row=row, column=1)
    tk.Label(tab_home, text="Charge Per Hour").grid(row=row, column=2)
    service_charges[-1].grid(row=row, column=3)
    tk.Label(tab_home, text="Hour Quantity").grid(row=row, column=4)
    service_numbers[-1].grid(row=row, column=5)
    tk.Label(tab_home, text="Tax (%)").grid(row=row, column=6)
    service_taxes[-1].grid(row=row, column=7)

# Create the Tkinter root window
root = tk.Tk()
root.title("Invoice Generator")

# Create the notebook (tabs)
tab_control = ttk.Notebook(root)

# Tab 1 - Home
tab_home = tk.Frame(tab_control)
tab_control.add(tab_home, text="Home")

# Customer Info Inputs
tk.Label(tab_home, text="Customer Company Name:").grid(row=0, column=0)
customer_company = tk.Entry(tab_home)
customer_company.grid(row=0, column=1)

tk.Label(tab_home, text="Customer Handler Name:").grid(row=1, column=0)
customer_handler_name = tk.Entry(tab_home)
customer_handler_name.grid(row=1, column=1)

tk.Label(tab_home, text="Customer Handler Email:").grid(row=2, column=0)
customer_handler_email = tk.Entry(tab_home)
customer_handler_email.grid(row=2, column=1)

tk.Label(tab_home, text="Customer Address (Line 1):").grid(row=3, column=0)
customer_address_line1 = tk.Entry(tab_home)
customer_address_line1.grid(row=3, column=1)

tk.Label(tab_home, text="Customer Address (Line 2):").grid(row=4, column=0)
customer_address_line2 = tk.Entry(tab_home)
customer_address_line2.grid(row=4, column=1)

# Add product items dynamically
item_titles = []
item_charges = []
item_numbers = []
item_taxes = []
add_product_item_button = tk.Button(tab_home, text="Add Product Item", command=add_product_item)
add_product_item_button.grid(row=5, column=0)

# Add service items dynamically
service_titles = []
service_charges = []
service_numbers = []
service_taxes = []
add_service_item_button = tk.Button(tab_home, text="Add Service Item", command=add_service_item)
add_service_item_button.grid(row=5, column=1)

# Tab 2 - Settings
tab_settings = tk.Frame(tab_control)
tab_control.add(tab_settings, text="Settings")

tk.Label(tab_settings, text="Provider Company:").grid(row=0, column=0)
provider_company = tk.Entry(tab_settings)
provider_company.grid(row=0, column=1)

tk.Label(tab_settings, text="Provider Handler Name:").grid(row=1, column=0)
provider_handler_name = tk.Entry(tab_settings)
provider_handler_name.grid(row=1, column=1)

tk.Label(tab_settings, text="Provider Handler Email:").grid(row=2, column=0)
provider_handler_email = tk.Entry(tab_settings)
provider_handler_email.grid(row=2, column=1)

tk.Label(tab_settings, text="Provider Address (Line 1):").grid(row=3, column=0)
provider_address_line1 = tk.Entry(tab_settings)
provider_address_line1.grid(row=3, column=1)

tk.Label(tab_settings, text="Provider Address (Line 2):").grid(row=4, column=0)
provider_address_line2 = tk.Entry(tab_settings)
provider_address_line2.grid(row=4, column=1)

# Tab 3 - Templates
tab_templates = tk.Frame(tab_control)
tab_control.add(tab_templates, text="Templates")

upload_button = tk.Button(tab_templates, text="Upload Template", command=upload_template)
upload_button.grid(row=0, column=0)

# Tab 4 - Create Invoice
tab_create_invoice = tk.Frame(tab_control)
tab_control.add(tab_create_invoice, text="Create Invoice")

create_invoice_button = tk.Button(tab_create_invoice, text="Create Invoice", command=create_invoice)
create_invoice_button.grid(row=0, column=0)

# Finalize
tab_control.pack(expand=1, fill="both")
root.mainloop()
