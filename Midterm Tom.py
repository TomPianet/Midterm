#Q1

a = 10
a = a + 2
print(a*2)
a = 19
print(a+3)
a = 19 // 2




#Q3
import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)




#Q6

#LISTTT

list = [1, 2, 3]
print("Original list:", list)
list[1] = 102
print("Modified list:", list)
list.append(4)
print("List after adding an item:", list)
list.remove(102)
print("List after removing an item:", list)

#STRINGGG
string = "hello"
print("Original string:", string)

try:
    string[1] = 'a'
except TypeError as e:
    print("Error:", e)

new_string = string.replace("e", "a")
print("New string:", new_string)

print("Original string after attempts to modify:", string)







#Q7

import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

modified_numbers = ['XX' if num <= 50 else num for num in random_numbers]
listfin = ['XX' if num <= 50 else None for num in random_numbers]
listfin = [num for num in listfin if num is not None]

print(listfin)



#Q8

def is_valid_url(url):
    # define the function that is going to say if there is http or https and if not it's not an url
    if not (url.startswith("http://") or url.startswith("https://")):
        return False

    # basically, if there is no . it is not a url so it's false regarding the function
    if '.' not in url:
        return False

    # same mechanic, if there is a space, it's not an url
    if ' ' in url:
        return False

    return True


# Examples
print(is_valid_url("https://www.google.es"))  #  True
print(is_valid_url("www.youtube.com"))  # False
print(is_valid_url("https:   /   /  www.google.es"))  # False





#Q9


def days_since_birthday(birthday):
    birthborn = int(birthday.split('-')[2])

    yearnow = 2024

    years_passed = yearnow - 1 - birthborn

    days = years_passed * 365

    leap_years = 0
    for year in range(birthborn + 1, yearnow):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years += 1

    days += leap_years

    return days

# Example usage
birthday = "21-06-2004"
print("Days since birthday:", days_since_birthday(birthday))



#Q10

def count_pattern_occurrences(text):
    # we input the function
    count = 0

    # The length of the text to avoid re-computing it
    text_length = len(text)

    # The length of the pattern end ("jeb") to use for substring comparison
    pattern_end_length = len("jeb")

    # Loop through each character in the text
    for i in range(text_length):
        # Check if the current character is 'C'
        if text[i] == 'C':
            # Loop through the remaining text to find "jeb"
            for j in range(i, text_length):
                # If we find a substring that ends with "jeb", increase the count
                if text[j:j + pattern_end_length] == "jeb":
                    count += 1
                    break

    #to know that you have how many occurences
    return count


#try now
text = "Here is a Cexamplejeb and here is another Cnotjeb and one more Ctestjeb."
matches = count_pattern_occurrences(text)
print(f"Number of matches: {matches}")
