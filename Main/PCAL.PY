import Main/Mechanics/problem1.py
import problem2
import problem3
import problem4
import problem5
import problem6
import problem7
import problem8
import problem9
def clear_screen():
    print("\n" * 20)

def safe_float_input(prompt, positive=False, zero_allowed=False):
    while True:
        try:
            val = float(input(prompt))
            if positive and val <= 0:
                print("Value must be positive.")
                continue
            if not zero_allowed and val == 0:
                print("Zero is not allowed.")
                continue
            return val
        except ValueError:
            print("Invalid number, try again.")

def prompt_show_solution():
    while True:
        ans = input("Show detailed solution? (Y/N): ").strip().lower()
        if ans in ('y','n'):
            return ans == 'y'
        print("Please enter Y or N.")



















def main():
    while True:
        clear_screen()
        print("Mechanics Problem Solver")
        print("1. Launch below horizontal")
        print("2. Fire hose height")
        print("3. Relative velocity")
        print("4. Simple free fall")
        print("5. Boat relative to ground")
        print("6. Baseball pitched roof")
        print("7. Pea projectile")
        print("8. Spitting cobra")
        print("9. frog jump")
        print("0. Exit")
        choice = input("Select (0-9): ").strip()
        if choice == '1':
            problem1_launch_below_horizontal()
        elif choice == '2':
            problem2_fire_hose_height()
        elif choice == '3':
            problem3_relative_velocity()
        elif choice == '4':
            problem4_free_fall()
        elif choice == '5':
            problem5_boat_speed_relative_to_ground()
        elif choice == '6':
            problem6_baseball_roof()
        elif choice == '7':
            problem7_pea_strike_ceiling()
        elif choice == '8':
            problem8_cobra_venom_range()
        elif choice == '9':
            problem9_frog_jump()
        elif choice == '0':
            print("Stay Golden")
            break
        else:
            print("Try again nigga.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
