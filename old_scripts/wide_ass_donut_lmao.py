import bpy
import math

scene = bpy.context.scene
car = bpy.data.objects['car']
pendulum = bpy.data.objects['pendulum']

# Parameters
radius = 5
total_frames = 240  # 120 for each circle
car_z = car.location.z

for frame in range(1, total_frames + 1):
    scene.frame_set(frame)
    
    # Calculate angle for circle motion
    if frame <= 120:
        t = frame
        direction = 1  # forward
    else:
        t = 240 - frame
        direction = -1  # reverse
    
    angle = t * 0.05 * direction
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    
    # Update car position
    car.location.x = x
    car.location.y = y
    car.location.z = car_z
    car.keyframe_insert(data_path="location")
    
    # Update car rotation to face movement direction
    heading = math.atan2(
        radius * math.sin(angle + 0.05),
        radius * math.cos(angle + 0.05)
    )
    car.rotation_euler[2] = heading + (math.pi if direction == -1 else 0)  # flip if reversing
    car.keyframe_insert(data_path="rotation_euler", index=2)
    
    # Simulate pendulum (fake swing)
    pendulum_angle = 0.3 * math.sin(frame * 0.15)
    pendulum.rotation_euler[1] = -pendulum_angle
    pendulum.keyframe_insert(data_path="rotation_euler", index=1)
