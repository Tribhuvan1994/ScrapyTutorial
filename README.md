# ScrapyTutorial

This is a scrapy project for Data Acquisition Management System. Gone through scrapy tutorial online.

This project is used to extract data from the website and store in a database. For this project I have used SQLite database. We can also save the data in JSON, xml or csv file as required.

For scraping, a virtual environment is created and scraping project is started. A python library scrapy is also installed. 
>>>pip install scrapy

Start the project by activating the virtual environment
>>>virtualenvironment\Scripts\activate

Then create a scrapy project
>>>scrapy startproject scrapy-tutorial

For scraping we must follow the laws of scrapping, otherwise the website may ban our user or ip address our system. 

CSS selector
A css selector is scrapy element which helps to extract the element and text in the element of the page. We can also use XPath selector. 

The extracted data are stored in item containers. The items can then be stored as json, xml or csv file. 
To upload the data into database also we need the item containers.

To Bypass the user agent for scraping we can use allowed agents provided by google. Or use scrapy-user-agents library provided by scrapy.