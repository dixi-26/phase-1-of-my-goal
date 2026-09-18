total_cart_value=float(input("enter"))
VIP=input("are you a VIP?(yes/no)")
VIP_status=(VIP=="yes")
discount=0
if total_cart_value>100:
    discount=total_cart_value*0.1
    if VIP_status=="yes":
        remaining_value=total_cart_value-discount
        discount=discount+(remaining_value*0.05)
else:
    print("no discount")
final_cart=total_cart_value-discount
standard_shipping=80
if final_cart>80 or VIP=="yes":
    standard_shipping=0
else:
    standard_shipping=80
print(discount)
print(final_cart)
print(standard_shipping)


     