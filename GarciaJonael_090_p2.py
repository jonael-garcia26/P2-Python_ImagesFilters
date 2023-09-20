import copy

def imcopy(image):
    image_copy = []

    for i in image:
        row = []
        for j in i:
            row.append(j)
        image_copy.append(row)

    return image_copy






'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is an inverted version of the input image. That is to say each 
    pixel's grayscale value should be inverted relative to the maximum value of 255.
'''
def invert(image):
    new_image = imcopy(image)
    Lr = len(new_image)
    Lc = len(new_image[0])

    for r in range(0,Lr):
        for c in range(0,Lc):
            new_image[r][c] = 255 - new_image[r][c]
    return new_image

'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a blurred version of the input image. The blur function 
    uses a weighted kernel which is applied the pixels centered on 
    image[i][j]. The value in the kernel is multiplied by the corresponding
    pixels in the image and the eighted average is used as new_image[i][j].
'''
def blur(image):
    new_image3 = imcopy(image)
    new_new_image3 = imcopy(image)
    Lr = len(new_image3)
    Lc = len(new_image3[0])

    kernel = [
        [1, 1, 1],
        [1, 7, 1],
        [1, 1, 1],
    ]
    total_wheights = (
        kernel[0][0] + kernel[0][1] + kernel[0][2] +
        kernel[1][0] + kernel[1][1] + kernel[1][2] +
        kernel[2][0] + kernel[2][1] + kernel[2][2])

    for y in range(0, Lr):
        for x in range(0, Lc):
            if y == 0 or y == len(new_image3) - 1 or x == 0 or x == len(new_image3[y]) - 1:
                new_new_image3[y][x] = 0
            
            else:
                weighted_sum = (
                  new_image3[y - 1][x - 1] * kernel[0][0] + new_image3[y - 1][x] * kernel[0][1] +
                  new_image3[y - 1][x + 1] * kernel[0][2] + new_image3[y][x - 1] * kernel[1][0] +
                  new_image3[y][x] * kernel[1][1] + new_image3[y][x + 1] * kernel[1][2] +
                  new_image3[y + 1][x - 1] * kernel[2][0] + new_image3[y + 1][x] * kernel[2][1] +
                  new_image3[y + 1][x + 1] * kernel[2][2])

                weighted_average = weighted_sum // total_wheights
                new_new_image3[y][x] = weighted_average
    return new_new_image3

'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a vertically flipped version of the input image. 
'''
def flip(image):

    new_image2 = imcopy(image)
    
    new_image2.reverse()

    return new_image2

'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a 2x2 tiled version of the input image. The tile function
    will group pixels in groups of 4 and map each one to one of the 4 tiles
    based on their relative position in the group. That is to say in 
    [[1, 2],
     [3, 4]]
    the number 1 will be in the top left tile, 2 in the top right tile, 
    and so on. Because nearby pixels are similar this will create an image 
    which loops like 4 copies of the same image but slightly different.

    To make the transformation, consider 4 pixels in each iteration 
    of the loop and map them to the corresponding tiles. Each tile will be
    half the length and half the width of the input image.
'''
def tile(image):
    new_image4 = imcopy(image)


    new_new_image4 = []
    Lr = len(new_image4)
    Lc = len(new_image4[0])

    tile1 = []
    for r in (range(0,Lr,2)):
        row1 = []
        for c in range(0,Lc,2):
            row1.append(new_image4[r][c])
        tile1.append(row1)
  

    tile2 = []
    for r in (range(0,Lr,2)):
        row2 = []
        for c in range(1,Lc,2):
            row2.append(new_image4[r][c])
        tile2.append(row2)

    
    tile3 = []
    for r in (range(1,Lr,2)):
        row3 = []
        for c in range(0,Lc,2):
            row3.append(new_image4[r][c])
        tile3.append(row3)


    tile4 = []
    for r in (range(1,Lr,2)):
        row4 = []
        for c in range(1,Lc,2):
            row4.append(new_image4[r][c])
        tile4.append(row4)


    for r in range(len(tile1)):
        tilesum = tile1[r] + tile2[r]
        new_new_image4.append(tilesum)
    for r in range(len(tile1)):
        tilesum2 = tile3[r] + tile4[r]
        new_new_image4.append(tilesum2)



    return new_new_image4














