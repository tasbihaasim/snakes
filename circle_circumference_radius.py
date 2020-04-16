import math
def circle_circumference_radius(list, area):
    '''
    args:
    list: radius_list – The list of radii of circles (arranged in ascending order)
    area: circle_area – Given area of a circle
    -------------
    Search for the circle whose area is equivalent to the circle_area .
    ---------------
    Return:
    Calculate its circumference
    and return
    it.

    '''
    
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        circle_area = round(math.pi * (list[midpoint]) ** 2, 2)
        if circle_area == area:
            return round(2 * math.pi * list[midpoint], 2)
        else:
            if area < circle_area:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return -1
