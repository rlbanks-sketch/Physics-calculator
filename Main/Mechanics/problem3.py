
import math
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