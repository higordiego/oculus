import cv2
import hashlib

def is_cuda_cv():
  try:
      count = cv2.cuda.getCudaEnabledDeviceCount()
      if count > 0:
          return 1
      else:
          return 0
  except:
      return 0

def calculate_hash(image_path):
    try:
        with open(image_path, 'rb') as f:
            data = f.read()
            sha256_hash = hashlib.sha256(data).hexdigest()
        return sha256_hash
    except Exception as e:
        print(f"Error calculating hash: {e}")
        return None
