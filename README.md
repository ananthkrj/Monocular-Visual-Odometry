# Monocular Visual Odometry

What is Visual Odometry:
- When we have a camera attached to a moving object and want a construct a trajectory using the video stream coming from the camera
- The act of using just one camera for this is called Monocular Visual Odometry
- in Monocular VO, can only measure movement by a singular unit, for example moved one unit in x, two units in y
- This is useful for small robots

The Problem:
Want to input stream of images, capture transition of these frames from state t to t + 1.Then find R (rotation matrix) and t (translation vector) which will describe motion of vector between two frames

Algorithm Outline:
- Capture the Images t and t + 1 which are frames
of gray scale images captured at certain times
- Undistort the images
- FAST algorithm used to detect featured in t, and track those features to t + 1. New detection triggered if features in transition drop below a threshold
- Nister's 5 point algorithm with RANSAC used to compute essential matrix
- Estimate R and t from essential matrix.

Don't need to distort with KITTI dataset

## FAST Feature Detection
-  Find corner, set test corner to point P. Draw a circle around the point. Bunch every pixel around circumference of point into a set. If intensity of that set of pixels exceeds original pixel point by a factor of I, that point is a corner.
