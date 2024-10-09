import os # os integration library
from dotenv import load_dotenv # .env usage library
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator # invoice generation library
from InvoiceGenerator.pdf import SimpleInvoice # invoice printing pdf manipulation library
import time # library for  dates & times

load_dotenv() # load the .env file


# Get values from .env file
Provider_Name = os.getenv('Provider_Name')
Provider_Logo_Path = os.getenv('Provider_Logo_Path')
Provider_Contact_Phone_Number = os.getenv('Provider_Contact_Phone_Number')
Provider_Contact_Email = os.getenv('Provider_Contact_Email')
Provider_Contact_Address = os.getenv('Provider_Contact_Address')
Provider_Bank_Account_Number = os.getenv('Provider_Bank_Account_Number')
Provider_Bank_Sort_Code = os.getenv('Provider_Bank_Sort_Code')
Creator_Name = os.getenv('Creator_Name')
Currency = os.getenv('Currency')
Currency_Code = os.getenv('Currency_Code')
Language = os.getenv('Language')

Current_Date = time.strftime("%m-%d-%Y")

Client_Company = str(input("Client Company Name: "))
client = Client(Client_Company) # set up client instance
provider = Provider(Provider_Name, bank_account=Provider_Bank_Account_Number, bank_code=Provider_Bank_Sort_Code) # set up provider instance
creator = Creator(Creator_Name) # setup creator

invoice = Invoice(client, provider, creator)
invoice.currency_locale = 'en_US.UTF-8'

def getitems():
    while True:
        #get input values
        Current_Item_Name = str(input("Name of Item to add (leave blank to stop adding items): "))
        if Current_Item_Name != '': # if a Item has been provided, add it, else finish item section
            Current_Item_Number = int(input("How Many Items?: "))
            Current_Item_Price = str(float(input(f"What is the price per item? (In {Currency}xxx.xx): ")))
            Current_Item_Tax = str(float(input("Tax % (Leave empty if not tax): ")))
            print("\n")
            if Current_Item_Tax != '': #if Tax has been provided, add item with tax, else add without tax
                invoice.add_item(Item(Current_Item_Number, Current_Item_Price, description=Current_Item_Name, tax=Current_Item_Tax))
            else:
                invoice.add_item(Item(Current_Item_Number, Current_Item_Price, description=Current_Item_Name))
        else: # if not item provided, break while loop
            break


getitems() # get the items as inputs
pdf = SimpleInvoice(invoice) # setup pdf invoice instance
pdf.gen(f"{Provider_Name}-Invoice-{Current_Date}.pdf", generate_qr_code=True) # generate invoice