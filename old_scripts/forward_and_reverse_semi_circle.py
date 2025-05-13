import bpy
import math

scene = bpy.context.scene
car = bpy.data.objects['car']
pendulum = bpy.data.objects['pendulum']

# Parameters
wheelbase = 2.5  # adjust to your model scale
steering_angle = math.radians(25)  # tighter turn
velocity = -0.2  # start in reverse
total_frames = 240
car_z = car.location.z

# Initial state
x, y = 0.0, 0.0
heading = math.radians(90)  # facing +Y

# Store path so we can retrace it later
path = []

for frame in range(1, total_frames + 1):
    scene.frame_set(frame)

    # First 120 frames: reverse driving
    if frame <= 120:
        v = velocity
    else:
        v = -velocity  # switch to forward after 120 frames

    # Save/retrieve path
    if frame <= 120:
        # Calculate new position and heading
        x += v * math.cos(heading)
        y += v * math.sin(heading)
        heading += (v / wheelbase) * math.tan(steering_angle)

        # Store the path to reverse later
        path.append((x, y, heading))
    else:
        # Replay path in reverse
        rev_frame = 240 - frame  # reverse index (0 to 119)
        x, y, heading = path[rev_frame]

    # Apply position and rotation
    car.location = (x, y, car_z)
    car.rotation_euler = (0, 0, heading)
    car.keyframe_insert(data_path="location")
    car.keyframe_insert(data_path="rotation_euler", index=2)

    # Pendulum (cosmetic swing)
    swing = 0.3 * math.sin(frame * 0.25)
    pendulum.rotation_euler[1] = -swing
    pendulum.keyframe_insert(data_path="rotation_euler", index=1)
