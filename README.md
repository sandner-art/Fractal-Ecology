# Fractal Ecology: Multi-Scale Agent Dynamics in Complex Iteration Spaces

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Status: Research](https://img.shields.io/badge/Status-Research-orange.svg)
![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-green.svg)

A real-time visualization and simulation platform exploring emergent ecological dynamics on fractal mathematical manifolds. This application demonstrates how computational agents exhibit complex behaviors when navigating multi-layered fractal properties: geometric (gradient fields), dynamic (escape velocity), and topological (iteration depth, local curvature).

🔗 **Live Demo**: [sandner-art/fractal-ecology](https://github.com/sandner-art/fractal-ecology)  
📚 **Research Context**: [Metacryptography Research](https://metacryptography.openresearch.uk/)

---

## Table of Contents

- [Overview](#overview)
- [Scientific Background](#scientific-background)
- [Mathematical Framework](#mathematical-framework)
- [Fractal Types & Properties](#fractal-types--properties)
- [Agent Behavior Model](#agent-behavior-model)
- [Ecosystem Metrics](#ecosystem-metrics)
- [Visualization Modes](#visualization-modes)
- [Technical Architecture](#technical-architecture)
- [Usage & Controls](#usage--controls)
- [Installation](#installation)
- [Research Applications](#research-applications)
- [Credits](#credits)
- [License](#license)

---

## Overview

**Fractal Ecology** is an interactive research tool that simulates prey-predator dynamics constrained to fractal iteration spaces. Unlike traditional agent-based models operating on Euclidean planes, agents here navigate the complex topology of fractal sets (Mandelbrot, Julia, Burning Ship, Tricorn, Nova, Cosine), responding to intrinsic mathematical properties that govern stability, chaos, and structural complexity.

The system provides:
- **Real-time simulation** of 24,000+ agents (18K prey, 6K predators)
- **6 distinct fractal types** with adjustable parameters
- **Property-aware behavior**: agents respond to iteration depth, escape velocity, and local curvature
- **Multi-dimensional visualization**: 2D trail accumulation, 3D phase-space volume, 4D temporal spectrum
- **Reactive color palettes** driven by live ecosystem metrics

This work extends concepts from:
- **Complex dynamics** (Mandelbrot, Julia sets)
- **Agent-based modeling** (Boids, swarm intelligence)
- **Information theory** (entropy, spatial complexity)
- **Computational ecology** (predator-prey systems)

---

## Scientific Background

### Motivation

Fractal sets exhibit **self-similarity across scales**, **non-integer dimensionality**, and **chaotic boundaries**—properties rarely explored as substrates for computational ecology. Traditional ecological models assume homogeneous or mildly heterogeneous environments. This platform investigates:

> **Research Question**: How do agent populations organize when constrained to navigate fractal manifolds with spatially-varying stability, complexity, and chaos?

### Hypothesis

We hypothesize that:
1. **Prey** will aggregate in **deep basins** (high iteration count regions), avoiding **chaotic boundaries** (high escape velocity)
2. **Predators** will patrol **transition zones** between stability and chaos, exploiting **topological complexity**
3. **Emergent metrics** (chaos, entropy, pressure, complexity) will reveal phase transitions in population dynamics

### Prior Work

- **Mandelbrot Set** (Mandelbrot, 1980): Foundation of fractal geometry
- **Julia Sets** (Gaston Julia, 1918): Parameter-dependent complex dynamics
- **Agent-based models** (Reynolds, 1987; Wilensky, 1999): Emergent collective behavior
- **Computational aesthetics** (Sims, 1991): Evolution in procedural spaces

This work synthesizes these domains into a unified platform for fractal-constrained ecological simulation.

---

## Mathematical Framework

### Fractal Iteration Systems

Each fractal type is defined by an **iteration function** f: ℂ → ℂ applied repeatedly until escape or convergence:

```
z_{n+1} = f(z_n, c, params)
```

Where:
- **z** = complex number (position in fractal space)
- **c** = complex constant (fractal parameter)
- **params** = additional parameters (power, scale, etc.)

The system computes:

1. **Potential Field** φ(z): smooth iteration count
   ```
   φ(z) = n + 1 - log₂(log|z_n|)  where |z_n| > escape_radius
   ```

2. **Gradient Field** ∇φ(z): direction of steepest descent
   ```
   ∇φ = (∂φ/∂x, ∂φ/∂y)
   ```

3. **Escape Velocity** v_esc(z): rate of divergence
   ```
   v_esc = log|z_final|² / max(1, n)
   ```

4. **Local Curvature** κ(z): Laplacian approximation
   ```
   κ ≈ |∇²φ| = |∂²φ/∂x² + ∂²φ/∂y²|
   ```

5. **Iteration Depth** d(z): normalized convergence measure
   ```
   d = n / n_max ∈ [0, 1]
   ```

### Implemented Fractals

| Fractal | Iteration Function | Parameters |
|---------|-------------------|------------|
| **Mandelbrot** | z² + c | Power (2-8), Max Iter |
| **Julia Set** | z² + c_fixed | C real/imag, Max Iter |
| **Burning Ship** | (|Re(z)|+i|Im(z)|)² + c | Power (2-6), Max Iter |
| **Tricorn** | conj(z)² + c | Power (2-6), Max Iter |
| **Nova** | z - a(z^n-1)/(nz^(n-1)) + c | Power n, A real/imag |
| **Cosine** | s·cos(z) + c | Scale s (0.5-3) |

Each fractal exhibits distinct topological signatures:
- **Mandelbrot**: Deep cardioid basin, filamentary boundaries
- **Julia**: Disconnected islands or connected dendrites
- **Burning Ship**: Angular, ship-like cliffs
- **Tricorn**: Mirror-symmetric structures
- **Nova**: Multi-attractor basins (Newton-like)
- **Cosine**: Transcendental chaos boundaries

---

## Fractal Types & Properties

### 1. Mandelbrot Set
**Formula**: z_{n+1} = z_n^p + c (starting z_0 = 0)

**Properties**:
- Main cardioid acts as prey attractor basin
- Seahorse valley filaments create predator patrol corridors
- Self-similar copies at all scales

**Notable Presets**:
- **Seahorse Valley** (-0.7436, 0.1318): Intricate spiral structures
- **Elephant Valley** (0.2825, 0.0085): Trunk-like formations
- **Mini Brots** (-1.7568, 0.0): Self-similar miniature copies

### 2. Julia Set
**Formula**: z_{n+1} = z_n² + c_fixed (starting z_0 = viewport point)

**Properties**:
- Parameter c determines connectivity (connected vs. disconnected)
- Prey scatter across isolated islands
- Predators hunt in inter-island gaps

**Notable Presets**:
- **Dendrite** (c=-0.4+0.6i): Tree-like branching
- **Siegel Disk** (c=-0.391-0.587i): Quasi-periodic orbits
- **Dragon** (c=-0.8+0.156i): Asymmetric formations

### 3. Burning Ship
**Formula**: z_{n+1} = (|Re(z)|+i|Im(z)|)^p + c

**Properties**:
- Absolute value creates sharp angular cliffs
- Predators lock onto high-gradient edges
- Ship-like main structure with mast/antenna details

### 4. Tricorn (Mandelbar)
**Formula**: z_{n+1} = conj(z_n)^p + c

**Properties**:
- Conjugate operation enforces mirror symmetry
- Symmetric predator patrol patterns
- Three-fold symmetry at critical points

### 5. Nova (Newton-like)
**Formula**: z_{n+1} = z_n - a(z_n^n - 1)/(n·z_n^(n-1)) + c

**Properties**:
- Multiple attractors (roots of z^n - 1)
- Prey form separate colonies per attractor
- Boundaries exhibit Julia-like chaos

### 6. Cosine Fractal
**Formula**: z_{n+1} = s·cos(z_n) + c

**Properties**:
- Transcendental function (non-polynomial)
- Highly chaotic boundaries
- Predators exhibit erratic hunting patterns

---

## Agent Behavior Model

### Three-Layer Property Response

Agents navigate using a **multi-scale field sampling** approach:

```javascript
field = sampleField(x, y) → {
  pot:    φ(x,y),      // Potential (smooth iteration count)
  gx, gy: ∇φ(x,y),     // Gradient (direction)
  cliff:  |∇φ|(x,y),   // Gradient magnitude (steepness)
  depth:  d(x,y),      // Iteration depth (basin depth)
  escVel: v_esc(x,y),  // Escape velocity (chaos measure)
  curve:  κ(x,y)       // Local curvature (complexity)
}
```

### Prey Dynamics

**Objective**: Seek stable, low-complexity regions

```
Force_prey = α·∇φ·(climb + depth_attraction)     // Climb gradients toward basins
           + β·Rot90(∇φ)·surf                    // Surf perpendicular (contour following)
           - γ·∇φ·escape_velocity                // Avoid chaos boundaries
           + noise

Speed_modifier = 1.0 - curve·0.4                 // Slow in complex regions
```

**Behavior Patterns**:
- Aggregate in **deep basins** (high φ, high depth)
- Slow down in **high-curvature zones** (careful exploration)
- Flee from **chaos boundaries** (high v_esc)

### Predator Dynamics

**Objective**: Hunt at transition zones, exploit complexity

```
Force_pred = α·∇φ·sign(target_band - φ)·(1 + curvature + depth_edge)  // Band-lock with complexity boost
           + β·Rot90(∇φ)·patrol                                        // Patrol perpendicular
           + noise

Speed_boost = 1.0 + escape_velocity·0.6                                // Faster in chaos zones
```

**Behavior Patterns**:
- Target **intermediate depths** (transition zones)
- Speed up in **chaos zones** (opportunistic)
- Track **complexity hotspots** (interesting terrain)

### Parameter Space

| Parameter | Range | Default | Effect |
|-----------|-------|---------|--------|
| Prey Count | 2K-30K | 18K | Population density |
| Predator Count | 1K-12K | 6K | Hunting pressure |
| Prey Climb | 0-100 | 25 | Gradient ascent strength |
| Prey Surf | 0-100 | 12 | Contour following |
| Predator Band | 10-80 | 35 | Target potential level |
| Predator Patrol | 0-100 | 55 | Perpendicular drift |

---

## Ecosystem Metrics

Four real-time metrics quantify population dynamics:

### 1. Chaos (σ_chaos)
**Definition**: Average cliff-edge proximity of prey

```
σ_chaos = (1/N_prey) Σ |∇φ|(x_i, y_i)
```

**Interpretation**:
- High → Prey near unstable boundaries
- Low → Prey in stable basins
- **Color**: Red-orange gradient

### 2. Entropy (σ_entropy)
**Definition**: Spatial variance of prey distribution

```
σ_entropy = √(Var(x_prey) + Var(y_prey))
```

**Interpretation**:
- High → Prey widely dispersed
- Low → Prey clustered/aggregated
- **Color**: Blue-cyan gradient
- **Theory**: Analogous to thermodynamic entropy (disorder)

### 3. Pressure (σ_pressure)
**Definition**: Spatial overlap of prey/predator populations

```
σ_pressure = Σ min(ρ_prey(cell), ρ_pred(cell)) / Σ ρ_prey(cell)
```

**Interpretation**:
- High → Hunting zones overlap prey habitats
- Low → Spatial segregation
- **Color**: Purple-magenta gradient
- **Mechanism**: Grid-based density calculation (16×16 bins)

### 4. Complexity (σ_complexity)
**Definition**: Average local curvature experienced by all agents

```
σ_complexity = (1/(N_prey + N_pred)) Σ κ(x_i, y_i)
```

**Interpretation**:
- High → Population in topologically complex regions
- Low → Population in smooth regions
- **Color**: Green-teal gradient
- **Insight**: Measures "terrain difficulty"

All metrics are **exponentially smoothed** (α=0.08) for temporal stability.

---

## Visualization Modes

### 1. 2D Trail Mode
**Method**: Persistent density accumulation on fractal background

**Rendering**:
- Background: Fractal potential φ(x,y) with property tinting:
  - **Blue tint**: Depth (iteration count)
  - **Orange tint**: Escape velocity (chaos)
  - **Brightness**: Local curvature (complexity)
- Prey trails: Additive density (decay 0.984/frame)
- Predator trails: Additive density (decay 0.982/frame)
- Colors: Reactive palette functions `prey(t, metrics)`, `pred(t, metrics)`

**Use Case**: Observe long-term spatial patterns, basin attraction

### 2. 3D Phase Volume
**Method**: Time-stacked 2D slices → 3D point cloud

**Structure**:
- Z-axis = Time (160-frame history)
- X-Y plane = Spatial coordinates
- Camera: Orbital (yaw/pitch/zoom), auto-rotation when idle

**Rendering**:
- Subsample: Every 4th agent, stride through history
- Accumulate into density+energy buffers
- Color:
  - Prey: Cyan-green via palette
  - Predators: Hot orange-red via palette
  - Brightness: Velocity energy

**Use Case**: Visualize temporal evolution, identify periodic orbits

### 3. 4D Temporal Spectrum
**Method**: 3D volume + hue encoding for time depth

**Enhancement**:
- Each frame's time depth (0→1) mapped to HSL hue shift
- Recent frames: Red-orange
- Mid-history: Green-cyan
- Oldest frames: Blue-purple

**Color Space**:
```
hue = base_hue + (frame_depth * 360°)
HSL(hue, saturation, lightness) → RGB
```

**Use Case**: Reveal evolutionary structure, phase transitions

---

## Technical Architecture

### Performance

- **Resolution**: 256×256 fractal field (65K samples)
- **Agent Count**: Up to 30K agents (default 24K)
- **Frame Rate**: ~60 FPS on modern hardware
- **Precision**: Float32Array for all field/agent data

### Optimization Strategies

1. **Field Caching**: Rebuild only on zoom/pan/fractal change
2. **Vectorized Iteration**: Batch-process field samples
3. **Subsampling**: 3D/4D modes subsample agents (stride=4) and history
4. **Log-scale Normalization**: Density visualization clarity
5. **Inertial Damping**: Smooth agent motion (prey: 0.88, pred: 0.90)

### Data Structures

```javascript
// Field arrays (256×256 = 65536 elements)
potential:   Float32Array  // Smooth iteration count
gradX, gradY: Float32Array  // Normalized gradient vectors
cliffMap:    Float32Array  // Gradient magnitude [0,1]
iterDepth:   Float32Array  // Iteration depth [0,1]
escapeVel:   Float32Array  // Escape velocity [0,1]
localCurve:  Float32Array  // Laplacian (complexity)

// Agent arrays (N agents)
preyX, preyY:   Float32Array  // Positions [0,1]²
preyVx, preyVy: Float32Array  // Velocities
predX, predY:   Float32Array
predVx, predVy: Float32Array

// History (160 frames for 3D/4D)
histPX, histPY: Array<Float32Array>  // Prey history
histRX, histRY: Array<Float32Array>  // Predator history
```

### Technology Stack

- **Language**: Vanilla JavaScript (ES6+)
- **Rendering**: Canvas 2D API + manual projection (3D/4D)
- **Math**: Complex iteration, gradient computation, HSL color space
- **UI**: CSS3 (glassmorphism, backdrop-filter)
- **Fonts**: Oxanium (geometric), Share Tech Mono (monospace)

---

## Usage & Controls

### Navigation

| Action | 2D Mode | 3D/4D Mode |
|--------|---------|------------|
| **Drag** | Pan fractal viewport | Orbit camera (yaw/pitch) |
| **Scroll/Pinch** | Zoom toward cursor | Camera zoom (0.3×-4×) |
| **Double-tap** | Reset view | Reset camera |

### Interface Elements

- **Top-left**: Fractal name + mode badge
- **Top-right**: Live metrics (Chaos, Entropy, Pressure, Complexity)
- **Top-center**: FPS counter
- **Bottom**: Mode tabs (2D / 3D / 4D)
- **Bottom-right**: 
  - ⚙️ Settings panel (fractal, parameters, ecology, palette)
  - ⬇️ Export PNG (timestamped)

### Settings Panel

**Fractal Section**:
- 6 main fractal chips
- 6 preset sub-chips per fractal (zoom locations)

**Parameters Section** (dynamic):
- Sliders adapt to active fractal
- Examples: Julia C parameters, Nova power, Cosine scale

**Ecology Section**:
- Agent counts (prey, predators)
- Behavior weights (climb, surf, band, patrol)

**Palette Section**:
- 6 reactive color schemes (Ember, Arctic, Blood, Deep Ocean, Void, Molten)
- Swatches show gradient preview

### Export

- **Format**: PNG (canvas.toDataURL)
- **Filename**: `fractal-ecology_{type}_{mode}_{timestamp}.png`
- **Resolution**: Current viewport dimensions

---

## Installation

### Option 1: Direct Usage
```bash
# Download the HTML file
wget https://github.com/sandner-art/fractal-ecology/fractal_ecology.html

# Open in browser
open fractal_ecology.html  # macOS
xdg-open fractal_ecology.html  # Linux
start fractal_ecology.html  # Windows
```

### Option 2: Web Server
```bash
# Python 3
python -m http.server 8000

# Node.js (http-server)
npx http-server

# Navigate to http://localhost:8000/fractal_ecology.html
```

### Option 3: GitHub Pages
```bash
git clone https://github.com/sandner-art/fractal-ecology.git
cd fractal-ecology
# Enable GitHub Pages in repository settings → serve from main branch
```

### Requirements

- **Browser**: Chrome 90+, Firefox 88+, Safari 14+ (supports ES6, Canvas 2D, backdrop-filter)
- **Display**: 1920×1080+ recommended (responsive down to mobile)
- **Hardware**: Multi-core CPU, 4GB+ RAM for smooth 60 FPS

---

## Research Applications

### Potential Use Cases

1. **Computational Ecology**
   - Test spatial pattern formation on heterogeneous substrates
   - Measure information flow in topologically complex environments

2. **Complex Systems**
   - Visualize attractor basins in high-dimensional systems
   - Identify phase transitions via metric time series

3. **Art & Design**
   - Generate fractal-constrained generative art
   - Export high-resolution images for print media

4. **Education**
   - Interactive demonstration of fractal geometry
   - Agent-based modeling pedagogy

5. **Mathematical Visualization**
   - Explore lesser-known fractals (Tricorn, Nova, Cosine)
   - Parameter space exploration via live sliders

### Future Extensions

- [ ] **Statistical Analysis**: Export metric time series (CSV)
- [ ] **Parameter Sweeps**: Automated fractal parameter scans
- [ ] **3D Fractals**: Extend to quaternion/octionion sets
- [ ] **Machine Learning**: Train agents via reinforcement learning
- [ ] **Multi-Species**: Add herbivore/carnivore tiers
- [ ] **Network Analysis**: Graph connectivity in sparse regions

---

## Credits

### Author
**Daniel Sandner**  
[sandner.art](https://sandner.art/)  
Artist, researcher, and creative technologist specializing in computational aesthetics, fractal geometry, and emergent systems. Daniel's work explores the intersection of mathematics, art, and complex systems through interactive media.

### Research Context
**Metacryptography Research**  
[openresearch.uk/metacryptography](https://metacryptography.openresearch.uk/)  
An interdisciplinary research initiative investigating novel approaches to cryptographic systems through the lens of computational complexity, information theory, and mathematical structures. This project contributes to understanding how complex iteration spaces can serve as substrates for computational processes.

### Acknowledgments

This work builds upon foundational research in:

- **Fractal Geometry**: Benoit Mandelbrot, Gaston Julia, Pierre Fatou
- **Complex Dynamics**: Adrien Douady, John Hubbard
- **Agent-Based Modeling**: Craig Reynolds (Boids, 1987)
- **Information Theory**: Claude Shannon, Andrey Kolmogorov
- **Computational Aesthetics**: Karl Sims, Golan Levin

Special thanks to the open-source community for tools and inspiration:
- Canvas API (W3C)
- Web standards (WHATWG, Ecma International)
- Mathematical visualization pioneers

### Citing This Work

If you use this software or methodology in your research, please cite:

```bibtex
@software{sandner2025fractalecology,
  author = {Sandner, Daniel},
  title = {Fractal Ecology: Multi-Scale Agent Dynamics in Complex Iteration Spaces},
  year = {2025},
  url = {https://github.com/sandner-art/fractal-ecology},
  version = {1.0.0},
  organization = {Metacryptography Research},
  note = {Interactive visualization platform for agent-based modeling on fractal manifolds}
}
```

---

## License

**MIT License**

Copyright (c) 2025 Daniel Sandner

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Contact & Contributions

**Website**: [sandner.art](https://sandner.art/)  
**Research**: [metacryptography.openresearch.uk](https://metacryptography.openresearch.uk/)  
**Issues**: [GitHub Issues](https://github.com/sandner-art/fractal-ecology/issues)   
**Discussions**: [GitHub Discussions](https://github.com/sandner-art/fractal-ecology/discussions) 

### Contributing

Contributions are welcome! Areas of interest:

- **New Fractals**: Implement additional iteration systems (quaternions, L-systems)
- **Behavioral Models**: Alternative agent physics (flocking, chemotaxis)
- **Metrics**: Novel complexity measures, information-theoretic quantities
- **Performance**: GPU acceleration (WebGL/WebGPU), WASM port
- **Visualization**: Advanced shaders, ray-marching, volumetric rendering

Please open an issue before starting major work to discuss design approach.

---

## Appendix: Mathematical Proofs & Derivations

### A. Smooth Iteration Count (Renormalisation)

For escape-time fractals with escape radius R:

```
φ(z) = n + 1 - log₂(log|z_n|/log R)
```

**Derivation**:
Near escape, |z_n| ≈ R·e^(2^(n-ν)) for smooth potential ν. Taking logs:
```
log|z_n| ≈ log R + 2^(n-ν)
log(log|z_n|) ≈ log(log R + 2^(n-ν)) ≈ (n-ν)log 2
ν ≈ n - log₂(log|z_n|/log R)
```

### B. Gradient Estimation (Central Differences)

For discrete field φ[i,j] on grid:
```
∂φ/∂x ≈ (φ[i+1,j] - φ[i-1,j]) / (2Δx)
∂φ/∂y ≈ (φ[i,j+1] - φ[i,j-1]) / (2Δy)
```

Normalization:
```
g = ∇φ / |∇φ|  (unit vector field)
```

### C. Entropy Calculation

Given N agents at positions {(x_i, y_i)}:
```
μ_x = (1/N)Σx_i,  μ_y = (1/N)Σy_i
σ²_x = (1/N)Σ(x_i - μ_x)²,  σ²_y = (1/N)Σ(y_i - μ_y)²
S = √(σ²_x + σ²_y)  (radial standard deviation)
```

Scaling factor k=2.2 chosen empirically for S ∈ [0,1].

---

**Version**: 1.0.0  
**Last Updated**: 2025-02-02  
**Status**: Active Research Project  

🌀 *Exploring the edge between order and chaos, one iteration at a time.* 🌀
