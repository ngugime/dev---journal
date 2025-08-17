def calculate_discount(price, discount_percent):
    
    """Calculate the final price after applying discount if discount is 20% or more."""
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    return price

# Get user input
price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and display result
final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:
    print(f"The final price after a {discount_percent}% discount is: ${final_price:.2f}")
else:
   print(f"No discount applied. The price remains: ${final_price:.2f}")
 
