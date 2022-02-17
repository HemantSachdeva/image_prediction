import os

from imageai.Detection import ObjectDetection

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(os.path.join(
    execution_path, "assets/binaries/yolo-tiny.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(
    execution_path, "assets/images/family.jpg"), output_image_path=os.path.join(execution_path, "assets/images/family-detected.jpg"), minimum_percentage_probability=30)

for eachObject in detections:
    print(eachObject.get("name"), " : ", eachObject.get("percentage_probability"),
          " : ", eachObject.get("box_points"))
    print("--------------------------------")
