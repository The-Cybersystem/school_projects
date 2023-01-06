# This is mostly a demonstration of detailed comments #

def palindrome_number(x): # Function definition and parameter
  is_palindrome = False # Default value for the indicator is false
  x = str(x)
  x_rev = x[slice(None, None, -1)] # Create a reverse string by stepping back 1 by 1 using the whole string and storing as x_rev for check
  if x == x_rev: # If the string is the same as it is when reversed
    is_palindrome = True # Indicator is True
    response =f"Input: x = {x}\nOutout: {is_palindrome}\nExplination: Reads {x_rev} from right to left. From from left to right, it reads {x}.\n" # Prints data and explaination of th einput number if the number is a palidrome
  else:
    response =f"Input: x = {x}\nOutout: {is_palindrome}\nExplination: Reads {x_rev} from right to left. From from left to right, it reads {x}. Therefore it is not a palindrome.\n" # Prints data and explaination of th einput number if the number is not a palidrome
  return response # exits the function and returns a value to whatever called the function (in this case it's to the print statement)

print(palindrome_number(121)) # Calls function passing 121 # True
print(palindrome_number(-121)) # Calls function passing -121 # False
print(palindrome_number(10)) # Calls function passsing 10 # False
print("----------------------") # Seperator from the main output
print(palindrome_number(input("Enter a number: "))) # User can check any number
