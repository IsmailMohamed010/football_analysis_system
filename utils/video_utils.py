import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Could not open video file: {video_path}")
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames


def save_video(output_frames, output_path):
    if not output_frames:
        raise ValueError("No frames to save.")
    
    height, width, layers = output_frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 24.0, (width, height))

    for frame in output_frames:
        out.write(frame)
    
    out.release()
    print(f"Video saved to {output_path}")