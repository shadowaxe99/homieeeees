```python
from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename
import os
from src.video_upload import uploadVideo
from src.video_processing import processVideo
from src.object_detection import detectObjects
from src.object_tracking import trackObjects
from src.null_object_generation import generateNullObjects

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    video_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return 'File uploaded successfully'

@app.route('/process', methods=['GET'])
def process_file():
    video_file = request.args.get('video_file')
    processed_video = processVideo(video_file)
    detected_objects = detectObjects(processed_video)
    tracked_objects = trackObjects(detected_objects)
    null_objects = generateNullObjects(tracked_objects)
    return send_from_directory(app.config['JSX_FOLDER'], null_objects)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
```
