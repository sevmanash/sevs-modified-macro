
self.keyboard.slowPress(".")
self.keyboard.slowPress("e")
sleep(0.12)
self.keyboard.keyDown("w")
self.keyboard.slowPress("space")
self.keyboard.slowPress("space")
sleep(4.2)
self.keyboard.slowPress(",")
sleep(1.5)
self.keyboard.keyUp("w")
self.keyboard.slowPress("space")
sleep(0.5)
self.keyboard.walk("d",2.5)
for _ in range(3):
    self.keyboard.keyDown("w")
    self.keyboard.slowPress('space')
    sleep(0.2)
    self.keyboard.keyUp("w")
    
self.keyboard.walk('w',2)
self.keyboard.keyDown("w")
self.keyboard.slowPress('space')
sleep(0.2)
self.keyboard.keyUp("w")
self.keyboard.walk('w',4)
self.keyboard.slowPress(".")
self.keyboard.keyDown("w")
self.keyboard.slowPress('space')
sleep(0.2)
self.keyboard.keyUp("w")
self.keyboard.walk('w',7)
self.keyboard.slowPress(",")
self.keyboard.keyDown("d")
self.keyboard.slowPress('space')
sleep(0.2)
self.keyboard.keyUp("d")
self.keyboard.walk("d",1.9)
self.keyboard.walk("s",2.9)




    
