from flask import Flask,render_template,request
from model import out

app=Flask(__name__)
    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/output', methods=['POST'])
def output():
    if request.method == 'POST':
        audio_file = request.files['audio']
        predicted_emotion = out(audio_file)
        return render_template('output.html', predicted_emotion=predicted_emotion)

if __name__ =='__main__':
    app.run(debug=True)