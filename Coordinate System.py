x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

# To find which Quadrant the point lies in

if x>0:
    if y>0:

        # x is greater than 0, y is greater than 0

        print("Quadrant 1")

    else:

        # x is greater than 0, y is less than 0

        print("Quadrant 4")

else:
    if y>0:

        #x is less 0, y is greater than 0

        print("Quadrant 2")

    else:

        #x is less than 0, y is less than 0

        print("Quadrant 3")
