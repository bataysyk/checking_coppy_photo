from PIL import Image, ImageChops
import os
import shutil

checklist = []

def check(dirname, dirway):
    global photo_2
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

        count_1 = 0
        count_2 = 0
        for photo_1 in checklist[:]:
            count_1 += 0
            try:
                for photo_2 in checklist[:]:
                    count_2 += 1
                    print(len(checklist))
                    print(f"{count_1} : {count_2}")
                    #print(photo_1)
                    #print(photo_2)
                    image_1 = Image.open(photo_1)
                    image_2 = Image.open(photo_2)
                    #try:
                    #result.show()
                    if photo_1 != photo_2:
                        result = ImageChops.difference(image_1, image_2)
                        if result.getbbox() == None:
                            where = os.path.basename(photo_1)
                            print(where)
                            print("="*50)
                            shutil.move(photo_1, "/home/dima/Picture/the_same/" + where)
                            checklist.remove(photo_2)
                        #except ValueError:
                            #print("="*30 )
                            #print("Images do not match!!!")
                            #print("="*30 )
            except FileNotFoundError:
                checklist.remove(photo_2)
                checklist.remove(photo_1)
                print("No such file or directory: ")

check("/home/dima/Picture", "/home/dima/Picture/the_same")
#Вычисляет ограничивающую рамку ненулевых областей на изображении.

# result.getbbox() в данном случае вернет (0, 0, 888, 666)
#result.save("/home/dima/Picture/image/result.jpg")

#
