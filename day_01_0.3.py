customer_age=int(input("Enter age:"))
ticket_price=0
if customer_age<12:
   ticket_price="$5"
elif customer_age>=65:
   ticket_price="$7"
else:
    ticket_price="$17"
print("Ticket price:",ticket_price)

