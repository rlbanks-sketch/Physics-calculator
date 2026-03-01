import math

def clear_screen():
    print("\n" * 20)

def safe_float_input(prompt, positive=False, zero_allowed=False):
    while True:
        try:
            val = float(input(prompt))
            if positive and val <= 0:
                print("Value must be positive.")
                continue
            if not zero_allowed and val == 0:
                print("Zero is not allowed.")
                continue
            return val
        except ValueError:
            print("Invalid number, try again.")

def prompt_show_solution():
    while True:
        ans = input("Show detailed solution? (Y/N): ").strip().lower()
        if ans in ('y','n'):
            return ans == 'y'
        print("Please enter Y or N.")

def problem1_launch_below_horizontal():
    clear_screen()
    print("Launch Below Horizontal\n")
    
    vi = safe_float_input("Init velocity (m/s): ", positive=True)
    theta_deg = safe_float_input("Angle below horiz (deg 0-90): ")
    if theta_deg < 0 or theta_deg > 90:
        print("Angle must be between 0 and 90.")
        return
    t_flight = safe_float_input("Time of flight (s): ", positive=True)
    vertical_drop = safe_float_input("Vertical drop from start (m): ", positive=True)

    g = 9.8
    theta = math.radians(theta_deg)
    vix = vi * math.cos(theta)
    viy = -vi * math.sin(theta)
    y0 = 0.5 * g * t_flight**2 - viy * t_flight
    xfinal = vix * t_flight
    a = 0.5 * g
    b = -viy
    c = -vertical_drop
    disc = b**2 - 4*a*c

    print("\nResults:")
    print("Initial velocity components:")
    print(" vix = {:.3f} m/s".format(vix))
    print(" viy = {:.3f} m/s (downward)".format(viy))
    print("Initial height y0 = {:.3f} m".format(y0))
    print("Horizontal range = {:.3f} m".format(xfinal))

    if disc < 0:
        print("Time to reach {:.3f} m below start: No real solution".format(vertical_drop))
    else:
        sqrt_disc = math.sqrt(disc)
        t1 = (-b + sqrt_disc) / (2*a)
        t2 = (-b - sqrt_disc) / (2*a)
        valid_times = [t for t in [t1,t2] if t > 0]
        if valid_times:
            print("Time to reach {:.3f} m below start: {:.3f} s".format(vertical_drop, min(valid_times)))
        else:
            print("Time to reach {:.3f} m below start: No positive time solution".format(vertical_drop))

    if prompt_show_solution():
        print("\nDetailed Solution:")
        print("1) Decompose velocity:")
        print("   vix = vi * cos(θ) = {:.3f} * cos({:.3f} rad) = {:.3f} m/s".format(vi, theta, vix))
        print("   viy = -vi * sin(θ) = -{:.3f} * sin({:.3f} rad) = {:.3f} m/s".format(vi, theta, viy))
        print("2) Calculate initial height y0:")
        print("   y0 = 0.5 * g * t² - viy * t = 0.5 * {:.1f} * {:.3f}² - ({:.3f}) * {:.3f} = {:.3f} m".format(g, t_flight, viy, t_flight, y0))
        print("3) Calculate horizontal range:")
        print("   xfinal = vix * t = {:.3f} * {:.3f} = {:.3f} m".format(vix, t_flight, xfinal))
        if disc >= 0:
            print("4) Solve quadratic for vertical drop time:")
            print("   a = {:.3f}, b = {:.3f}, c = {:.3f}".format(a, b, c))
            print("   Discriminant = {:.3f}".format(disc))
            if valid_times:
                print("   Valid positive times: {}".format(", ".join("{:.3f}s".format(t) for t in valid_times)))
                print("   Time to reach vertical drop = {:.3f} s".format(min(valid_times)))
            else:
                print("   No positive time solution.")

def problem2_fire_hose_height():
    clear_screen()
    print("Fire Hose Height at Building\n")
    vi = safe_float_input("Init speed vi (m/s): ", positive=True)
    theta_deg = safe_float_input("Angle above horiz (deg 0-90): ")
    if theta_deg < 0 or theta_deg > 90:
        print("Angle must be between 0 and 90.")
        return
    d = safe_float_input("Distance to building d (m): ", positive=True)
    g = 9.8
    theta = math.radians(theta_deg)
    vix = vi * math.cos(theta)
    viy = vi * math.sin(theta)
    t = d / vix
    y = viy * t - 0.5 * g * t ** 2

    print("\nResults:")
    print("Time to reach building: {:.3f} s".format(t))
    print("Height at building: {:.3f} m".format(y))

    if prompt_show_solution():
        print("\nDetailed Solution:")
        print("1) Decompose velocity:")
        print("   vix = {:.3f} * cos({:.3f} rad) = {:.3f} m/s".format(vi, theta, vix))
        print("   viy = {:.3f} * sin({:.3f} rad) = {:.3f} m/s".format(vi, theta, viy))
        print("2) Calculate time to reach building: t = d / vix = {:.3f} / {:.3f} = {:.3f} s".format(d, vix, t))
        print("3) Calculate height at building:")
        print("   y = viy*t - 0.5*g*t² = {:.3f}*{:.3f} - 0.5*{:.1f}*{:.3f}² = {:.3f} m".format(viy, t, g, t, y))

def problem3_relative_velocity():
    clear_screen()
    print("Relative Velocity: Cruise vs Patrol\n")
    v_cruise = safe_float_input("Cruise ship speed (m/s, south): ")
    v_patrol = safe_float_input("Patrol boat speed (m/s): ")
    angle_deg = safe_float_input("Patrol boat dir (deg N of W 0-90): ")
    if angle_deg < 0 or angle_deg > 90:
        print("Angle must be 0 to 90 deg.")
        return
    angle_std_deg = 180 - angle_deg
    angle_std_rad = math.radians(angle_std_deg)
    vC_x = 0
    vC_y = -v_cruise
    vP_x = v_patrol * math.cos(angle_std_rad)
    vP_y = v_patrol * math.sin(angle_std_rad)
    v_rel_x = vC_x - vP_x
    v_rel_y = vC_y - vP_y

    print("\nResults:")
    print("Relative velocity components:")
    print(" v_rel_x = {:.3f} m/s".format(v_rel_x))
    print(" v_rel_y = {:.3f} m/s".format(v_rel_y))

    if prompt_show_solution():
        print("\nDetailed Solution:")
        print("1) Cruise ship velocity components:")
        print("   vC_x = 0 (due south)")
        print("   vC_y = -{:.3f} m/s".format(v_cruise))
        print("2) Patrol boat velocity components:")
        print("   angle from +x east = 180° - {:.3f}° = {:.3f}°".format(angle_deg, angle_std_deg))
        print("   vP_x = {:.3f} * cos({:.3f} rad) = {:.3f} m/s".format(v_patrol, angle_std_rad, vP_x))
        print("   vP_y = {:.3f} * sin({:.3f} rad) = {:.3f} m/s".format(v_patrol, angle_std_rad, vP_y))
        print("3) Relative velocity vector = cruise - patrol:")
        print("   v_rel_x = 0 - {:.3f} = {:.3f} m/s".format(vP_x, v_rel_x))
        print("   v_rel_y = -{:.3f} - {:.3f} = {:.3f} m/s".format(v_cruise, vP_y, v_rel_y))

def problem4_free_fall():
    clear_screen()
    print("Simple Free Fall\n")
    y0 = safe_float_input("Initial height y0 (m): ", positive=True)
    viy = safe_float_input("Initial vertical velocity viy (m/s): ")
    g=9.8
    a=0.5*g
    b=-viy
    c=-y0
    disc=b*b-4*a*c
    if disc < 0:
        print("No real solution for time.")
        return
    sqrt_disc=math.sqrt(disc)
    t1=(b+sqrt_disc)/(2*a)
    t2=(b-sqrt_disc)/(2*a)
    times=[t for t in [t1,t2] if t>=0]
    if not times:
        print("No positive time solution.")
        return
    t_impact=min(times)
    v_impact=viy - g*t_impact

    print("\nResults:")
    print("Time to hit ground: {:.3f} s".format(t_impact))
    print("Impact velocity: {:.3f} m/s".format(v_impact))

    if prompt_show_solution():
        print("\nDetailed Solution:")
        print("1) Equation: y = y0 + viy*t - 0.5*g*t² = 0")
        print("2) Coefficients: a = {:.3f}, b = {:.3f}, c = {:.3f}".format(a,b,c))
        print("3) Discriminant = {:.3f}".format(disc))
        print("4) Positive solution for t = {:.3f} s".format(t_impact))
        print("5) Impact velocity: v = viy - g * t = {:.3f} - {:.1f} * {:.3f} = {:.3f} m/s".format(viy,g,t_impact,v_impact))

def problem5_boat_speed_relative_to_ground():
    clear_screen()
    print("Boat speed relative to ground\n")

    v_boat = safe_float_input("Boat speed relative to water (m/s): ", positive=True)
    v_current = safe_float_input("River current speed (m/s, east): ", positive=True)

    # Boat heading east (with current)
    speed_east = v_boat + v_current
    # Boat heading west (against current)
    speed_west = abs(v_boat - v_current)  # absolute speed relative to ground

    print("\nResults:")
    print("Boat speed relative to ground when heading east (with current): {:.3f} m/s".format(speed_east))
    print("Boat speed relative to ground when heading west (against current): {:.3f} m/s".format(speed_west))

    if prompt_show_solution():
        print("\nDetailed Solution:")
        print("1) When heading east (with current): speeds add linearly")
        print("   Speed = boat speed + current speed = {:.3f} + {:.3f} = {:.3f} m/s".format(v_boat, v_current, speed_east))
        print("2) When heading west (against current): speeds subtract")
        print("   Speed = |boat speed - current speed| = |{:.3f} - {:.3f}| = {:.3f} m/s".format(v_boat, v_current, speed_west))

def problem6_baseball_roof():
    clear_screen()
    print("Baseball rolling off pitched roof\n")

    v_rollerspeed = safe_float_input("Speed rolling down/off roof (m/s): ", positive=True)
    angle_deg = safe_float_input("Roof pitch angle (deg below horiz): ")
    if angle_deg < 0 or angle_deg > 90:
        print("Angle must be between 0 and 90.")
        return
    y_roof = safe_float_input("Roof edge height (m): ", positive=True)

    g = 9.8
    theta = math.radians(angle_deg)

    # Velocity components (angle below horizontal, vertical component negative/downward)
    vix = v_rollerspeed * math.cos(theta)
    viy = - v_rollerspeed * math.sin(theta)  # downward is negative

    # Solve for time until ball hits ground y=0:
    # 0 = y_roof + viy * t - 0.5 * g * t^2
    a = 0.5 * g
    b = viy
    c = y_roof

    disc = b**2 - 4*a*c
    if disc < 0:
        print("No real solution for time in air.")
        return
    sqrt_disc = math.sqrt(disc)
    t1 = (-b + sqrt_disc) / (2*a)
    t2 = (-b - sqrt_disc) / (2*a)
    times = [t for t in [t1, t2] if t > 0]
    if not times:
        print("No positive time solution.")
        return
    t_air = min(times)

    x = vix * t_air

    print("\nResults:")
    print("Time in air: {:.3f} s".format(t_air))
    print("Horizontal distance from roof edge: {:.3f} m".format(x))
    print("Horizontal distance from roof edge: {:.3f} m".format(x))

    if prompt_show_solution():
        print("\nDetailed Solution:")
        print("1) Velocity components off roof:")
        print("   vix = {:.3f} * cos({:.3f} rad) = {:.3f} m/s".format(v_rollerspeed, theta, vix))
        print("   viy = -{:.3f} * sin({:.3f} rad) = {:.3f} m/s".format(v_rollerspeed, theta, viy))
        print("2) Solve y(t) = 0 for time in air:")
        print("   a = 0.5 * g = {:.3f}".format(a))
        print("   b = -viy = {:.3f}".format(b))
        print("   c = -y_roof = {:.3f}".format(c))
        print("   Discriminant = {:.3f}".format(disc))
        print("3) Time in air (positive root): {:.3f} s".format(t_air))
        print("4) Horizontal distance x = vix * t_air = {:.3f} * {:.3f} = {:.3f} m".format(vix, t_air, x))

def problem7_pea_strike_ceiling():
    clear_screen()
    print("Pea projectile strike ceiling\n")

    v0 = safe_float_input("Launch speed (m/s): ", positive=True)
    angle_deg = safe_float_input("Launch angle (deg above horiz): ")
    if angle_deg < 0 or angle_deg > 90:
        print("Angle must be 0 to 90.")
        return
    h_ceiling = safe_float_input("Ceiling height above table (m): ", positive=True)

    g = 9.8
    theta = math.radians(angle_deg)
    vix = v0 * math.cos(theta)
    viy = v0 * math.sin(theta)

    # Equation y(t) = viy * t - 0.5*g*t^2 = h_ceiling
    # Rearrange: 0.5*g*t^2 - viy * t + h_ceiling = 0
    a = 0.5 * g
    b = -viy
    c = h_ceiling
    disc = b*b - 4*a*c

    if disc < 0:
        print("Projectile never reaches the ceiling height.")
        return
    sqrt_disc = math.sqrt(disc)
    t1 = (b + sqrt_disc) / (2*a)
    t2 = (b - sqrt_disc) / (2*a)
    times = [t for t in [t1, t2] if t > 0]
    if not times:
        print("Projectile never reaches ceiling height on upward or downward path.")
        return
    t_hit = min(times)

    # Calculate vertical and horizontal velocities at impact:
    vix_impact = vix  # horizontal velocity constant
    viy_impact = viy - g * t_hit
    v_impact = math.sqrt(vix_impact**2 + viy_impact**2)

    print("\nResults:")
    print("Time to reach ceiling: {:.3f} s".format(t_hit))
    print("Speed on striking ceiling: {:.3f} m/s".format(v_impact))

    if prompt_show_solution():
        print("\nDetailed Solution:")
        print("1) Decompose initial velocity:")
        print("   vix = {:.3f} * cos({:.3f} rad) = {:.3f} m/s".format(v0, theta, vix))
        print("   viy = {:.3f} * sin({:.3f} rad) = {:.3f} m/s".format(v0, theta, viy))
        print("2) Solve y(t) = h_ceiling:")
        print("   0.5*g*t² - viy*t + h = 0")
        print("   a = {:.3f}, b = {:.3f}, c = {:.3f}".format(a,b,c))
        print("   Discriminant = {:.3f}".format(disc))
        print("3) Positive solution for t: {:.3f} s".format(t_hit))
        print("4) Velocity components at impact:")
        print("   vix = {:.3f} m/s (constant)".format(vix_impact))
        print("   viy = {:.3f} - {:.3f} * {:.3f} = {:.3f} m/s".format(viy, g, t_hit, viy_impact))
        print("5) Impact speed = sqrt(vix² + viy²) = {:.3f} m/s".format(v_impact))

def problem8_cobra_venom_range():
    clear_screen()
    print("Spitting Cobra Venom Range\n")

    h_launch = safe_float_input("Launch height (m): ", positive=True)
    v0 = safe_float_input("Launch speed (m/s): ", positive=True)
    angle_deg = safe_float_input("Launch angle (deg above horiz): ")

    if angle_deg < 0 or angle_deg > 90:
        print("Angle must be between 0 and 90.")
        return

    g = 9.8
    theta = math.radians(angle_deg)
    vix = v0 * math.cos(theta)
    viy = v0 * math.sin(theta)

    # Quadratic for time until projectile hits ground (y=0):
    # y(t) = h_launch + viy*t - 0.5*g*t² = 0
    a = 0.5 * g
    b = -viy
    c = -h_launch
    disc = b*b - 4*a*c
    if disc < 0:
        print("No real solution for time of flight.")
        return
    sqrt_disc = math.sqrt(disc)
    t1 = (b + sqrt_disc) / (2*a)
    t2 = (b - sqrt_disc) / (2*a)
    times = [t for t in [t1,t2] if t > 0]
    if not times:
        print("No positive time solution.")
        return
    t_land = max(times)

    # Horizontal distance
    x = vix * t_land

    print("\nResults:")
    print("Time of flight: {:.3f} s".format(t_land))
    print("Horizontal distance traveled: {:.3f} m".format(x))

    if prompt_show_solution():
        print("\nDetailed Solution:")
        print("1) Velocity components:")
        print("   vix = {:.3f} * cos({:.3f} rad) = {:.3f} m/s".format(v0, theta, vix))
        print("   viy = {:.3f} * sin({:.3f} rad) = {:.3f} m/s".format(v0, theta, viy))
        print("2) Time of flight from quadratic:")
        print("   0.5*g*t² - viy*t - h_launch = 0")
        print("   a = {:.3f}, b = {:.3f}, c = {:.3f}".format(a,b,c))
        print("   Discriminant = {:.3f}".format(disc))
        print("3) Positive time to land: {:.3f} s".format(t_land))
        print("4) Horizontal range: x = vix * t = {:.3f} * {:.3f} = {:.3f} m".format(vix, t_land, x))

def problem9_frog_jump():
    clear_screen()
    print("Calaveras County Jumping Frog Jubilee\n")

    d_jump = safe_float_input("Jump distance (m): ", positive=True)
    angle_deg = safe_float_input("Launch angle (deg): ")
    if angle_deg < 0 or angle_deg > 90:
        print("Angle must be between 0 and 90.")
        return

    g = 9.8
    theta = math.radians(angle_deg)

    # Range formula: d = (v^2 * sin(2θ)) / g → v = sqrt( d * g / sin(2θ) )
    sin_2theta = math.sin(2*theta)
    if sin_2theta == 0:
        print("Invalid angle (sin 2θ = 0).")
        return

    v_launch = math.sqrt(d_jump * g / sin_2theta)

    # Time of flight: t = 2*v*sin(θ) / g
    t_flight = 2 * v_launch * math.sin(theta) / g

    print("\nResults:")
    print("Launch speed needed: {:.3f} m/s".format(v_launch))
    print("Time of flight: {:.3f} s".format(t_flight))

    if prompt_show_solution():
        print("\nDetailed Solution:")
        print("1) Range formula: d = (v² sin(2θ))/g")
        print("2) Solve for v:")
        print("   v = sqrt( d * g / sin(2θ) )")
        print("   d = {:.3f}, g = {:.3f}, sin(2θ) = {:.3f}".format(d_jump, g, sin_2theta))
        print("   v = sqrt({:.3f} * {:.3f} / {:.3f}) = {:.3f} m/s".format(d_jump, g, sin_2theta, v_launch))
        print("3) Time of flight:")
        print("   t = 2 * v * sin(θ) / g")
        print("     = 2 * {:.3f} * sin({:.3f} rad) / {:.3f} = {:.3f} s".format(v_launch, theta, g, t_flight))


def main():
    while True:
        clear_screen()
        print("Mechanics Problem Solver")
        print("1. Launch below horizontal")
        print("2. Fire hose height")
        print("3. Relative velocity")
        print("4. Simple free fall")
        print("5. Boat relative to ground")
        print("6. Baseball pitched roof")
        print("7. Pea projectile")
        print("8. Spitting cobra")
        print("9.frog jump")
        print("0. Exit")
        choice = input("Select (0-9): ").strip()
        if choice == '1':
            problem1_launch_below_horizontal()
        elif choice == '2':
            problem2_fire_hose_height()
        elif choice == '3':
            problem3_relative_velocity()
        elif choice == '4':
            problem4_free_fall()
        elif choice == '5':
            problem5_boat_speed_relative_to_ground()
        elif choice == '6':
            problem6_baseball_roof()
        elif choice == '7':
            problem7_pea_strike_ceiling()
        elif choice == '8':
            problem8_cobra_venom_range()
        elif choice == '9':
            problem9_frog_jump()
        elif choice == '0':
            print("Stay Golden")
            break
        else:
            print("Try again nigga.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
