from flask import Flask, render_template, request
from OCR_utils import load, finalResult, sortResult
from OCR_utilsB import testOCR, finalResultB

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/build')
def build():
    return render_template("result.html")


@app.route('/ocr_result', methods=['POST', 'GET'])
def ocr_result():
    print(request.form['uri'])
    result = sortResult(finalResult(load(request.form['uri'])))
    # result = finalResult(load(request.form['uri']))
    print(result)

    return render_template("result.html", result=result)


@app.route('/ocr_resultB', methods=['POST', 'GET'])
def ocr_resultB():
    checkL, resultL, unitL, refL, \
    checkR, resultR, unitR, refR = finalResultB(request.form['uri'])

    check = checkL + checkR
    result = resultL + resultR
    unit = unitL + unitR
    ref = refL + refR

    return render_template("resultB.html", check=check, result=result, unit=unit, ref=ref)


@app.errorhandler(500)
def internal_error(error):
    return render_template("err.html")


if __name__ == '__main__':
    app.run()
