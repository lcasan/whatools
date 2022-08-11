def window_position(root, width, height):
    x = root.winfo_screenwidth() // 2 - width // 2
    y = root.winfo_screenheight() // 2 - height // 2
    position = str(width) + "x" + str(height) + "+" + str(x) + "+" + str(y)
    
    return position          