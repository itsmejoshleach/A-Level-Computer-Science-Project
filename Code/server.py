from flask import Flask, render_template
import os # os integration library
from dotenv import load_dotenv # .env usage library
from datetime import date, timedelta, time # library for  dates & times

load_dotenv() # load the .env file
app = Flask(__name__)

# Get values from .env file
#Creator_Name = os.getenv('Creator_Name')
Currency = os.getenv('Currency')
#Currency_Code = os.getenv('Currency_Code')



Provider = { # Provider details, as a dictionary
    "Name": os.getenv('Provider_Name'),
    "Contact_Phone_Number": os.getenv('Provider_Contact_Phone_Number'),
    "Contact_Email": os.getenv('Provider_Contact_Email'),
    "Address_1": os.getenv('Provider_Contact_Address_1'),
    "Address_2": os.getenv('Provider_Contact_Address_2'),
    "Bank_Account_Number": os.getenv('Provider_Bank_Account_Number'),
    "Bank_Sort_Code": os.getenv('Provider_Bank_Sort_Code')
}

Customer = { # customer details, as a dictionary
    "Company_Name": "TestCustomer",
    "Handler_Name": "Jeff Goodwell",
    "Address_1": "AnotherFakebuilding, AnotherFakeRoad",
    "Address_2": "AnotherFakeTown, AnotherFakeCountry, AnotherFakePostcode",
    "Handler_Email": "hello@TestCustomer.com"
}

ProductItems = [ # items, as a dictionary (subtotals blank at this point)
    {
        'title': 'Product1',
        'charge_per_item': '30.00',
        'item_number': '10',
        'tax': '15',
        'subtotal': ''
    },
    {
        'title': 'Product2',
        'charge_per_item': '45.00',
        'item_number': '12',
        'tax': '20',
        'subtotal': ''
    },
    {
        'title': 'Product3',
        'charge_per_item': '52.00',
        'item_number': '5',
        'tax': '10',
        'subtotal': ''
    }
]
ServiceItems = [
    {
        'title': 'Service1',
        'charge_per_item': '30.00',
        'item_number': '10',
        'tax': '15',
        'subtotal': ''
    },
    {
        'title': 'Service2',
        'charge_per_item': '45.00',
        'item_number': '12',
        'tax': '20',
        'subtotal': ''
    },
    {
        'title': 'Service3',
        'charge_per_item': '52.00',
        'item_number': '5',
        'tax': '10',
        'subtotal': ''
    }
]

Invoice_Number = "000001" # invoice number

def percentageof(percentage, number): # provide percentage and whole, returns calculated answer, e.g. percentageof(4,100) will return 4
    percent_calc = (int(percentage) * int(number)) / 100
    return int(percent_calc)

def findsubtotals(Items): # populate the Items instance with subtotals for each Product
    for item in Items:
        running_subtotal = 0
        subtotal_with_tax, subtotal_without_tax = 0,0 # reset temp subtotals to 0
        subtotal_without_tax = float(item['charge_per_item']) * float(item['item_number']) # charge per item times by number of items gives tax-free subtotal
        subtotal_with_tax = subtotal_without_tax + percentageof(item['tax'], subtotal_without_tax) # use function to calculate percentage and add it on top of subtotal
        item['subtotal'] = int(subtotal_with_tax)
        #running_subtotal = running_subtotal + int(subtotal_with_tax) # add to running subtotal
    #return running_subtotal
    return 200

def findtotal(Items): # find the overall total of all items (including tax)
    running_total = 0
    for item in Items: # for each item
        total_with_tax, total_without_tax = 0,0 # reset temp totals to 0
        total_without_tax = float(item['charge_per_item']) * float(item['item_number']) # charge per item times by number of items gives tax-free total
        total_with_tax = total_without_tax + percentageof(item['tax'], total_without_tax) # use function to calculate percentage and add it on top of total
        running_total = running_total + int(total_with_tax) # add to running total
    return running_total

def formatdate(Unformatted_Date): # give it a YYYY-MM-DD date and it returns a DD-MM-YYYY date
    Date_Formatted = str(Unformatted_Date).split("-") # becomes, YYYY,MM,DD
    Year = Date_Formatted[0]
    Month = Date_Formatted[1]
    Day = Date_Formatted[2]
    Date_Formatted = f"{Day}-{Month}-{Year}"
    return Date_Formatted

def getcurrentdate(): # get a DD-MM-YYYY date
    Current_Date = date.today()
    Current_Date_Formatted = formatdate(Current_Date)
    return Current_Date_Formatted

def getduedate(daystilldue): # get due date when given days from now in form DD-MM-YYYY
    Current_Date = date.today()
    Due_Date = Current_Date + timedelta(daystilldue)
    Due_Date_Formatted = formatdate(Due_Date)
    return Due_Date_Formatted

@app.route('/') # on main page '/' render the invoice template
def hello_world():
    findsubtotals(ProductItems) # populate the subtotals
    findsubtotals(ServiceItems) # populate the subtotals
    overalltotal = findtotal(ProductItems) + findtotal(ServiceItems)
    return render_template('invoice.html',
                           Date=getcurrentdate(), # Pass through current date
                           Invoice_Number = Invoice_Number, # PAss through invoice number
                           Due_Date=getduedate(14), # pass through Due date (14 days from current date)
                           Provider=Provider, # pass through provider details
                           Customer=Customer, # pass through customer details
                           ProductItems=ProductItems,
                           ServiceItems=ServiceItems,
                           Total=overalltotal, # pass through total
                           Currency=Currency # pass through currency sign
    ) # render html template with all variables passed through

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port)