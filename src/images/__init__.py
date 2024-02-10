
import cv2
from PIL import Image
from PIL.ExifTags import TAGS
from pillow_heif import register_heif_opener
from PIL.ExifTags import GPSTAGS
import urllib.parse

register_heif_opener()

from src.helpers import is_cuda_cv, calculate_hash

def get_exif(file_name):
    image: Image.Image = Image.open(file_name)
    return image.getexif()


def get_geo(exif):
    for key, value in TAGS.items():
        if value == "GPSInfo":
            break
    gps_info = exif.get_ifd(key)
    return {
        GPSTAGS.get(key, key): value
        for key, value in gps_info.items()
    }

def get_url_google_maps(latitude_decimal, longitude_decimal):
    google_maps_url = f"https://www.google.com/maps/search/?api=1&query={latitude_decimal},{longitude_decimal}"
    return urllib.parse.quote(google_maps_url, safe=':/?&=')

def get_params_geo(geo):
    refLat = geo['GPSLatitudeRef']
    refLng = geo['GPSLongitudeRef']

    lat = geo['GPSLatitude']
    lng = geo['GPSLongitude']
    
    latitude_decimal = dms_to_decimal(lat, refLat)
    longitude_decimal = dms_to_decimal(lng, refLng)
    return get_url_google_maps(latitude_decimal, longitude_decimal)
    
def dms_to_decimal(dms, direction):
    degrees, minutes, seconds = dms
    decimal = degrees + minutes/60 + seconds/3600
    if direction in ['S', 'W']:
        decimal *= -1
    elif direction in ['E', 'N']:
        decimal *= 1
    return decimal

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

    max_label_length = max(len(label) for label in info_dict.keys())

    for label, value in info_dict.items():
        print(f"{label:{max_label_length}}: {value}")

    exifdata = image.getexif()

    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode()

        print(f"{tag:{max_label_length}}: {data}")

    geo = get_geo(exifdata)
    
    
    for item in geo:
        data = geo.get(item)
        
        print(f"{item:{max_label_length}}: {data}")

    file_hash = calculate_hash(image_path)
    print(f"{'maps':{max_label_length}}: {get_params_geo(geo)}\n") 
    if file_hash:
        print(f"{'hash':{max_label_length}}: {file_hash}\n")
    

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
    
    return enhanced_image
