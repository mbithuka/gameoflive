import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

# Create a sphere
phi = np.linspace(0, np.pi, 100)
theta = np.linspace(0, 2 * np.pi, 100)
phi_grid, theta_grid = np.meshgrid(phi, theta)
x = np.sin(phi_grid) * np.cos(theta_grid)
y = np.sin(phi_grid) * np.sin(theta_grid)
z = np.cos(phi_grid)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.axis("off")
# Plot the sphere
sphere = ax.plot_surface(x, y, z, color='b', alpha=0.6)

# Plot the axes
ax.plot([0, 1.5], [0, 0], [0, 0], color='r', lw=2)  # X-axis
ax.plot([0, 0], [0, -1.5], [0, 0], color='g', lw=2)  # Y-axis
ax.plot([0, 0], [0, 0], [0, 1.5], color='b', lw=2)  # Z-axis

# Plot the equator
equator_radius = 1  # Adjust the radius of the equator
equator_phi = np.pi / 2  # Phi for the equator (90 degrees)
equator_x = equator_radius * np.cos(theta)
equator_y = equator_radius * np.sin(theta)
equator_z = np.zeros_like(theta)
ax.plot(equator_x, equator_y, equator_z, color='r', linewidth=2)

# Plot a circle on the Arctic
arctic_radius = 0.75  # Adjust the radius of the Arctic circle
arctic_z = arctic_radius * np.ones_like(theta)  # Z-coordinate of the Arctic circle
arctic_x = np.sqrt(1 - arctic_z**2) * np.cos(theta) * equator_radius
arctic_y = np.sqrt(1 - arctic_z**2) * np.sin(theta) * equator_radius
ax.plot(arctic_x, arctic_y, arctic_z, color='g', linewidth=2)

# Plot a random point on the sphere
random_theta = np.random.uniform(0, 2 * np.pi)
random_phi = np.random.uniform(0, np.pi)
random_x = np.sin(random_phi) * np.cos(random_theta)
random_y = np.sin(random_phi) * np.sin(random_theta)
random_z = np.cos(random_phi)
ax.scatter(random_x, random_y, random_z, color='r', s=1)

# Calculate the probability of the random point being inside the Arctic circle
if random_z >= arctic_radius:
    probability_inside_arctic = 1.0
else:
    probability_inside_arctic = 0.0

# Print the probability
print("Probability of generating a point inside the Arctic circle:", probability_inside_arctic)

# Set axis limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

def rotate_sphere(angle):
    ax.view_init(30, angle)
    return sphere, equator_x

# Create animation
ani = animation.FuncAnimation(fig, rotate_sphere, frames=np.arange(0, 360, 1), interval=50)

plt.show()
