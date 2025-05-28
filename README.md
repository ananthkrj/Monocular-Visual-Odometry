# Monocular Visual Odometry

What is Visual Odometry:
- When we have a camera attached to a moving object and want a construct a trajectory using the video stream coming from the camera
- The act of using just one camera for this is called Monocular Visual Odometry
- in Monocular VO, can only measure movement by a singular unit, for example moved one unit in x, two units in y
- This is useful for small robots
- In short Monocular Visual Odometry is crucial as it enables vehicles/Robots to estimate their positions and form a trajectory using images through a singular camera

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
-  Find corner, set test corner to point P. Draw a circle around the point.
- Set a threshold value t 
- Bunch every pixel around circumference of point into a set. 
- If intensity of that set of pixels exceeds original pixel point by a factor of I, meaning those set of pixels are clearly darker or lighter than p. P is a corner.

## Feature Detection
- Use KLT tracker in OpenCV to look around every corner to be tracked, and uses this to find the corner in next image.
- Need to perform feature re-detection as we will lose some points when detecting.

## Essential Matrix
- To form the essential matrix use the five point algorithm which solves number of non linear equations and requied minimum number of points possible.

## Ransac
- Use RANSAC to handle outliers, which is an iterative algorithm
- At every iteration it sample 5 points from the set of corresponding points, estimates essential matrix, then checks to make sure the other points are not outliers when compared to the esential matrix
- Done in one line through OpenCV

## How to Compute R, t from essential matrix
- use recover Pose, with E (essential matrix), 2 points, R, t, focal, pp, and mask as parameters

## Trajectory Tracking
- Pose of the camera is denoted by R_pos and t_pos, can track the trajectory using a formation of equations

## Heuristics
- A heuristic is a guiding principle used to simplify a complex problem that can come up 
- A heurestic here would be, the forward direction is always a priority. As a hypothetical case where the robot/vehicle stops due to an intersecting object. This could lead the algoirthm to believe the vehicle itself is moving sideways due to the motion of the intersecting object. By setting forward as dominant direction this situation is avoided. 