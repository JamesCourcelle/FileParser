from operator import itemgetter
import parse_csv


class Bid():
    def __init__(self, bid):
        self.bid_id = int(bid["Auction ID"])
        self.title = bid["Auction Title"]
        self.fund = bid["Fund"]
        self.amount = bid["Auction Fee Total"]
        
        
class Node():
    def __init__(self, bid):
        self.right = None
        self.left = None
        self.bid = bid
        

class BinarySearchTree():
    def __init__(self):
        self.root = None 
    
    def add_node(self, bid):
        current_node = self.root
        new_node = Node(bid)
        
        while (current_node != None):
            if (new_node.bid.bid_id < current_node.bid.bid_id):
                #print("new_node is less than current_node")
                if (current_node.left == None):
                    current_node.left = new_node
                    current_node = None
                else:
                    current_node = current_node.left
            else:
                if (new_node.bid.bid_id > current_node.bid.bid_id):
                    #print("new_node is greater than current_node")
                    if (current_node.right == None):
                        current_node.right = new_node
                        current_node = None
                    else:
                        current_node = current_node.right
                

    def insert(self, bid):
        if self.root == None:
            self.root = Node(bid)
        else:
            self.add_node(bid)
   

def load_bids(csv_path, bst):
    print("Loading CSV file ")   
    list_bids = parse_csv.open_file(csv_path)
    sorted_list = sorted(list_bids, key=itemgetter("Auction ID"))
    
    try:
        for i in sorted_list:
            bid = Bid(i)
            print("Bid ID: %s, Item: %s, Fund: %s, Amount: %s" % (bid.bid_id, bid.title, bid.fund, bid.amount))
            bst.insert(bid)
               
    except IOError:
        print("An error occurred when trying to read the file")
        
    return bst
            
print()


check_bid = 98912
bst = BinarySearchTree()
csv_path = 'eBid_Monthly_Sales.csv'

load_bids(csv_path, bst)

# TODO: Need to figure out a way to load bids globally. Possible return or have function act at global scope.
print(bst.root.right.bid.bid_id)


