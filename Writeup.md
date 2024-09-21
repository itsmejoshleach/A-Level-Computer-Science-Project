# A Level Computer Science Project Writeup

---
---

# Analysis:
## Problem Identification

I am going to make a **Invoice software** app named **“reddere”** which is latin, so adds sophistication and is pronounceable by many languages as many languages are latin derived. This will be a software that you can enter products and/or services into and it will **calculate and display as a PDF** invoice, which can **later be emailed** to the client.

I will use computational methods such as, **decomposition** to break down the code, so it’s simpler and easier to understand the sections I need to create. I will do this by breaking down the frontend and backend and emailing system into different files. I will use kivy which helps to compartmentalize a modular design and make it easier to create and understand the layout, and the code for future use.

Another computational method i will be using is **Abstraction.** This method will be used to remove all extra information, for example background images, and it means I can focus on completing the app and then adding in the additional functions afterwards. Removing unnecessary information and functions.

I will also use methods like the **Trial and Error approach** to complete my project, as finding what works and what doesn’t will make my life easier moving forward.

I will use methods of **Client feedback** to ensure that the app I am creating is the app that is wanted by the **Stakeholders** as getting my target audience involved will help make the app better.

- The problem is the lack of Invoice Software that is available open source and is easy to install and run. I am building a python-based Invoice creation app that has PDF functionality.
- I will use decomposition to break down the app into sections, modularization to compartmentalize the project into different segments. I will use Trial and Error for creating the app components, allowing them to be tested in different scenarios.

## Stakeholders

This app is aimed at Sole Traders and small business owners who need a simple and easy to use UI to complete simple invoicing tasks. It can ofc be used by bigger businesses that do not require many functions, but require an app that works well for invoicing. However the aim will be 1->5 people companies that want simplicity. I will create tutorials to help those of all ages, from experienced company owners to young teenagers just starting out. The backgrounds and icons will be simple and openly sourced, making the UI functional and removing the need for me to create artwork and / or find colours that work (I am colourblind). This also allows it to be simple and not distracting.

- This is aimed at Sole Traders and small business owners, it will target UK based companies, due to tax calculations and locale limits. The requirements are that of a low footprint app that doesn’t take up lots of space on a device. It Primarily targets Windows Computers.

## Research

In my app, the user needs to enter products and services and use templates to format a document, I have included some similar apps and services that do this, and have given me inspiration for my solution.

> Invoicehome is a mobile and browser-based invoicing software that is easy to use and has simple templates for you to fill in with forms. The downsides are that it limits the number of invoices you can create behind a paywall, which doesn’t work for bigger companies, or Sole Traders with many invoices needed to be created. It requires a login and is hard to customise the branding and colours of the templates. The upsides are that it is cloud-based and therefore can be accessed from anywhere, and that it can do quotes alongside invoices. The main upside is the use of templates so that all you need to do is fill out the forms with your data and it will populate the template. From this i would take the ability to create quotes, and the idea of templates is good, but I would want more customisable templates or custom templates all together. I definitely don’t want to include the paywalls but the ability to email from within the software may be nice to include.
>
> ![InvoiceHome Demo.png](./img/InvoiceHome%20Demo.png)


> Canva is a browser based design software that uses drag and drop sections for design, I like this as I could use it for the template editing, an upside to this is that it is easy to customize the template, but a downside of Canva is the need for a browser and the internet being consistent to create something, so i would take from this that i need to create a system that does not constantly rely on an internet connection to create an invoice, only needing it to send it out if wanted. I would include the ability to add images and text boxes, and the usage of templates. I wouldn’t include the account, and limits on the creation of images and decals.
> 
> ![Canva Demo.png](./img/Canva%20Demo.png)

> Photopea is a free, web-based image editor designed to mimic the functionality of Adobe Photoshop, offering tools for tasks like photo editing, graphic design, and web graphics creation. The interface closely resembles Photoshop, making it familiar for experienced users. Accessible directly from the browser without installation, Photopea provides a powerful alternative for professionals and hobbyists, with both free and premium features.
>
> ![Photopea Demo.jpg](./img/Photopea%20Demo.jpg)

Essential Features:

- The software needs to have the ability to create PDF invoices, that can then be sent to clients.
- It must be easy to use as an app.
- It must have the ability to add branding, and/or customize the look of the invoice
- It must be able to invoice for products to for services.

Limitations:

- The software may only be able to export the PDF, not necessarily send it from within the app.
- It may not be able to be ported to Mobile Devices for use.
- It won’t be able to directly take payments

Hardware & Software Requirements:

My software will need a CPU to do the processing, Primary Storage, such as RAM, for storing the program, Secondary Storage for storage of data.

Software; Python isn’t needed to run the app. As it will made into an executable. But a browser will be required to download the app.

---
---

# TLA Design

## Decompose the problem
  User Interface:
  - Input forms (customer info/branding, Product/Service details)
  - View Invoices
  - Generate Invoices
  - Edit/Update Invoice Details
  - Navigation Menu (Home, Settings, Invoice History)

  Invoice Management:
  - Create Invoice
    - Generate unique invoice ID
    - Add Products / Services
    - Add Customer Details
  - Save Invoice
  - Update Invoice
  - Delete Invoice

  Product / Service Management:
  - Add New
  - Update (Pricing, description)
  - View
  - Delete

  Reporting:
  - Generate invoice reports (total sales, outstanding payments)
  - Filter reports by date, customer or product
  - export reports (PDF, CSV)

  Settings:
  - Configure Tax Rates
  - Customise template
  - Currency settings


## Design of Structure
> ### Flowchart:
> ![Design - Flowchart](./img/Design%20-%20Flowchart.drawio.png)

> ### Create a decomposition diagram and explain and justify what you have done and why you have done it.
> ![Design - Decomposition Diagram](./img/Design%20-%20Decomposition%20Diagram.drawio.png)

> ### Create pseudocode of your program – you will probably do this. Explain what you have done and why you have done it. You will add pseudocode for your different versions for top marks.
> [Pseudocode.md](./Pseudocode.md)

> ### Sketch / draw screens of your game – (not actual game/program) / program and label
> ![App Sketch.png](./img/App%20Sketch.drawio.png)

## Usability Features

Create a list of usability features and justify the choices. E.g., The way the menu works, the display, the controls. Possible paragraphs you might have are: Navigation, consistency, user feedback, visual clarity, efficiency, flexibility and error prevention.

## Data Dictionary Table

| Variable name | Datatype | Description | Validation |
| --- | --- | --- | --- |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |

## Validation

Describe how you will enter that data entered is reasonable. E.g. restrictions the options they can choose from a menu, the data they can type in as a name, the control keys they can press.

## Iterative Test Table

List all the different ways you will check each version of your game works as it should.

An example is below, don’t copy this exactly.

| Test No. | What testing & why | How testing | Test data (What is entered) e.g. left key pressed | Expected result |
| --- | --- | --- | --- | --- |
| 1   | Menu – ensure they can start a new game | Typing menu option | 1   | A new game should load |

## Post Development Testing

Same table as above but this final testing including testing of each **success criteria** and each **usability feature** from design that you will test when the program is finished.