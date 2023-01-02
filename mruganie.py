# CZY TU TRZEBA COŚ KOMENTOWAĆ?
import time as tm
import pygame as pg

# LISTA WYŚWIETLANYCH ELEMENTÓW (W STR BO TAK ŁATWIEJ)
lit: list = 'ABCDEF GHIJKL MNOPRS TUWYZ '
dlugo: int = len(lit)

# PYGAME BAZA
pg.init()
win_width = win_height = 800
okienko: tuple = (win_width, win_height)
win: object = pg.display.set_mode(okienko)
pg.display.set_caption("Literki - mruganie")

# NAPIS JEST ROBIONY
font: object = pg.font.Font('freesansbold.ttf', 300)
white: tuple = (255,255,255) # KOD RGB DLA KOLORU BIAŁEGO
black: tuple = (0, 0, 0)     # KOD RGB DLA KOLORU CZARNEGO

# TAKA O FUNKCJA DO DZIAŁANIA W OGÓLE
def settings():
    """
    Co funkcja robi, każdy widzi - po prostu pozwala wyjść i daje fajne przerwy
    """
    global i, keys
    for event in pg.event.get():
        if event.type == pg.QUIT:
            i = -1
    keys = pg.key.get_pressed()
    pg.time.delay(998)

# FUNKCJA DO WYŁĄCZANIA, NIE DZIAŁA TAK PŁYNNIE BO JEST TM.SLEEP
def exit():
    """
    Przytrzymujesz ESCAPE i program się zamyka, proste.
    """
    global i
    if keys[pg.K_ESCAPE]:
        i = -1


# NO TUTAJ JUŻ WIADOMKA, PĘTLA DO DZIAŁANIA PROGRAMU W OGÓLE
i: int = 0
while (i+1): # ROBIĘ TO TAK, ŻEBY WEWNĄTRZ PĘTLI NIE ROBIĆ DRUGIEJ PĘTLI
    win.fill(white)
    settings()
    idx: int = i%dlugo
    litera = lit[idx]
    text: object = font.render(litera, True, black)
    textRect: object = text.get_rect()
    textRect.center: tuple = (win_width//2, win_height//2)
    win.blit(text, textRect)
    pg.display.update()
    i += 1
    exit()
    with open("litery_czas.csv", "a") as myfile:
        myfile.write(litera + ',' + str(tm.time()) + '\n')

pg.quit()
