def centralizar(root):
    

    width = 1043
    height = 453

    screen_width = root.winfo_screenwidth() 
    screen_height = root.winfo_screenheight()

    x = (screen_width/2) - (width/2)

    y = ((screen_height/2) - (height/2)) -50

    return root.geometry('%dx%d+%d+%d' % (width, height, x, y))