
import math
def problem4_free_fall():
    clear_screen()
    print("Simple Free Fall\n")
    y0 = safe_float_input("Initial height y0 (m): ", positive=True)
    viy = safe_float_input("Initial vertical velocity viy (m/s): ")
    g=9.8
    a=0.5*g
    b=-viy
    c=-y0
    disc=b*b-4*a*c
    if disc < 0:
        print("No real solution for time.")
        return
    sqrt_disc=math.sqrt(disc)
    t1=(b+sqrt_disc)/(2*a)
    t2=(b-sqrt_disc)/(2*a)
    times=[t for t in [t1,t2] if t>=0]
    if not times:
        print("No positive time solution.")
        return
    t_impact=min(times)
    v_impact=viy - g*t_impact

    print("\nResults:")
    print("Time to hit ground: {:.3f} s".format(t_impact))
    print("Impact velocity: {:.3f} m/s".format(v_impact))

    if prompt_show_solution():
        print("\nDetailed Solution:")
        print("1) Equation: y = y0 + viy*t - 0.5*g*t² = 0")
        print("2) Coefficients: a = {:.3f}, b = {:.3f}, c = {:.3f}".format(a,b,c))
        print("3) Discriminant = {:.3f}".format(disc))
        print("4) Positive solution for t = {:.3f} s".format(t_impact))
        print("5) Impact velocity: v = viy - g * t = {:.3f} - {:.1f} * {:.3f} = {:.3f} m/s".format(viy,g,t_impact,v_impact))