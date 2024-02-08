import cv2

def is_cuda_cv():
  try:
      count = cv2.cuda.getCudaEnabledDeviceCount()
      if count > 0:
          return 1
      else:
          return 0
  except:
      return 0
