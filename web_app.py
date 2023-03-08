import qrcode
from PIL import Image
import cv2
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from flask import Flask, request, render_template
from check import Shelfmanagment

app = Flask(__name__)

shelf = Shelfmanagment()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['query_img']
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
        img = Image.open(file.stream)
        img.save(uploaded_img_path)
        im = cv2.imread(uploaded_img_path)
        outputs = shelf.score_image(im)
        output, data = shelf.make_image(im, outputs)
        html_table = data.to_html()
        plt.imsave('static/output_img.jpeg', output)
        s = 'Total amount pay {}'.format(np.round(sum(data['Net_price']), 2))
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(s)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        text = 'Total amount pay {}'.format(np.round(sum(data['Net_price']), 2))
        img.save("static/QR_code.png")
        qrcodes = 'static/QR_code.png'
        output = 'static/output_img.jpeg'
        text = 'Total amount pay {}'.format(np.round(sum(data['Net_price']), 2))
        return render_template('index.html',
                               query_path=uploaded_img_path,
                               scores=output, table=html_table, qrcodes=qrcodes, text=text)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run("0.0.0.0")
