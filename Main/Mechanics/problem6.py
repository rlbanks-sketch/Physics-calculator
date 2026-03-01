import math
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