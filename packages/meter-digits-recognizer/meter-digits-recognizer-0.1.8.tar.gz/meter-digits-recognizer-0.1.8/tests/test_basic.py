import os
import cv2
from meter_digits_recognizer import MeterDigitsRecognizer

def test_meter_digits_recognition():
    images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images")
    img_filenames = [
        "0/1_hot_water_meter_20210212_065239.jpg",
        "1/1_cold_water_meter_20210210_215613.jpg",
        "2/6_cold_water_meter_20210307_221149.jpg",
        "3/6_cold_water_meter_20210210_121529.jpg",
        "4/6_cold_water_meter_20210212_123308.jpg",
        "5/7_cold_water_meter_20210128_013005.jpg",
        "6/6_cold_water_meter_20210210_134531.jpg",
        "7/6_cold_water_meter_20210209_202508.jpg",
        "8/6_cold_water_meter_20210209_080446.jpg",
        "9/5_cold_water_meter_20210209_100446.jpg",
        "10/7_cold_water_meter_20210126_160005.jpg",
    ]

    # Read images
    images = []
    for filename in img_filenames:
        img = cv2.imread(os.path.join(images_dir, filename))
        images.append(img)

    dr = MeterDigitsRecognizer()
    predictions, confidences = dr.run(images)
    print("predictions", predictions)
    print("confidences", confidences)
    assert len(predictions) == len(images)
    assert all([predicted == truth for predicted, truth in zip(predictions, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])])
