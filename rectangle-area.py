import math
class GeometryCalculator:

    def calculate_rectangle_area(self, length, width):

        return length * width

if __name__ == "__main__":
    

    calculator = GeometryCalculator()

    width = 6
    length = 8

    print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length, width)}")
