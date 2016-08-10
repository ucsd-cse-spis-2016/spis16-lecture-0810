from PIL import Image

def drawings():
    pic = Image.open("butterfly.jpg")

   
    for x_col in range(pic.size[0]):
        for x_row in range(pic.size[1]):
            (r,g,b)= pic.getpixel((x_col,x_row))
            if (r+g+b)/3 < 25:
                pic.putpixel( (x_col, x_row), (255, 0, 0))


    

        
    pic.show()


drawings()

# Draw a horizontal line across the picture on row 100
# Generalize this so that it works for any picture
# Draw another horizontal line that ends in the middle of the picture
# Draw 4 horizontal lines on rows 100, 200, 300, 400 (Try again with nested loops)
# Draw a grey horizontal bar covering the top 100 rows 
# Draw a grey vertical bar covering the first 100 columns
# Cover the whole picture in grey
# Cover the top half of the picture in grey
# Cover the top left quadrant in grey
# Cool effects: increase the red content by 50%


