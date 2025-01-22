# Discount Price Calculator - www.101computing.net/discount-price-calculator/

price = int(input("enter the price of your item"))
discount_rate = int(input("enter the percentage discount"))

discount = price*discount_rate/100

discounted_price = price - discount

print("the price before = ", price)
print("discount = ", discount_rate)
print("price ofter discount = ", discounted_price)