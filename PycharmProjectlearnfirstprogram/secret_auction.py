import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bidding_finished=False

def find_highest_bidder(bidding_record):
 highest_bid = 0
 #bidding_record= {"angela" :123 , "james":312}
 for bidder in bidding_record:
      bid_amount= bidding_record[bidder]
      if bid_amount>highest_bid:
       highest_bid=bid_amount
       winner = bidder
      print(f"the winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
 bids = {}
 name=input("what is your name?:")
 price= int( input("what is your bit?:$"))
 bids[name]=price
 should_continue= input("are there any other bidders? type 'yes' or 'no'. ")
 if should_continue=="no":
   bidding_finished=True
   find_highest_bidder(bids)
 elif should_continue=="yes":
  os.system('cls' if os.name == 'nt' else 'clear')


