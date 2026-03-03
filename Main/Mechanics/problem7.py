
import math
from clearScreen import clear_screen
from SafeFloat import safe_float_input
from ShowSolution import prompt_show_solution
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
    b = viy
    c = -h_ceiling
    disc = b**2 - 4*a*c

    if disc < 0:
        print("Projectile never reaches the ceiling height.")
        return
    sqrt_disc = math.sqrt(disc)
    t1 = (-b + sqrt_disc) / (2*a)
    t2 = (-b - sqrt_disc) / (2*a)
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