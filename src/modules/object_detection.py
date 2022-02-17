import os

from imageai.Detection import ObjectDetection


def detect_object(args):

    execution_path = os.getcwd()
    image_path = args.get("image")
    output_path = args.get("output")

    detector = ObjectDetection()
    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath(os.path.join(
        execution_path, "assets/binaries/yolo-tiny.h5"))
    detector.loadModel()

    detections, objects_path = detector.detectObjectsFromImage(input_image=os.path.join(
        execution_path, image_path), output_image_path=os.path.join(execution_path, output_path),
        minimum_percentage_probability=30, extract_detected_objects=True)

    return detections, objects_path


if __name__ == "__main__":
    from args_parser import args_parser

    args = args_parser()

    detections, objects_path = detect_object(args)
    for eachObject, eachObjectPath in zip(detections, objects_path):
        print(eachObject.get("name"), " : ", eachObject.get("percentage_probability"),
              " : ", eachObject.get("box_points"))
        print("Object's image saved in " + eachObjectPath)
        print("--------------------------------")
