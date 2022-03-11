import os
import shutil

xml_dir = "/media/qisens/2tb1/python_projects/inference_pr/tfrecord-viewer/new_dataset_overfitting_test13_riverarea_area123/train/new_data/anno_new_data"
img_dir = "/media/qisens/2tb1/python_projects/training_pr/R2CNN_Faster_RCNN_Tensorflow/data/io/origin/robndbox/png/train/annotations"
new_img_dir = "/media/qisens/2tb1/python_projects/inference_pr/tfrecord-viewer/new_dataset_overfitting_test13_riverarea_area123/train/new_data/img_new_data"

for path, dirs, files in os.walk(xml_dir):
    for file in files:
        new_filename = file.replace("xml", "png")
        img_path = os.path.join(img_dir, new_filename)
        if os.path.exists(img_path):
            shutil.move(img_path, new_img_dir