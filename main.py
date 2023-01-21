import pygame as pg
board = [" "," "," "," "," "," "," "," "," "]
pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption("Tik Tac Toe Bot")


circle = pg.image.load("circle.gif")
circle = pg.transform.scale(circle, ((165,165)))
cross = pg.image.load("cross.gif")
cross = pg.transform.scale(cross, ((165,165)))

turn = "o"

run = True
while run:
    screen.fill((255,255,255))

    (mouse_x, mouse_y) = pg.mouse.get_pos()
    pressed_keys = pg.key.get_pressed()

    # Move Select
    if turn == "o":
        if (mouse_x > 0 and mouse_x < 165 and mouse_y > 0 and mouse_y < 165 and event.type == pg.MOUSEBUTTONDOWN): board[0] = "o"
        if (mouse_x > 165 and mouse_x < 330 and mouse_y > 0 and mouse_y < 165 and event.type == pg.MOUSEBUTTONDOWN): board[1] = "o"
        if (mouse_x > 330 and mouse_y > 0 and mouse_y < 165 and event.type == pg.MOUSEBUTTONDOWN): board[2] = "o"
        if (mouse_x > 0 and mouse_x < 165 and mouse_y > 165 and mouse_y < 330 and event.type == pg.MOUSEBUTTONDOWN): board[3] = "o"
        if (mouse_x > 165 and mouse_x < 330 and mouse_y > 165 and mouse_y < 330 and event.type == pg.MOUSEBUTTONDOWN): board[4] = "o"
        if (mouse_x > 330 and mouse_y > 165 and mouse_y < 330 and event.type == pg.MOUSEBUTTONDOWN): board[5] = "o"
        if (mouse_x > 0 and mouse_x < 165 and mouse_y > 330 and event.type == pg.MOUSEBUTTONDOWN): board[6] = "o"
        if (mouse_x > 165 and mouse_x < 330 and mouse_y > 330 and event.type == pg.MOUSEBUTTONDOWN): board[7] = "o"
        if (mouse_x > 330 and mouse_y > 330 and event.type == pg.MOUSEBUTTONDOWN): board[8] = "o"
        if (pg.MOUSEBUTTONDOWN == event.type): turn = "x"
    if turn == "x":
        if (mouse_x > 0 and mouse_x < 165 and mouse_y > 0 and mouse_y < 165 and event.type == pg.MOUSEBUTTONDOWN): board[0] = "o"
        if (mouse_x > 165 and mouse_x < 330 and mouse_y > 0 and mouse_y < 165 and event.type == pg.MOUSEBUTTONDOWN): board[1] = "o"
        if (mouse_x > 330 and mouse_y > 0 and mouse_y < 165 and event.type == pg.MOUSEBUTTONDOWN): board[2] = "o"
        if (mouse_x > 0 and mouse_x < 165 and mouse_y > 165 and mouse_y < 330 and event.type == pg.MOUSEBUTTONDOWN): board[3] = "o"
        if (mouse_x > 165 and mouse_x < 330 and mouse_y > 165 and mouse_y < 330 and event.type == pg.MOUSEBUTTONDOWN): board[4] = "o"
        if (mouse_x > 330 and mouse_y > 165 and mouse_y < 330 and event.type == pg.MOUSEBUTTONDOWN): board[5] = "o"
        if (mouse_x > 0 and mouse_x < 165 and mouse_y > 330 and event.type == pg.MOUSEBUTTONDOWN): board[6] = "o"
        if (mouse_x > 165 and mouse_x < 330 and mouse_y > 330 and event.type == pg.MOUSEBUTTONDOWN): board[7] = "o"
        if (mouse_x > 330 and mouse_y > 330 and event.type == pg.MOUSEBUTTONDOWN): board[8] = "o"
        if (pg.MOUSEBUTTONDOWN == event.type): turn = "o"

    if board[0] == "o": screen.blit(circle, (0, 0))
    if board[1] == "o": screen.blit(circle, (165, 0))
    if board[2] == "o": screen.blit(circle, (330, 0))
    if board[3] == "o": screen.blit(circle, (0, 165))
    if board[4] == "o": screen.blit(circle, (165, 165))
    if board[5] == "o": screen.blit(circle, (330, 165))
    if board[6] == "o": screen.blit(circle, (0, 330))
    if board[7] == "o": screen.blit(circle, (165, 330))
    if board[8] == "o": screen.blit(circle, (330, 330))

    pg.draw.line(screen, (0,0,0), (165,0), (165, 500), 10)
    pg.draw.line(screen, (0,0,0), (330,0), (330, 500), 10)
    pg.draw.line(screen, (0,0,0), (0,160), (500,160), 10)
    pg.draw.line(screen, (0,0,0), (0,330), (500,330), 10)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    pg.display.flip()
    

quit()