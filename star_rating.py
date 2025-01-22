#Star Rating Validation - www.101computing.net/flowchart-to-python-code-star-rating-validation/

star_rating = -1

while star_rating < 0 or star_rating > 5:
    
    star_rating = int(input("enter a star rating between 0 and 5"))
    
print("Thank you!")