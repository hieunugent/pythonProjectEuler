from art import logo1
import os
#HINT: You can call clear() to clear the output in the console.
print(logo1)
bids = {}
bid_finish = False
def find_highest_bidder(bidding_record):
    highest_bid =0
    winner=""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if int(bid_amount) > int(highest_bid):
            highest_bid = bid_amount
            winner = bidder
    print(winner + "is winner with $"+ str(highest_bid))
        
while not bid_finish:
    name = input("what is your name ? ")
    price = input("what is your Bid price? $")
    bids[name] = price
    shouldcontinue = input(" do you want to continue yes /no ?").lower()
    if shouldcontinue == 'no':
        bid_finish= True
        find_highest_bidder(bids)
    elif shouldcontinue == 'yes':
        print("print this")
        os.system('clear')


    


