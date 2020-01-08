
lucky_numbers = [42, 4, 8, 15, 16, 23]
friends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)           #list friend will be added with lucky_numbers
friends.append("Creed")         #Creed will be added to the list
friends.insert(1, "Kelly")      #Kelly will be added to the second position of the list
friends.remove("Jim")       #Jim will be removed from the list
print(friends.index("Kevin"))       #it will print out the index position of the kevin
print(friends.count("Jim"))         #it will print out the cont of Jim element of the list
lucky_numbers.sort()      #it will sort the list in ascending order
print(friends)
lucky_numbers.reverse()     #it will reverse the list
friends2 = friends.copy()   #it will copy friends list to friends2
print(lucky_numbers)
print(friends2)
