from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
total_bids = {}


print(logo)
print("Welcome to the secret auction program.")
def auction():
  start = True
  highest_bid = 0
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  other = input("Are there any other bidders? Type \"yes\" or \"no\".\n").lower()
  total_bids[name] = bid
  if other == "yes":
    clear()
    auction()
  elif other == "no":
    while start:
      for key in total_bids:
          if highest_bid < total_bids[key]:
            highest_bid = total_bids[key]
          elif highest_bid == total_bids[key]:
            clear()
            print(f"Congrats {key}! You have won with a bid of ${total_bids[key]}!! ")
            start = False
      
  else:
    print("Please make sure you typed it right and try again :)")
    
auction()