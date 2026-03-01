import math
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