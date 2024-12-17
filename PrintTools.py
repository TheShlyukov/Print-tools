import time
import sys
import random

class printtools():
    def withDelay(text, delay):
        time.sleep(int(delay))
        print(text)
    def byLetter(text, delay):
        for l in text:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(delay)
        print("")
    def typeEmulate(text, speed):
        typing_speed = speed #wpm
        for l in text:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(random.random()*10.0/typing_speed)
        print("")
    def p(lines):
        if lines=="":
            print("")
        else:
            for i in range(int(lines)):
                print("")
class printToolsTest():
  def test():
    printtools.byLetter("hello, world!", 0.1)
    printtools.p(3)
    printtools.typeEmulate("Heeeey fjsadhgfljkdsagvjkdsfhgfui;ehufk;ehf", 50)
    printtools.withDelay('the end', 2)
