from numba import jit
import os, sys
import shutil
import PIL
from PIL import Image, ImageChops
import time

# задаёт директорию для сортировки
dir_name = os.path.abspath(sys.argv[1])

try:
    new_dir = os.path.abspath(sys.argv[2])
except:
    new_dir = dir_name


@jit(forceobj=True)
def diferents(image_1, image_2):
    ImageChops.difference(image_1, image_2)


def image_sort(dirname, newdir, recur=0):
    if not recur:
        print('sorting started ...')  # если главная папка
    else:
        print('sorting started in %s...' % dirname)  # если подпапка

    # собирает все подпапки в список и рекурсивно обходит
    checklist = []

    if not recur:
        print('sorting completed!')

        if os.path.isdir(dirname):
            for x in os.listdir(dirname):
                print(x)
                absx = dirname + os.sep + x
                if os.path.isfile(absx):
                    checklist.append(absx)
                elif os.path.isdir(absx):
                    for x in os.listdir(absx):
                        adsx_2 = absx + os.sep + x
                        if os.path.isfile(adsx_2):
                            checklist.append(adsx_2)
                        else:
                            print("this file is not file!!! (ще ращ потрібно перевірити чи це діректорія)")

            print(checklist)
            count_1 = 0
            count_2 = 0

            while True:
                try:

                    for photo_1 in checklist[count_1:]:  # resolution_1 = Image.open(photo_1).size
                        count_1 += 1
                        for photo_2 in checklist[count_2:]:
                            count_2 += 1
                            image_1 = Image.open(photo_1)
                            image_2 = Image.open(photo_2)
                            result = diferents(image_1=image_1, image_2=image_2)
                            print(result)  # print(result.getbbox())
                            if result == None:  # .getbbox()
                                print("NONE" * 10)
                                shutil.move(photo_1, "/home/dima/pil_picture/xxx")
                except ValueError:
                    continue
                except shutil.Error:
                    continue
                except FileNotFoundError:
                    print("No such file or directory: ")
                except PIL.UnidentifiedImageError:
                    print("gggggggggggggggggggggg")
                    continue
                print("Перебор закончился!!!")
                time.sleep(2)


if __name__ == '__main__':
    image_sort(dir_name, new_dir)
