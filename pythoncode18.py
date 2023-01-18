'''Given two lists a, b. Check if two lists have at least one element common in them. Examples:

Input : a = [1, 2, 3, 4, 5]
        b = [5, 6, 7, 8, 9]
Output : True

Input : a=[1, 2, 3, 4, 5]
        b=[6, 7, 8, 9]
Output : False'''

def common(list1, list2):

    result = False

    for x in list1:
 
        for y in list2:

            if x == y:

                result = True

                return result 

    return result


a = [1, 2, 3, 4, 5]

b = [5, 6, 7, 8, 9]

print(common(a, b))
 

a = [1, 2, 3, 4, 5]

b = [6, 7, 8, 9]

print(common(a, b))