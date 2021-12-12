# # # print("Hello World")
# # counties = ["Arapahoe","Denver","Jefferson"]
# counties.append("El Paso")
# print(counties)
# print(counties[1:])
# counties_tuple = ("Arapahoe","Denver","Jefferson")
# print(counties_tuple[:2])
# type_three = type(3)
# print(type_three)
# ballots = 1,341
# print(ballots)
# print(type(ballots))
# print(type(73.81))
# print(type("Hello World"))
# print(type(True))
# print(type('True'))
# print(5 + 2 * 3)
# print(8 // 5 - 3)
# print(8 + 22 * 2 - 4)
# print(16 - 3 / 2 + 7 - 1)
# print(3 ** 3 % 5)
# print(5 + 9 * 3 / 2 - 4)
# voting_data = [
#     {'county': 'Arapahoe', 'registered_voters': 422829}, 
#     {'county': 'Denver', 'registered_voters': 463353}, 
#     {'county': 'Jefferson', 'registered_voters': 432438}
# ]
# voting_data.insert(1, {'county': 'El Paso', 'registered_voters': 461149})
# print(voting_data)

# voting_data.remove( {'county': 'Arapahoe', 'registered_voters': 422829})
# print(voting_data)

# voting_data[2] = {'county': 'Denver', 'registered_voters': 463353}
# voting_data[1] = {'county': 'Jefferson', 'registered_voters': 432438}
# print(voting_data)

# voting_data.append({'county': 'Arapahoe', 'registered_voters': 422829})
# print(voting_data)

# score = int(input("What is your test score? "))
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict:
#     print(county)

# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict:
#     print(counties_dict[county])

# for county in counties_dict:
#     print(counties_dict.get(county))
# Import the datetime class from the datetime module.
# import datetime

# # Use the now() attribute on the datetime class to get the present time.
# now = datetime.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

import csv
dir(csv)