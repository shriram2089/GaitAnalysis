import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define your custom coordinates for the stick figure body parts
body_parts = {
    'head': (0, 0, 2),
    'shoulder': (0, 0, 1),
    'elbow': (-1, 0, 0),
    'hand': (-2, 0, -1),
    'hip': (0, 0, 0),
    'knee': (1, 0, -1),
    'foot': (2, 0, -2)
}

# Define the sequence of movements for walking
walk_sequence = [
    {'elbow': (0, 0, 0), 'hand': (-1, 0, -1)},
    {'elbow': (1, 0, 0), 'hand': (0, 0, 0)},
    {'knee': (1, 0, -1), 'foot': (0, 0, -1)},
    {'knee': (0, 0, -1), 'foot': (-1, 0, -2)}
]

# Define connections between body parts
connections = [
    ('head', 'shoulder'),
    ('shoulder', 'elbow'),
    ('elbow', 'hand'),
    ('shoulder', 'hip'),
    ('hip', 'knee'),
    ('knee', 'foot')
]

# Create a function to update the stick figure's positions for each frame
def update(frame):
    ax.clear()  # Clear the previous frame
    ax.set_xlim(-3, 3)  # Set limits for x-axis
    ax.set_ylim(-3, 3)  # Set limits for y-axis
    ax.set_zlim(-3, 3)  # Set limits for z-axis

    # Plot body parts
    for part, (x, y, z) in body_parts.items():
        ax.scatter(x, y, z, color='black')  # Plot body parts as black dots

    # Plot connections between body parts
    for connection in connections:
        part1, part2 = connection
        x1, y1, z1 = body_parts[part1]
        x2, y2, z2 = body_parts[part2]
        ax.plot([x1, x2], [y1, y2], [z1, z2], color='black')

    # Update body parts according to the walk sequence
    if frame < len(walk_sequence):
        for part, (x, y, z) in walk_sequence[frame].items():
            body_parts[part] = (x, y, z)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ani = animation.FuncAnimation(fig, update, frames=len(walk_sequence), interval=500)

plt.show()
