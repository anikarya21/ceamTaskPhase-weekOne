import random

input_list = [] #The list which contains the intial inputs

for i in range(5): #Loops to get the initial inputs and add it to the input_list[]
    add_row = []
    for j in range(5):
        add_col = []
        for k in range(3):
            add_col.append(random.randint(0, 255))
        add_row.append(add_col)
    input_list.append(add_row)

def display(input_list_display,row=5,column=5): #DISPLAY MATRIX FUNCTION
    output_list_pixel = []
    for i in range(3):

        if(i==0): print("RED")
        elif(i==1): print("GREEN")
        else: print("BLUE")

        print()
        
        for j in range(row):
            for k in range(column):
                print(input_list_display[j][k][i], end = " ")
            print()
            print()
    print()
    print()
    return 0

def inverse(input_list_inverse): #INVERSE FUNCTION
    output_list_pixel = []
    for i in range(5): 
        row = []
        for j in range(5):
            col = []
            for k in range(3):
                col.append(255 - input_list_inverse[i][j][k])
            row.append(col)
        output_list_pixel.append(row)
    return output_list_pixel

def brightness(input_list_brightness, brightness_value): #BRIGHTNESS FUNCTION
    output_list_pixel = []
    for i in range(5):
        row = []
        for j in range(5):
            col = []
            for k in range(3):
                col.append(min(input_list_brightness[i][j][k] + brightness_value, 255))
            row.append(col)
        output_list_pixel.append(row)
    return output_list_pixel

def contrast(input_list_contrast, contrast_value): #CONTRAST FUNCTION
    output_list_pixel = []
    for i in range(5):
        row = []
        for j in range(5):
            col = []
            for k in range(3):
                if (contrast_value * (input_list_contrast[i][j][k] - 128) + 128 > 0):
                    col.append(min(contrast_value * (input_list_contrast[i][j][k] - 128) + 128, 255))
                else:
                    col.append(0)
            row.append(col)
        output_list_pixel.append(row)
    return output_list_pixel

def thresholding(input_list_thresholding, threshold_value, low = 255, high = 0): #THRESHOLDING FUNCTION
    output_list_pixel = []
    for i in range(5):
        row = []
        for j in range(5):
            col = []
            for k in range(3):
                if (input_list_thresholding[i][j][k] > threshold_value):
                    col.append(low)
                else:
                    col.append(high)
            row.append(col)
        output_list_pixel.append(row)
    return output_list_pixel

def flip_vertical(input_list_flip_vertical): #FLIP VERTICAL FUNCTION
    output_list_geometry = []
    for i in range(5):
        row = []
        for j in range(4, -1, -1):
            col = []
            for k in range(3):
                col.append(input_list_flip_vertical[i][j][k])
            row.append(col)
        output_list_geometry.append(row)
    return output_list_geometry

def flip_horizontal(input_list_flip_horizontal): #FLIP HORIZONTAL FUNCTION
    output_list_geometry = []
    for i in range(5):
        row = []
        for j in range(5):
            col = []
            for k in range(3):
                col.append(input_list_flip_horizontal[4-i][j][k])
            row.append(col)
        output_list_geometry.append(row)
    return output_list_geometry

def transform(input_list_transform): #TRANSFORM FUNCTION
    output_list_geometry = []
    for i in range(5):
        row = []
        for j in range(5):
            col = []
            for k in range(3):
                col.append(input_list_transform[j][i][k])
            row.append(col)
        output_list_geometry.append(row)
    return output_list_geometry

def rotate_90(input_list_rotate_90): #ROTATE 90 FUNCTION
    output_list_geometry = []
    function_transform_rotate_90 = transform(input_list_rotate_90)
    output_list_geometry = flip_horizontal(function_transform_rotate_90)
    return output_list_geometry

def rotate_180(input_list_rotate_180): #ROTATE 180 FUNCTION
    output_list_geometry = []
    output_list_geometry = flip_vertical(input_list_rotate_180)
    output_list_geometry = flip_horizontal(output_list_geometry)
    return output_list_geometry

def rotate_270(input_list_rotate_270): #ROTATE 270 FUNCTION
    output_list_geometry = []
    function_transform_rotate_270 = transform(input_list_rotate_270)
    output_list_geometry = flip_vertical(function_transform_rotate_270)
    return output_list_geometry  

def crop(input_list_crop, row, column): #CROP FUNCTION
    output_list_geometry = []
    for i in range(row):
        row = []
        for j in range(column):
            col = []
            for k in range(3):
                col.append(input_list_crop[i][j][k])
            row.append(col)
        output_list_geometry.append(row)
    return output_list_geometry

print("The input image is: ")

display(input_list) #Display the input image first

user_pixel = input("Enter (inverse, brightness, contrast, thresholding): ") #Enter the function the user wants to perform on the matrix image
print()
print()

if (user_pixel == "inverse"): #THIS IS FOR THE PIXEL FUNCTIONS AND ALGORITHMS
    display(inverse(input_list))
elif (user_pixel == "brightness"):
    user_brightness = int(input("Enter the brightness value: "))
    print()
    print()
    display(brightness(input_list, user_brightness))
elif (user_pixel == "contrast"):
    user_contrast = int(input("Enter the contrast value: "))
    print()
    print()
    display(contrast(input_list,user_contrast))
elif (user_pixel == "thresholding"):
    user_thresholding = int(input("Enter the thresholding value: "))
    print()
    print()
    display(thresholding(input_list,user_thresholding))

user_geometry = input("Enter (flip, rotate, crop): ")
print()
print()

if (user_geometry == "flip"):
    user_flip = input("Vertical or Horizontal: ")
    print()
    print()
    if (user_flip == "Vertical"):
        display(flip_vertical(input_list))
    elif (user_flip == "Horizontal"):
        display(flip_horizontal(input_list))

elif (user_geometry == "crop"):
    user_geometry_crop = input("Enter the crop matrix: (a x b)")
    print()
    print()
    user_geometry_crop = user_geometry_crop.replace(" ","")
    user_row, user_column = int(user_geometry_crop.split("x")[0]), int(user_geometry_crop.split("x")[1])
    display(crop(input_list, user_row, user_column),user_row,user_column)

elif (user_geometry == "rotate"):
    user_rotate = int(input("Enter the rotation value: (90, 180, 270): "))
    print()
    print()
    if (user_rotate == 90):
        display(rotate_90(input_list))
    elif (user_rotate == 180):
        display(rotate_180(input_list))
    elif (user_rotate == 270):
        display(rotate_270(input_list))

#EDGE DETECTION

output_list_edge_contrast = []
total = 0

def edgeDetection(input_list_edgeDetection):
    user_contrast_edgeDetection = int(input("Enter the contrast value: "))
    print()
    print()
    function_contrast_edgeDetection = contrast(input_list_edgeDetection,user_contrast_edgeDetection)

    total_mean = 0

    for i in range(5):
        for j in range(5):
            for k in range(3):
                total_mean += function_contrast_edgeDetection[i][j][k]

    total_mean = (total_mean / 25) * 1.35  #Anything above 100% total_mean and 35% more of total_mean

    function_contrast_thresholding = thresholding(function_contrast_edgeDetection, total_mean, "*", " ")

    for i in range(5):
        row = []
        for j in range(5):
            if (function_contrast_thresholding[i][j] == "*" and (i == 0 or i == 4) and (j != 0 and j != 4)):
                row.append("-")
            elif (function_contrast_thresholding[i][j] == "*" and (j == 0 or j == 4) and (i != 0 and i != 4)):
                row.append("|")
            elif (function_contrast_thresholding[i][j] == "*"):
                row.append("*")
            else:
                row.append(" ")
        output_list_edge_contrast.append(row)
    return output_list_edge_contrast

user_edge = input("Do you want to identify edges and borders also? (Y/N): ")
print()
print()

if (user_edge == "Y"):
    display(edgeDetection(input_list))
