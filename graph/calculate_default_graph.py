import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def calculate_default_graph(mass_a,mass_b,mass_c,mass_d,g,height):
    # Linear curve equation
    def linear_curve(mass_a,t):
        return height - (mass_a * g) * t

    # Parabolic curve equation
    def parabolic_curve(mass_b,t):
        end_point_x = np.sqrt(2 * height / (mass_b * g))
        slope = -height / end_point_x
        a = -height / (end_point_x**2)
        return 2 * (slope * t + height) - (a * t**2 + height)

    # Circular curve equation
    def circular_curve(mass_c,t):
        end_point_x = 2 * np.sqrt(height / (mass_c * g))
        slope = -height / end_point_x
        a = -height / (end_point_x**2)
        return 2 * (slope * t + height) - (a * t**2 + height)

    # Cycloidal curve equation
    def cycloid_curve(mass_d,t):
        end_point_x = (2 * height / np.pi) * np.sqrt(np.pi / (2 * (mass_d * g) * height))
        slope = -height / end_point_x
        a = -height / (end_point_x**2)
        return 2 * (slope * t + height) - (a * t**2 + height)

    # Find the time at which each curve reaches 0 height
    linear_time_to_reach_zero = height / (mass_a * g)
    parabolic_time_to_reach_zero = np.sqrt(2 * height / (mass_b * g))
    circular_time_to_reach_zero = 2 * np.sqrt(height / (mass_c * g))
    cycloid_time_to_reach_zero = (2 * height / np.pi) * np.sqrt(np.pi / (2 * (mass_d * g) * height))

    # Create subplots for each curve
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle('Default Graph')
    axs[0, 0].set_title('Linear Curve')
    axs[0, 1].set_title('Parabolic Curve')
    axs[1, 0].set_title('Circular Curve')
    axs[1, 1].set_title('Cycloidal Curve')

    # Set up the plot limits for each curve
    axs[0, 0].set_xlim(0, linear_time_to_reach_zero)
    axs[0, 0].set_ylim(0, height)
    axs[0, 1].set_xlim(0, parabolic_time_to_reach_zero)
    axs[0, 1].set_ylim(0, height)
    axs[1, 0].set_xlim(0, circular_time_to_reach_zero)
    axs[1, 0].set_ylim(0, height)
    axs[1, 1].set_xlim(0, cycloid_time_to_reach_zero)
    axs[1, 1].set_ylim(0, height)

    # Create empty lines for each curve
    linear_line, = axs[0, 0].plot([], [], 'b-', label='Linear')
    parabolic_line, = axs[0, 1].plot([], [], 'g-', label='Parabolic')
    circular_line, = axs[1, 0].plot([], [], 'r-', label='Circular')
    cycloid_line, = axs[1, 1].plot([], [], 'm-', label='Cycloidal')

    # Create empty points for each curve
    linear_point, = axs[0, 0].plot([], [], 'bo', label=f'Linear: {linear_time_to_reach_zero:.2f}s')
    parabolic_point, = axs[0, 1].plot([], [], 'go', label=f'Parabolic: {parabolic_time_to_reach_zero:.2f}s')
    circular_point, = axs[1, 0].plot([], [], 'ro', label=f'Circular: {circular_time_to_reach_zero:.2f}s')
    cycloid_point, = axs[1, 1].plot([], [], 'mo', label=f'Cycloidal: {cycloid_time_to_reach_zero:.2f}s')

    # Set common labels for x-axis and y-axis
    for ax in axs.flat:
        ax.set_xlabel('Time')
        ax.set_ylabel('Height')

    # Add legend to each subplot
    axs[0, 0].legend()
    axs[0, 1].legend()
    axs[1, 0].legend()
    axs[1, 1].legend()

    # Function to update the plot for each frame
    def update(frame):
        t = np.linspace(0, frame, 100)

        # Update linear curve
        linear_line.set_data(t, linear_curve(mass_a,t))
        linear_point.set_data([linear_time_to_reach_zero], [linear_curve(mass_a,linear_time_to_reach_zero)])

        # Update parabolic curve
        parabolic_line.set_data(t, parabolic_curve(mass_b,t))
        parabolic_point.set_data([parabolic_time_to_reach_zero], [parabolic_curve(mass_b,parabolic_time_to_reach_zero)])

        # Update circular curve
        circular_line.set_data(t, circular_curve(mass_c,t))
        circular_point.set_data([circular_time_to_reach_zero], [circular_curve(mass_c,circular_time_to_reach_zero)])

        # Update cycloidal curve
        cycloid_line.set_data(t, cycloid_curve(mass_d,t))
        cycloid_point.set_data([cycloid_time_to_reach_zero], [cycloid_curve(mass_d,cycloid_time_to_reach_zero)])

        return (linear_line, linear_point, parabolic_line, parabolic_point, circular_line, circular_point, cycloid_line, cycloid_point)

    # Create the animation
    animation = FuncAnimation(fig, update, frames=np.arange(0, max(linear_time_to_reach_zero, parabolic_time_to_reach_zero, circular_time_to_reach_zero, cycloid_time_to_reach_zero), 0.1), blit=True)

    # Adjust spacing between subplots
    fig.tight_layout()

    # Show the plot
    plt.show()