import time
import sys
from random import randrange

print("hello")
print("what is your name?")
name_value = input()
print("Hello, %s " % (name_value))
time.sleep(2)
print("Here's a few ways in which you could respond during an introduction")
time.sleep(2)
print("A")
time.sleep(1)
print("I think that's a great name!")

time.sleep(2)
print("B")
time.sleep(1)
print("%s.. so cool, I really dig it!" %(name_value))

time.sleep(2)
print("Here's what a more humanistic response time would look like, just thinking in terms of dynamics when printing out to a screen.")
time.sleep(3)
name_value = ((name_value) + "...that's beautiful, just like you!")
for c in name_value:
  sys.stdout.write(c)
  sys.stdout.flush()
  seconds = "0." + str(randrange(1, 4, 1))
  seconds = float(seconds)
  time.sleep(seconds)
print()
time.sleep(2)
print("Notice the difference? It's subtle but it's there.")
time.sleep(1)
