from gamelib import *

game = Game(800,640,"Mega Mania")

bk = Image("images\\iceman.png",game)
bk.resizeTo(game.width,game.height)

megaman = Animation("m 0.gif",5,game,134/5,51/1)
megaman = Animation("m 1.gif",9,game,218/5,89/2)
megaman = Animation("m 2.gif",11,game,182/5,139/2)
megaman = Animation("m 3.gif",16,game,281/6,146/3)
megaman = Animation("m 4.gif",10,game,259/6,101/2)
megaman = Animation("m 5.gif",5,game,171/5,59/1)
megaman = Animation("m 6.gif",3,game,124/3,55/1)
megaman = Animation("m 7.gif",15,game,220/6,126/3)
megaman = Animation("m 8.gif",11,game,183/5,144/3)
megaman = Animation("m 9.gif",16,game,183/5,144/3)
megaman = Animation("m 10.gif",4,game,182/4,53/1)
megaman = Animation("m 11.gif",5,game,169/5,54/1)
megaman = Animation("m 12.gif",3,game,132/3,54/1)

bass = Animation("b 1.gif",27,game,554/15,155/2)
bass = Animation("b 2.gif",2,game,101/2,58/1)
bass = Animation("b 3.gif",1,game,52/1,55/1)
bass = Animation("b 4.gif",13,game,550/13,61/1)
bass = Animation("b 6.gif",16,game,632/16,42/1)
bass = Animation("b 7.gif",54,game,642/19,186/3)
bass = Animation("b 8.gif",27,game,617/13,119/2)
bass = Animation("b 9.gif",35,game,621/19,128/2)
bass = Animation("b 10.gif",15,game,626/15,61/1)
bass = Animation("b 11.gif",15,game,479/15,77/1)
bass = Animation("b 12.gif",14,game,586/14,54/1)
bass = Animation("b 13.gif",4,game,226/4,48/1)
bass = Animation("b 14.gif",2,game,104/2,60/1)
bass = Animation("b 15.gif",2,game,68/2,68/2)

0 = Animation("z 1.gif",22,game,1005/22,65/1)
0 = Animation("z 2.gif",15,game,919/15,79/1)
0 = Animation("z 3.gif",32,game,845/16,118/2)
0 = Animation("z 4.gif",34,game,1005/12,212/3)
0 = Animation("z 6.gif",14,game,569/14,83/1)

jb = Animation("jbm 1.png",10,game,355/5,139/2)
jb = Animation("jbm 2.png",5,game,396/5,85/1)
jb = Animation("jbm 3.png",3,game,197/3,75/1)

x = Animation("x 1.gif",21,game,637/21,56/1)
x = Animation("x 2.gif",7,game,192/7,53/1)
x = Animation("x 3.gif",19,game,353/10,102/2)
x = Animation("x 4.gif",7,game,219/7,49/1)
x = Animation("x 5.gif",9,game,292/7,44/1)
#x = Animation("x 6.gif",5,game,171/5,59/1)
x = Animation("x 7.gif",11,game,371/11,46/1)
x = Animation("x 8.gif",1,game,19/1,23/1)
x = Animation("x 9.gif",11,game,283/7,34/1)
x = Animation("x 10.gif",5,game,188/5,50/1)
x = Animation("x 11.gif",3,game,170/3,40/1)
x = Animation("x 12.gif",4,game,187/4,40/1)


c = Animation("jbm 1.png",10,game,355/5,139/2)
c = Animation("jbm 2.png",5,game,396/5,85/1)
c = Animation("jbm 3.png",3,game,197/3,75/1)

reploid = Animation("r 1.gif",8,game,525/8,65/1)
reploid = Animation("r 2.gif",10,game,738/10,86/1)
reploid = Animation("r 3.gif",19,game,353/10,102/2)
reploid = Animation("r 4.gif",12,game,875/12,90/1)
reploid = Animation("r 5.gif",8,game,524/8,82/1)
reploid = Animation("r 6.gif",10,game,613/10,84/1)
reploid = Animation("r 7.gif",19,game,738/19,88/1)
reploid = Animation("r 8.gif",12,game,892/12,87/1)

ridearmor = Animation("ra 1.png",1,game,71/1,57/1)
ridearmor = Animation("ra 2.png",1,game,71/1,53/1)

wily = animation("w 1.png",16,game,380/4,375/4)



fm = Animation('fm 1,41',6,game,378/6,117/2)
fm = Animation("fm 2.gif",3,game,160/3,41/1)
fm = Animation("fm 3.gif",3,game,142/3,75/1)
fm = Animation("fm 4.gif",7,game,361/1,56/1)


slash man = Animation (s 1,29,game,417/6,477/6)


while not game.over:
    game.processInput()
    bk.draw()
    megaman.draw()
    game.update(20)

game.quit()

            

