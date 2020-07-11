def setup():
    size(600, 600)
    background(255)
    strokeWeight(5)
    global obrazunio
    obrazunio = loadImage("maxresdefault.jpg")
    noFill()
 
def draw():
    try:
        image(obrazunio, 69, 69, 210, 150)
    except:
        fill(0)
        text("cos jest nie tak z obrazem", 25, 25)
        stroke("#FF0000")
    else:
        stroke("#0000FF")
    finally:
        rect(69, 69, 210, 150)
        
#2pkt
