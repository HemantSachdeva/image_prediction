from modules.args_parser import args_parser
from modules.image_prediction import predict_image
from modules.object_detection import detect_object

args = args_parser()

if args.get("predict") is not None:
    predictions, probabilities = predict_image(args)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction, " : ", eachProbability)

elif args.get('detect') is not None:
    detections, objects_path = detect_object(args)
    for eachObject, eachObjectPath in zip(detections, objects_path):
        print(eachObject.get("name"), " : ", eachObject.get("percentage_probability"),
              " : ", eachObject.get("box_points"))
        print("Object's image saved in " + eachObjectPath)
        print("--------------------------------")
