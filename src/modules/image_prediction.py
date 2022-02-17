import os

from imageai.Classification import ImageClassification


def predict_image(args):

    execution_path = os.getcwd()
    image_path = args.get("image")

    prediction = ImageClassification()
    prediction.setModelTypeAsMobileNetV2()
    prediction.setModelPath(os.path.join(
        execution_path, "assets/binaries/mobilenet_v2.h5"))
    prediction.loadModel(classification_speed="fast")

    predictions, probabilities = prediction.classifyImage(
        os.path.join(execution_path, image_path), result_count=5)

    return predictions, probabilities


if __name__ == "__main__":
    from args_parser import args_parser

    args = args_parser()

    predictions, probabilities = predict_image(args)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction, " : ", eachProbability)
