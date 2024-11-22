def calculator(a, b, operator):
    # Handle addition
    if operator == "+":
        return a + b
    
    # Handle subtraction
    elif operator == "-":
        return a - b
    
    # Handle multiplication
    elif operator == "*":
        return a * b
    
    # Handle division
    elif operator == "/":
        if b == 0:  # Prevent division by zero
            return "undefined"  # Or return None if preferred
        return a / b
    
    # Handle modulus
    elif operator == "%":
        if b == 0:  # Prevent modulus by zero
            return "undefined"  # Or return None if preferred
        return a % b
    
    # Handle greater than comparison
    elif operator == ">":
        return a > b
    
    # Handle greater than or equal comparison
    elif operator == ">=":
        return a >= b
    
    # Handle less than comparison
    elif operator == "<":
        return a < b
    
    # Handle less than or equal comparison
    elif operator == "<=":
        return a <= b
    
    # Handle invalid operator
    else:
        return "invalid operator" 


def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def winning_numbers(ticket, drawn_numbers):
    match_count = 0
    for num in ticket:
        if num in drawn_numbers:
            match_count += 1
    
    if match_count == 3:
        return "First"
    elif match_count == 2:
        return "Second"
    elif match_count == 1:
        return "Third"
    else:
        return "No"
    
def are_anagrams(str1, str2):
    """
    This function checks if two strings are anagrams of each other.

    Parameters:
    ----------
    str1 : str
        The first string to be compared.
    str2 : str
        The second string to be compared.

    Returns:
    -------
    bool:
        Returns True if the two strings are anagrams, otherwise False.

    Example:
    --------
    are_anagrams("listen", "silent")  # Output: True
    are_anagrams("hello", "world")    # Output: False
    """

    # Function implementation here ...

    str1 = str1.lower()
    str2 = str2.lower()

    # Check if the sorted characters of both strings are equal
    output = sorted(str1) == sorted(str2)


    return output

def calculate_average(numbers):
    """
    This function calculates the average of a list of numbers using a for loop.

    Parameters:
    ----------
    numbers : list
        A list of numerical values (int or float).

    Returns:
    -------
    float:
        The average of the numbers in the list. If the list is empty, returns None.

    Example:
    --------
    calculate_average([10, 20, 30, 40, 50])  # Output: 30.0
    """
    
    # Function implementation here ...

    if not numbers:  # Handle empty list case
        return None

    total_sum = 0
    count = 0

    # Iterate through the list to calculate sum and count
    for num in numbers:
        total_sum += num
        count += 1

    # Calculate average
    average = total_sum / count

    return average

def calculate_weekly_pay(hours_worked):
    """
    Calculate the weekly pay for an employee based on the number of hours worked.
    
    Parameters:
    hours_worked (int): The total number of hours worked by the employee in a week.
    
    Returns:
    float: The total weekly pay.
    """
    regular_rate = 12  # £12 per hour for up to 35 hours
    overtime_rate = 18  # £18 per hour for hours worked beyond 35 hours
    standard_hours = 35  # Threshold for regular pay



    # Function implementation here ...

    if hours_worked <= standard_hours:
        # No overtime, all hours paid at regular rate
        total_pay = hours_worked * regular_rate
    else:
        # Regular pay for standard hours + overtime pay for extra hours
        overtime_hours = hours_worked - standard_hours
        total_pay = (standard_hours * regular_rate) + (overtime_hours * overtime_rate)



    return total_pay

def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """
    


    # Function implementation here ...
    output = True #setting the default to true as i assume the number input is a prime

    # Handle edge cases
    if num <= 1:
        output = False
    elif num <= 3:
        output = True
    else:
        # Check divisibility by 2 or 3
        if num % 2 == 0 or num % 3 == 0:
            output = False
        else:
            # Loop through numbers up to the square root of num
            for i in range(5, int(num**0.5) + 1, 6):
                if num % i == 0 or num % (i + 2) == 0:
                    output = False
                    break  # remove from the loop as soon as a divisor is found


    return output


def sum_of_evens(min_value, max_value):
    
    """Find the sum of even numbers between two given numbers (inclusive).

    Args:
        min_value (int): Minimum number
        max_value (int): Maximum number

    Returns:
        total: sum of the even numbers between min_value and max_value

    Example:

    min_value = 10
    max_value = 13
    total = sum_of_evens(min_value, max_value)
    print(total) # total is 22.

    """



    # Function implementation here ...

    total = 0  # Initialize total sum

    # Iterate through all numbers between min_value and max_value (inclusive)
    for number in range(min_value, max_value + 1):
        # Check if the number is even
        if number % 2 == 0:
            total += number
    
    
    return total

def celsius_to_fahrenheit(celsius):
   # complete your function implementation... 
   output = (9 / 5) * celsius + 32

   return output

def decrypt_cypher_text(encrypted_text, key):
    """
    Decrypts an encrypted text using a given key.

    Parameters:
    ----------
    encrypted_text : str
        The text to be decrypted.
    key : int
        The key used to decrypt the text.

    Returns:
    -------
    str:
        The decrypted text as a single string.
    
    Example:
    --------
    encrypted_text = "Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu$"
    key = 3
    decrypt_cypher_text(encrypted_text, key)
    # Output: "Face error you make in programming is an opportunity to become a better developer."
    """
    
    # function implementation here...
    decrypted_text = ""  # Initialize an empty string to store the decrypted text.

    for char in encrypted_text:
        # Convert the character to its ASCII code, subtract the key, and find the remainder modulo 256.
        decrypted_ascii = (ord(char) - key) % 256
        # Convert the ASCII code back to a character.
        decrypted_char = chr(decrypted_ascii)
        # Append the decrypted character to the decrypted_text string.
        decrypted_text += decrypted_char
        
    return decrypted_text

def find_maximum_difference(a, b):
    # code implementation here...

    # get the first for each
    min_a = a[0]
    max_a = a[0]
    min_b = b[0]
    max_b = b[0]

    # Loop through list a to find the minimum and maximum values
    for num in a:
        if num < min_a:
            min_a = num
        if num > max_a:
            max_a = num

    # Loop through list b to find the minimum and maximum values
    for num in b:
        if num < min_b:
            min_b = num
        if num > max_b:
            max_b = num

    # Calculate the differences manually
    difference1 = max_a - min_b
    difference2 = max_b - min_a

    # Find the larger of the two differences manually
    if difference1 > difference2:
        maximum = difference1
    else:
        maximum = difference2
    
    return maximum

def fuel_cost(distance_miles):
#     # Constants
    MPG = 50  # Miles per gallon
    LITERS_PER_GALLON = 4.5
    PRICE_PER_LITER = 1.49  # Price in pounds per liter
#     continue function implementation here...
    total_cost = PRICE_PER_LITER * distance_miles * LITERS_PER_GALLON / MPG
    
    return total_cost

def is_golden_number(n):
    # function implementation ...
    boolean = False  # Initialize the boolean variable

    for a in range(1, n):  # Iterate through all possible values of a
        b = n - a  # Calculate b such that n = a + b
        if b > 0 and (a * b) % 1000 == 0:  # Check the conditions
            boolean = True  # Set to True if conditions are met
            break  # Exit the loop as we found a valid pair

    return boolean

def km_to_miles(kilometers):
    # complete function implementation here...

    miles_per_kilometer = 0.62

    # Convert kilometers to miles
    miles = kilometers * miles_per_kilometer

    # rounding to 3 decimal places
    miles = int(miles * 1000 + 0.5) / 1000.0

    return miles

def letter_occurrence(input_string):
    # complete function implementation...
    count = 0

    # Loop through each character in the string
    for char in input_string:
        # Compare the character with 'a' and 'A'
        if char == 'a' or char == 'A':
            count += 1

    return count

def annual_net_income(gross_salary):
    # complete your function implementation here...
    tax_rate = 0

    # Determine tax rate based on gross salary
    if gross_salary >= 45000:
        tax_rate = 50 / 100  # Equivalent to 50%
    elif 30000 <= gross_salary < 45000:
        tax_rate = 30 / 100  # Equivalent to 30%
    else:
        tax_rate = 15 / 100  # Equivalent to 15%

    # Calculate net salary
    net_salary = gross_salary * (1 - tax_rate)

    return net_salary