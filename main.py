import scipy
from PIL import Image, ImageDraw
from scipy import ndimage
import numpy as np
import random
from math import sqrt
import sys
from Class_Object import MyObject


def polyton(width, height, draw, pix):
    for i in range(width):
        for j in range(height):
            a_1 = pix[i, j][0]
            b_1 = pix[i, j][1]
            c_1 = pix[i, j][2]
            S_1 = (a_1 + b_1 + c_1) // 3
            draw.point((i, j), (S_1, S_1, S_1))
    return


def tobinary(width, height, draw, pix):
    # factor = 100
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if S / 3 > 180:
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
    return


def BinPoly(Name, Name_to):
    image = Image.open(Name)  # Открываем изображение.
    draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.
    pix = image.load()  # Выгружаем значения пикселей.
    polyton(width, height, draw, pix)
    image.save('image/poly_' + Name_to, "JPEG")
    tobinary(width, height, draw, pix)
    image.save('image/bin_' + Name_to, "JPEG")
    del draw
    return


def tobinary_errosiu(image):
    draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.
    pix = image.load()  # Выгружаем значения пикселей.
    # factor = 100
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if S > 180:
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
    return


def tobinary_2(image):
    draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.
    pix = image.load()  # Выгружаем значения пикселей.
    # factor = 100
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if S > 230:
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
    return


def myfilter(Name):
    path = Name  # Your image path
    img = Image.open(path)
    width = img.size[0]  # Определяем ширину.
    height = img.size[1]  # Определяем высоту.
    members = [(0, 0)] * 9
    newimg = Image.new("RGB", (width, height), "white")
    for i in range(1, width - 1):
        for j in range(1, height - 1):
            members[0] = img.getpixel((i - 1, j - 1))
            members[1] = img.getpixel((i - 1, j))
            members[2] = img.getpixel((i - 1, j + 1))
            members[3] = img.getpixel((i, j - 1))
            members[4] = img.getpixel((i, j))
            members[5] = img.getpixel((i, j + 1))
            members[6] = img.getpixel((i + 1, j - 1))
            members[7] = img.getpixel((i + 1, j))
            members[8] = img.getpixel((i + 1, j + 1))
            members.sort()
            newimg.putpixel((i, j), (members[4]))
    newimg.save(Name, 'JPEG')
    return


def mydelot(name):
    image = Image.open(name)  # Открываем изображение.
    draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.
    pix = image.load()  # Выгружаем значения пикселей.
    for i in range(1, width - 1):
        for j in range(1, height - 1):
            if pix[i, j][0] == 0 and pix[i, j + 1][0] != 0:
                draw.point((i, j), (255, 255, 255))
            if pix[i, j][0] != 0 and pix[i, j - 1][0] == 0:
                draw.point((i, j - 1), (255, 255, 255))
            if pix[i, j][0] == 0 and pix[i + 1, j][0] != 0:
                draw.point((i + 1, j), (255, 255, 255))
            if pix[i, j][0] != 0 and pix[i - 1, j][0] == 0:
                draw.point((i - 1, j), (255, 255, 255))
    image.save(name, "JPEG")
    return


def Obrabotka():
    print("Binarizacia")
    BinPoly('hard/hard_2.jpg', 'test.jpg')

    i = 0
    # while i < 5:
    #     print("median filter  i =", i)
    #     myfilter('image/bin_test.jpg')
    #     i += 1

    im = Image.open('image/bin_test.jpg')
    tobinary_2(im)
    im.save('image/bin_test.jpg', 'JPEG')

    print("Erosia")
    im = Image.open('image/bin_test.jpg')
    im = ndimage.binary_erosion(im).astype(np.uint)
    scipy.misc.imsave('image/erosion_1.jpg', im)

    im = Image.open('image/erosion_1.jpg')
    tobinary_errosiu(im)
    im.save('image/erosion_bin.jpg', 'JPEG')

    im = Image.open('image/erosion_bin.jpg')
    im = ndimage.binary_erosion(im).astype(np.uint)

    scipy.misc.imsave('image/erosion_2.jpg', im)
    im = Image.open('image/erosion_2.jpg')
    tobinary_errosiu(im)
    im.save('image/erosion_2_bin.jpg', 'JPEG')

    im = Image.open('image/erosion_2_bin.jpg')
    im = ndimage.binary_erosion(im).astype(np.uint)
    scipy.misc.imsave('image/erosion_3.jpg', im)
    im = Image.open('image/erosion_3.jpg')
    tobinary_errosiu(im)
    im.save('image/erosion_3_bin.jpg', 'JPEG')

    im = Image.open('image/erosion_3_bin.jpg')
    im = ndimage.binary_erosion(im).astype(np.uint)
    scipy.misc.imsave('image/erosion_3_2.jpg', im)

    im = Image.open('image/erosion_3_2.jpg')
    tobinary_errosiu(im)
    im.save('image/erosion_3_2_bin.jpg', 'JPEG')

    # mydelot('image/erosion_3_2_bin.jpg')
    #
    # im = Image.open('image/erosion_3_2_bin.jpg')
    # tobinary_2(im)
    # im.save('image/result.jpg', 'JPEG')

    print("Filter")
    i = 0
    while i < 5:
        print("median filter  i =" , i)
        myfilter('image/erosion_3_2_bin.jpg')
        i += 1
    print("Binarizacia_resultata")
    im = Image.open('image/erosion_3_2_bin.jpg')
    tobinary_2(im)
    im.save('image/result.jpg', 'JPEG')

    return


def SetCompactness(Objects):
    for i in Objects:
        i.CalcCompactness()
    return


def recursive_poisk(matr, pix, row, line, index, maxH, maxW):
    if pix[row, line][0] > 200 and matr[row][line] == 0:

        if row >= maxW - 1 or line >= maxH - 1:
            return

        if row == 0 or line == 0:
            return

        matr[row][line] = index

        recursive_poisk(matr, pix, row - 1, line, index, maxH, maxW)
        recursive_poisk(matr, pix, row, line - 1, index, maxH, maxW)
        recursive_poisk(matr, pix, row + 1, line, index, maxH, maxW)
        recursive_poisk(matr, pix, row, line + 1, index, maxH, maxW)

    return


def SaveResult(matr):
    im = Image.new("RGB", (width, height), color='black')
    draw = ImageDraw.Draw(im)  # Создаем инструмент для рисования.
    for i in range(1, width - 1):
        for j in range(1, height - 1):
            if matr[i][j] > 0:
                draw.point((i, j), (255, 255, 255))
    im.save("image/result_search.jpg")
    return


def Poisk():
    image_1 = Image.open('image/result.jpg')  # Открываем изображение.
    #image_1 = Image.open("image/result_delot_bin.jpg")  # Открываем изображение.
    width_1 = image.size[0]  # Определяем ширину.
    height_1 = image.size[1]  # Определяем высоту.
    pix = image_1.load()  # Выгружаем значения пикселей.
    matr = np.zeros((width_1, height_1), np.int_)
    index = 1
    for i in range(15, width_1 - 15):
        for j in range(15, height_1 - 15):
            recursive_poisk(matr, pix, i, j, index, height_1, width_1)
            index += 1
    return matr



def InitObject(matrix_1, width_1, height_1):
    List_Object = []
    List_Index = []
    List_Index_Count = []

    for i in range(1, width_1 - 1):
        for j in range(1, height_1 - 1):
            if matrix_1[i][j] != 0:
                if List_Index.count(matrix_1[i][j]) == 0:
                    List_Object.append(MyObject(matrix_1[i][j], 1, 1))
                    List_Index.append(matrix_1[i][j])
                    List_Index_Count.append(list((matrix_1[i][j], 1, 1)))
                else:
                    for tm in range(0, len(List_Index_Count)):
                        if List_Index_Count[tm][0] == matrix_1[i][j]:
                            List_Index_Count[tm][1] = List_Index_Count[tm][1] + 1
                            if matrix_1[i][j - 1] == 0 or matrix_1[i][j + 1] == 0 or matrix_1[i - 1][j] == 0 or \
                                    matrix_1[i + 1][j] == 0:
                                List_Index_Count[tm][2] = List_Index_Count[tm][2] + 1

    result = []
    for i in range(0, len(List_Object)):
        List_Object[i].square = List_Index_Count[i][1]
        List_Object[i].perimeter = List_Index_Count[i][2]
        if List_Object[i].square > 30:#                            // подумать надо ли
            result.append(List_Object[i])
    return result


def K_means(List_Obj, num):
    num_classter = num

    List_Centroid = []

    List_Rand = []
    succ_iter = 0

    while succ_iter != num_classter:
        temp_classter = random.randint(0, len(List_Object) - 1)
        if List_Rand.count(temp_classter) == 0:
            tm = MyObject(0, List_Obj[temp_classter].square, List_Obj[temp_classter].perimeter)
            tm.CalcCompactness()
            tm.elongation = List_Obj[temp_classter].elongation
            List_Centroid.append(tm)
            succ_iter += 1

    finish = 0

    List_Distance = []
    count = 0
    while finish != 1:

        count += 1
        for i in range(0, len(List_Obj)):
            for j in range(0, len(List_Centroid)):
                List_Distance.append(sqrt((List_Obj[i].square - List_Centroid[j].square) ** 2  + (List_Obj[i].perimeter - List_Centroid[j].perimeter) ** 2 + (List_Obj[i].compactness - List_Centroid[j].compactness) ** 2  + (List_Obj[i].elongation - List_Centroid[j].elongation) ** 2 ))              #без делотации


            List_Obj[i].claster = List_Distance.index(min(List_Distance))
            List_Distance.clear()

        for i in List_Centroid:
            i.perimeter = i.square = i.compactness = 0

        for i in range(0, len(List_Obj)):
            List_Centroid[List_Obj[i].claster].square += List_Obj[i].square
            List_Centroid[List_Obj[i].claster].perimeter += List_Obj[i].perimeter
            List_Centroid[List_Obj[i].claster].compactness += List_Obj[i].compactness
            List_Centroid[List_Obj[i].claster].elongation += List_Obj[i].elongation

        for i in range(0, len(List_Centroid)):
            num_obj_in_claster = 1
            for j in List_Obj:
                if j.claster == i:
                    num_obj_in_claster += 1
            List_Centroid[i].square = List_Centroid[i].square / num_obj_in_claster
            List_Centroid[i].perimeter = List_Centroid[i].perimeter / num_obj_in_claster
            List_Centroid[i].compactness = List_Centroid[i].compactness / num_obj_in_claster
            List_Centroid[i].elongation = List_Centroid[i].elongation / num_obj_in_claster
        if count == 5:
            break
    return


def RGB_Result(List_obj, matr):
    claster_0 = (255, 0, 0)
    claster_1 = (0, 255, 0)
    claster_2 = (0, 0, 255)
    claster_3 = (255, 255, 0)
    claster_4 = (0, 255, 255)
    im = Image.new("RGB", (width, height), color='black')
    draw = ImageDraw.Draw(im)  # Создаем инструмент для рисования.
    List_index_claster = []

    for i in List_obj:
        List_index_claster.append((i.index, i.claster))

    for i in range(1, width - 1):
        for j in range(1, height - 1):
            if matr[i][j] != 0:
                for ob in List_index_claster:
                    if matr[i][j] == ob[0]:
                        if ob[1] == 0:
                            draw.point((i, j), claster_0)
                        if ob[1] == 1:
                            draw.point((i, j), claster_1)
                        if ob[1] == 2:
                            draw.point((i, j), claster_2)
                        if ob[1] == 3:
                            draw.point((i, j), claster_3)
                        if ob[1] == 4:
                            draw.point((i, j), claster_4)
    im.save("image/result_search_RGB.jpg")
    return


def Elongation(matrix_1, List_Object_1, width_1, height_1):

    rev_index_1 = [0,0]
    rev_index_2 = [0,0]
    rev_index_3 = [0, width_1]
    rev_index_4 = [0, height_1]

    for tm in range(0, len(List_Object)):
        first_index = 0
        for i in range(0, width_1 - 1):
            for j in range(0,height_1 - 1):
                if first_index == 0 and matrix_1[i][j] == List_Object_1[tm].index:
                    rev_index_1 = [i, j]
                    first_index = 1;
                if matrix_1[i][j] == List_Object_1[tm].index:
                    if i > rev_index_2[0] and j > rev_index_1[1]: # ??????????7
                        rev_index_2 = [i, j]
                    if i < rev_index_3[0] and j > rev_index_2[0]:
                        rev_index_3 = [i,j]
                    if i > rev_index_4[0] and j < rev_index_4[0]:
                        rev_index_4 = [i,j]
        tmp_elongation = sqrt((rev_index_1[0] - rev_index_2[0]) ** 2 + (rev_index_1[1] - rev_index_2[1]) ** 2)/sqrt((rev_index_3[0] - rev_index_4[0])**2 + (rev_index_3[1]-rev_index_4[1])**2)
        List_Object_1[tm].elongation = tmp_elongation
    return

def printobj(List_Object_1):
    for i in range(0, len(List_Object_1)):
        print("index - ", List_Object_1[i].index, " square - ", List_Object_1[i].square, " perimetr - ",
              List_Object_1[i].perimeter, " compactness - ", List_Object_1[i].compactness, " claster - ",
              List_Object_1[i].claster, " elongation - ", List_Object_1[i].elongation)
    return

sys.setrecursionlimit(50000)
Obrabotka()

image = Image.open('image/result.jpg')  # Открываем изображение.
#image = Image.open("image/result_delot_bin.jpg")  # Открываем изображение.
width = image.size[0]  # Определяем ширину.
height = image.size[1]  # Определяем высоту.

print("Poisk")
matrix = Poisk()
print("Save")
SaveResult(matrix)

print("Init")
List_Object = InitObject(matrix, width, height)
SetCompactness(List_Object)
Elongation(matrix, List_Object, width, height)
print("Введите количество кластеров n >= 2")
num_classter = int(input())

print("K-means")
K_means(List_Object, num_classter)
print("Save_rgb")
RGB_Result(List_Object, matrix)

