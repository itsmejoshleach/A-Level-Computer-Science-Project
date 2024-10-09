# A Level Computer Science Coursework

## What I'm making:
I'm making a python-based invoicing software based around Sole-Traders.



## Setup
Install the required python packages: ```python -m pip install -r requirements```


## Template Design:
### These are the variables available to you for invoice template design:

```{{Invoice_Number}}``` - Invoice ID Number
```{{Date}}`` - Current Date (DD-MM-YYYY)
```{{Due_Date}}``` - Current Date + 14 Days (DD-MM-YYYY)
```{{Currency}}``` - Currency Symbol (e.g. £, $, €)
```{{Total}}`` - Total Cost

#### Provider:
  ```{{Provider['Name']}}``` - Provider Name
  ```{{Provider['Logo_Path']}}``` - Provider Logo Image Path
  ```{{Provider['Contact_Email']}}``` - Provider Contact Email
  ```{{Provider['Contact_Phone_Number']}}``` - Provider Contact Phone Number
  ```{{Provider['Address_1']}}``` - Provider Address (1st Line)
  ```{{Provider['Address_2']}}``` - Provider Address (2nd Line)
  ```{{Provider['Bank_Account_Number']}}``` - Provider Bank Account Number
  ```{{Provider['Bank_Sort_Code']}}``` - Provider Bank Sort Code


#### Customer:
  ```{{Customer['Company_Name']}}``` - Customer Company Name
  ```{{Customer['Handler_Name']}}``` - Customer Account Handler Name
  ```{{Customer['Handler_Email']}}``` - Customer Account Handler Email
  ```{{Customer['Address_1']}}``` - Customer Address (1st Line)
  ```{{Customer['Address_2']}}``` - Customer Address (2nd Line)

#### Item:
  ```{{Item['title']}}``` - Title Of Product/Service
  ```{{Item['charge_per_item']}}``` - Cost Of 1 Item
  ```{{Item['item_number']}}``` - Number Of Items In Order
  ```{{Item['tax']}}``` - Tax (%)
  ```{{Item['subtotal']}}``` - (Charge Per Item * Item Number) + Tax% for each Item

  Example of a for loop, to show all items:
  ```
  {% for Item in Items %}
      <tr class="item">
        <td>
          {{Item['title']}}
        </td>
        <td>
          {{Currency}}{{Item['charge_per_item']}}
        </td>
        <td>
          {{Item['item_number']}}
        </td>
        <td>
          {{Item['tax']}}%
        </td>
        <td>
          {{Currency}}{{Item['subtotal']}}
        </td>
      </tr>
      {% endfor %}
  ```