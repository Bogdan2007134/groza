from random import randint as rt
from PIL import Image
import numpy
from data import main_obj
import copy

lengt = 0


def logic(current_pos, ramifications, x, first):
    copy = current_pos
    current = current_pos
    ran = rt(0, 20)
    random = rt(0, 1)
    index = 1 if random == 0 else (-1)
    try:
        if x == 0:
            current_pos += (-1)
        elif x == 1:
            current_pos += 0
        elif x == 2:
            current_pos += 1
    except TypeError:
        print("[ERROR] hz chto za huynya")
    try:
        if ramifications == 6 and lengt == 0:
            for i in range(ran):
                if i % 3 == 0:
                    random = rt(0, 1)
                    index = 1 if random == 0 else (-1)
                current -= index
                data[first + i, current] = [0, 0, 255]
    except IndexError:
        print(f"[ERROR] index not in list: {first}")
    if current_pos >= 0 and current_pos <= 150:
        return current_pos
    else:
        return copy,


source = rt(0, 149)

current_position = source
data = numpy.zeros((150, 150, 3), dtype=numpy.uint8)

for first in range(len(main_obj)):

    ramifications = rt(0, 6)
    x = rt(0, 2)
    current_position = logic(current_position, ramifications, x, first)
    try:
        data[first, current_position] = [0, 0, 255]
    except:
        pass


image = Image.fromarray(data)
image.show()
