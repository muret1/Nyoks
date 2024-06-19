courses = ["computer science","IT","BIT","software engineering",]
print(courses)
# accessing an element in an array
print(courses[2])

# Looping through an array
for x in courses:
    print(x)
    # adding a new element into an array
    courses.append("Datascience")
    print(courses)

    #deleting ana element
    courses.remove("IT")
    print(courses)