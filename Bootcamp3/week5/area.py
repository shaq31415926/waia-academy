def calc_area(height, width):
    """Function to calculate the area of the rectangle"""
    print(f"The height is {height}")
    print(f"The width is {width}")

    area = height * width
    area = round(area, 2)

    return area


# specify the height and width
h = 78
w = 8.765

area = calc_area(h, w)
print(f"The area of the rectangle is {area} cm2")
