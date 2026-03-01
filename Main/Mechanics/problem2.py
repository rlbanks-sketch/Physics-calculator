
import math
from clearScreen import clear_screen
from SafeFloat import safe_float_input
from ShowSolution import prompt_show_solution
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