import pygame

def input_G_code ():
    parameter_list = ['', '', '', '', '']
    g_list = []
    file = open('G-codes.txt', 'r')
    for line in file:
        g_list += [line]
    for i in range (0, len(g_list)-1):
        g_list[i] = g_list[i][0:-1]
    file.close()
    for i in range (0, len(g_list)):
        g_line = g_list[i]
        g_command = g_line.split(' ')[0]
        if g_command == 'G00':
            parameter_list[0] = g_line.split(' ')[1][1:]
            parameter_list[1] = g_line.split(' ')[2][1:]
        if g_command == 'G01':
            parameter_list[2] = g_line.split(' ')[1][1:]
            parameter_list[3] = g_line.split(' ')[2][1:]
            parameter_list[4] = g_line.split(' ')[3][1:]
    return parameter_list


def Visual (coord_list):
    pygame.init()
    display_width = 800
    display_height = 600
    display = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Visualization')
    done = False
    clock = pygame.time.Clock()
    black = (0,0,0)
    white = (255, 255, 255)
    display.fill(white)
    coord_list1 = ['', '', '', '', '']
    coord_list1[0] = coord_list[0]
    coord_list1[1] = display_height - int(coord_list[1])
    coord_list1[2] = coord_list[2]
    coord_list1[3] = display_height - int(coord_list[3])
    coord_list1[4] = coord_list[4]
    print(coord_list)
    print(coord_list1)
    cutter_x = 0
    cutter_y = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            pygame.draw.circle(display, black, [cutter_x, cutter_y], 20)
            
            pygame.draw.line(display,black,[int(coord_list1[0]),int(coord_list1[1])],
                             [int(coord_list1[2]), int(coord_list1[3])], 1)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

print(input_G_code())
Visual(input_G_code())
