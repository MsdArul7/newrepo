import cv2
import os

# Use an absolute path or make sure the path is correct relative to your working directory
video_path = "birthday_video.mp4"  # Replace with the actual path to your video file

# Check if the file exists before trying to open it
if not os.path.exists(video_path):
    print(f"Error: The file '{video_path}' does not exist.")
    print(f"Current working directory: {os.getcwd()}")
else:
    # Initialize the video capture object
    cap = cv2.VideoCapture(video_path)
    
    # Check if the video file was opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open video file. The file may be corrupted or in an unsupported format.")
    else:
        # Read and display video frames
        while True:
            success, frame = cap.read()
            if not success:
                break
            cv2.imshow("Birthday Video", frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break
        
        # Release resources
        cap.release()
        cv2.destroyAllWindows()