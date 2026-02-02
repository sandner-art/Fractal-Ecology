import numpy as np
import matplotlib.pyplot as plt

def predator_prey_fractal(resolution=(1000, 1000), n_prey=60000, n_predators=20000, steps=250):
    print("Initializing Ecosystem...")
    H, W = resolution
    
    # 1. Generate the Environment (The "Terrain")
    # Seahorse Valley - A rich environment with both deep bulbs and sharp cliffs
    center = -0.743643 + 0.131825j
    width = 0.005
    
    y, x = np.ogrid[center.imag - width/2 : center.imag + width/2 : H * 1j,
                    center.real - width/2 : center.real + width/2 : W * 1j]
    c_grid = x + 1j*y
    
    print("  Mapping Potential & Gradient Fields...")
    max_iter = 100
    z = np.zeros_like(c_grid)
    potential = np.zeros(c_grid.shape, dtype=float)
    mask = np.full(c_grid.shape, True, dtype=bool)
    
    # Standard smooth iteration count
    for i in range(max_iter):
        if not np.any(mask): break
        z[mask] = z[mask]**2 + c_grid[mask]
        diverged = np.abs(z) > 100
        newly_div = mask & diverged
        if np.any(newly_div):
            smooth = i + 1 - np.log2(np.log(np.abs(z[newly_div])))
            potential[newly_div] = smooth
            mask[newly_div] = False
            
    # Interior points get max potential
    potential[mask] = max_iter
    
    # Calculate Gradient (Slope) - used for navigation
    grad_y, grad_x = np.gradient(potential)
    
    # Normalize Gradient (Direction only)
    grad_mag = np.sqrt(grad_x**2 + grad_y**2)
    grad_mag[grad_mag == 0] = 1e-9 # Safe divide
    
    dir_x = grad_x / grad_mag
    dir_y = grad_y / grad_mag
    
    # "Cliff Map" - Identifies the sharp boundaries (High Gradient Magnitude)
    # Predators love this.
    cliff_intensity = grad_mag / np.max(grad_mag)
    
    # --- 2. Initialize Agents ---
    print(f"  Releasing {n_prey} Prey and {n_predators} Predators...")
    
    # Random start positions
    prey_x = np.random.uniform(0, W, n_prey)
    prey_y = np.random.uniform(0, H, n_prey)
    pred_x = np.random.uniform(0, W, n_predators)
    pred_y = np.random.uniform(0, H, n_predators)
    
    # Velocities
    prey_vx = np.random.randn(n_prey) * 0.5
    prey_vy = np.random.randn(n_prey) * 0.5
    pred_vx = np.random.randn(n_predators) * 0.5
    pred_vy = np.random.randn(n_predators) * 0.5
    
    # Trail Maps (Accumulators)
    trail_prey = np.zeros((H, W))
    trail_pred = np.zeros((H, W))
    
    # Physics Settings
    prey_speed = 1.0
    pred_speed = 1.8 # Predators are faster
    
    # Simulation Loop
    print("  Simulating Survival Dynamics...")
    
    for step in range(steps):
        # --- PREY LOGIC ---
        # 1. Sample Environment
        ix = np.clip(prey_x.astype(int), 0, W-1)
        iy = np.clip(prey_y.astype(int), 0, H-1)
        
        # 2. Force: Climb the Potential (Seek Safety/Interior)
        # They want to move UP the gradient (+dir_x, +dir_y)
        fx = dir_x[iy, ix] * 0.2
        fy = dir_y[iy, ix] * 0.2
        
        # 3. Force: Flow Tangent (Surf the lines)
        # Cross product of gradient (-dir_y, dir_x)
        # This makes them orbit rather than just fall in
        fx += -dir_y[iy, ix] * 0.1
        fy += dir_x[iy, ix] * 0.1
        
        # 4. Update Prey
        prey_vx = prey_vx * 0.9 + fx # Inertia + Force
        prey_vy = prey_vy * 0.9 + fy
        
        # Normalize speed
        v_norm = np.sqrt(prey_vx**2 + prey_vy**2)
        v_norm[v_norm==0] = 1
        prey_vx = (prey_vx / v_norm) * prey_speed
        prey_vy = (prey_vy / v_norm) * prey_speed
        
        prey_x += prey_vx
        prey_y += prey_vy
        
        # --- PREDATOR LOGIC ---
        # 1. Sample Environment
        pix = np.clip(pred_x.astype(int), 0, W-1)
        piy = np.clip(pred_y.astype(int), 0, H-1)
        
        # 2. Force: Seek the Cliffs (High Gradient Magnitude)
        # They are attracted to where 'cliff_intensity' is high
        # We can simulate this by making them surf the Iso-lines (Tangent)
        # but biased towards the "Edge Zone" (Potential ~ 20-30)
        
        curr_pot = potential[piy, pix]
        
        # Target Potential: The Chaotic Edge is usually around iter 20-40 in smooth count
        target = 30.0
        diff = target - curr_pot
        
        # Steer towards target potential
        # If diff > 0 (too far out), go up gradient
        # If diff < 0 (too deep in), go down gradient
        pfx = dir_x[piy, pix] * np.sign(diff) * 0.3
        pfy = dir_y[piy, pix] * np.sign(diff) * 0.3
        
        # Add strong circulation (Patrolling)
        pfx += -dir_y[piy, pix] * 0.5
        pfy += dir_x[piy, pix] * 0.5
        
        # 3. Update Predators
        pred_vx = pred_vx * 0.92 + pfx
        pred_vy = pred_vy * 0.92 + pfy
        
        # Normalize Speed
        pv_norm = np.sqrt(pred_vx**2 + pred_vy**2)
        pv_norm[pv_norm==0] = 1
        pred_vx = (pred_vx / pv_norm) * pred_speed
        pred_vy = (pred_vy / pv_norm) * pred_speed
        
        pred_x += pred_vx
        pred_y += pred_vy
        
        # --- Record Trails ---
        # Only record if in bounds
        valid_prey = (prey_x >= 0) & (prey_x < W) & (prey_y >= 0) & (prey_y < H)
        valid_pred = (pred_x >= 0) & (pred_x < W) & (pred_y >= 0) & (pred_y < H)
        
        np.add.at(trail_prey, (prey_y[valid_prey].astype(int), prey_x[valid_prey].astype(int)), 1)
        np.add.at(trail_pred, (pred_y[valid_pred].astype(int), pred_x[valid_pred].astype(int)), 1)

    print("  Rendering Habitat Map...")
    
    # Log scale for trails
    img_prey = np.log(trail_prey + 1)
    img_prey /= np.max(img_prey)
    
    img_pred = np.log(trail_pred + 1)
    img_pred /= np.max(img_pred)
    
    # Background: Structure of the Fractal (Dim Gray)
    structure = potential / max_iter
    
    # Composition
    # Red Channel = Predators (Chaos Hunters)
    # Green Channel = Prey (Stability Seekers)
    # Blue Channel = Structure/Water
    
    final_img = np.zeros((H, W, 3))
    
    # Predators are Hot Orange/Red
    final_img[:,:,0] = img_pred * 1.5 + structure * 0.2
    final_img[:,:,1] = img_prey * 1.2 + img_pred * 0.4 # Yellow overlap
    final_img[:,:,2] = img_prey * 0.5 + structure * 0.4
    
    # Enhance contrast
    final_img = np.clip(np.power(final_img, 0.8), 0, 1)
    
    fig, ax = plt.subplots(figsize=(10, 10), facecolor='black')
    ax.imshow(final_img, origin='lower')
    ax.axis('off')
    plt.title("Predator-Prey Fractal Ecology\n(Green=Prey/Basins, Red=Predators/Manifolds)", color='white')
    plt.savefig("predator_prey_fractal.png", facecolor='black')
    print("[+] Analysis saved: predator_prey_fractal.png")     
    plt.show()

predator_prey_fractal()