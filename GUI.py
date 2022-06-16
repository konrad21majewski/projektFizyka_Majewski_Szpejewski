import math

import pygame
import fizyka
import inputBoxes as ib
from  planetrary_systems import examples

pygame.init()
# okno startowe
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Problem trzech ciał')
FPS = 60

# kolory
background_colour = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

screen.fill(background_colour)
pygame.display.flip()
clock = pygame.time.Clock()


# wyświetla tekst na określonej pozycji - font nie ulega zmianie
def drawText(tekst, width, height):
    smallfont = pygame.font.SysFont('Corbel', 25)
    text = smallfont.render(tekst, True, color)
    screen.blit(text, (width / 2, height / 2))


# tworzy identyczn przyciski jedynie ze zmiennym tekstem oraz pozycją
def button(x, y, tekst, event):
    response = False
    width = x
    height = y
    smallfont = pygame.font.SysFont('Corbel', 20)
    text = smallfont.render(tekst, True, color)

    mouse = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
            response = True

    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])
        screen.blit(text, (width / 2, height / 2))
    return response


# tworzy niewidzialny dla ludzkiego oka ze względu na kolor tła przycisk
def surfaceButton(x, y, event, sizex, sizey):
    response = False
    width = x
    height = y

    mouse = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if width / 2 <= mouse[0] <= width / 2 + sizex and height / 2 <= mouse[1] <= height / 2 + sizey:
            response = True

    pygame.draw.rect(screen, (0, 0, 0), [width / 2, height / 2, sizex, sizey])
    return response

def drawExample(planetList):
    planets = planetList
    run = True
    stopped = run
    while run:
        clock.tick(FPS)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 40, 800, 760))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(140, 0, 660, 40))
        for event3 in pygame.event.get():
            if event3.type == pygame.QUIT:
                pygame.quit()
            if button(0, 0, "Menu", event3):
                planets = []
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(screen)

        pygame.display.update()



def main():
    # przechowuje informację o tym czy symulacja jest zatrzymana bądź nie
    stopped = True
    # przechowuje informację o tym czy wybrana została pozycja dla dodawanej planety
    cross = False
    # przechowuje informację o działaniu programu
    running = True

    zeroDzieli = False

    clock = pygame.time.Clock()

    # Tworzenie bloków tekstowe do wypełnienia przez użytkownika

    # promień
    input_box1 = ib.InputBox(300, 220, 140, 32)
    # masa
    input_box2 = ib.InputBox(300, 300, 140, 32)
    # prędkość Y
    input_box3 = ib.InputBox(300, 380, 140, 32)
    # prędkość X
    input_box4 = ib.InputBox(300, 460, 140, 32)

    input_boxes = [input_box1, input_box2, input_box3, input_box4]

    planets = []

    while running:
        # określenie ilości klatek na sekundę
        clock.tick(FPS)

        # rozpoczęcie działania
        for event in pygame.event.get():

            # kliknij X to zamknie się program
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.QUIT:
                pygame.quit()

            # pole wyboru pozycji
            if surfaceButton(0, 100, event, 800, 800):
                cross = True
                mouse = pygame.mouse.get_pos()
                print(mouse[0], mouse[1])
                catchX = (mouse[0] - 800 / 2) / 250
                catchY = (mouse[1] - 800 / 2) / 250
                print(catchX, catchY)

            if cross:
                pygame.draw.rect(screen, color_light, [mouse[0] - 20, mouse[1] - 5, 40, 10])
                pygame.draw.rect(screen, color_light, [mouse[0] - 5, mouse[1] - 20, 10, 40])

            if zeroDzieli:
                pygame.draw.rect(screen, (100, 0, 0), pygame.Rect(195, 40, 530, 40))
                drawText("Ciała nie mogą być ustawione w tym samym miejscu", 400, 100)
                # planets.pop(len(planets)-1)

            # planety wyświetlane przed startem

            if (stopped):
                for planet in planets:
                    planet.draw(screen)

            pygame.display.update()

            # przyciski

            if (button(0, 0, "Dodaj", event)):
                done = False
                screen.fill((30, 30, 30))
                while not done:
                    drawText("Promień", 600, 380)
                    drawText("Masa [kg]", 600, 540)
                    drawText("*10^(24)", 1000, 600)
                    drawText("Prędkość Y [km/s]", 600, 700)
                    drawText("Prędkość X [km/s]", 600, 860)

                    for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            pygame.quit()

                        if button(1100, 200, "Czerwony", event):
                            pygame.draw.rect(screen, RED, pygame.Rect(385, 50, 120, 25))
                            color = RED

                        if button(800, 200, "Biały", event):
                            pygame.draw.rect(screen, WHITE, pygame.Rect(385, 50, 120, 25))
                            color = WHITE

                        if button(500, 200, "Niebieski", event):
                            pygame.draw.rect(screen, BLUE, pygame.Rect(385, 50, 120, 25))
                            color = BLUE

                        if button(200, 200, "Żółty", event):
                            pygame.draw.rect(screen, YELLOW, pygame.Rect(385, 50, 120, 25))
                            color = YELLOW

                        drawText("Kolor: ", 650, 100)

                        if button(900, 1050, "Powrót", event):
                            done = True

                        if button(400, 1050, "Gotowe", event):
                            try:
                                XD = catchY
                            except UnboundLocalError:
                                catchY = 0
                                catchX = 0
                            try:
                                XD = color
                            except:
                                color = RED
                            try:
                                if (float(input_box1.text) == 0):
                                    drawText("Promień nie może być równy zero", 500, 1400)
                                    raise ValueError
                                if (float(input_box2.text) == 0):
                                    drawText("Masa nie może być równa zero", 500, 1400)
                                    raise ValueError
                                planets.append(
                                    fizyka.Planet(catchX, catchY, float(input_box1.text), color,
                                                  float(input_box2.text)))
                                planets[-1].y_vel = float(input_box3.text) * 1000 * (-1)
                                planets[-1].x_vel = float(input_box4.text) * 1000
                                done = True
                            except ValueError:
                                drawText("Nie można dodać obiektu", 500, 1300)
                                drawText("Wpisano niewłaściwe dane", 500, 1350)

                        for box in input_boxes:
                            box.handle_event(event)

                    for box in input_boxes:
                        box.update()

                    for box in input_boxes:
                        box.draw(screen)

                    pygame.display.flip()

                screen.fill((0, 0, 0))

            button(0, 0, "Dodaj", event)

            # run = False;
            try:
                if (button(300, 0, "Start", event)):
                    print("start")
                    run = True
                    stopped = run
                    while run:
                        clock.tick(FPS)
                        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 40, 800, 760))
                        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(140, 0, 660, 40))
                        for event3 in pygame.event.get():
                            if event3.type == pygame.QUIT:
                                pygame.quit()
                            if (button(0, 0, "Menu", event3)):
                                run = False;

                        for planet in planets:
                            planet.update_position(planets)
                            planet.draw(screen)

                        pygame.display.update()
                        zeroDzieli = False
            except ZeroDivisionError:
                zeroDzieli = True

            if button(600, 0, "Reset", event):
                screen.fill((0, 0, 0))
                planets = []

            if button(900, 0, "Usuń ostatnia", event):
                try:
                    planets.pop(len(planets) - 1)
                except IndexError:
                    print(IndexError)

            if button(1200, 0, "Przykłady", event):
                choosing = True
                while choosing:
                    clock.tick(FPS)
                    screen.fill((30, 30, 30))
                    for eventExamples in pygame.event.get():
                        drawText("Wybierz jeden z przedstawionych przykładów: ", 350, 400)
                        if eventExamples.type == pygame.QUIT:
                            pygame.quit()
                        if button(0,0,"Menu", eventExamples):
                            choosing = False

                        for ex in examples:
                            if button((examples.index(ex)%5)*300 + 60, 600+150*math.floor((examples.index(ex)/5)), ex[1], eventExamples):
                                drawExample(ex[0])
                                choosing = False

                        pygame.display.update()

            pygame.display.update()


if __name__ == '__main__':
    main()
