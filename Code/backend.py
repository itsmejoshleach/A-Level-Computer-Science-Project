from flask import Flask, render_template, send_file, request
import os # os integration library
from dotenv import load_dotenv # .env usage library
from datetime import date, timedelta, time # library for dates & times
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json
import requests
import pdfkit # HTML -> pdf

load_dotenv() # load the .env file
app = Flask(__name__)

# Get values from .env file
Currency = os.getenv('Currency')

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
        total_with_tax = total_without_tax + percentageof(item['tax'], total_without_tax) # use function to calculate percentage and add it on top of subtotal
        running_total = running_total + total_with_tax
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

def getpostdata(request): # return data based on web request
    data = request.json
    print(f"[LOG] - request (json) (string) (\" -> \'): {request}")
    print(f"[LOG] - request (json) (string) (\" -> \') (json.loads): {data}")

    # Create provider and customer dictionaries based on the form input
    Provider = {
        "Name": data['Provider']['Name'],
        "Contact_Phone_Number": data['Provider']['Phone_Number'],
        "Contact_Email": data['Provider']['Email'],
        "Address_1": data['Provider']['Address_1'],
        "Address_2": data['Provider']['Address_2'],
        "Bank_Account_Number": data['Provider']['Bank_Account_Number'],
        "Bank_Sort_Code": data['Provider']['Bank_Sort_Code'],
        "Logo_Path": data['Provider']['Logo_Path']
    }

    Customer = {
        "Company_Name": data['Customer']['Company_Name'],
        "Handler_Name": data['Customer']['Handler_Name'],
        "Handler_Email": data['Customer']['Handler_Email'],
        "Address_1": data['Customer']['Address_1'],
        "Address_2": data['Customer']['Address_2']
    }

    # Get the product and service items
    #ProductItems = data.getlist('ProductItems[]')
    ProductItems = []
    for item in data['ProductItems']:
        ProductItems.append(item)

    #ServiceItems = data.getlist('ServiceItems[]')
    ServiceItems = []
    for item in data['ServiceItems']:
        ServiceItems.append(item)

    InvoiceNumber = data['InvoiceNumber']

    print(f"Got Post Data: {Provider, Customer, ProductItems, ServiceItems, InvoiceNumber}")
    return Provider, Customer, ProductItems, ServiceItems, InvoiceNumber

@app.route('/posttest', methods=['POST']) # Accept only POST requests
def posttest():
    if request.method == 'POST':
        print(f"[LOG] - POST Request Received")
        print(f"\n [LOG] - Print request: {request}")
        print(f"\n [LOG] - Print request (json): {request.json}")
        Provider, Customer, ProductItems, ServiceItems, InvoiceNumber = getpostdata(request)
        # Do the rest of the calculations (subtotals, total)
        findsubtotals(ProductItems)
        findsubtotals(ServiceItems)
        overalltotal = findtotal(ProductItems) + findtotal(ServiceItems)
        
        print(f"Date: {getcurrentdate()}")
        print(f"Invoice Number: {InvoiceNumber}")
        print(f"Due Date: {getduedate(14)}")
        print(f"Provider Details: {Provider}")
        print(f"Customer Details: {Customer}")
        print(f"Product Items: {ProductItems}")
        print(f"Service Items: {ServiceItems}")
        print(f"Overall Total Calculated: {Currency}{overalltotal}")
        print("\n")

        print(f"Request: \n {request.json}")
        return request.json, 200
    else:
        return 400

@app.route('/gettestinvoice', methods=['GET', 'POST'])
def gettestinvoice():
    if request.method == 'POST':
        test_json_payload = request.json
        #test_json_payload = json.loads(test_payload)
        print("[LOG] - POST Payload chosen to forward")
    elif request.method == 'GET':
        with open('template_request.json') as file:
            test_payload = json.load(file)
        test_json_payload = json.loads(test_payload)
        print("[LOG] - GET chosen, template data chosen to forward")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    request_URL = 'http://127.0.0.1:8080/invoicedata'
    response = requests.post(request_URL, json=test_json_payload, headers=headers)
    data_response - response.json()
    print(f"[LOG] - response: {response}")
    print(f"[LOG] - response (json()): {data}")
    return data, 200

@app.route('/getinvoicehtml', methods=['POST']) # Accept only POST requests, returns HTML data for invoice
def getinvoicehtml():
    print(f"[LOG] - POST Request Received")
    Provider, Customer, ProductItems, ServiceItems, InvoiceNumber = getpostdata(request)
    # Do the rest of the calculations (subtotals, total)
    findsubtotals(ProductItems)
    findsubtotals(ServiceItems)
    overalltotal = findtotal(ProductItems) + findtotal(ServiceItems)

    invoice_html_data = render_template('invoice.html',
                            Date=getcurrentdate(),
                            Invoice_Number=InvoiceNumber,
                            Due_Date=getduedate(14),
                            Provider=Provider,
                            Customer=Customer,
                            ProductItems=ProductItems,
                            ServiceItems=ServiceItems,
                            Total=overalltotal,
                            Currency=Currency)
    return invoice_html_data, 200

@app.route('/writeinvoicepdf', methods=['POST'])
def writeinvoicepdf():
    Provider, Customer, ProductItems, ServiceItems, InvoiceNumber = getpostdata(request)
    # Do the rest of the calculations (subtotals, total)
    findsubtotals(ProductItems)
    findsubtotals(ServiceItems)
    overalltotal = findtotal(ProductItems) + findtotal(ServiceItems)

    invoice_html_data = render_template('invoice.html',
                            Date=getcurrentdate(),
                            Invoice_Number=InvoiceNumber,
                            Due_Date=getduedate(14),
                            Provider=Provider,
                            Customer=Customer,
                            ProductItems=ProductItems,
                            ServiceItems=ServiceItems,
                            Total=overalltotal,
                            Currency=Currency)
    #htmltopdf(invoice_html_data, 'invoice.pdf')
    return "Generating PDF", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)