import os
import cv2
import numpy as np
import argparse
import uuid


parser = argparse.ArgumentParser(description="Extract keyframes from videos in a specified folder")
parser.add_argument("-i", "--input", help="input folder with video files", required=True)
parser.add_argument("-o", "--output", help="output folder with keyframes", default="keyframes")
parser.add_argument("-d", "--difference", help="keyframe's percentage of difference from a previous frame",
                    default=75, type=int)
args = parser.parse_args()

def extract_keyframes(video_path, out_dir_path, change_ratio):
    """
    Extracts keyframes from a video by diffing two adjacent frames
    :param video_path:
    :param change_ratio: by which two frames differ (0.0 - 0%, 1.0 - 100% difference)
    :param out_dir_path: where to save extracted keyframes
    :return:
    """
    frame_count = 0
    cap = cv2.VideoCapture(video_path)
    ret, previous_frame = cap.read()
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    total_pixels = width * height
    pixels_changed_threshold = total_pixels * change_ratio

    while ret:
        ret, current_frame = cap.read()

        if ret:
            diff = cv2.absdiff(current_frame, previous_frame)
            pixels_changed = np.count_nonzero(diff)
            if pixels_changed > pixels_changed_threshold * 3:
                percent_changed = int(round(pixels_changed / total_pixels / 3, 2) * 100)
                # print("%s%% of the image changed" % percent_changed)
                out_name = "%s_%s_%s.jpg" % (os.path.splitext(os.path.basename(video_path))[0], frame_count, uuid.uuid4().hex[:6])
                keyframe_dir_path = os.path.join(out_dir_path, video_path.split(os.sep)[-1])
                if not os.path.isdir(keyframe_dir_path):
                    os.makedirs(keyframe_dir_path)
                out_path = os.path.join(keyframe_dir_path, out_name)
                cv2.imwrite(out_path, current_frame)
            previous_frame = current_frame
            frame_count += 1


if __name__ == "__main__":
    if not os.path.isdir(args.output):
        os.makedirs(args.output)
    try:
        for path, subdirs, files in os.walk(args.input):
            for name in files:
                file_path = os.path.join(path, name)
                if file_path.endswith(".mp4") or file_path.endswith(".webm"):
                    print("Extracting keyframes from:", file_path)
                    extract_keyframes(file_path, args.output, args.difference / 100)
    except Exception as e:
        print(str(e))
