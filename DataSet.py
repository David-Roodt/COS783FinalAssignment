import numpy as np
from os import listdir
from os.path import isfile, join

def getDataSet(DataSetType):
    X = [] # Images
    Y = [] # 0 = fake, 1 = real

    if(DataSetType == 0):
        TestOrTrain = 'Train'
    else:
        TestOrTrain = 'Test'

    path = TestOrTrain+'/REAL'

    allFiles = [f for f in listdir(path) if isfile(join(path, f))]
    for file in allFiles:
        if file.endswith('jpg') or file.endswith('png'):
            X.append(prepare_image(file))        
            Y.append(1)     # label for authentic images 
            
    print(f'Total images: {len(X)}\nTotal labels: {len(Y)}')


    path = TestOrTrain+'FAKE'       #folder path of the forged images in the dataset

    allFiles = [f for f in listdir(path) if isfile(join(path, f))]
    for file in allFiles:
        if file.endswith('jpg') or file.endswith('png'):
            X.append(prepare_image(file))        
            Y.append(1)     # label for authentic images 
            
    print(f'Total images: {len(X)}\nTotal labels: {len(Y)}')

    X = np.array(X)
    Y = np.array(Y)
    X = X.reshape(-1, 128, 128, 3)

    return X, Y