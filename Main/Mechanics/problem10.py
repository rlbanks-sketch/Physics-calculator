import math
from clearScreen import clear_screen
from SafeFloat import safe_float_input
from ShowSolution import prompt_show_solution

def calculate_relative_velocity():
    clear_screen()
    print("Enter the velocity of the cruise ship:")
    v_c = float(input("Speed (m/s) (cruise ship, due south): "))
    
    print("\nEnter the velocity of the patrol boat:")
    v_p = float(input("Speed (m/s) (patrol boat): "))
    angle_deg = float(input("Direction of patrol boat velocity (degrees north of west): "))
    
    # Convert angle to radians
    angle_rad = math.radians(angle_deg)
    
    # Components of cruise ship velocity (due south)
    v_c_x = 0.0
    v_c_y = -v_c
    
    # Components of patrol boat velocity
    v_p_x = -v_p * math.cos(angle_rad)
    v_p_y = v_p * math.sin(angle_rad)
    
    # Relative velocity components (cruise ship relative to patrol boat)
    v_rel_x = v_c_x - v_p_x
    v_rel_y = v_c_y - v_p_y
    
    print("\nDo you want to see the detailed solution steps? (yes/no)")
    show_steps = input().strip().lower()
    
    if show_steps == 'yes':
        print("\n--- Solution Steps ---")
        print(f"1. Cruise ship velocity vector (x, y): ({v_c_x:.2f}, {v_c_y:.2f}) m/s")
        print(f"2. Patrol boat velocity vector (x, y): ({v_p_x:.2f}, {v_p_y:.2f}) m/s")
        print("   - Patrol boat x-component: -v_p * cos(angle) = -{:.2f} * cos({:.2f}°) = {:.2f}".format(v_p, angle_deg, v_p_x))
        print("   - Patrol boat y-component: v_p * sin(angle) = {:.2f} * sin({:.2f}°) = {:.2f}".format(v_p, angle_deg, v_p_y))
        print(f"3. Relative velocity x-component: v_c_x - v_p_x = {v_c_x:.2f} - ({v_p_x:.2f}) = {v_rel_x:.2f} m/s")
        print(f"4. Relative velocity y-component: v_c_y - v_p_y = {v_c_y:.2f} - ({v_p_y:.2f}) = {v_rel_y:.2f} m/s")
        print("----------------------")
    
    print(f"\nRelative velocity components of the cruise ship relative to the patrol boat:")
    print(f"   x-component: {v_rel_x:.2f} m/s")
    print(f"   y-component: {v_rel_y:.2f} m/s")

if __name__ == "__main__":
    calculate_relative_velocity()
