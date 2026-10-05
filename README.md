# 3D Interactive Projectile Motion Simulator

An interactive, 3D physics simulation built with Python and VPython. This application models classical projectile trajectories using numerical time-stepping integration, providing real-time visual animation alongside analytical predictions.

---

## 📌 Features

- **Real-Time 3D Rendering**: Visualizes the cannon barrel, launch platform, projectile trajectory trail, and landing plane.
- **Interactive UI Controls**: Adjust launch angle ($1^\circ - 90^\circ$) via an interactive slider and customize initial velocity directly.
- **Analytical vs. Numerical Comparison**: Computes the exact theoretical range $R = \frac{v^2 \sin(2\theta)}{g}$ and benchmarks it against step-by-step Euler integration ($\Delta t = 0.005\text{ s}$).
- **Dynamic Camera Positioning**: Pre-configured camera vectors ensure clear framing of the trajectory and landing spot.
- **Automated Collision Detection**: Detects surface boundary impact based on physical bounding box and sphere radius calculations.

---

## 🧮 Theoretical Background

The simulation combines closed-form kinematic models with discrete step-by-step numerical integration:

1. **Analytical Range Formula**:
   $$R = \frac{v^2 \sin(2\theta)}{g}$$

2. **Numerical Integration Scheme**:
   At each time step $\Delta t = 0.005$:
   $$\vec{v}_{t+\Delta t} = \vec{v}_t + \vec{g} \cdot \Delta t$$
   $$\vec{r}_{t+\Delta t} = \vec{r}_t + \vec{v}_{t+\Delta t} \cdot \Delta t$$

---

## 🛠️ Installation & Setup

### Prerequisites

Ensure you have Python installed ($3.8+$ recommended):

```bash
python --version
```

### Dependencies

Install VPython via pip:

```bash
pip install vpython
```

---

## 🚀 Running the Simulator

1. Clone or download this repository:
   ```bash
   git clone https://github.com/your-username/vpython-projectile-simulator.git
   cd vpython-projectile-simulator
   ```

2. Run the script:
   ```bash
   python Projectile.py
   ```

3. A browser tab will open automatically rendering the 3D scene and interactive UI controls.

---

## 💻 Code Structure

```text
├── Projectile.py       # Main simulation script containing UI setup and integration loop
└── README.md           # Project documentation
```

Key functions inside `Projectile.py`:
- `show_theory()`: Calculates closed-form theoretical range based on user slider and input values.
- `launch()`: Instantiates projectile entities, calculates initial velocity vector components, and resets system state.
- `while True`: Continuous rendering loop running at `vp.rate(200)` executing state updates and checking ground boundary collisions.

---

## 📄 License

Distributed under the MIT License. Feel free to modify and adapt for educational or research purposes.
