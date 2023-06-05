import tkinter as tk
import customtkinter

def learn_more(app):
    learn_more_frame = customtkinter.CTkFrame(master=app, width=600, height=500, corner_radius=0)
    
    learn_more_title = customtkinter.CTkLabel(learn_more_frame, text="Learn More Page")
    learn_more_title.pack(pady=(10,0), padx=10)
    
    text_explanation_content = """Linear Curve
    
A linear curve, also known as a straight line, is a basic mathematical concept in geometry and algebra. It is the simplest form of a curve and is characterized by having a constant slope or rate of change.

In a two-dimensional Cartesian coordinate system, a linear curve is represented by an equation in the form of y = mx + b, where m is the slope of the line, and b is the y-intercept (the point where the line intersects the y-axis). The slope determines the steepness of the line, indicating how much the y-coordinate changes for a given change in the x-coordinate.

A linear curve can be described as a sequence of points that lie in a straight line, forming a consistent and predictable pattern. It has the same slope and follows the same direction throughout its length. Any two points on a linear curve can be used to calculate the slope and determine the equation of the line.

Linear curves have several important properties:
1. Constant Slope: The slope of a linear curve remains constant along its entire length. It indicates the rate of change of the y-coordinate with respect to the x-coordinate.
2. Y-Intercept: The y-intercept is the point where the line intersects the y-axis. It represents the value of y when x is equal to zero.
3. X-Intercept: The x-intercept is the point where the line intersects the x-axis. It represents the value of x when y is equal to zero.
4. Linearity: A linear curve is characterized by its straightness. It does not bend or curve in any way.

Linear curves have numerous applications in various fields, such as physics, economics, engineering, and data analysis. They are used to model and analyze relationships between variables that exhibit a constant rate of change. Additionally, linear regression is a common statistical technique that uses linear curves to fit a line to a set of data points and make predictions based on that line.



Parabola Curve

A parabola is a U-shaped curve that is symmetric about its vertex. It is a conic section formed by the intersection of a right circular cone and a plane parallel to one of the cone's sides.

In a two-dimensional Cartesian coordinate system, a parabola is represented by an equation in the form of y = ax^2 + bx + c, where a, b, and c are constants. The coefficient a determines the direction and width of the parabola. If a is positive, the parabola opens upward, and if a is negative, it opens downward.

The vertex of a parabola is the point where the curve reaches its minimum or maximum value, depending on the direction it opens. It is given by the coordinates (h, k), where h = -b/(2a) and k = f(h), with f(h) being the value of y when x = h.

Parabolas have several important properties:
1. Axis of Symmetry: The axis of symmetry is a vertical line that passes through the vertex of the parabola. It divides the parabola into two symmetric halves.
2. Focus: The focus is a point inside the parabola that is equidistant from the vertex and the directrix. It is denoted by (h, k + 1/(4a)).
3. Directrix: The directrix is a horizontal line that is equidistant from the vertex and the focus. It is given by the equation y = k - 1/(4a).
4. Vertex Form: The vertex form of a parabola's equation is y = a(x - h)^2 + k, where (h, k) is the vertex.

Parabolas have various applications in physics, engineering, optics, computer graphics, and many other fields. They are used to describe the trajectories of projectiles, the shapes of satellite dishes, the behavior of antennas, and the paths of light rays reflecting off a curved surface, among other things.



Circle Curve

A circle graph, also known as a pie chart, is a visual representation of data that is divided into sectors, each representing a proportion or percentage of a whole. It is called a circle graph because it resembles a circle, with each sector resembling a slice of a pie.

In a circle graph, the entire circle represents the total or 100% of the data. Each sector within the circle corresponds to a specific category or group within the data set. The size of each sector is determined by the proportion or percentage it represents.

Circle graphs are commonly used to display data that can be divided into categories, such as survey results, sales distribution, or demographic composition. They provide a clear and intuitive way to compare the relative sizes of different categories within a whole.

To create a circle graph, the data is first divided into categories and the corresponding proportions or percentages are calculated. These values are then used to determine the angle of each sector in the circle. The central angle of each sector is proportional to the proportion or percentage it represents.

Circle graphs are effective for presenting data at a glance and can convey information quickly and easily. They are widely used in presentations, reports, and publications to communicate data and statistics in a visually appealing manner.



Cycloid Curve

A cycloid is a curve traced by a point on the circumference of a rolling circle. It is a specific type of curve in mathematics that exhibits interesting properties and is often studied in the field of geometry.

In a cycloid, the rolling circle is usually considered to be of a fixed radius, and the point on the circumference of the rolling circle traces the path as it rolls along a straight line. The resulting curve is known as a cycloid.

Cycloids have unique characteristics:
1. Parametric Equations: A cycloid can be defined using parametric equations. For a cycloid generated by a circle of radius r, the parametric equations for the x and y coordinates of the point on the circumference are:
    x = r(t - sin(t))
    y = r(1 - cos(t))
   where t is the parameter that represents the angle of rotation of the rolling circle.
   
2. Symmetry: Cycloids are symmetric curves. The arc traced by the point on the circumference from the starting position to the ending position is symmetric with respect to the horizontal line passing through the center of the rolling circle.

3. Cusps: A cycloid has cusps, which are points of self-intersection where the curve changes direction. These cusps occur when the rolling circle completes one full rotation.

Cycloids have various applications in mathematics, physics, and engineering. They are used to model the motion of objects, such as wheels rolling on a surface or pendulums swinging back and forth. Cycloidal motion is also utilized in gear designs and in the study of fluid dynamics.

The study of cycloids has fascinated mathematicians for centuries due to their intriguing properties and geometric beauty. They continue to be an important topic in mathematics and serve as an example of how complex curves can arise from simple motions.
"""

    # Create a custom scrollbar
    explanation_scrollbar = customtkinter.CTkScrollbar(learn_more_frame)
    explanation_scrollbar.pack(side=customtkinter.RIGHT, fill=customtkinter.Y)

    # Create a Text widget
    text_explanation = tk.Text(learn_more_frame, wrap=tk.WORD, yscrollcommand=explanation_scrollbar.set)
    text_explanation.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    text_explanation.insert(tk.END, text_explanation_content)

    # Disable the text widget
    text_explanation.configure(state="disabled")

    # Configure the scrollbar to work with the Text widget
    explanation_scrollbar.configure(command=text_explanation.yview)

    return learn_more_frame
