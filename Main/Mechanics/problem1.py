import math
from clearScreen import clear_screen
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