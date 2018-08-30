from operator import itemgetter
import parse_csv


class Bid():
    def __init__(self, bid):
        self.bid_id = int(bid["ArticleID"])
        self.title = bid["ArticleTitle"]
        self.fund = bid["Fund"]
        self.amount = bid["WinningBid "]
        
        
class Node():
    def __init__(self, bid):
        self.right = None
        self.left = None
        self.bid = bid
        

class BinarySearchTree():
    def create_tree(self, bid_list, start, end):
        if start >= end:
            return None
            
        midpoint = int((start + end) / 2)
        print("Start is", start)
        print("Midpoint is", midpoint)
        print("End is", end)
        root = Node(Bid(bid_list[midpoint]))
        
        root.left = self.create_tree(bid_list, start, midpoint-1)
        print("Hit complete end on left side")
        root.right = self.create_tree(bid_list, midpoint+1, end)
        print("Hit complete end on right side")
        
        return root
        

def load_bids(csv_path):
    print("Loading CSV file ")   
    list_bids = parse_csv.open_file(csv_path)
    sorted_list = sorted(list_bids, key=itemgetter("ArticleID"))
    bst = BinarySearchTree()
    start = 0
    end = len(sorted_list)
    
    
    try:
        bst.create_tree(sorted_list, start, end)      
    except IOError:
        print("An error occurred when trying to read the file")
        
    return bst
    
print()


check_bid = 98912
csv_path = 'eBid_Monthly_Sales_Dec_2016.csv'

load_bids(csv_path)
