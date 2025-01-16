logo = r'''
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
print("WELCOME TO THE SECRET AUCTION\n")
resume=True
biddings={}
max_bid=0
max_bidder=""

while resume:
 name=input("what is your name? ")
 bid=int(input("what is your bid? "))
 biddings[name]=bid
 more=input("are there more bidders? y/n ")
 if more=='n':
     resume=False
     print("\n"*20)
 elif more=='y':
     print("\n"*20)
     
for i in biddings:
    if max_bid<biddings[i]:
      max_bid=biddings[i]
      max_bidder=i
      
print(f"\n\nthe bidding winner is {max_bidder} for ${max_bid}")      
      
   
 
