import parse_csv


list_bids = parse_csv.open_file('eBid_Monthly_Sales_Dec_2016.csv')

for bid in list_bids:
    parse_csv.print_bid(bid)
