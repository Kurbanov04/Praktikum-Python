import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon, Rectangle, Polygon
import itertools as itr 
import numpy as np
import copy
import math

#Визуализация фигур
def visualization(cor1: int, cor2: int, *n_array: list, numVertices = 6, radius_for_polygons = 1, common_visual = False):
    # Создаем фигуру и оси
    fig, ax = plt.subplots()

    # Задаем пределы осей
    ax.set_xlim(cor1, cor2)
    ax.set_ylim(cor1, cor2)

    # Рисуем оси координат
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    # Добавляем цифры на оси X
    for x in range(cor1, cor2+1):
        if x != 0:
            ax.text(x + 0.1, -0.5, str(x), fontsize=5, color='k')

    # Добавляем цифры на оси Y
    for y in range(cor1, cor2+1):
        if y != 0:
            ax.text(-0.5, y + 0.1, str(y), fontsize=5, color='k', ha='right', va='center')

    #Условие для визуализаций
    for array in n_array:
        if common_visual:          
            shape = Polygon(array, edgecolor="k")
            ax.add_patch(shape)
    
        else: 
            for arr in array:
                if len(arr) > 2:
                    shape = Polygon(arr, edgecolor="k")
                    ax.add_patch(shape)
                
                elif len(arr) <= 2:
                    shape = RegularPolygon(arr, numVertices = numVertices , radius=radius_for_polygons, facecolor="blue", edgecolor="black")
                    ax.add_patch(shape)
        
    plt.show()
       
#Генератор прямоугольников
def gen_rectangle(count: int, growth = 0, distance_between = 1, vertical = False):
    
    n = 0
    array_positive = []
    array_negative = []
    for i in range(count):
       
        if vertical:
            array_positive += [[[growth, i+n], [growth+2, i+n], [growth+2, i+1+n], [growth, i+1+n]]]
            array_negative += [[[growth, -i-n-1], [growth+2, -i-n-1], [growth+2, -i-2-n], [growth, -i-2-n]]]
        
        else:
            array_positive += [[[i+n, growth], [i+n, growth+2], [i+1+n, growth+2], [i+1+n, growth]]]
            array_negative += [[[-i-n-1, growth], [-i-n-1, growth+2], [-i-2-n, growth+2], [-i-2-n, growth]]]
        
        n += distance_between

    array = array_positive + array_negative
    return array

#visualization(-15, 15, gen_rectangle(10, 5, vertical = True))

#Генератор триугольников
def gen_triangle(count: int, growth = 0, distance_between = 1.5, vertical = False):

    n = 0
    array_positive = []
    array_negative = []
    for i in range(count):

        if vertical:
            array_positive += [[[growth, i+n], [growth+2, i+1+n], [growth, i+2+n]]]
            array_negative += [[[growth, -i-n-0.5], [growth+2, -i-1.5-n,],[growth, -i-2.5-n]]]
        
        else:
            array_positive += [[[i+n, growth], [i+1+n, growth+2], [i+2+n, growth]]]
            array_negative += [[[-i-n-0.5, growth], [-i-1.5-n, growth+2],[-i-2.5-n, growth]]]

        n += distance_between

    array = array_positive + array_negative
    return array

#visualization(-15, 15, gen_triangle(10))

#Генератор шестиугольников
def gen_hexagon(count: int, growth = 0, distance_between = 1.5, vertical = False):

    n = 0
    array_positive = []
    array_negative = []
    for i in range(count):
        
        if vertical:
            array_positive += [[growth+1, i+n+0.9]]
            array_negative += [[growth+1, -i-n-1.5]]

        else:
            array_positive += [[i+n+0.9, growth+1]]
            array_negative += [[-i-n-1.5, growth+1]]
        
        n += distance_between 

    array = array_positive + array_negative
    return array

#visualization(-10, 10, gen_hexagon(10, 5, vertical = True), gen_hexagon(10, 2, vertical = True))
#visualization(-10, 10, [[0,0],[0,1],[1,1],[1,0]], common_visual = True)

#Паралельнная проекция
def tr_translate(array: list, x = 0, y = 0):

    new_array = copy.deepcopy(array)     #Модуль copy для глубокого копирования

    for arr in new_array:
        if len(arr) > 2:
            for i in arr:
                i[0] += x
                i[1] += y
                        
        elif len(arr) <= 2:
            arr[0] += x
            arr[1] += y

    return new_array

#visualization(-10, 10, tr_translate(gen_rectangle(10),x = 1, y = 5))

#Поворот фигур
def tr_rotate(array: list, corner = 0, vertical = False):
    new_array = copy.deepcopy(array)     #Модуль copy для глубокого копирования
    array_positive = new_array[:int(len(new_array)/2)]
    array_negative = new_array[int(len(new_array)/2):]  

    n = 0
    for arr1 in array_positive:
        if vertical:
            if len(arr1) > 2:
                for i in arr1:
                    if corner >= 0:
                        i[0] += n
                    elif corner < 0:
                        i[0] += n-2
                           
            elif len(arr1) <= 2:
                if corner >= 0:
                    arr1[0] += n
                elif corner < 0:
                    arr1[0] += n-2
    
        else:
            if len(arr1) > 2:
                for i in arr1:
                    if corner >= 0:
                        i[1] += n
                    elif corner < 0:
                        i[1] += n-2
                           
            elif len(arr1) <= 2:
                if corner >= 0:
                    arr1[1] += n
                elif corner < 0:
                    arr1[1] += n-2
        n += corner
    
    n = 0
    for arr2 in array_negative:
        if vertical:
            if len(arr2) > 2:
                for i in arr2:
                    if corner >= 0:
                        i[0] += -n-2
                    elif corner < 0:
                        i[0] += -n
                           
            elif len(arr2) <= 2:
                if corner >= 0:
                    arr2[0] += -n-2
                elif corner < 0:
                    arr2[0] += -n
    
        else:
            if len(arr2) > 2:
                for i in arr2:
                    if corner >= 0:
                        i[1] += -n-2
                    elif corner < 0:
                        i[1] += -n
                           
            elif len(arr2) <= 2:
                if corner >= 0:
                    arr2[1] += -n-2
                elif corner < 0:
                    arr2[1] += -n
        n += corner


    return array_positive + array_negative

#visualization(-15,15, tr_rotate(gen_rectangle(6,vertical = True), corner = -2, vertical = True))

#Симметрия фигур
def tr_symmetry(array: list, center_of_symmetry = 0, vertical = False):
    new_array = copy.deepcopy(array)     #Модуль copy для глубокого копирования

    for arr in new_array:
        if len(arr) > 3:
            for i in arr:
                if vertical:
                    i[0] += center_of_symmetry
                else:
                    i[1] += center_of_symmetry

        elif len(arr) == 3:
            just_value = [2,-2,2]
            for num,i in enumerate(arr):
                if vertical:
                    i[0] += center_of_symmetry + just_value[num]
                else:
                    i[1] += center_of_symmetry + just_value[num]              
                        
        elif len(arr) <= 2:
            if vertical:
                arr[0] += center_of_symmetry
            else:
                arr[1] += center_of_symmetry

    return new_array

#visualization(-15,15, tr_symmetry(gen_triangle(6), center_of_symmetry = 3))
#visualization(-15,15, gen_triangle(6), tr_symmetry(gen_triangle(6), center_of_symmetry = 3))

#Гомотетия фигур
def tr_homothety(array: list, corner = 0, index = 0):
    new_array = copy.deepcopy(array)     #Модуль copy для глубокого копирования
    array_positive = new_array[:int(len(new_array)/2)]
    array_negative = new_array[int(len(new_array)/2):]   

    n = 0
    k = 0
    for arr1 in array_positive:

        if len(arr1) > 3:
            rn_lst = [0,0,k,k]
            for num,i in enumerate(arr1):
                if corner >= 0:
                    i[1] += n
                elif corner < 0:
                    i[1] += n-2
                i[0] += rn_lst[num]

        elif len(arr1) == 3:
            rn_lst = [0,n,n+n]
            for num,i in enumerate(arr1):
                if corner >= 0:
                    i[1] += n
                elif corner < 0:
                    i[1] += n-2
                i[0] += rn_lst[num]
        
        n += corner
        k += index
    
    n = 0
    k = 0
    for arr2 in array_negative:
            
        if len(arr2) > 3:
            rn_lst = [0,0,-k,-k]
            for num,i in enumerate(arr2):
                if corner >= 0:
                    i[1] += -n-2
                elif corner < 0:
                    i[1] += -n
                i[0] += rn_lst[num]

        elif len(arr2) == 3:
            rn_lst = [0,-n,-n-n]
            for num,i in enumerate(arr2):
                if corner >= 0:
                    i[1] += -n-2
                elif corner < 0:
                    i[1] += -n

                i[0] += rn_lst[num]
                   
        n += corner
        k += index


    return array_positive + array_negative

#visualization(-15,15, tr_homothety(gen_rectangle(6),corner = 4, index = 1))

#Фильтрации фигур, являющихся выпуклыми многоугольниками
def flt_convex_polygon(array: list):
    new_array = []

    for arr in array:

        if len(arr) > 3:
            if len(arr) == 4:
                new_array += [arr]

        elif len(arr) == 3:
            if len(arr) == 3:
                new_array += [arr]
            
        elif len(arr1) <= 2:
            if len(arr) == 2:
                new_array += [arr]

    return new_array

#print(flt_convex_polygon(gen_triangle(4)))

#Фильтрации фигур, имеющих хотя бы один угол, совпадающий с заданной точкой 
def flt_angle_point(array: list, point: list):   #point = [1, 1]
    new_array = []

    for arr in array:
        if len(arr) > 3:
            for i in arr:
                if i == point:
                    new_array += [arr]

        elif len(arr) == 3:
            for i in arr:
                if i == point:
                    new_array += [arr]
            
        elif len(arr1) <= 2:
            if arr == point:
                new_array += [arr]

    return new_array

#print(flt_angle_point(gen_triangle(4), point = [1,2]))

#Фильтрации выпуклых многоугольников, включающих заданную точку (внутри многоугольника) 
def flt_point_inside(array: list, point: list):       #point = [1, 1]
    new_array = []

    for arr in array:
        if len(arr) > 3:
            if len(arr) == 4:
                for i in arr:
                    if i == point:
                        new_array += [arr]

        elif len(arr) == 3:
            for i in arr:
                if len(arr) == 3:
                    if i == point:
                        new_array += [arr]
            
        elif len(arr1) <= 2:
            if len(arr) == 2:
                if arr == point:
                    new_array += [arr]

    return new_array

#print(flt_point_inside(gen_triangle(4), point = [1,2]))

#Фильтрации выпуклых многоугольников, включающих любой из углов заданного многоугольника
def flt_polygon_angeles_inside(array: list, *points: list):       #point = [1, 1]
    new_array = []

    for arr in array:
        if len(arr) > 3:
            if len(arr) == 4:
                for i in arr:
                    for point in points:
                        if i == point:
                            new_array += [arr]

        elif len(arr) == 3:
            for i in arr:
                if len(arr) == 3:
                    for point in points:
                        if i == point:
                            new_array += [arr]
            
        elif len(arr1) <= 2:
            if len(arr) == 2:
                for point in points:
                    if arr == point:
                        new_array += [arr]

    return new_array

#print(flt_polygon_angeles_inside(gen_triangle(4), [1,2]))

#Cклейки полигонов в одну последовательность полигонов из нескольких последовательностей полигонов      
def zip_polygons(*arrays: list):

    if len(arrays) == 1:
        return "Функция работает с несколькими массивами"

    result = []
    for polygons in zip(*arrays):
        merged_polygon = []
        for polygon in polygons:
            merged_polygon.extend(polygon)
        result.append(merged_polygon)
    return result

#print(zip_polygons([((1,1), (2,2), (3,1)), ((11,11), (12,12), (13,11))], [((1,-1), (2,-2), (3,-1)), ((11,-11), (12,-12), (13,-11))]))

#Генерация значений по старту и шагу
def count_2D(start1: int, start2: int, count: int, step1 = 0, step2 = 0): 

    array = [[start1,start2]]
    for arr in range(count):
        array += [[start1 + (step1*(arr+1)), start2 + (step2*(arr+1))]]

    return array

#print(count_2D(start1 = 1, start2 = 1, count = 2, step1 = 1, step2 = 2))

#Cклейки полигонов в одну последовательность полигонов из нескольких последовательностей 
def zip_tuple(*arrays: list):
    return list(zip(*arrays))

#print(zip_tuple([(1,1),  (2,2), (3,3), (4,4)], [(2,2), (3,3), (4,4), (5,5)], [(3,3), (4,4), (5,5), (6,6)]))

#Поиск угла, самого близкого к началу координат 
def arg_origin_nearest(points: list):  # points -> [(2,2), (3,3), (4,4), (5,5)]
    nearest_point = points[0]
    nearest_distance = math.sqrt(nearest_point[0]**2 + nearest_point[1]**2)

    for point in points[1:]:
        distance = math.sqrt(point[0]**2 + point[1]**2)
        if distance < nearest_distance:
            nearest_point = point
            nearest_distance = distance

    return nearest_point

#print(arg_origin_nearest([(2, 3), (4, 1), (1, 5), (3, 2)]))



        



