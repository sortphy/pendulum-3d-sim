import bpy
import math

scene = bpy.context.scene
car = bpy.data.objects['car']
pendulum = bpy.data.objects['pendulum']

# Car parameters
wheelbase = 2.5   # adjust to your car's size
velocity = 0.1    # positive for forward, negative for reverse
steering_angle = math.radians(15)  # fixed turning angle

# Start position
x, y = 0.0, 0.0
heading = math.radians(90)  # facing +Y (adjust if needed)

for frame in range(1, 241):
    scene.frame_set(frame)
    
    # Switch direction at halfway
    if frame == 121:
        velocity = -velocity  # reverse direction
    
    # Update position
    x += velocity * math.cos(heading)
    y += velocity * math.sin(heading)
    
    # Update heading using turning radius formula
    heading += (velocity / wheelbase) * math.tan(steering_angle)
    
    # Apply to Blender object
    car.location = (x, y, car.location.z)
    car.rotation_euler = (0, 0, heading)
    
    car.keyframe_insert(data_path="location")
    car.keyframe_insert(data_path="rotation_euler", index=2)
    
    # Pendulum swing (just cosmetic)
    pendulum_angle = 0.3 * math.sin(frame * 0.2)
    pendulum.rotation_euler[1] = -pendulum_angle
    pendulum.keyframe_insert(data_path="rotation_euler", index=1)
