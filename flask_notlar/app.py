from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Basit bir veri yapısı ile notları saklamak
notlar = []

@app.route('/')
def index():
    return render_template('index.html', notlar=notlar)

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        baslik = request.form['baslik']
        icerik = request.form['icerik']
        notlar.append({'baslik': baslik, 'icerik': icerik})
        return redirect(url_for('index'))
    return render_template('add_note.html')

@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    if 0 <= note_id < len(notlar):
        del notlar[note_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
