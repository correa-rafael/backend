# QR Code Detection Backend

The QR Code Detection Backend is a server-side application responsible for handling image processing tasks and detecting QR codes within uploaded images. It utilizes [RT-DETR](https://github.com/lyuwenyu/RT-DETR), a Transformer-based AI model for real-time object detection, fine-tuned to accurately identify QR codes.

## Features

- **QR Code Detection:** Utilizes the fine-tuned RT-DETR model to detect QR codes within uploaded images.
- **Flask API:** Built with Flask, a micro web framework in Python, the backend provides endpoints for image upload and QR code detection.

## Technologies Used

- **Flask:** A lightweight and flexible web framework for Python, Flask powers the backend of the QR Code Detection Backend, providing a robust foundation for handling image processing and serving API endpoints.
- **ONNX Runtime:** Integrates the RT-DETR model using ONNX Runtime, enabling efficient and accurate object detection for QR codes.

## Deployment

The backend of the QR Code Detection is deployed on the [Adaptable](https://qr-detection-app-backend.adaptable.app) platform, ensuring reliable and scalable performance for handling image processing tasks and serving API requests. It works in conjunction with the frontend application, with the frontend handling user interactions and the backend performing the heavy lifting of image processing and AI-based QR code detection. The frontend is deployed on [Vercel](https://qr-detection-app.vercel.app/), implemented in the [qr-detection-app](https://github.com/correa-rafael/qr-detection-app/) repository.

## Installation

To run the QR Code Detection Backend locally, follow these steps:

1. Clone this repository.
2. Navigate to the project directory.
3. Install dependencies using `pip install -r requirements.txt`.
4. Start the Flask server using `python app.py`.

## Usage

To use the QR Code Detection Backend, developers can interact with the provided API endpoints to upload images and receive detection results for QR codes within the images.

## Contributing

Contributions to the QR Code Detection Backend are welcome! Whether it's through opening a pull request, submitting an issue, or providing feedback, your contributions help enhance and improve the backend for all users.
