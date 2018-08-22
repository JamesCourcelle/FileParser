import parse_csv


class Bid():
    def __init__(self):
        self.bid_id = ""
        self.title = ""
        self.fund = ""
        self.amount = 0.0

    def load_bid(self, bid):
        self.bid_id = int(bid["Auction ID"])
        self.title = bid["Auction Title "]
        self.fund = bid["Fund"]
        self.amount = bid["Auction Fee Total"]
		
		
list_bids = parse_csv.open_file('eBid_Monthly_Sales.csv')

new_list = []

for bid in list_bids:
    current_bid = Bid()
    current_bid.load_bid(bid)
    new_list.append(current_bid)
   
check_bid = 98912


# This code is used to test the check_bid to see if the bid ID matches any in the file. This type
# of search has a performance of O(N) and is directly proportional to the input data.
def contains_bid(bid_list, check):
    counter = 0         # Testing how many iterations it takes
    for bid in bid_list:
        if check(bid):
            counter += 1
            print("The count is %s" % counter)
            return True
        counter += 1
        print("The bid ID is %s and the count is %s" % (bid.bid_id, counter))
        
    return False

if contains_bid(new_list, lambda bid: bid.bid_id == check_bid):
    print("Bid was found")
else:
    print("Bid was not found")
        
	




'''my_bid = Bid()

my_bid.load_bid(list_bids[0])

parse_csv.print_bid(my_bid)'''
