```python
from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from src.video_upload import uploadVideo
from src.video_processing import processVideo
from src.object_detection import detectObjects
from src.object_tracking import trackObjects
from src.null_object_generation import generateNullObjects

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        video_file = request.files['video-upload']
        filename = secure_filename(video_file.filename)
        video_file.save(os.path.join('uploads', filename))
        uploadVideo(filename)
        return redirect(url_for('processing', filename=filename))

@app.route('/processing/<filename>')
def processing(filename):
    processVideo(filename)
    return redirect(url_for('detection', filename=filename))

@app.route('/detection/<filename>')
def detection(filename):
    detected_objects = detectObjects(filename)
    return redirect(url_for('tracking', filename=filename, detected_objects=detected_objects))

@app.route('/tracking/<filename>/<detected_objects>')
def tracking(filename, detected_objects):
    tracked_objects = trackObjects(filename, detected_objects)
    return redirect(url_for('generation', filename=filename, tracked_objects=tracked_objects))

@app.route('/generation/<filename>/<tracked_objects>')
def generation(filename, tracked_objects):
    null_objects = generateNullObjects(filename, tracked_objects)
    return render_template('result.html', null_objects=null_objects)

if __name__ == '__main__':
    app.run(debug=True)
```