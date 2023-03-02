import sys


# as an example to run this code type python area.py 10 10

def area(height, width):
    area = height * width

    return area


height = int(sys.argv[1])
width = int(sys.argv[2])

print(f"The area is {area(height, width)}")
