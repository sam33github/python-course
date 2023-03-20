friends=["sam","arun","muthuvel","karthi","maran","ashok"]
friends_2=["am","aru","muthu","kathi","maan","asok"]
lucky_numbers=[2,4,8,5,7,1,0]
print(friends,lucky_numbers)

friends.append("muthuvel")
print(friends)

friends.insert(1,"karthi")
print(friends)

friends.remove("sam")
print(friends)

friends.extend(lucky_numbers)
print(friends)

friends.pop()
print(friends)

print(friends.index("arun"))

print(friends.count("muthuvel"))

lucky_numbers.sort(reverse=True)
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends_2=friends.copy()
print(friends_2)
 
 