import customtkinter
from tkinter import messagebox
import graph.visualize_custom_graph as vc

def custom_graph(app):

    custom_graph_frame = customtkinter.CTkFrame(master=app, width=300, height=300,corner_radius=0)
    
    label = customtkinter.CTkLabel(custom_graph_frame, text="Custom Graphs")
    label.pack(pady=(10,0))
    
    mass_a_input = customtkinter.CTkTextbox(custom_graph_frame, height=10)
    mass_a_input.insert("0.0", "Mass")
    mass_a_input.pack(pady=(10,0), padx=(0,10))
    
    gravity_input = customtkinter.CTkTextbox(custom_graph_frame, height=10)
    gravity_input.insert("0.0", "Gravity")
    gravity_input.pack(pady=(10,0), padx=(0,10))
    
    height_input = customtkinter.CTkTextbox(custom_graph_frame, height=10)
    height_input.insert("0.0", "Height")
    height_input.pack(pady=(10,0), padx=(0,10))
    
    background_color_option = customtkinter.CTkOptionMenu(custom_graph_frame, values=["red", "green",'blue'])
    background_color_option.pack(pady=(10,0), padx=10)
    
    curve_option = customtkinter.CTkOptionMenu(custom_graph_frame, values=["linear curve", "parabolic curve",'circular curve','cycloid curve'])
    curve_option.pack(pady=(10,0), padx=10)
    
    def validate_input(input_value, message):
        try:
            # Try converting the input to an integer
            int_value = int(input_value)
            return int_value
        except ValueError:
            try:
                # Try converting the input to a float
                float_value = float(input_value)
                return float_value
            except ValueError:
                # Display error message if the input is neither an integer nor a float
                messagebox.showerror("Error", message)
                return None
    
    def handle_load_graph():
        if validate_input(mass_a_input.get('1.0', 'end-1c'), 'mass must be a valid number!') is None:
            return
        if validate_input(gravity_input.get('1.0', 'end-1c'), 'gravity must be a valid number!') is None:
            return
        if validate_input(height_input.get('1.0', 'end-1c'), 'height must be a valid number!') is None:
            return
        
        mass = int(float(mass_a_input.get('1.0', 'end-1c')))
        g = float(gravity_input.get('1.0', 'end-1c'))
        height = float(height_input.get('1.0', 'end-1c'))
        color = background_color_option.get()
        curve = curve_option.get()
        
        vc.visualize_custom_graph(mass, g, height, color, curve)

        
    save_and_load_graph_button = customtkinter.CTkButton(custom_graph_frame, text="Load Graph", command=handle_load_graph)
    save_and_load_graph_button.pack(pady=(10,10), padx=10)
    
    return custom_graph_frame