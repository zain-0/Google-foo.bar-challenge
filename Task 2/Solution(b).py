def solution(x, y):
    # Calculate the difference between y and 1
    y_difference = y - 1
    
    # Calculate the corner value based on x and y_difference
    corner = x + y_difference
    
    # Calculate the id using the corner value
    id = int(corner * (corner + 1) / 2)
    
    id = id - y_difference

    return str(id)
