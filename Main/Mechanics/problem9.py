
import math
from clearScreen import clear_screen
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
