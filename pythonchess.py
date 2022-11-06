import pygame
import pygame_gui
import time

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
gray = (60, 60, 60)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255,255,0)
purple = (138,43,226)
orange = (255,165,0)
pink = (255,105,180)
fuchsia = (255,0,255)
dis_width = 800
dis_height = 800
dis = pygame.display.set_mode((dis_width, dis_height), pygame.RESIZABLE)
pygame.display.set_caption("Python chess by Mike Wolski")
clock = pygame.time.Clock()

manager = pygame_gui.UIManager((dis_width, dis_height))

def startscreen():
    dis_width = dis.get_width()
    dis_height = dis.get_height()
    manager.clear_and_reset()
    manager.set_window_resolution((dis_width, dis_height))
    so = (dis_width + dis_height)/80
    title_font = pygame.font.SysFont("bahnschrift", int(so*4))
    dis.fill(gray)
    bpawnimg = pygame.image.load("b_pawn.png")
    bpawnimg = pygame.transform.scale(bpawnimg, (so*10, so*10))
    wpawnimg = pygame.image.load("w_pawn.png")
    wpawnimg = pygame.transform.scale(wpawnimg, (so*10, so*10))

    def title(msg,color, y):
        mesg = title_font.render(msg, True, color)
        dis.blit(mesg, [(dis_width-mesg.get_rect().width)/2, y])

    def bpawn(x, y):
        dis.blit(bpawnimg, (dis_width*x, dis_height*y))
    def wpawn(x, y):
        dis.blit(wpawnimg, (dis_width*x, dis_height*y))

    box = {
    "start_button": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/2-so*5, dis_height*1/3), (so*10, so*2)), text="Start", manager=manager),
    "white_button": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2), (so*10, so*2)), text="Choose white", manager=manager),
    "black_buttono" : pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2), (so*10, so*2)), text="Choose black", manager=manager),
    }

    wpawn(1/8, 1/5)
    bpawn(5/8, 1/5)

    while True:
        time_delta = clock.tick(60)/1000.0
        title("CHESS", green, 0)
        manager.draw_ui(dis)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.VIDEORESIZE:
                dis_height = dis.get_height()
                dis_width = dis.get_width()
                so = (dis_width + dis_height)/80
                title_font = pygame.font.SysFont("bahnschrift", int(so*4))
                dis.fill(gray)
                manager.clear_and_reset()
                manager.set_window_resolution((dis_width, dis_height))
                title("CHESS", green, 0)
                so = (dis_width + dis_height)/80
                wpawn(1/8, 1/5)
                bpawn(5/8, 1/5)
                box = {
                "start_button": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/2-so*5, dis_height*1/3), (so*10, so*2)), text="Start", manager=manager),
                "white_button": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2), (so*10, so*2)), text="Choose white", manager=manager),
                "black_button": pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2), (so*10, so*2)), text="Choose black", manager=manager),
                }

                bpawnimg = pygame.image.load("b_pawn.png")
                bpawnimg = pygame.transform.scale(bpawnimg, (so*10, so*10))
                wpawnimg = pygame.image.load("w_pawn.png")
                wpawnimg = pygame.transform.scale(wpawnimg, (so*10, so*10))
                pygame.display.update()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == box["start_button"]:
                    gameloop()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == box["white_button"]:
                    wpawn(1/8, 1/5)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == box["black_button"]:
                    bpawn(5/8, 1/5)
            manager.process_events(event)
        manager.update(time_delta)
def gameloop():
    dis_width = dis.get_width()
    dis_height = dis.get_height()
    so = (dis_width + dis_height)/240
    dis.fill(gray)
    game_over = False
    bbishimg = pygame.image.load("b_bishop.png")
    bbishimg = pygame.transform.scale(bbishimg, (so*14, so*14))
    bkingimg = pygame.image.load("b_king.png")
    bkingimg = pygame.transform.scale(bkingimg, (so*14, so*14))
    brookimg = pygame.image.load("b_rook.png")
    brookimg = pygame.transform.scale(brookimg, (so*14, so*14))
    bknightimg = pygame.image.load("b_knight.png")
    bknightimg = pygame.transform.scale(bknightimg, (so*14, so*14))
    bqueenimg = pygame.image.load("b_queen.png")
    bqueenimg = pygame.transform.scale(bqueenimg, (so*14, so*14))
    bpawnimg = pygame.image.load("b_pawn.png")
    bpawnimg = pygame.transform.scale(bpawnimg, (so*14, so*14))
    wbishimg = pygame.image.load("w_bishop.png")
    wbishimg = pygame.transform.scale(wbishimg, (so*14, so*14))
    wkingimg = pygame.image.load("w_king.png")
    wkingimg = pygame.transform.scale(wkingimg, (so*14, so*14))
    wrookimg = pygame.image.load("w_rook.png")
    wrookimg = pygame.transform.scale(wrookimg, (so*14, so*14))
    wknightimg = pygame.image.load("w_knight.png")
    wknightimg = pygame.transform.scale(wknightimg, (so*14, so*14))
    wqueenimg = pygame.image.load("w_queen.png")
    wqueenimg = pygame.transform.scale(wqueenimg, (so*14, so*14))
    wpawnimg = pygame.image.load("w_pawn.png")
    wpawnimg = pygame.transform.scale(wpawnimg, (so*14, so*14))

    def bpawn(x, y):
        dis.blit(bpawnimg, (dis_width*x, dis_height*y))
    def wpawn(x, y):
        dis.blit(wpawnimg, (dis_width*x, dis_height*y))
    def brook(x, y):
        dis.blit(brookimg, (dis_width*x, dis_height*y))
    def wrook(x, y):
        dis.blit(wrookimg, (dis_width*x, dis_height*y))
    def bbish(x, y):
        dis.blit(bbishimg, (dis_width*x, dis_height*y))
    def wbish(x, y):
        dis.blit(wbishimg, (dis_width*x, dis_height*y))
    def bking(x, y):
        dis.blit(bkingimg, (dis_width*x, dis_height*y))
    def wking(x, y):
        dis.blit(wkingimg, (dis_width*x, dis_height*y))
    def bqueen(x, y):
        dis.blit(bqueenimg, (dis_width*x, dis_height*y))
    def wqueen(x, y):
        dis.blit(wqueenimg, (dis_width*x, dis_height*y))
    def bknight(x, y):
        dis.blit(bknightimg, (dis_width*x, dis_height*y))
    def wknight(x, y):
        dis.blit(wknightimg, (dis_width*x, dis_height*y))

    def blank(x, y, c):
        pygame.draw.rect(dis, c, [dis_width*x, dis_height*y, dis_width*1/8, dis_height*1/8])
        pygame.display.update()

    class area():
        def __init__(self, x, y, taken, c):
            self.rect = pygame.draw.rect(dis, c, [dis_width*x, dis_height*y, dis_width*1/8, dis_height*1/8])
            self.taken = taken
            self.x = x
            self.y = y
            self.c = c
            if self.taken == 1:
                wpawn(x, y)
            if self.taken == 2:
                wrook(x, y)
            if self.taken == 3:
                wknight(x, y)
            if self.taken == 4:
                wbish(x, y)
            if self.taken == 5:
                wking(x, y)
            if self.taken == 6:
                wqueen(x, y)
            if self.taken == 7:
                bpawn(x, y)
            if self.taken == 8:
                brook(x, y)
            if self.taken == 9:
                bknight(x, y)
            if self.taken == 10:
                bbish(x, y)
            if self.taken == 11:
                bking(x, y)
            if self.taken == 12:
                bqueen(x, y)
    
    a1 = area(0,0,2, gray)
    a2 = area(1/8,0,3, black)
    a3 = area(2/8,0,4, gray)
    a4 = area(3/8,0,5, black)
    a5 = area(4/8,0,6, gray)
    a6 = area(5/8,0,4, black)
    a7 = area(6/8,0,3, gray)
    a8 = area(7/8,0,2, black)
    b1 = area(0,1/8,1, black)
    b2 = area(1/8,1/8,1, gray)
    b3 = area(2/8,1/8,1, black)
    b4 = area(3/8,1/8,1, gray)
    b5 = area(4/8,1/8,1, black)
    b6 = area(5/8,1/8,1, gray)
    b7 = area(6/8,1/8,1, black)
    b8 = area(7/8,1/8,1, gray)
    c1 = area(0,2/8,0, gray)
    c2 = area(1/8,2/8,0, black)
    c3 = area(2/8,2/8,0, gray)
    c4 = area(3/8,2/8,0, black)
    c5 = area(4/8,2/8,0, gray)
    c6 = area(5/8,2/8,0, black)
    c7 = area(6/8,2/8,0, gray)
    c8 = area(7/8,2/8,0, black)
    d1 = area(0,3/8,0, black)
    d2 = area(1/8,3/8,0, gray)
    d3 = area(2/8,3/8,0, black)
    d4 = area(3/8,3/8,0, gray)
    d5 = area(4/8,3/8,0, black)
    d6 = area(5/8,3/8,0, gray)
    d7 = area(6/8,3/8,0, black)
    d8 = area(7/8,3/8,0, gray)
    e1 = area(0,4/8,0, gray)
    e2 = area(1/8,4/8,0, black)
    e3 = area(2/8,4/8,0, gray)
    e4 = area(3/8,4/8,0, black)
    e5 = area(4/8,4/8,0, gray)
    e6 = area(5/8,4/8,0, black)
    e7 = area(6/8,4/8,0, gray)
    e8 = area(7/8,4/8,0, black)
    f1 = area(0,5/8,0, black)
    f2 = area(1/8,5/8,0, gray)
    f3 = area(2/8,5/8,0, black)
    f4 = area(3/8,5/8,0, gray)
    f5 = area(4/8,5/8,0, black)
    f6 = area(5/8,5/8,0, gray)
    f7 = area(6/8,5/8,0, black)
    f8 = area(7/8,5/8,0, gray)
    g1 = area(0,6/8,7, gray)
    g2 = area(1/8,6/8,7, black)
    g3 = area(2/8,6/8,7, gray)
    g4 = area(3/8,6/8,7, black)
    g5 = area(4/8,6/8,7, gray)
    g6 = area(5/8,6/8,7, black)
    g7 = area(6/8,6/8,7, gray)
    g8 = area(7/8,6/8,7, black)
    h1 = area(0,7/8,8, black)
    h2 = area(1/8,7/8,9, gray)
    h3 = area(2/8,7/8,10, black)
    h4 = area(3/8,7/8,11, gray)
    h5 = area(4/8,7/8,12, black)
    h6 = area(5/8,7/8,10, gray)
    h7 = area(6/8,7/8,9, black)
    h8 = area(7/8,7/8,8, gray)

    pygame.display.update()

    def move(a):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if a.rect.collidepoint(event.pos):
                    if a.taken == 1:
                        blank(a.x, a.y, a.c)
                        a.taken -= 1
                        pygame.display.update()
                    elif a.taken == 7:
                        blank(a.x, a.y, a.c)
                        a.taken -= 7
                        pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type==pygame.VIDEORESIZE:
                dis_height = dis.get_height()
                dis_width = dis.get_width()
                dis.fill(gray)
                a1 = area(0,0,2, gray)
                a2 = area(1/8,0,3, black)
                a3 = area(2/8,0,4, gray)
                a4 = area(3/8,0,5, black)
                a5 = area(4/8,0,6, gray)
                a6 = area(5/8,0,4, black)
                a7 = area(6/8,0,3, gray)
                a8 = area(7/8,0,2, black)
                b1 = area(0,1/8,1, black)
                b2 = area(1/8,1/8,1, gray)
                b3 = area(2/8,1/8,1, black)
                b4 = area(3/8,1/8,1, gray)
                b5 = area(4/8,1/8,1, black)
                b6 = area(5/8,1/8,1, gray)
                b7 = area(6/8,1/8,1, black)
                b8 = area(7/8,1/8,1, gray)
                c1 = area(0,2/8,0, gray)
                c2 = area(1/8,2/8,0, black)
                c3 = area(2/8,2/8,0, gray)
                c4 = area(3/8,2/8,0, black)
                c5 = area(4/8,2/8,0, gray)
                c6 = area(5/8,2/8,0, black)
                c7 = area(6/8,2/8,0, gray)
                c8 = area(7/8,2/8,0, black)
                d1 = area(0,3/8,0, black)
                d2 = area(1/8,3/8,0, gray)
                d3 = area(2/8,3/8,0, black)
                d4 = area(3/8,3/8,0, gray)
                d5 = area(4/8,3/8,0, black)
                d6 = area(5/8,3/8,0, gray)
                d7 = area(6/8,3/8,0, black)
                d8 = area(7/8,3/8,0, gray)
                e1 = area(0,4/8,0, gray)
                e2 = area(1/8,4/8,0, black)
                e3 = area(2/8,4/8,0, gray)
                e4 = area(3/8,4/8,0, black)
                e5 = area(4/8,4/8,0, gray)
                e6 = area(5/8,4/8,0, black)
                e7 = area(6/8,4/8,0, gray)
                e8 = area(7/8,4/8,0, black)
                f1 = area(0,5/8,0, black)
                f2 = area(1/8,5/8,0, gray)
                f3 = area(2/8,5/8,0, black)
                f4 = area(3/8,5/8,0, gray)
                f5 = area(4/8,5/8,0, black)
                f6 = area(5/8,5/8,0, gray)
                f7 = area(6/8,5/8,0, black)
                f8 = area(7/8,5/8,0, gray)
                g1 = area(0,6/8,7, gray)
                g2 = area(1/8,6/8,7, black)
                g3 = area(2/8,6/8,7, gray)
                g4 = area(3/8,6/8,7, black)
                g5 = area(4/8,6/8,7, gray)
                g6 = area(5/8,6/8,7, black)
                g7 = area(6/8,6/8,7, gray)
                g8 = area(7/8,6/8,7, black)
                h1 = area(0,7/8,8, black)
                h2 = area(1/8,7/8,9, gray)
                h3 = area(2/8,7/8,10, black)
                h4 = area(3/8,7/8,11, gray)
                h5 = area(4/8,7/8,12, black)
                h6 = area(5/8,7/8,10, gray)
                h7 = area(6/8,7/8,9, black)
                h8 = area(7/8,7/8,8, gray)
                so = (dis_width + dis_height)/240
                bbishimg = pygame.image.load("b_bishop.png")
                bbishimg = pygame.transform.scale(bbishimg, (so*14, so*14))
                bkingimg = pygame.image.load("b_king.png")
                bkingimg = pygame.transform.scale(bkingimg, (so*14, so*14))
                brookimg = pygame.image.load("b_rook.png")
                brookimg = pygame.transform.scale(brookimg, (so*14, so*14))
                bknightimg = pygame.image.load("b_knight.png")
                bknightimg = pygame.transform.scale(bknightimg, (so*14, so*14))
                bqueenimg = pygame.image.load("b_queen.png")
                bqueenimg = pygame.transform.scale(bqueenimg, (so*14, so*14))
                bpawnimg = pygame.image.load("b_pawn.png")
                bpawnimg = pygame.transform.scale(bpawnimg, (so*14, so*14))
                wbishimg = pygame.image.load("w_bishop.png")
                wbishimg = pygame.transform.scale(wbishimg, (so*14, so*14))
                wkingimg = pygame.image.load("w_king.png")
                wkingimg = pygame.transform.scale(wkingimg, (so*14, so*14))
                wrookimg = pygame.image.load("w_rook.png")
                wrookimg = pygame.transform.scale(wrookimg, (so*14, so*14))
                wknightimg = pygame.image.load("w_knight.png")
                wknightimg = pygame.transform.scale(wknightimg, (so*14, so*14))
                wqueenimg = pygame.image.load("w_queen.png")
                wqueenimg = pygame.transform.scale(wqueenimg, (so*14, so*14))
                wpawnimg = pygame.image.load("w_pawn.png")
                wpawnimg = pygame.transform.scale(wpawnimg, (so*14, so*14))
                pygame.display.update()
            move(a1)
            move(a2)
            move(a3)
            move(a4)
            move(a5)
            move(a6)
            move(a7)
            move(a8)
            move(b1)
            move(b2)
            move(b3)
            move(b4)
            move(b5)
            move(b6)
            move(b7)
            move(b8)
            move(c1)
            move(c2)
            move(c3)
            move(c4)
            move(c5)
            move(c6)
            move(c7)
            move(c8)
            move(d1)
            move(d2)
            move(d3)
            move(d4)
            move(d5)
            move(d6)
            move(d7)
            move(d8)
            move(e1)
            move(e2)
            move(e3)
            move(e4)
            move(e5)
            move(e6)
            move(e7)
            move(e8)
            move(f1)
            move(f2)
            move(f3)
            move(f4)
            move(f5)
            move(f6)
            move(f7)
            move(f8)
            move(g1)
            move(g2)
            move(g3)
            move(g4)
            move(g5)
            move(g6)
            move(g7)
            move(g8)
            move(h1)
            move(h2)
            move(h3)
            move(h4)
            move(h5)
            move(h6)
            move(h7)
            move(h8)

        clock.tick(60)
    pygame.quit()
    quit()

startscreen()