
import math
from clearScreen import clear_screen
from SafeFloat import safe_float_input
from ShowSolution import prompt_show_solution
def safe_float_input(prompt, positive=False):
    while True:
        try:
            val = float(input(prompt))
            if positive and val <= 0:
                print("Value must be positive.")
                continue
            return val
        except ValueError:
            print("Invalid input, please enter a number.")

def problem7_pea_strike_ceiling():
    print("Pea projectile strike ceiling\n")

    v0 = safe_float_input("Launch speed (m/s): ", positive=True)
    angle_deg = safe_float_input("Launch angle (deg above horiz): ")
    if angle_deg < 0 or angle_deg > 90:
        print("Angle must be between 0 and 90 degrees.")
        return
    h_ceiling = safe_float_input("Ceiling height above table (m): ", positive=True)

    g = 9.8  # acceleration due to gravity (positive scalar for downward acceleration)
    theta = math.radians(angle_deg)

    # Initial velocity components
    vix = v0 * math.cos(theta)
    viy = v0 * math.sin(theta)

    # The vertical position as a function of time:
    # y(t) = viy * t - 0.5 * g * t^2
    # We want to find time t when y(t) = h_ceiling
    # => 0.5*g*t^2 - viy * t + h_ceiling = 0
    a = 0.5 * g
    b = -viy
    c = h_ceiling

    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        print("Projectile never reaches the ceiling height.")
        return

    sqrt_discriminant = math.sqrt(discriminant)
    t1 = (-b + sqrt_discriminant) / (2 * a)
    t2 = (-b - sqrt_discriminant) / (2 * a)

    # We consider only positive times
    times = [t for t in [t1, t2] if t > 0]

    if not times:
        print("Projectile never reaches the ceiling height at positive time.")
        return

    t_hit = min(times)

    # Vertical velocity at impact:
    # vy(t) = viy - g * t
    vy_impact = viy - g * t_hit

    # Horizontal velocity stays constant
    vx_impact = vix

    # Resultant speed on striking ceiling:
    v_impact = math.sqrt(vx_impact**2 + vy_impact**2)

    print("\nResults:")
    print(f"Time to reach ceiling: {t_hit:.3f} s")
    print(f"Speed on striking ceiling: {v_impact:.3f} m/s")

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
        print("   vix = {:.3f} m/s (constant)".format(v_impact))
        print("   viy = {:.3f} - {:.3f} * {:.3f} = {:.3f} m/s".format(viy, g, t_hit, v_impact))
        print("5) Impact speed = sqrt(vix² + viy²) = {:.3f} m/s".format(v_impact))