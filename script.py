import bpy
import math

scene = bpy.context.scene
car = bpy.data.objects['car']
pendulum = bpy.data.objects['pendulum']

# Reset transforms
car.location = (0, 0, car.location.z)
pendulum.rotation_euler = (0, 0, 0)

for frame in range(1, 121):  # 120 frames
    scene.frame_set(frame)
    
    # Simulate a sine wave oscillation for the pendulum
    angle = 0.5 * math.sin(frame * 0.1)  # in radians
    
    # Set pendulum rotation (around Y axis)
    pendulum.rotation_euler[1] = -angle
    pendulum.keyframe_insert(data_path="rotation_euler", index=1)
    
    # Move car (make it move more visibly)
    car.location.x += 0.05 * math.cos(frame * 0.1)
    car.keyframe_insert(data_path="location", index=0)
    
    print(f"Frame {frame}: angle={angle:.2f}, car_x={car.location.x:.2f}")
