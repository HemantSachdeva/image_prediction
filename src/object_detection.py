import os

from imageai.Detection import ObjectDetection

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(os.path.join(
    execution_path, "assets/binaries/yolo-tiny.h5"))
detector.loadModel()
detections, objects_path = detector.detectObjectsFromImage(input_image=os.path.join(
    execution_path, "assets/images/family.jpg"), output_image_path=os.path.join(execution_path, "assets/images/family-detected.jpg"),
    minimum_percentage_probability=30, extract_detected_objects=True)

for eachObject, eachObjectPath in zip(detections, objects_path):
    print(eachObject.get("name"), " : ", eachObject.get("percentage_probability"),
          " : ", eachObject.get("box_points"))
    print("Object's image saved in " + eachObjectPath)
    print("--------------------------------")
