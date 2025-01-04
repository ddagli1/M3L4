# İçeri Aktar
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Form sonuçları 
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # seçilen resmi almak
        selected_image = request.form.get('image-selector')

        # Görev #2. Metni almak
        text_top = request.form.get('textTop')
        text_bottom = request.form.get('textBottom')

        # Görev #3. Metnin konumunu almak
        text_top_y = request.form.get('textTop_y')
        text_bottom_y = request.form.get('textBottom_y')

        # Görev #3. Metnin rengini almak
        selected_color = request.form.get('color-selector')

        return render_template('index.html', 
                               # Seçilen resmi görüntüleme
                               selected_image=selected_image, 

                               # Görev #2. Metni görüntüleme
                               text_top=text_top,
                               text_bottom=text_bottom,


                               # Görev #3. Rengi görüntüleme
                               selected_color = selected_color,
                               
                               # Görev #3. Metnin konumunu görüntüleme
                               text_top_y = text_top_y,
                               text_bottom_y = text_bottom_y

                               )
    else:
        # Varsayılan olarak ilk resmi görüntüleme
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True, port=8080)
