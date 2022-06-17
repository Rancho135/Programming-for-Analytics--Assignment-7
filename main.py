#****************************************************************
#Name: GOODNEWS GOODNEWS

#
#ANA1001 Lab 7
#****************************************************************

#Create a function that takes a list as an argument.

def my_function(foods):
  '''list of food i love to eat'''
  for food in foods:
    message = (f"I love to eat {food.title()}")
    print(message)
food_lists = ['chicken', 'rice', 'bagel']
my_function(food_lists)


#Create a function that takes arbitrary arguments *args.
def soup_list(*add_ons):
  '''print list of things i need to make a soup'''
  print("\n Items i need to make a soup: ")
  for add_on in add_ons:
    print(f" - {add_on}")
soup_list('fish', 'chicken')
soup_list('vegetable', 'salt','oil')


#Explain the difference between  **kwargs and *args and show an example (code is optional).
print("\nThe asterisk before the parameter *args tells python to make an empty tuple called args, \nwhile the double asterisk before the parameter **kwargs tells python to make an empty dictionary called kwargs.\n")

#Create a function with arbitrary keyword arguments **kwargs.
def build_profile(first, last, **info):
  '''A dictionary containing information about me'''
  info["first"] = first
  info["last"] = last
  return info
user = build_profile(first = "Goodnews", last = "Agbadu", college = "cambrian", hobbies = "Sports", location = "canada.")
print(user)


#Create a function that prints who is in space right now from within the function. Use the API from http://open-notify.org/Open-Notify-API/People-In-Space/. Print from within the function, don't return any value.
import requests
import json
people = requests.get('http://api.open-notify.org/astros.json')
results = json.loads(people.text)
#Create a function that takes arbitrary arguments *info
def build_profile(*info):
  '''print the list of people in space right now'''
  print("\nNames of people in space right now")
  for details in results['people']:
    print(details['name'])

build_profile()