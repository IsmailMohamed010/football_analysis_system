from ultralytics import YOLO
import supervision as sv
class tracker():
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.tracker = sv.ByteTrack()

    def detect_frames(self, frame):
        bathch_size = 20
        detections = []
        for i in range(0, len(frame), bathch_size):
            detections_batch = self.model.predict(frame[i:i + bathch_size],conf=0.1)
            detections += detections_batch
            break
        return detections

    def get_object_tracks(self, frame):
        detections = self.detect_frames(frame)
        
        for frame_num, detection in enumerate(detections):
            cls_name = detection.names
            cls_name_inv = {v: k for k, v in cls_name.items()}
            #print(cls_name)
            # convert detections to sv.Detections
            supervision_detections = sv.Detections.from_ultralytics(detection)

            for object_idx, class_id in enumerate(supervision_detections.class_id):
                if cls_name[class_id] == 'goalkeeper':
                    supervision_detections.class_id[object_idx] = cls_name_inv['player']

            # track objects
            

            print(supervision_detections) 
            break