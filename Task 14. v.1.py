#The author of the code: https://github.com/Agurkoff
"""
Programming tutorial: M.V. Sysoeva, I.V. Sysoev.
Programming for "normal" ones from scratch in Python part 1.
Task on function.
========================================================================================================================
    Task №14.
    Description:
Solve the problem of online commerce.
Several buyers have made purchases in the online store throughout the year.
For each purchase, the name of the buyer was recorded (string)and the amount spent (real).
Write a function that calculates for each customer and outputs in the form of a dictionary by
to all customers (of the form name: value) one of the following parameters:
1. number of purchases;
2. the average purchase amount;
3. the maximum purchase amount;
4. the minimum purchase amount;
5. the total amount of all purchases.
The function input is passed:
• either 2 lists, in the first of which the names of buyers (may be repeated), in the second - the amount of purchases;
• either 1 list consisting of pairs of the form (name, amount);
• either a dictionary in which names are used as keys, and as values - lists with amounts.
========================================================================================================================
"""


# The function "def change" constantly asks the person whether he is a customer of the store or not.
def change(change_one):
    print("Do you want to buy something in our store?")
    print("Yes or No?")
    change_one = str(input())
    return change_one


# The function "def name_client" asks for the person's name, if he is a customer of the store (or if you entered "yes").
# And sends data to the "dictionary_clients" function.
def name_client():
    print("What is your name?")
    name = str(input())
    return name


# The function "def money_client" asks the client, how much money he spent.
# And sends data to the "dictionary_clients" function.
# It is also possible to correct the error, if you entered an incorrect value. In the form of "try / except"
def money_client():
    global money
    print("How much money did you spend?")
    try:
        money = float(input())
    except ValueError:
        print("Incorrectly entered value 'money'! \nPlease enter the value correctly!")
        money_client()
    return money


# The function "def dictionary_clients", which takes values from the function "def name_client" and "def money_client".
# The created dictionary receives data, where: "name" = key, "money" = value.
# In the created list, I write down all the "money" values that were entered by the customers of the store.
def dictionary_clients(name, money, list_of_all):
    list_of_all.append(money)
    dict[name] = money
    return dict, list_of_all


# Main code.
dict = {}  # A dictionary is created.
list_of_all = []  # A list is created.
change_one = str()
while "yes" in change(change_one):
    dictionary_clients(name_client(), money_client(), list_of_all)
else:
    print("Good bye!")
print(dict)
# print(list_of_all)  Checking how list works.
print('Number of purchases - ', len(list_of_all), '\nThe minimum number of purchase - ', min(list_of_all),
      '\nThe maximum number of purchase - ', max(list_of_all), '\nThe total amount of all purchases - ',
      sum(list_of_all), '\nThe average purchase amount - ', round(sum(list_of_all) / len(list_of_all), 2))
