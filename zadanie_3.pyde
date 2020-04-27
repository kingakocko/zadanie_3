def setup():
    global positionOfFirstLetter
    global positionOfSecondLetter
    global s
    global change
    global letters
    global arrColors
    global pressedKey
    size(500,600)
    positionOfFirstLetter = [width/2, height/2]
    positionOfSecondLetter = [width/2 + 30, height/2]
    s = 100
    pressedKey = 0
    letters = ["K", "K"]
    arrColors = ["#423C40", "#79BFA1"]
    change = 0
    textSize(s)
    noFill()
    stroke("#79BFA1")
    triangle(positionOfFirstLetter[0]-50, positionOfFirstLetter[1]+s, positionOfFirstLetter[0]+200, positionOfSecondLetter[1]+s, (positionOfFirstLetter[0]+positionOfFirstLetter[0]+150)/2, positionOfFirstLetter[1]-100) # trójkąt nie jest kształtem nie standardowym, ale zaliczę, bo go nie mieliśmy
   
def draw():
    x = mouseLetter(positionOfFirstLetter[0], positionOfFirstLetter[1])
    y = pressedKey
    if change == 1:
        a = x
        x = y
        y = a
    fill(arrColors[x])
    text(letters[0], positionOfFirstLetter[0], positionOfFirstLetter[1] + 90)
    fill(arrColors[y])
    text(letters[1], positionOfSecondLetter[0] + 45, positionOfSecondLetter[1] + 90)
   
def mouseLetter(xPos, yPos):
    if mouseX >= xPos:
        if mouseX <= xPos + s/2:
            if mouseY >= yPos:
                if mouseY <= yPos + s:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0
 
def keyPressed():
    global change
    global pressedKey
    if keyCode == LEFT:
        change = 1
    elif keyCode == RIGHT:
        change = 1
    if key == letters[1].lower():
        pressedKey = 1  
def keyReleased():
    global change
    global pressedKey
    if keyCode == LEFT:
        change = 0
    elif keyCode == RIGHT:
        change = 0
    if key == letters[1].lower():
        pressedKey = 0
        
# na pewno na wszystko wpadłaś sama?
# dało się prościej
# 1,75p
# po za nazwami nawet kolory macie takie same z Danilukiem, jeżeli sie to powtórzy, nie zaliczę zadania
