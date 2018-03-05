import cv2
import numpy as np

train_file = 'train.txt'
data_directory = '/Users/nicholasjoodi/Documents/ucdavis/computerScience/VisualRecognition/diagrams_with_google_label/'
default_image_size = 224
stats_file = 'stats.txt'
with open(train_file, 'r') as _file:
    rows = _file.readlines()
    size = len(rows)
    # size = 20
    np_reports = np.empty((size, default_image_size, default_image_size,3))
    np_satelites = np.empty((size, default_image_size, default_image_size,3))
    for i in range(size):
        image_files = rows[i].strip().split('\t')
        # print(data_directory+image_files[0])
        img_report = cv2.resize(cv2.imread(data_directory+image_files[0]), (default_image_size,default_image_size))
        # print(np.shape(img_report))
        img_satelite = cv2.resize(cv2.imread(data_directory+image_files[1]), (default_image_size,default_image_size))
        np_reports[i] = img_report
        np_satelites[i] = img_satelite
    print('report statistics')
    print(np.shape(np_reports))
    mean, std = np.zeros((3), dtype=np.float32),np.zeros((3), dtype=np.float32)
    mean = np.mean(np_reports,(0,1,2))
    std = np.std(np_reports,(0,1,2))
    print(mean)
    print(std)
    print('satelite statistics')
    mean_satelite = np.mean(np_satelites,(0,1,2))
    std_satelite = np.std(np_satelites,(0,1,2))
    print(mean_satelite)
    print(std_satelite)
with open(stats_file, 'w') as s_file:
    s_file.write("report statistics:\n")
    s_file.write(" - mean:")
    s_file.write(str(mean)+'\n')
    s_file.write(" - std:")
    s_file.write(str(std)+'\n\n')
    s_file.write("satelite statistics:\n")
    s_file.write(" - mean:")
    s_file.write(str(mean_satelite)+'\n')
    s_file.write(" - std:")
    s_file.write(str(std_satelite))