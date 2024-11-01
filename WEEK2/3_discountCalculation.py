print("What is the price!");
price = int(input("The price is: "))
# priceInt = int(price);
print("What is the discount!");
discount = int(input("The discount percentage is: "))
# discountInt = int(discount); 

print("The actual price is: ", (price-(price*discount/100)));