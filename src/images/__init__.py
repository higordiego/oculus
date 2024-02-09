
import cv2
from PIL import Image
from PIL.ExifTags import TAGS
from pillow_heif import register_heif_opener

register_heif_opener()

from src.helpers import is_cuda_cv, calculate_hash

def extract_info_image(image_path):
    print('[x] - Segue o resultado abaixo\n')
    image = Image.open(image_path)
    info_dict = {
        "Filename": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1)
    }

    for label,value in info_dict.items():
        print(f"{label:25}: {value}")

    exifdata = image.getexif()

    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:25}: {data}")

    file_hash = calculate_hash(image_path)
    if file_hash:
        print("hash                     :", file_hash)
        print("\n")


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

    enhanced_image = sr.upsample(image)
    enhanced_image = cv2.resize(enhanced_image,dsize=None, fx=8,fy=8)

    return enhanced_image
