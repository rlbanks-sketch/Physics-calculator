
import math
from clearScreen import clear_screen
from SafeFloat import safe_float_input
from ShowSolution import prompt_show_solution
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
    disc = b*2 - 4*a*c
    if disc < 0:
        print("No real solution for time of flight.")
        return
    sqrt_disc = math.sqrt(disc)
    t1 = (-b + sqrt_disc) / (2*a)
    t2 = (-b - sqrt_disc) / (2*a)
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