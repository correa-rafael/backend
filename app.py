from flask import Flask, request, send_file
from flask_cors import CORS
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import io
import onnxruntime as ort

app = Flask(__name__)
CORS(app)

# Load ONNX model
ort_session = ort.InferenceSession('model_rtdetr_r18vd_6x_orig.onnx')

@app.route('/detect_qr_codes', methods=['POST'])
def detect_qr_codes():
    # Check if the POST request has a file part
    if 'image' not in request.files:
        return 'No image found in request', 400

    image_file = request.files['image']

    # Ensure file is an image
    if not image_file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        return 'Uploaded file is not an image', 400

    # Load image
    image = Image.open(image_file).convert('RGB')
    image_resized = image.resize((640, 640))
    image_data = np.array(image_resized, dtype=np.float32) / 255.0
    image_data = np.expand_dims(image_data.transpose(2, 0, 1), axis=0)
    size = np.array([[640, 640]], dtype=np.int64)

    # Perform inference
    output = ort_session.run(None, {'images': image_data, "orig_target_sizes": size})
    labels, boxes, scores = output

    # Draw bounding boxes on the original image
    draw = ImageDraw.Draw(image)
    threshold = 0.4

    for i in range(image_data.shape[0]):
        scr = scores[i]
        lab = labels[i][scr > threshold]
        scaled_boxes = boxes[i][scr > threshold]

        for j, b in enumerate(scaled_boxes):
            # Rescale bounding boxes to match the original image size
            b[0] *= (image.width / 640)
            b[1] *= (image.height / 640)
            b[2] *= (image.width / 640)
            b[3] *= (image.height / 640)

            # Draw bounding boxes
            draw.rectangle(b, outline='red', width=5)
            
    # Save the image in memory
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    image_bytes.seek(0)

    return send_file(image_bytes, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)