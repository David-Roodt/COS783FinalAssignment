import numpy as np
import os
from tqdm.notebook import tqdm

def getTrainSet():
    X = [] # Images
    Y = [] # 0 = fake, 1 = real


    path = 'train/REAL'
    for filename in tqdm(os.listdir(path),desc="Processing Images : "):
        if filename.endswith('jpg') or filename.endswith('png'):
            full_path = os.path.join(path, filename)
            X.append(prepare_image(full_path))        
            Y.append(1)     # label for authentic images 
            
    print(f'Total images: {len(X)}\nTotal labels: {len(Y)}')


    path = 'train/FAKE'       #folder path of the forged images in the dataset
    for filename in tqdm(os.listdir(path),desc="Processing Images : "):
        if filename.endswith('jpg') or filename.endswith('png'):
            full_path = os.path.join(path, filename)
            X.append(prepare_image(full_path))        
            Y.append(0)     # label for forged images 
            
    print(f'Total images: {len(X)}\nTotal labels: {len(Y)}')

    X = np.array(X)
    Y = np.array(Y)
    X = X.reshape(-1, 128, 128, 3)
    
    return X, Y