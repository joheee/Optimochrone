import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
height = 100  # initial height
g = 9.8  # acceleration due to gravity
mass = 1  # mass value

def visualize_custom_graph(mass, g, height, color, curve):
    # Linear curve equation
    def linear_curve(mass, t):
        return height - (mass * g) * t

    # Parabolic curve equation
    def parabolic_curve(mass, t):
        end_point_x = np.sqrt(2 * height / (mass * g))
        slope = -height / end_point_x
        a = -height / (end_point_x**2)
        return 2 * (slope * t + height) - (a * t**2 + height)

    # Create a single plot
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(curve)

    if color == 'red':
        color = 'r'
    elif color == 'green':
        color = 'g'
    elif color == 'blue':
        color = 'b'    

    if curve == 'linear curve':
        linear_time_to_reach_zero = height / (mass * g)
        ax.set_xlim(0, linear_time_to_reach_zero)
        ax.set_ylim(0, height)
        linear_line, = ax.plot([], [], f'{color}-', label='Linear')
        linear_point, = ax.plot([], [], f'{color}o', label=f'Linear: {linear_time_to_reach_zero:.2f}s')

        def update(frame):
            t = np.linspace(0, frame, 100)

            # Update linear curve
            linear_line.set_data(t, linear_curve(mass, t))
            linear_point.set_data([linear_time_to_reach_zero], [linear_curve(mass, linear_time_to_reach_zero)])

            return linear_line, linear_point

        # Create the animation
        animation = FuncAnimation(
            fig,
            update,
            frames=np.arange(0, linear_time_to_reach_zero, 0.1),
            blit=True
        )

        # Adjust spacing
        fig.tight_layout()

        ax.set_xlabel('Time')
        ax.set_ylabel('Height')
        ax.legend()

        plt.show()
    else:
        parabolic_time_to_reach_zero = np.sqrt(2 * height / (mass * g))
        ax.set_xlim(0, parabolic_time_to_reach_zero)
        ax.set_ylim(0, height)
        parabolic_line, = ax.plot([], [], f'{color}-', label='Parabolic')
        parabolic_point, = ax.plot([], [], f'{color}o', label=f'Parabolic: {parabolic_time_to_reach_zero:.2f}s')

        def update(frame):
            t = np.linspace(0, frame, 100)

            # Update parabolic curve
            parabolic_line.set_data(t, parabolic_curve(mass, t))
            parabolic_point.set_data([parabolic_time_to_reach_zero], [parabolic_curve(mass, parabolic_time_to_reach_zero)])

            return parabolic_line, parabolic_point

        # Create the animation
        animation = FuncAnimation(
            fig,
            update,
            frames=np.arange(0, parabolic_time_to_reach_zero, 0.1),
            blit=True
        )

        # Adjust spacing
        fig.tight_layout()

        # Show the plot
        ax.set_xlabel('Time')
        ax.set_ylabel('Height')
        ax.legend()
        
        plt.show()