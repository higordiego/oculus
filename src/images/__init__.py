
import cv2

from src.helpers import is_cuda_cv

def enhance_image(image_path, model_path, name):
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(model_path)

    model_version = name.split('_')[1] if len(name.split('_')) > 1 else 'x3'
    model_name = name.split('/')[-2] if '/' in name else name.split('_')[0]

    scale_factor = int(model_version[1])

    sr.setModel(model_name, scale_factor)
    if is_cuda_cv() > 0:
        sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
    

    image = cv2.imread(image_path)
    image = image.astype('float32') / 255.0
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

    enhanced_image = sr.upsample(image)
    enhanced_image = (enhanced_image * 255.0).astype('uint8')

    return enhanced_image
