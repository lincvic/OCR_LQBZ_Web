# -*- coding: utf-8 -*-
# @Time    : 2018/7/26 11:46
# @Author  : Lincvic
# @Email   : lincvic@yahoo.com
# @File    : OCR_utilsB.py
# @SoftwareName: PyCharm

import cv2
from aip import AipOcr
from PIL import Image


def loadImagePIL(filePath):
    '''

    PIL 读取图片
    :param filePath:
    :return:

    '''
    return Image.open(filePath)


def loadImage(filePath):
    '''

    openCV 读取图片
    :param filePath: Image Path
    :return: cv2 image

    '''

    return cv2.imread(filePath)


def getImage(filePath):
    '''

    ocr 读取图片Binary
    :param filePath: inner Image Path
    :return: binary image

    '''

    with open(filePath, 'rb') as fp:
        return fp.read()


def ocr(filePath):
    '''

    ocr 处理图片
    :param filePath: Image Path
    :return: result

    '''

    APP_ID = ''
    API_KEY = ''
    SECRET_KEY = ''

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    image = getImage(filePath)

    result = client.basicAccurate(image)
    return result


def selfCrop(x, y, w, h, image):
    '''

    切图
    :param x:
    :param y:
    :param w:
    :param h:
    :param image:
    :return: 图片

    '''

    image = image.crop((x, y, x + w, y + h))
    image.save("static/tempImage/temp.png")

    return image


def finalResultB(filePath):
    '''

    处理图片
    :param image: PIL Image
    :return: result

    '''

    image = loadImagePIL(filePath)
    checkLResult = []
    checkRResult = []
    resultLResult = []
    resultRResult = []
    unitLResult = []
    unitRResult = []
    refLResult = []
    refRResult = []

    checkL = selfCrop(50, 650, 850, 1100, image)
    checkLResult = setResult()

    resultL = selfCrop(950, 630, 200, 1130, image)
    resultLResult = setResult()

    unitL = []
    unitL.append(selfCrop(1230, 620, 200, 100, image))
    unitLResult.append(setResult()[0])
    unitL.append(selfCrop(1230, 735, 250, 100, image))
    unitLResult.append(setResult()[0])
    unitL.append(selfCrop(1230, 830, 250, 100, image))
    unitLResult.append(setResult()[0])
    unitL.append(selfCrop(1230, 925, 250, 100, image))
    unitLResult.append(setResult()[0])
    unitL.append(selfCrop(1230, 1020, 250, 100, image))
    unitLResult.append(setResult()[0])
    unitL.append(selfCrop(1230, 1115, 250, 100, image))
    unitLResult.append(setResult()[0])
    unitL.append(selfCrop(1230, 1210, 250, 100, image))
    unitLResult.append(setResult()[0])
    unitL.append(selfCrop(1230, 1295, 250, 100, image))
    unitLResult.append(setResult()[0])
    unitL.append(selfCrop(1230, 1385, 250, 100, image))
    unitLResult.append(setResult()[0])
    unitL.append(selfCrop(1230, 1475, 250, 100, image))
    unitLResult.append(setResult()[0])
    unitL.append(selfCrop(1230, 1565, 250, 100, image))
    unitLResult.append(setResult()[0])
    unitL.append(selfCrop(1230, 1655, 250, 100, image))
    unitLResult.append(setResult()[0])

    refL = selfCrop(1470, 620, 500, 1150, image)
    refLResult = setResult()

    checkR = selfCrop(2000, 620, 800, 1150, image)
    checkRResult = setResult()
    resultR = selfCrop(3000, 620, 200, 1150, image)
    resultRResult = setResult()
    unitR = []
    unitR.append(selfCrop(3230, 620, 200, 100, image))
    unitRResult.append(setResult()[0])
    unitR.append(selfCrop(3230, 735, 290, 100, image))
    unitRResult.append(setResult()[0])
    unitR.append(selfCrop(3230, 830, 290, 100, image))
    unitRResult.append(setResult()[0])
    unitR.append(selfCrop(3230, 925, 290, 100, image))
    unitRResult.append(setResult()[0])
    unitR.append(selfCrop(3230, 1010, 290, 100, image))
    unitRResult.append(setResult()[0])
    unitR.append(selfCrop(3230, 1100, 290, 100, image))
    unitRResult.append(setResult()[0])
    unitR.append(selfCrop(3230, 1190, 290, 100, image))
    unitRResult.append(setResult()[0])
    unitR.append(selfCrop(3230, 1280, 290, 100, image))
    unitRResult.append(setResult()[0])
    unitR.append(selfCrop(3230, 1370, 290, 100, image))
    unitRResult.append(setResult()[0])
    unitR.append(selfCrop(3230, 1460, 290, 100, image))
    unitRResult.append(setResult()[0])
    unitR.append(selfCrop(3230, 1550, 290, 100, image))
    unitRResult.append(setResult()[0])
    unitR.append(selfCrop(3230, 1640, 290, 100, image))
    unitRResult.append(setResult()[0])
    refR = selfCrop(3520, 600, 400, 1120, image)
    refRResult = setResult()

    return checkLResult, resultLResult, unitLResult, refLResult, \
           checkRResult, resultRResult, unitRResult, refRResult


def setResult():
    '''

    处理结果
    :return: result

    '''

    result = []
    temp = ocr("static/tempImage/temp.png")
    for item in temp['words_result']:
        result.append(item['words'])

    return result



