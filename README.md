# FileParser
Simple app that takes in a .csv file and provides search and sort methods using various common algorithms.

## ---Current Tasks---



## ---Completed Tasks---
* Create a way to read in the file in a usable way.
   Added the ability to read a .csv file in using the DictReader method. This returned a list of dictionaries   
   for each bid. A print_bid method was added to print the bid ID, title, fund, and amount.   
   
* Create a Bid class to hold the bid ID, title, fund and amount.
* Ensure that a bid from the .csv file can be loaded into an instance of the Bid class.
   Added Bid class that loads in a bid ID, title, fund, and amount for each bid in the .csv file.   
   Completed ability to iterate over a list of bids to check if the list of bid IDs matches an ID number passed in.   
   (Updated file to start reading eBid_Monthly_Sales.csv as this is larger. It required changing dictionary keys as they   
   are different in this file.)   