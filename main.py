from utils import read_video, save_video
from Trackers import tracker
def main():
    video_frames = read_video("input/08fd33_4.mp4")
    print(f"Read {len(video_frames)} frames from the video.")
 
    # Initialize tracker and process video frames
    video_tracker = tracker("models/best.pt")
    video_tracker.get_object_tracks(video_frames)

    save_video(video_frames, "processed_video.avi")

if __name__ == "__main__":
    main()