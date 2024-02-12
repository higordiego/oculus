import cv2
import os
from src.helpers import is_cuda_cv


def extract_frames_and_process(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)
        frame_count += 1
    cap.release()
    cv2.destroyAllWindows()
    return frame_count

def super_resolve_video(input_video, output_video, model_path, name):
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(model_path)

    model_version = model_path.split('_')[1].split('.')[0] if len(model_path.split('_')) > 1 else 'x3'
    model_name = model_path.split('/')[-2] if '/' in model_path else model_path.split('_')[0]

    scale_factor = int(model_version[1])

    sr.setModel(model_name, scale_factor)

    if is_cuda_cv() > 0:
        sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

    video_capture = cv2.VideoCapture(input_video)
    output_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH) * scale_factor)
    output_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT) * scale_factor)
    output_fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    output_fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_video_writer = cv2.VideoWriter(output_video, output_fourcc, output_fps, (output_width, output_height))

    try:
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            sr_frame = sr.upsample(frame)
            output_video_writer.write(sr_frame)
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário.")
        sys.exit(0)
    finally:
        video_capture.release()
        output_video_writer.release()
        cv2.destroyAllWindows()
