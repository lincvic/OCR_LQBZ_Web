# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 16:01
# @Author  : Lincvic
# @Email   : lincvic@yahoo.com
# @File    : OCR_utils.py
# @SoftwareName: PyCharm

import pytesseract as te
from PIL import Image
import re
import cv2
import numpy


def tesseract_ocr(image):
    '''

    OCR识别
    :param image: PIL Image
    :return result: String

    '''
    image = Image.fromarray(image)
    result = te.image_to_string(image, config="digits")
    strInfo = re.compile(' ')
    result = strInfo.sub('', result)

    return result


def selfBinary(gray):
    '''

    二值化
    :param gray:PIL Image
    :return  bin:openCV Binary Image

    '''
    gray = cv2.cvtColor(numpy.asarray(gray), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

    T, bin = cv2.threshold(gray, 248, 255, cv2.THRESH_BINARY)

    return bin


def load(uri):
    '''

    读取图片，返回PIL 图片
    :param uri: Image Path
    :return PIL Image

    '''

    return Image.open(uri)


def selfCrop(x, y, w, h, image):
    '''

    PIL切图
    :param x:
    :param y:
    :param w:
    :param h:
    :param image: PIL image
    :return: openCV Binary image
    '''
    return selfBinary(image.crop((x, y, x + w, y + h)))


def finalResult(image):
    '''

    OCR最终结果
    :param image: PIL image
    :return: result: List
    '''
    result = []
    origin = []

    origin.append(selfCrop(294, 35, 53, 22, image))
    origin.append(selfCrop(294, 58, 53, 22, image))
    origin.append(selfCrop(294, 83, 53, 22, image))
    origin.append(selfCrop(294, 108, 53, 22, image))
    origin.append(selfCrop(294, 132, 53, 22, image))
    origin.append(selfCrop(294, 155, 53, 22, image))
    origin.append(selfCrop(296, 180, 51, 22, image))
    origin.append(selfCrop(294, 206, 53, 22, image))
    origin.append(selfCrop(294, 231, 53, 22, image))
    origin.append(selfCrop(294, 257, 53, 22, image))
    origin.append(selfCrop(294, 282, 53, 22, image))
    origin.append(selfCrop(294, 306, 53, 22, image))

    origin.append(selfCrop(880, 35, 53, 22, image))
    origin.append(selfCrop(880, 58, 53, 22, image))
    origin.append(selfCrop(880, 83, 53, 22, image))
    origin.append(selfCrop(880, 108, 49, 22, image))
    origin.append(selfCrop(880, 132, 53, 22, image))
    origin.append(selfCrop(880, 157, 53, 22, image))
    origin.append(selfCrop(880, 182, 53, 22, image))
    origin.append(selfCrop(880, 208, 53, 22, image))
    origin.append(selfCrop(880, 233, 53, 22, image))
    origin.append(selfCrop(880, 259, 53, 22, image))
    origin.append(selfCrop(880, 284, 53, 22, image))
    origin.append(selfCrop(880, 308, 53, 22, image))

    for index, item in enumerate(origin):
        temp = tesseract_ocr(item)
        if temp != '':
            result.append(temp)
        else:
            cv2.imwrite("static/images/" + str(index) + ".png", item)
            result.append(str(index) + ".png")
    return result


def sortResult(result):
    '''

    处理结果，与参考值做对比，未识别的保存图片
    :param result
    :return: result

    '''

    makeChange(result, 0, 4, 10)
    makeChange(result, 1, 3.5, 5.0)
    makeChange(result, 2, 110, 150)
    makeChange(result, 3, 35, 45)
    makeChange(result, 4, 100, 300)
    makeChange(result, 5, 82, 95)
    makeChange(result, 6, 27, 31)
    makeChange(result, 7, 320, 360)
    makeChange(result, 8, 39, 46)
    makeChange(result, 9, 11.5, 15)
    makeChange(result, 10, 2.0, 7.0)
    makeChange(result, 11, 50, 70)
    makeChange(result, 12, 1.18, 3.74)
    makeChange(result, 13, 20, 40)
    makeChange(result, 14, 0.2, 1.0)
    makeChange(result, 15, 3, 10)
    makeChange(result, 16, 0.05, 0.3)
    makeChange(result, 17, 1, 6)
    makeChange(result, 18, 0.01, 0.08)
    makeChange(result, 19, 0.1, 1.2)
    makeChange(result, 20, 13, 43)
    makeChange(result, 21, 7.6, 13.2)
    makeChange(result, 22, 9, 18.1)
    makeChange(result, 23, 0.16, 0.4)

    return result


def makeChange(result, i, min, max):
    '''

    :param result: 结果 List
    :param i: 索引
    :param min: 最小值
    :param max: 最大值
    :return: 处理之后结果

    '''

    if result[i].endswith(".png"):
        pass
    elif float(result[i]) < min:
        result[i] = "↓" + result[i]
    elif float(result[i]) > max:
        result[i] = "↑" + result[i]

    return result

# TODO 数据库


if __name__ == '__main__':
    '''
    
    测试
    
    '''

    gray = load("/Users/wong/Documents/Internship/OCRPROJ/Sample/finalSample.png")
    result = finalResult(gray)
    print(sortResult(result))
