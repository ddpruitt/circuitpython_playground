import time
import board
import neopixel

pixel_pin = board.D6

num_pixels = 4*8

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.01, auto_write=False
)

while True:
    pixels.fill((255, 0, 0))
    pixels.show()
    time.sleep(1)

    pixels.fill((0, 255, 0))
    pixels.show()
    time.sleep(1)

    pixels.fill((0, 0, 255))

    pixels.show()
    time.sleep(1)

