def jump(self, dirKey):
    self.keyboard.keyDown(dirKey)
    time.sleep(1.5)
    self.keyboard.slowPress('space')
    sleep(0.2)
    self.keyboard.keyUp(dirKey)

for _ in range(3):
    self.keyboard.press(".")
self.keyboard.slowPress("e")
sleep(0.08)
self.keyboard.keyDown("w")
sleep(0.5)
self.keyboard.slowPress("space")
self.keyboard.slowPress("space")
sleep(2.7)
self.keyboard.slowPress(",")
sleep(3.5)
self.keyboard.keyUp("w")
self.keyboard.walk("d",4)
self.keyboard.walk("w",1.5)
jump(self, "w")
self.keyboard.walk("w",0.5)
jump(self, "w")
self.keyboard.walk("w",1.5)
self.keyboard.walk("s",0.55)

