from moviepy.editor import *
import webbrowser
from threading import Timer
import os
from flask import *
from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilename
import os

path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'uploads')
ALLOWED_EXTENSIONS = {'exe','dll'}

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

dir = UPLOAD_FOLDER
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

app = Flask(__name__)
app.secret_key = 'nouman'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def upload1():  
    root=Tk()
    root.attributes('-topmost', 1)
    Tk().withdraw()
    filename = askdirectory()
    print(filename)
    root.destroy()  

    path=filename

    root=Tk()
    root.attributes('-topmost', 1)
    Tk().withdraw()
    path2 = askdirectory()
    print(path2)
    root.destroy()  

    list = os.listdir(path)

    for f in list:
        # print(path+f)
        # ff,fg=f.split(".")
        print(list)
        new=path2+'/'+f+".mp3"
        # print(new)
        try:
            videoclip = VideoFileClip(path+'/'+f)

            audioclip = videoclip.audio
            
            audioclip.write_audiofile(new)

            audioclip.close()
            videoclip.close()
            a="SUCCESSFULLY DONE"
        except:
            a="ERROR"
            pass
    
    return render_template("result.html", disp=a)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def open_browser():
    webbrowser.open_new('http://127.0.0.1:2000/')


if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(port=2000, debug=True, threaded=True, use_reloader=False)