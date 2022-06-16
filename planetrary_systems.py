import math

from fizyka import Planet
# kolory
background_colour = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
PURPLE = (118,0,142)
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

systemNiceTwo = [Planet(-0.5,0,20,BLUE,700000), Planet(0.5,0,20,RED,700000)]
systemNiceTwo[0].y_vel = 12500
systemNiceTwo[1].y_vel = -12500

likeMilky = [Planet(0,0,30,YELLOW,90000), Planet(-1,0,16,BLUE,600), Planet(1,0,16,RED,600)]
likeMilky[1].y_vel = 5000
likeMilky[2].y_vel = -5000

szybkie = [Planet(-0.7,0,15,BLUE,800000), Planet(0.7,0,15,BLUE,800000), Planet(-0.4,-0.9,10,WHITE,20),Planet(0.4,0.9,10,PURPLE,20) ]
szybkie[0].y_vel = 13000
szybkie[1].y_vel = -13000
szybkie[2].y_vel = 23000
szybkie[3].y_vel = -23000

trzyZagadka = [Planet(-0.7,0,15,BLUE,800000), Planet(0.7,0,15,BLUE,800000), Planet(0,-0.9,10,WHITE,10)]
trzyZagadka[0].y_vel = 13000
trzyZagadka[1].y_vel = -13000
trzyZagadka[2].y_vel = 25000

takie = [Planet(-0.9,0,12,BLUE,50000), Planet(0.9,0,12,RED,50000), Planet(0,-0.9,12,WHITE,50000), Planet(0,0.9,12,YELLOW,50000)]
takie[0].y_vel=4880
takie[1].y_vel=-4880
takie[2].x_vel=-4880
takie[3].x_vel=4880

takie1 = [Planet(-0.9,0,12,BLUE,50000), Planet(0.9,0,12,RED,50000), Planet(0,-0.9,12,WHITE,50000), Planet(0,0.9,12,YELLOW,50000)]
takie1[0].y_vel=5500
takie1[1].y_vel=-5500
takie1[2].x_vel=-5500
takie1[3].x_vel=5500

takie2 = [Planet(-0.9,0,12,BLUE,50000), Planet(0.9,0,12,RED,50000), Planet(0,-0.9,12,WHITE,50000), Planet(0,0.9,12,YELLOW,50000)]
takie2[0].y_vel=4000
takie2[1].y_vel=-4000
takie2[2].x_vel=-4000
takie2[3].x_vel=4000

MM = 90000
takieRR = [Planet(-0.5,-0.5,13,RED,MM), Planet(-0.5,0.5,13,BLUE,MM), Planet(0.866,0,13,WHITE,MM)]
velo = 5000
takieRR[0].x_vel = -velo
# takieRR[0].y_vel = velo
takieRR[1].x_vel = velo
# takieRR[1].y_vel = -velo
# takieRR[2].x_vel = -math.sqrt(velo)
takieRR[2].y_vel = -velo

MA = 220000
buty = [Planet(-0.4,-1,13,RED,MA), Planet(-0.4,0,13,BLUE,MA), Planet(0.466,-0.5,13,WHITE,MA)]
veloelo = 10000
buty[0].x_vel = veloelo*math.cos(0.698132*math.pi)
buty[0].y_vel = veloelo*math.sin(0.698132*math.pi)

buty[1].x_vel = -veloelo*math.cos(0.698132*math.pi)
buty[1].y_vel = veloelo*math.sin(0.698132*math.pi)

buty[2].y_vel = -veloelo




examples = [[systemNiceTwo,"Dwie Fajne"],[likeMilky, "Trzy nudne"],[trzyZagadka,"Trzy ciekawe"],[szybkie,"Nibysymetria (4)"], [takie,"Okrąg (4)"],
            [takie1,"Od środka (4)"], [takie2,"Do środka (4)"],[takieRR,"Trzy losowe"],[buty,"Ósemka"]]
