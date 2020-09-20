import time
from pynput.mouse import Button, Controller
mouse = Controller()
# Read pointer position
time.sleep(3)
print('The current pointer position is {0}'.format(
mouse.position))
