def prompt_show_solution():
    while True:
        ans = input("Show detailed solution? (Y/N): ").strip().lower()
        if ans in ('y','n'):
            return ans == 'y'
        print("Please enter Y or N.")