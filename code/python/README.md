# The Predator-Prey Fractal Habitat

[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-yellow.svg)](LICENSE_CODE.md)
[![ORCID](https://img.shields.io/badge/Author-Daniel%20Sandner-blue?style=flat&logo=orcid)](https://orcid.org/0000-0002-1041-814X)

**Author:** [Daniel Sandner](https://github.com/sandner-art)


By implementing a **Predator-Prey** dynamic, we stop treating the fractal as a static picture and start treating it as an **Ecosystem**.

This approach reveals the **Functional Regions** of the fractal:
1.  **The Prey (Basin Seekers):** They will identify the **Stable Attractors**. In dynamical systems theory, these are the regions where the system settles down.
2.  **The Predators (Chaos Surfers):** They will identify the **Unstable Manifolds** (the filaments and boundaries). These are the highways that energy travels along but never settles.

The resulting image will be a **"Habitat Map"** of the Mandelbrot set.

### The Algorithm: Ecosystem Dynamics
We will run a physics simulation with two distinct species interacting with the **Potential Field** ($P$) of the fractal.

*   **Prey (Green Agents):**
    *   **Drive:** Seek high Potential ($P \to \text{Max}$).
    *   **Behavior:** They flock towards the deep interior "bulbs."
    *   **Insight:** Their clustering density measures the **"Basin Depth"** or stability margin.
*   **Predators (Red Agents):**
    *   **Drive:** Seek high Gradient ($|\nabla P| \to \text{Max}$).
    *   **Behavior:** They patrol the sharp edges where stability transitions to chaos.
    *   **Insight:** Their paths highlight the **"Critical Phase Transitions."**

### Python Implementation: The Predator-Prey Habitat

code\python\predator_prey_fractal.py

### Scientific Insights from this Visualization

When you look at the generated image, you will see something distinct from a standard plot:

1.  **The Green Sanctuaries (Prey):**
    *   You will see bright green clusters accumulating in the "bulbs" and spiral centers.
    *   **Insight:** These identify the **Basins of Attraction**. In a dynamical system, if you start a process here, it will remain stable. These are the "safe zones" of the math.
    *   Notice that the prey don't fill the bulb evenly; they swirl in specific orbits. This visualizes the **Limit Cycle** geometry within the bulb.

2.  **The Red Highways (Predators):**
    *   The predators will form sharp, glowing red lines outlining the fractal shapes.
    *   **Insight:** These are the **Unstable Manifolds** (or Separatrices). These are the critical boundaries where the system decides whether to stabilize or explode.
    *   In chaos theory, these "highways" are where energy and information travel most efficiently.

3.  **The "Kill Zones" (Yellow/Orange):**
    *   Where the Green and Red mix, you get Yellow.
    *   **Insight:** This is the **Edge of Chaos**. It is the most complex region where stable orbits (Prey) and chaotic trajectories (Predators) come into extremely close contact. This is where phase transitions happen.

### Further Expansions

If you want to push this ecosystem idea further, here are two paths:

1.  **Evolutionary Fractal:**
    *   Give the agents a "genome" (e.g., three parameters for how they react to the potential field).
    *   Kill agents that drift into the black void (divergence).
    *   Replicate agents that stay in the colored zones.
    *   **Result:** The agents will *evolve* the perfect mathematical formula to navigate the Mandelbrot set. You essentially "breed" a function that solves the fractal.

2.  **Sonification:**
    *   Map the density of Prey vs Predators to audio.
    *   As you pan over the fractal, stable regions sound harmonious (sine waves), and boundary regions sound noisy (white noise/granular synthesis). This creates an auditory map of stability.
