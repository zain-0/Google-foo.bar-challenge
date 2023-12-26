def function( x,y ):
    # Calculate the difference between the sum of elements in list x and the sum of elements in list y
    uniqueInteger = sum(x) - sum(y)
    # Compare the lengths of lists x and y
    if len(x) > len(y):
    # If the length of list x is greater, return the calculated uniqueInteger
        return uniqueInteger
    else:
    # If the length of list y is greater or equal, return the negation of uniqueInteger
        return -1 * uniqueInteger

#inputList = [[5, -2, 10, -7, 3, -1,2],[5, -2, 10, -7, 3, -1]]
#print(function(inputList))
