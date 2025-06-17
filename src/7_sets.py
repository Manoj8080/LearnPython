#create set
my_set={1,2,3,4}
print(my_set)

#set operations
#add values
my_set.add(5)
print(my_set)

#remove
my_set.remove(4)
print(my_set)

#union, intersection and difference
#union operation combines two sets and return all unique elements
set1={3,4,5,6}
print(my_set|set1)

#intersection returns only the common elements
print(my_set&set1)

#difference returns elements in first set but not in second set
print(my_set-set1)
print(set1-my_set)