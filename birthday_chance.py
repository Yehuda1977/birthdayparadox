import datetime
from datetime import datetime as d
import random
import decimal

# This function finds a random date between 2017 and 2020, thereby including a leap year. 
def get_random_date():
    start = datetime.date(2017, 1, 1)
    end = datetime.date(2020, 12, 31)
    difference = end - start
    difference_days = difference.days
    random_number_of_days = random.randrange(difference_days)
    random_date = start + datetime.timedelta(days=random_number_of_days)
    
    return random_date    

# This function creates a list of random birthdays for N people 
def create_room_of_people(N):
    birthdays = []
    for i in range(0, N):
        birthdays.append(get_random_date())
   
    return birthdays

# This function checks a list of random birthdays to determine if 
# there are any matches for month and day
def check_room_for_matches(birthdays):
    match = False
    # create copy of list
    birthdays_copy = birthdays
    # Runs through all possible comparisons--N + N-1 + N-2... to find match
    # For example, if N is 23 there will be 253 comparisons/chances of finding a matching birthday
    while len(birthdays_copy) > 1 :
        for i in range(1, len(birthdays_copy)):
            if birthdays_copy[0].day == birthdays_copy[i].day:
                if birthdays_copy[0].month == birthdays_copy[i].month:
                    match = True
        birthdays_copy.pop(0)
  
    return match

# This function runs the simulation for a room of N people 
# and returns the chance of finding a match after X number of runs through the simulation
def chance_by_number_of_runs(N, runs):
    match_value = False
    match_true = 0
    match_false = 0
    
    for i in range(0, runs):
        list_of_birthdays_in_room = create_room_of_people(N)
        match_value = check_room_for_matches(list_of_birthdays_in_room)
        if match_value:
            match_true += 1
        else:
            match_false += 1

    return(match_true/runs)# returns chance of finding match

# This function runs the simulation until the desired level of accuracy is reached
# and then returns the chance of finding a birthday match with that level of accuracy
def chance_by_accuracy(N, accuracy):
    match_value = False
    match_true = 0
    match_false = 0
    accuracy_of_chance = 0
    runs = 0
    chance = 0
    # calculate the accuracy by finding the exponent and taking the absolute value
    desired_accuracy = abs(decimal.Decimal(str(accuracy)).as_tuple().exponent)
    # while loop will continue until desired accuracy is reached
    while accuracy_of_chance != desired_accuracy:
        list_of_birthdays_in_room = create_room_of_people(N)
        match_value = check_room_for_matches(list_of_birthdays_in_room)
        if match_value:
            match_true += 1
        else:
            match_false += 1
        runs += 1
        # calculate the chance of finding a birthday match
        chance = match_true/runs
        # calculate the accuracy of the current iteration by finding the exponent and taking the absolute value
        # this feeds back into the loop which terminates once desired accuracy matches the current accuracy
        accuracy_of_chance = abs(decimal.Decimal(str(chance)).as_tuple().exponent)
    return chance


################################################################
# Simulators 
################################################################

def runs_simulation(N, runs):
    chance = chance_by_number_of_runs(N, runs)
    print(f'Given N = {N} and the number of runs = {runs}')
    print(f'Given {N} people, the chance of at least two people having the same birthday is: {chance}.\n')

def accuracy_simulation(N, accuracy):
    chance = chance_by_accuracy(N, accuracy)
    print(f'Given N = {N} and the desired accuracy = {accuracy}')
    print(f'Given {N} people, the chance of at least two people having the same birthday is: {chance}.\n')

# Inputs are N and the number of runs
print('\n1. Inputs are N and the number of runs\n')
runs_simulation(23, 500)
runs_simulation(23, 5000)

# Inputs are N and the desired accuracy (e.g. 0.001)
print('\n2. Inputs are N and the desired accuracy (e.g. 0.001)\n')
accuracy_simulation(23, .001)
accuracy_simulation(23, .0001)

################################################################
# Sample output
################################################################
# 1. Inputs are N and the number of runs

# Given N = 23 and the number of runs = 500
# Given 23 people, the chance of at least two people having the same birthday is: 0.464.

# Given N = 23 and the number of runs = 5000
# Given 23 people, the chance of at least two people having the same birthday is: 0.5068.


# 2. Inputs are N and the desired accuracy (e.g. 0.001)

# Given N = 23 and the desired accuracy = 0.001
# Given 23 people, the chance of at least two people having the same birthday is: 0.625.

# Given N = 23 and the desired accuracy = 0.0001
# Given 23 people, the chance of at least two people having the same birthday is: 0.4375.
