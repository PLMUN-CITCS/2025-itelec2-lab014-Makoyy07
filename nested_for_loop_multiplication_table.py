# Filename: nested_for_loop_multiplication_table.py

# Outer loop for rows (1 to 5)
for i in range(1, 6):
    # Inner loop for columns (1 to 5)
    for j in range(1, 6):  # Indent this loop!
        # Calculate the product
        product = i * j  # Indent this line!
        # Print the product with formatting
        print(f"{product:4}", end="")  # Indent this line!
    # New line after each row
    print()  # Indent this line!
