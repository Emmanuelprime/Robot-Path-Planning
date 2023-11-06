from PIL import Image, ImageDraw

width_of_grid = 400
height_of_grid = 400

white_color = 255

# Create a blank white image
maze_image = Image.new("L", (width_of_grid, height_of_grid), white_color)

# Create a drawing context
draw = ImageDraw.Draw(maze_image)

# Define the size of each cell
cell_size = 40

# Create walls and objects (black cells)
for x in range(0, width_of_grid, cell_size):
    for y in range(0, width_of_grid, cell_size):
        draw.rectangle([x, y, x + cell_size, y + cell_size], fill=0)  # 0 represents black



# Save the maze image as a PNG file
maze_image.save("maze.png")
