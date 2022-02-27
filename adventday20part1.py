#input data- read files
rawdata = open("C:\codingstuff\day20input.txt")
datastring = rawdata.read()
rawdata.close()
testdataraw = open("C:\codingstuff\day20testinput.txt")
testdatastring = testdataraw.read()
testdataraw.close()

#input data- list of strings
datalines = datastring.split("\n\n")
testlines = testdatastring.split("\n\n")

#---------what data am i testing----------
data= datalines

image_enhancement_algorithm= data[0]
input_image= data[1].split("\n")



# ---part 1-----------------
import numpy as np

#because the picture field is infinite, add a margin of ten pixels before and after.
picture_grid = np.zeros((len(input_image)+20, len(input_image[0])+20), dtype=int)
picture_grid_1= np.zeros((len(input_image)+20, len(input_image[0])+20), dtype=int)
picture_grid_2= np.zeros((len(input_image)+20, len(input_image[0])+20), dtype=int)



def gridpopulator (input_image, output_grid):
    for y, string in enumerate(input_image):
        for x, value in enumerate(string):
            if value == "#":
                output_grid[y+10, x+10] = 1

gridpopulator(input_image, picture_grid)

def image_enhancer (input_picture_grid, output_picture_grid, enhancement_algorithm):
    for index, value in np.ndenumerate(input_picture_grid):
        y= index[0]
        x= index[1]
        if y > 0 and y < input_picture_grid.shape[0]-1 and x > 0 and x < input_picture_grid.shape[1]-1:
            binary_string= ""
            binary_string += str(input_picture_grid[y - 1, x - 1])
            binary_string += str(input_picture_grid[y - 1, x])
            binary_string += str(input_picture_grid[y - 1, x + 1])
            binary_string += str(input_picture_grid[y, x - 1])
            binary_string += str(input_picture_grid[y, x])
            binary_string += str(input_picture_grid[y, x + 1])
            binary_string += str(input_picture_grid[y + 1, x - 1])
            binary_string += str(input_picture_grid[y + 1, x])
            binary_string += str(input_picture_grid[y + 1, x + 1])
            try:
                if enhancement_algorithm[int(binary_string, 2)] == "#":
                    output_picture_grid[y,x] = 1
            except IndexError:
                pass

image_enhancer(picture_grid, picture_grid_1, image_enhancement_algorithm)

image_enhancer(picture_grid_1, picture_grid_2, image_enhancement_algorithm)

#because of the infinite size constraints. the edges won't be wiped clear properly, so discard the outermost few  rows by indexing them out
print("total light pixels after 2 enhancements:" , np.sum(picture_grid_2[3:-3, 3:-3]))