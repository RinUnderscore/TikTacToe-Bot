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

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # Move Select
    if (mouse_x > 0 and mouse_x < 165 and mouse_y > 0 and mouse_y < 165 and event.type == pg.MOUSEBUTTONDOWN): board[0] = "o"; turn = "x"
    if (mouse_x > 165 and mouse_x < 330 and mouse_y > 0 and mouse_y < 165 and event.type == pg.MOUSEBUTTONDOWN): board[1] = "o"; turn = "x"
    if (mouse_x > 330 and mouse_y > 0 and mouse_y < 165 and event.type == pg.MOUSEBUTTONDOWN): board[2] = "o"; turn = "x"
    if (mouse_x > 0 and mouse_x < 165 and mouse_y > 165 and mouse_y < 330 and event.type == pg.MOUSEBUTTONDOWN): board[3] = "o"; turn = "x"
    if (mouse_x > 165 and mouse_x < 330 and mouse_y > 165 and mouse_y < 330 and event.type == pg.MOUSEBUTTONDOWN): board[4] = "o"; turn = "x"
    if (mouse_x > 330 and mouse_y > 165 and mouse_y < 330 and event.type == pg.MOUSEBUTTONDOWN): board[5] = "o"; turn = "x"
    if (mouse_x > 0 and mouse_x < 165 and mouse_y > 330 and event.type == pg.MOUSEBUTTONDOWN): board[6] = "o"; turn = "x"
    if (mouse_x > 165 and mouse_x < 330 and mouse_y > 330 and event.type == pg.MOUSEBUTTONDOWN): board[7] = "o"; turn = "x"
    if (mouse_x > 330 and mouse_y > 330 and event.type == pg.MOUSEBUTTONDOWN): board[8] = "o"; turn = "x"

    # AI
    for a in range (len(board)):
        if board[a] == "o":
            print("Occupied")
        if board[a] != "o" or board[a] != "x" or board[a] != " ":
            board[a] = "x"


    # Rendeing
    if board[0] == "o": screen.blit(circle, (0, 0))
    if board[1] == "o": screen.blit(circle, (165, 0))
    if board[2] == "o": screen.blit(circle, (330, 0))
    if board[3] == "o": screen.blit(circle, (0, 165))
    if board[4] == "o": screen.blit(circle, (165, 165))
    if board[5] == "o": screen.blit(circle, (330, 165))
    if board[6] == "o": screen.blit(circle, (0, 330))
    if board[7] == "o": screen.blit(circle, (165, 330))
    if board[8] == "o": screen.blit(circle, (330, 330))
    if board[0] == "x": screen.blit(cross, (0, 0))
    if board[1] == "x": screen.blit(cross, (165, 0))
    if board[2] == "x": screen.blit(cross, (330, 0))
    if board[3] == "x": screen.blit(cross, (0, 165))
    if board[4] == "x": screen.blit(cross, (165, 165))
    if board[5] == "x": screen.blit(cross, (330, 165))
    if board[6] == "x": screen.blit(cross, (0, 330))
    if board[7] == "x": screen.blit(cross, (165, 330))
    if board[8] == "x": screen.blit(cross, (330, 330))

    pg.draw.line(screen, (0,0,0), (165,0), (165, 500), 10)
    pg.draw.line(screen, (0,0,0), (330,0), (330, 500), 10)
    pg.draw.line(screen, (0,0,0), (0,160), (500,160), 10)
    pg.draw.line(screen, (0,0,0), (0,330), (500,330), 10)

    pg.display.flip()
    

quit()