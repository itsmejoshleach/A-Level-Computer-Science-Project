import tkinter as tk
from tkinter import TclError, ttk

root = tk.Tk()
root.title("Invoice Creator")
root.resizable(0, 0)

# layout on the root window
root.columnconfigure(0, weight=4)
root.columnconfigure(1, weight=1)

customer_company = tk.StringVar()
customer_handler_name = tk.StringVar()
customer_handler_email = tk.StringVar()
customer_address_1 = tk.StringVar()
customer_address_2 = tk.StringVar()

def create_invoice():
  print(Customer['Address_2'])

def create_menu_frame(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=3)

    ttk.Button(frame, text='Home').grid(column=0, row=0)
    ttk.Button(frame, text='Settings').grid(column=0, row=1)
    ttk.Button(frame, text='Templates').grid(column=0, row=2)
    ttk.Button(frame, text='Cancel').grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame

def create_customer_details_subframe(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Label(frame, text='Customer Company:').grid(column=0, row=0, sticky=tk.W)
    ttk.Entry(frame, textvariable=customer_company, width=30).grid(column=1, row=0, sticky=tk.W)

    ttk.Label(frame, text='Customer Handler Name:').grid(column=0, row=1, sticky=tk.W)
    ttk.Entry(frame, textvariable=customer_handler_name, width=30).grid(column=1, row=1, sticky=tk.W)

    ttk.Label(frame, text='Customer Handler Email:').grid(column=0, row=2, sticky=tk.W)
    ttk.Entry(frame, textvariable=customer_handler_email, width=30).grid(column=1, row=2, sticky=tk.W)

    ttk.Label(frame, text='Customer Address (Line 1):').grid(column=0, row=3, sticky=tk.W)
    ttk.Entry(frame, textvariable=customer_address_1, width=30).grid(column=1, row=3, sticky=tk.W)

    ttk.Label(frame, text='Customer Address (Line 2):').grid(column=0, row=4, sticky=tk.W)
    ttk.Entry(frame, textvariable=customer_address_2, width=30).grid(column=1, row=4, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame

def create_provider_details_subframe(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Label(frame, text='Provider Company:').grid(column=0, row=0, sticky=tk.W)
    ttk.Entry(frame, width=30).grid(column=1, row=0, sticky=tk.W)

    ttk.Label(frame, text='Provider Handler Name:').grid(column=0, row=1, sticky=tk.W)
    ttk.Entry(frame, width=30).grid(column=1, row=1, sticky=tk.W)

    ttk.Label(frame, text='Provider Handler Email:').grid(column=0, row=2, sticky=tk.W)
    ttk.Entry(frame, width=30).grid(column=1, row=2, sticky=tk.W)

    ttk.Label(frame, text='Provider Address (Line 1):').grid(column=0, row=3, sticky=tk.W)
    ttk.Entry(frame, width=30).grid(column=1, row=3, sticky=tk.W)

    ttk.Label(frame, text='Provider Address (Line 2):').grid(column=0, row=4, sticky=tk.W)
    ttk.Entry(frame, width=30).grid(column=1, row=4, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame

def create_details_frame(container):
  frame = ttk.Frame(container)

  create_customer_details_subframe(frame).grid(column=1, row=0)
  create_provider_details_subframe(frame).grid(column=1, row=1)

  return frame

def create_products_subframe(container):
  frame = ttk.Frame(container)

  frame.columnconfigure(0, weight=1)

  ttk.Label(frame, text='Title: ').grid(column=0, row=0, sticky=tk.W)
  ttk.Entry(frame, width=30).grid(column=1, row=0, sticky=tk.W)

  ttk.Label(frame, text='Charge Per Item: ').grid(column=0, row=1, sticky=tk.W)
  ttk.Entry(frame, width=30).grid(column=1, row=1, sticky=tk.W)

  ttk.Label(frame, text='Item Number: ').grid(column=0, row=2, sticky=tk.W)
  ttk.Entry(frame, width=30).grid(column=1, row=2, sticky=tk.W)

  ttk.Label(frame, text='Tax (%): ').grid(column=0, row=3, sticky=tk.W)
  ttk.Entry(frame, width=30).grid(column=1, row=3, sticky=tk.W)

  for widget in frame.winfo_children():
      widget.grid(padx=5, pady=5)

  return frame

def create_services_subframe(container):
  frame = ttk.Frame(container)

  frame.columnconfigure(0, weight=1)

  ttk.Label(frame, text='Title: ').grid(column=0, row=0, sticky=tk.W)
  ttk.Entry(frame, width=30).grid(column=1, row=0, sticky=tk.W)

  ttk.Label(frame, text='Price Per Hour: ').grid(column=0, row=1, sticky=tk.W)
  ttk.Entry(frame, width=30).grid(column=1, row=1, sticky=tk.W)

  ttk.Label(frame, text='Total Hours: ').grid(column=0, row=2, sticky=tk.W)
  ttk.Entry(frame, width=30).grid(column=1, row=2, sticky=tk.W)

  ttk.Label(frame, text='Tax (%): ').grid(column=0, row=3, sticky=tk.W)
  ttk.Entry(frame, width=30).grid(column=1, row=3, sticky=tk.W)

  for widget in frame.winfo_children():
      widget.grid(padx=5, pady=5)

  return frame

def create_submit_button_subframe(container):
  frame = ttk.Frame(container)

  frame.columnconfigure(0, weight=1)

  ttk.Button(frame, text="Login", command=create_invoice).grid(column=0, row=0, sticky=tk.W)

  for widget in frame.winfo_children():
      widget.grid(padx=5, pady=5)

  return frame

def create_invoice_frame(container):
  frame = ttk.Frame(container)

  frame.columnconfigure(0, weight=1)

  create_products_subframe(frame).grid(column=1, row=0)
  create_services_subframe(frame).grid(column=1, row=1)
  create_submit_button_subframe(frame).grid(column=1, row=2)

  for widget in frame.winfo_children():
    widget.grid(padx=5, pady=5)

  return frame

create_menu_frame(root).grid(column=0, row=0)
create_details_frame(root).grid(column=1, row=0)
create_invoice_frame(root).grid(column=2, row=0)

Customer = { # customer details, as a dictionary
    "Company_Name": customer_company,
    "Handler_Name": customer_handler_name,
    "Handler_Email": customer_handler_email,
    "Address_1": customer_address_1,
    "Address_2": customer_address_2
}


root.mainloop()