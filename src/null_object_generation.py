```python
import json
from src.object_tracking import tracked_objects

null_objects = []

def generateNullObjects():
    global null_objects
    null_objects = []

    for obj in tracked_objects:
        null_object = {
            "position": obj["position"],
            "orientation": obj["orientation"]
        }
        null_objects.append(null_object)

    with open('null_objects.jsx', 'w') as file:
        file.write(json.dumps(null_objects))

    print("nullObjectGenerationComplete")
```