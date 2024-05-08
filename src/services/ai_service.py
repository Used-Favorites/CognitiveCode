from typing import Sequence
import cv2
from cv2.dnn import Net, MatLike


def detect_objects(image_path: str) -> None:
    # Load YOLO
    net: Net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    layer_names: Sequence[str] = net.getLayerNames()
    output_layers: list = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # Load image
    img: MatLike = cv2.imread(image_path)
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels: int = img.shape

    # Detecting objects
    # Rest of the code...
    blob: MatLike = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs: Sequence[MatLike] = net.forward(output_layers)

    # Rest of the code...
    cv2.waitKey(0)
    cv2.destroyAllWindows()
