def roman_to_int(roman: str) -> int:
    # Dictionary to map Roman numerals to their respective integer values
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Initialize the total sum
    total = 0
    prev_value = 0

    # Loop through each character in the Roman numeral string
    for char in roman:
        current_value = roman_map[char]
        
        # If the current value is greater than the previous value, subtract the previous value twice (to undo the addition)
        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value

        # Update the previous value for the next iteration
        prev_value = current_value

    return total


# Example usage
roman_numeral = input("Enter a Roman numeral: ")
integer_value = roman_to_int(roman_numeral)
print(f"The integer value of {roman_numeral} is {integer_value}.")
