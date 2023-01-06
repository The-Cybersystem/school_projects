# Name: miles_to_km  |  Parameters: miles  | Purpose: Converts miles input to kilometers and rounds to 2 decimal places and prints to console
# Test Values: 3.1 miles = 4.99 km  |  100 miles = 160.93 km
def miles_to_km(miles):
  print(f'{miles} miles = {round(miles * 1.609344, 2)} km')


miles_to_km(3.1)  # 4.99 km
miles_to_km(100)  # 160.93 km


# Name: fahr_to_cel  |  Parameters: fahrenheit | Purpose: Converts fahrenheit input to celcius, rounds to 2 decimal places, and prints to console
# Test Values: 32F=0C  |  100F=37.78C
def fahr_to_cel(fahrenheit):
  print(f'{fahrenheit}F = {round((fahrenheit-32)*.5556,2)}C')


fahr_to_cel(32)  # 0C
fahr_to_cel(100)  # 37.78C


# Name: miles_per_hour  |  Parameters: miles, minutes  | Converts mph based on inputs of miles and minutes, rounds to 2 decimal places, and prints to console
# Test Values: 1 mile, 10 minutes = 6.00 mph  |  2.5 miles, 18 minutes = 8.33 mph
def miles_per_hour(miles, minutes):
  print(
    f'{miles} miles, {minutes} minutes = {round((miles/(minutes/60)),2)} mph')


miles_per_hour(1, 10)  # 6 mph
miles_per_hour(2.5, 18)  # 8.33 mph

# Name: XXX_to_English  |  Parameters: word
# Choose 5 words from a foreign lanugage of your choice. Create a function that will "convert" them from the foreign language to English. Include a "catch all" else statement that will state "Sorry, I don't recognize that word!" if a word is input that is not part of your progrmam's recognized words
def dutch_to_english(word):
  if word == 'Hallo':
    print(f"Dutch: {word}, English: Hello")
  elif word == 'Welterusten':
    print(f"Dutch: {word}, English: Good night")
  elif word == 'Ochtend':
    print(f"Dutch: {word}, English: Morning")
  elif word == 'Vliegtuig':
    print(f"Dutch: {word}, English: Airplane/Aircraft")
  elif word == 'Computertechnologie':
    print(f"Dutch: {word}, Enghlish: Computer science")
  else:
    print(f"Dutch: {word}, English: Sorry, I don't recognize that word!")

dutch_to_english('Hallo')
dutch_to_english('Welterusten')
dutch_to_english('Ochtend')
dutch_to_english('Vliegtuig')
dutch_to_english('Computertechnologie')
dutch_to_english('Brein')
