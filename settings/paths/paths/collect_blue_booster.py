exec(open("./paths/field_blue flower.py").read())
self.keyboard.press("space")
self.keyboard.keyDown("a")
sleep(8)
self.keyboard.slowPress("space")
sleep(0.2)
self.keyboard.keyUp("a")
self.keyboard.walk("w",4)
self.keyboard.walk("d",5)
self.keyboard.walk("a",0.25)
self.keyboard.walk("s",7)
