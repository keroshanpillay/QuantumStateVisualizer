import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm, genlaguerre, factorial
from matplotlib.animation import FuncAnimation
import matplotlib.colors as colors

# Constants
a0 = 1  # Bohr radius, using atomic units for simplicity

def psi_nlm(r, theta, phi, n, l, m):
    """Calculate the wave function psi for given quantum numbers and coordinates."""
    rho = 2 * r / (n * a0)
    N = np.sqrt((2/(n*a0))**3 * factorial(n-l-1) / (2*n*factorial(n+l)))
    L = genlaguerre(n-l-1, 2*l+1)(rho)
    R = np.exp(-rho/2) * rho**l * L
    Y = sph_harm(m, l, phi, theta)
    return N * R * Y

def psi_superposition(r, theta, phi, states, weights):
    """Calculate a superposition of multiple quantum states."""
    psi_total = np.zeros_like(r, dtype=np.complex_)
    for state, weight in zip(states, weights):
        n, l, m = state
        psi_total += weight * psi_nlm(r, theta, phi, n, l, m)
    return psi_total

# Quantum state transition list and their weights at each frame
state_transitions = [
    ((1,0,0), (2,0,0)),
    ((2,0,0),(2,1,-1)),
    ((2,1,-1), (2,1,0)),
    ((2,1,0),(2,1,1)),
    ((2,1,1),(3,0,0)),
    ((3,0,0),(3,1,-1)),
    ((3,1,-1),(3,1,0)),
    ((3,1,0),(3,1,1)),
    ((3,1,1),(3,2,-2)),
    ((3,2,-2),(3,2,-1)),
    ((3,2,-1),(3,2,0)),
    ((3,2,0),(3,2,1)),
    ((3,2,1),(3,2,2)),
    ((3,2,2),(4,0,0)),
    ((4, 0, 0), (4, 1, -1)),
    ((4, 1, -1), (4, 1, 0)),
    ((4, 1, 0), (4, 1, 1)),
    ((4, 1, 1), (4, 2, -2)),
    ((4,2,-2), (4,2,-1)),
    ((4,2,-1), (4,2,0)),
    ((4,2,0), (4,2,1)),
    ((4,2,1), (4,2,2)),
    ((4,2,2), (4,3,-3)),
    ((4,3,-3), (4,3,-2)),
    ((4,3,-2), (4,3,-1)),
    ((4,3,-1), (4,3,0))
]

# Total frames and frames per transition
total_frames = len(state_transitions) * 30
frames_per_transition = total_frames // len(state_transitions)

# Define a grid in spherical coordinates
space_size = 200
r = np.linspace(0, 40*a0, space_size)
theta = np.linspace(0, np.pi, space_size)
phi = np.pi / 2
r, theta, phi = np.meshgrid(r, theta, phi, indexing='ij')

# Convert to Cartesian coordinates for plotting
x = r * np.sin(theta) * np.cos(phi)
z = r * np.cos(theta)

def ease_in_out_sine(x):
    """Ease-in-out using sine function."""
    return -(np.cos(np.pi * x) - 1) / 2

def linear(x):
    return x

def update(frame):
    # Determine current transition and calculate weights
    transition_index = frame // frames_per_transition
    if transition_index >= len(state_transitions):
        transition_index = len(state_transitions) - 1
    frame_within_transition = frame % frames_per_transition
    progress = frame_within_transition / frames_per_transition
    weight = linear(progress)  # Use ease-in-out for smooth transition

    # Current and next states
    current_state, next_state = state_transitions[transition_index]
    weights = [1 - weight, weight]

    # Compute superposition psi for the current frame
    psi = psi_superposition(r, theta, phi, [current_state, next_state], weights)
    probability_density = np.abs(psi)**2
    probability_density_2d = np.sum(probability_density, axis=2)

    # Plotting
    plt.clf()
    max_density = np.max(probability_density_2d)
    levels = np.linspace(0, max_density, 100)
    log_norm = colors.LogNorm(vmin=1e-5, vmax=max_density)
    plt.contourf(x[:, :, 0], z[:, :, 0], probability_density_2d, levels=levels, cmap='viridis', norm=log_norm)
    plt.contourf(-x[:, :, 0], z[:, :, 0], probability_density_2d, levels=levels, cmap='viridis', norm=log_norm)
    plt.colorbar(label='Probability Density')
    plt.xlabel('x (in Bohr radii)')
    plt.ylabel('z (in Bohr radii)')
    plt.title(f'Transition Frame: {frame}')

# Setup and run the animation
fig = plt.figure(figsize=(10, 7))
ani = FuncAnimation(fig, update, frames=total_frames, repeat=False)

# Save or display the animation
ani.save('hydrogen_atom_transitions.mp4', writer='ffmpeg', dpi=200, fps=60)
# To display in Jupyter, uncomment:
# from IPython.display import HTML
# HTML(ani.to_html5_video())
