import os

from imageai.Prediction import ImagePrediction

execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath(os.path.join(
    execution_path, "assets/binaries/mobilenet_v2.h5"))
prediction.loadModel()

predictions, probabilities = prediction.classifyImage(
    os.path.join(execution_path, "assets/images/car.jpg"), result_count=5)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction, " : ", eachProbability)
