import numpy as np
import matplotlib.pyplot as plt

# Constants
height = 10  # initial height
g = 9.8  # acceleration due to gravity
mass = 1.0  # mass value

def export_default_graph(mass_a,mass_b,mass_c,mass_d,g,height,filename):
    # Linear curve equation
    def linear_curve(t):
        return height - (mass_a * g) * t

    # Parabolic curve equation
    def parabolic_curve(t):
        end_point_x = np.sqrt(2 * height / (mass_b * g))
        slope = -height / end_point_x
        a = -height / (end_point_x**2)
        return 2 * (slope * t + height) - (a * t**2 + height)

    # Circular curve equation
    def circular_curve(t):
        end_point_x = 2 * np.sqrt(height / (mass_c * g))
        slope = -height / end_point_x
        a = -height / (end_point_x**2)
        return 2 * (slope * t + height) - (a * t**2 + height)

    # Cycloidal curve equation
    def cycloid_curve(t):
        end_point_x = (2 * height / np.pi) * np.sqrt(np.pi / (2 * (mass_d * g) * height))
        slope = -height / end_point_x
        a = -height / (end_point_x**2)
        return 2 * (slope * t + height) - (a * t**2 + height)

    # Find the time at which each curve reaches 0 height
    linear_time_to_reach_zero = height / (mass_a * g)
    parabolic_time_to_reach_zero = np.sqrt(2 * height / (mass_b * g))
    circular_time_to_reach_zero = 2 * np.sqrt(height / (mass_c * g))
    cycloid_time_to_reach_zero = (2 * height / np.pi) * np.sqrt(np.pi / (2 * (mass_d * g) * height))

    # Plot the curves
    t = np.linspace(0, max(linear_time_to_reach_zero, parabolic_time_to_reach_zero, circular_time_to_reach_zero, cycloid_time_to_reach_zero), 100)

    fig, ax = plt.subplots()

    ax.plot(t, np.maximum(linear_curve(t), 0), 'b-', label='Linear')
    ax.plot(t, np.maximum(parabolic_curve(t), 0), 'g-', label='Parabolic')
    ax.plot(t, np.maximum(circular_curve(t), 0), 'r-', label='Circular')
    ax.plot(t, np.maximum(cycloid_curve(t), 0), 'm-', label='Cycloidal')

    # Plot the points where each curve reaches 0 height
    ax.plot(linear_time_to_reach_zero, 0, 'bo', label=f'Linear: {linear_time_to_reach_zero:.2f}s')
    ax.plot(parabolic_time_to_reach_zero, 0, 'go', label=f'Parabolic: {parabolic_time_to_reach_zero:.2f}s')
    ax.plot(circular_time_to_reach_zero, 0, 'ro', label=f'Circular: {circular_time_to_reach_zero:.2f}s')
    ax.plot(cycloid_time_to_reach_zero, 0, 'mo', label=f'Cycloidal: {cycloid_time_to_reach_zero:.2f}s')

    ax.set_ylim(0, height)
    ax.set_xlim(0, max(linear_time_to_reach_zero, parabolic_time_to_reach_zero, circular_time_to_reach_zero, cycloid_time_to_reach_zero))

    ax.set_xlabel('Time')
    ax.set_ylabel('Height')
    ax.legend()

    plt.savefig(f'result/{filename}')

    return True