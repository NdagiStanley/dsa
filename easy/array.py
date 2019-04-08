"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


Level: Easy
"""

# Input - array of length 2 tuples
# Output - int

# Example:
# Input: [(30, 75), (0, 50), (60, 150)]
# Output: 2


def rooms(array):
    # create room for first entry
    # check if next entry needs a room
    # if not add no room
    # if so add room
    # check availability every time
    rooms = []
    for i in array:
        start, end = i[0], i[1]
        if i == array[0]:
            rooms.append([i for i in range(start, end + 1)])
        else:
            for j in rooms:
                # (0,50)
                if start not in j:
                    rooms.append([i for i in range(start, end + 1)])
                    break
                elif end not in j:
                    rooms.append([i for i in range(start, end + 1)])
                    break

    return rooms


result = rooms([(30, 75), (0, 50), (60, 150)])
print([i for i in result])
