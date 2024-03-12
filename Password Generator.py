#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_letter_list = random.sample(letters,len(letters))
random_number_list = random.sample(numbers,len(numbers))
random_symbol_list = random.sample(symbols,len(symbols))


pw_letter_list = random_letter_list[0 : nr_letters]
pw_number_list = random_number_list[0 : nr_letters]
pw_symbol_list = random_symbol_list[0 : nr_symbols]

pw_list = pw_letter_list + pw_number_list + pw_symbol_list

random_pw_list = random.sample(pw_list, len(pw_list))
sum_of_character = nr_letters + nr_numbers + nr_symbols

for i in range(0,sum_of_character):
  print(random_pw_list[i],end='')
