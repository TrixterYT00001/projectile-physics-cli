import math

def simulate_projectile(v0, angle_deg):
    g = 9.81
    angle_rad = math.radians(angle_deg)
    
    # Physics Formulas
    t_flight = (2 * v0 * math.sin(angle_rad)) / g
    max_height = (v0**2 * math.sin(angle_rad)**2) / (2 * g)
    total_range = (v0**2 * math.sin(2 * angle_rad)) / g
    
    print(f"--- Simulation Results ---")
    print(f"Angle: {angle_deg}° | Initial Velocity: {v0}m/s")
    print(f"Time of Flight: {t_flight:.2f}s")
    print(f"Max Height: {max_height:.2f}m")
    print(f"Horizontal Range: {total_range:.2f}m\n")

    # Simple text-based "Flex" trajectory
    print("Trajectory Plot:")
    for y in range(10, -1, -1):
        line = ""
        for x in range(0, 40):
            # Equation of trajectory: y = x*tan(theta) - (g*x^2)/(2*v0^2*cos^2(theta))
            # Scaled for terminal view
            scaled_x = x * (total_range / 40)
            target_y = scaled_x * math.tan(angle_rad) - (g * scaled_x**2) / (2 * v0**2 * math.cos(angle_rad)**2)
            if abs(target_y - (y * max_height / 10)) < (max_height / 15):
                line += "●"
            else:
                line += " "
        print(f"{y:2d}| {line}")
    print("   " + "-" * 40 + "> Range")

simulate_projectile(50, 4
  5)
