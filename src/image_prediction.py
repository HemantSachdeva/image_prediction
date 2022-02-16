import os

from imageai.Classification import ImageClassification

execution_path = os.getcwd()

prediction = ImageClassification()
prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath(os.path.join(
    execution_path, "assets/binaries/mobilenet_v2.h5"))
prediction.loadModel(classification_speed="fast")

predictions, probabilities = prediction.classifyImage(
    os.path.join(execution_path, "assets/images/car.jpg"), result_count=5)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction, " : ", eachProbability)
