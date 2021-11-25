from flask import Flask, request, render_template, app
import numpy as np
from skimage.feature import greycomatrix, greycoprops
application = Flask(__name__)
image = np.random.randint(0, 5, size=(4, 4))
print(image)
dist = [1]
angg = [0]
sol = greycomatrix(image, [1], [0., np.pi / 4., np.pi / 2., 3. * np.pi / 4.], levels=image.max() + 1)
matrixGlcm = sol[:, :, 0, 0]
print(matrixGlcm)
print(sol[:, :, 0, 1])
@application.route('/')
def hello_world():
    return render_template('ViewGLCM.html', Matrix1=image, GlcmMatrix=matrixGlcm, Distance=1, Angle=0)
@application.route('/', methods=['POST'])
def my_form_post():
    distance = int(request.form['disttvall'])
    print(distance)
    angle = request.form['anggvall']
    valang = 0
    print(angle)
    if angle == "45":
        valang = 3*np.pi/4
    elif angle == "90":
        valang = np.pi/2
    elif angle == "135":
        valang = np.pi/4
    print(valang)
    res = greycomatrix(image, [distance], [valang], levels=image.max() + 1)
    matrixres = np.transpose(res[:, :, 0, 0])
    return render_template('ViewGLCM.html', Matrix1=image, GlcmMatrix=matrixres, Distance=distance, Angle=angle)
@application.route('/glcm')
def glcm_ui():
    return render_template('ViewGLCM.html', Matrix1=image, GlcmMatrix=matrixGlcm)
if __name__ == '__main__':
    application.run()

