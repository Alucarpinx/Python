# Collection of numbers
positive = []
negative = []
# Loop while keepGoing is true
while True:
    value = float(input("Please enter a positive or negative number (enter a zero to end): "))
    
    if value == 0:
        break  # Exit the loop if the user inputs zero
     # If positive, add to positive collection
    if value > 0:
        positive.append(value)
    # If negative, add to negative collection
    elif value < 0:
        negative.append(value)

# Output two collections
print("Positive Values Entered:", positive)
print("Negative Values Entered:", negative)