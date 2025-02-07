"""
Author: Vu Anh Quan Tran
Assignment: #1
"""
gym_member = "Alex Alliton" #string
preferred_weight_kg = 20.5 #float
highest_reps = 25 #int
membership_active = True #bool

#workout_stats dictionary. Keys: (string) names of friends. Values: tuple (3 ints) containing minutes of yoga, running and weightlifting respectively
workout_stats = {
    "Alex": (30,45,20),
    "Jamie": (45, 50, 30),
    "Taylor": (60, 20, 0),
    "Darren": (10, 45, 10),
    "Will": (50, 50, 30)
}

#empty dictionary, to be merged with workout_stats
workout_stats_total = {}

for key,value in workout_stats.items(): #extract key (string) and value (int tuple)
    total_key = f"{key}_Total"
    total_val = 0
    for x in value:
        total_val = total_val + x
    workout_stats_total[total_key] = total_val

#merge original stats dict and total dict
workout_stats.update(workout_stats_total)

#nested list, each element is a list comprising of friend's name (string) and int list extracted from tuple, containing minutes of workout for each friend
workout_list=[]
for key, val in workout_stats.items():
    if type(val) is tuple: # this skips the workout totals
        a =list(val) #turns tuple to list
        a.insert(0, key)#add name of friend to appropriate list
        workout_list.append(a)

#print yoga and running time for ALL friends
for x in workout_list:
    print(f"{x[0]}'s yoga and and running minutes: {x[1:3]}")

#print weightlifting minutes of last two friends
print("\nWeightlifting minutes of last two friends:")
for x in workout_list[-2:]:
    print(f"{x[0]}: {x[-1]} minutes")
print("\n")

#check if any friend excercised at least 120 minutes and congratulate if so
for x in workout_list:
    total = sum(x[1:])
    if total >= 120:
        print(f"Great job staying active, {x[0]}!")

#get record of friend using user input
name = input("\nEnter name to see their exercise record: ")
if workout_stats.get(name, -1) == -1:
    print(f"Friend {name} not found in the records.")
else:
    values = list(workout_stats.get(name))
    name_total = name + "_Total"
    values.append(workout_stats.get(name_total))
    print(f"\n{name}'s record found!")
    print(f"Yoga minutes: {values[0]}")
    print(f"Running minutes: {values[1]}")
    print(f"Weightlifting minutes: {values[2]}")
    print(f"Total minutes: {values[3]}")

#Print highest and lowest total
total_names = []
total_list = []
for key, val in workout_stats_total.items():
    key = key.removesuffix("_Total")
    total_names.append(key)
    total_list.append(val)
highest_total = max(total_list)
lowest_total = min(total_list)
highest_friend = total_names[total_list.index(highest_total)]
lowest_friend = total_names[total_list.index(lowest_total)]
print(f"\nFriend with highest total workout minutes: {highest_friend} with {highest_total} minutes!")
print(f"Friend with lowest total workout minutes: {lowest_friend} with {lowest_total} minutes!")

