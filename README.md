# Hydrogen Atom Quantum State Transitions Visualization

This Python script visualizes quantum state transitions of a hydrogen atom using Python's scientific libraries such as NumPy, SciPy, and Matplotlib. It computes and animates transitions between various quantum states of a hydrogen atom by calculating the probability density of the electron's position in space for a given set of quantum numbers. The visualization showcases the beauty and complexity of quantum mechanical behaviors in atomic systems.

## Features

- Calculation of wave functions for hydrogen atom quantum states using spherical harmonics and generalized Laguerre polynomials.
- Visualization of quantum state transitions through smooth interpolations between states, represented as α|𝒏𝒍𝒎⟩ + β|𝒏'𝒍'𝒎'⟩, where α decreases and β increases over time.
- Generation of animations showcasing the dynamic evolution of electron probability densities across different quantum states, with dots representing the values of 𝒏𝒍𝒎, and solid lines showing possible allowed transitions.
- Display of spatial probability density of finding an electron in a hydrogen atom, enhancing understanding of quantum numbers (𝒏, 𝒍, 𝒎) and their roles in specifying the state of the hydrogen atom:
    - 𝒏: total energy
    - 𝒍: total angular momentum
    - 𝒎: z-component of angular momentum
- Utilization of the following formula to compute wavefunctions: 
$$\psi_{n l m}(r, \vartheta, \varphi)=\sqrt{\left(\frac{2}{n a_0}\right)^3 \frac{(n-l-1) !}{2 n[(n+l) !]}} e^{-\rho / 2} \rho^l L_{n-l-1}^{2 l+1}(\rho) \cdot Y_{l m}(\vartheta, \varphi)$$

## Requirements

To run this script, you need a Python environment with the following packages installed:

- `numpy`
- `matplotlib`
- `scipy`

These packages can be installed via pip:

```bash
pip install numpy matplotlib scipy
```

## Usage
1. Ensure you have all the required packages installed in your Python environment.
2. Place the script in your project directory.
3. Run the script using Python:
```bash
python hydrogen_atom_visualization.py
```
The script will generate an MP4 video file named hydrogen_atom_transitions_smooth_ease.mp4 in the directory, illustrating the transitions between the quantum states of a hydrogen atom.

## How It Works
- The script defines key functions for computing the wave function of a hydrogen atom's electron for given quantum numbers (n, l, m) and coordinates (r, theta, phi).
- It then defines a function to calculate superpositions of these wave functions, allowing for the visualization of transitions between states.
- The animation iterates through predefined state transitions, smoothly interpolating between them to visualize the electron's probability density changes.
- The visualization is performed in a 2D plane for simplicity, focusing on the x and z coordinates by integrating out the y dimension.
## Visualization Details
- The script uses a contour plot to visualize the probability density on a 2D plane.
- Probability densities are normalized and displayed using a logarithmic scale to enhance visibility across orders of magnitude.
- Transitions between states are animated using a smooth ease-in-out sine function, providing a visually appealing transition effect.

## Contributing
Contributions to improve the script or extend its capabilities are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License
This project is open-sourced under the MIT License. See the LICENSE file for more details.

## Acknowledgments
This script was developed for educational purposes to assist in the understanding and visualization of quantum mechanical systems, specifically tailored for the physics community interested in quantum mechanics and atomic physics.
