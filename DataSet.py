from os import listdir
from os.path import isfile

import numpy as np

import ELAConverter


def PreProcess(image_path):
    return np.array(ELAConverter.convert_to_ela_image(image_path, 90).resize((128, 128))).flatten() / 255.0

def getDataSet(DataSetType):
    X = [] # Images
    Y = [] # 0 = fake, 1 = real

    if(DataSetType == 0):
        TestOrTrain = 'train'
    else:
        TestOrTrain = 'test'

    path = TestOrTrain+'/REAL'
    print(path);

    allFiles = []
    for f in listdir(path):
        if(isfile(path + '/'+ f)):
            allFiles.append(path + '/'+ f);
    
    for file in allFiles:
        if file.endswith('jpg') or file.endswith('png'):
            X.append(PreProcess(file))        
            Y.append(1)     # label for authentic images 
            
    print(f'Total images: {len(X)}\nTotal labels: {len(Y)}')


    path = TestOrTrain+'/FAKE'
    print(path);

    allFiles = []
    for f in listdir(path):
        if(isfile(path + '/'+ f)):
            allFiles.append(path + '/'+ f);
    
    for file in allFiles:
        if file.endswith('jpg') or file.endswith('png'):
            X.append(PreProcess(file))        
            Y.append(0)     # label for authentic images 
            
    print(f'Total images: {len(X)}\nTotal labels: {len(Y)}')

    X = np.array(X)
    Y = np.array(Y)
    X = X.reshape(-1, 128, 128, 3)

    return X, Y