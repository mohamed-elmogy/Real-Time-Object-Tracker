# Real-Time-Object-Tracker

This project implements a real-time object tracker using OpenCV in Python. The system allows a user to select an object in the first frame and then tracks it in real-time as it moves.

## Features

- Select an object to track in the first frame.
- Real-time tracking using OpenCV's CSRT tracker.
- Display tracking results in a live video feed.
- Press 'q' to exit the tracking window.

## Requirements

Ensure you have the following installed:

- Python 3.x
- OpenCV

You can install OpenCV using pip:

```sh
pip install opencv-python
```

## Usage

1. Clone the repository:

```sh
git clone [https://github.com/mohamed-elmogy/Real-Time-Object-Tracker]
cd Real-Time-Object-Tracker
```

2. Run the script:

```sh
python real_time_tracker.py
```

3. Select an object in the first frame.
4. The system will track the object in real-time.

## Demo

A recorded demo showcasing the tracking performance is available in the `demo/` folder.

## Implementation Details

- Uses OpenCV's `TrackerCSRT_create()` for high-accuracy tracking.
- Allows users to manually select an object using `cv2.selectROI()`.
- Updates the tracking box in real-time and displays the output.

##


