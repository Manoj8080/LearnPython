# break : exits the loop immediately
movies=['inception','interstellar','the matrix','titanic']
print(movies)
for i in movies:
    print("now watching", i)
    if i=='the matrix':
        print("stop")
        break

# continue : skips the current iteration and moves to next
dishes=['pasta','curry','spicy noodles','salad']
for dish in dishes:
    if "spicy" in dish:
        print("skipping",dish)
        continue
    print("eating ",dish)

# pass : does nothing, uses as placeholder for future logic
tasks=['clean','skip','hehe']
for task in tasks:
    if task=='skip':
        pass
    else:
        print("doing task",task)

