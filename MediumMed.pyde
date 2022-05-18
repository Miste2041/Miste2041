def setup():
    global photo
    size(800,800)
    frameRate(50000)
    photo=loadImage("zxc.jpg")
    image(photo,-100,-100)
    push()
    fill(138,43,226)
    ellipse(0,0,300,300)
    pop()
    #1ГЛАЗ
    push()
    fill(0,206,209)
    ellipse(30,40,50,50)
    ellipse(20,40,50,50)
    ellipse(40,40,50,50)
    pop()
    #2ГЛАЗ-ЗРАЧОК
    push()
    fill(0,0,0)
    ellipse(335,340,15,15)
    pop()
    #2ГЛАЗ
    push()
    fill(00,206,209)
    ellipse(460,340,50,50)
    ellipse(450,340,50,50)
    ellipse(470,340,50,50)
    pop()
    #НОС
    push()
    fill(255,255,0)
    ellipse(400,400,43,43)
    pop()
    #РОТ
    line(450,450,300,400)
    line(451,451,301,401)
    line(452,452,302,402)
    #1ГЛАЗ-ЗРАЧОК  
    push()
    fill(0,0,0)
    ellipse(475,340,15,15)
    pop()
def draw():
    
    if mousePressed==True and mouseButton==RIGHT:
        zek(mouseX,mouseY)
    if keyPressed==True and key=="M" or key=="m" or key=="ь" or key=="Ь":
        eew(mouseX,mouseY)
    if keyPressed==True and key=="N" or key=="n" or key=="т" or key=="Т":
        eee(mouseX,mouseY)
    if keyPressed==True and key=="E" or key=="e" or key=="у" or key=="У":
        eeq(0,0)
    
def zek(x,y):
    translate(x,y)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(0,0,random(1,40),random(1,40))
def eew(x,y):
    push()
    translate(x,y)
    ellipse(0,0,100,100)
    pop()
def eee(x,y):
    push()
    translate(x,y)
    rect(0,0,random(10,50),random(10,50))    
    pop()     
def eeq(x,y):
    push()
    ellipse(0,0,10000,10000)
    pop()
