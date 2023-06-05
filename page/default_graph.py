import customtkinter
import graph.calculate_default_graph as cd
import graph.export_default_graph as ed
from tkinter import messagebox
from datetime import datetime

def default_graph(app):

    default_graph_frame = customtkinter.CTkFrame(master=app, width=300, height=300,corner_radius=0)
    
    label = customtkinter.CTkLabel(default_graph_frame, text="Default Graphs")
    label.pack(pady=(10,0))
    
    mass_a_input = customtkinter.CTkTextbox(default_graph_frame, height=10)
    mass_a_input.insert("0.0", "Mass A")
    mass_a_input.pack(pady=(10,0), padx=(0,10))
    
    mass_b_input = customtkinter.CTkTextbox(default_graph_frame, height=10)
    mass_b_input.insert("0.0", "Mass B")
    mass_b_input.pack(pady=(10,0), padx=(0,10))
    
    mass_c_input = customtkinter.CTkTextbox(default_graph_frame, height=10)
    mass_c_input.insert("0.0", "Mass C")
    mass_c_input.pack(pady=(10,0), padx=(0,10))
    
    mass_d_input = customtkinter.CTkTextbox(default_graph_frame, height=10)
    mass_d_input.insert("0.0", "Mass D")
    mass_d_input.pack(pady=(10,0), padx=(0,10))
    
    gravity_input = customtkinter.CTkTextbox(default_graph_frame, height=10)
    gravity_input.insert("0.0", "Gravity")
    gravity_input.pack(pady=(10,0), padx=(0,10))
    
    height_input = customtkinter.CTkTextbox(default_graph_frame, height=10)
    height_input.insert("0.0", "Height")
    height_input.pack(pady=(10,0), padx=(0,10))
    
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
        if validate_input(mass_a_input.get('1.0', 'end-1c'), 'mass a must be a valid number!') is None:
            return
        if validate_input(mass_b_input.get('1.0', 'end-1c'), 'mass b must be a valid number!') is None:
            return
        if validate_input(mass_c_input.get('1.0', 'end-1c'), 'mass c must be a valid number!') is None:
            return
        if validate_input(mass_d_input.get('1.0', 'end-1c'), 'mass d must be a valid number!') is None:
            return
        if validate_input(gravity_input.get('1.0', 'end-1c'), 'gravity must be a valid number!') is None:
            return
        if validate_input(height_input.get('1.0', 'end-1c'), 'height must be a valid number!') is None:
            return

        mass_a = int(float(mass_a_input.get('1.0', 'end-1c')))
        mass_b = int(float(mass_b_input.get('1.0', 'end-1c')))
        mass_c = int(float(mass_c_input.get('1.0', 'end-1c')))
        mass_d = int(float(mass_d_input.get('1.0', 'end-1c')))
        g = float(gravity_input.get('1.0', 'end-1c'))
        height = float(height_input.get('1.0', 'end-1c'))
        
        cd.calculate_default_graph(mass_a,mass_b,mass_c,mass_d,g,height)
    
    save_and_load_graph_button = customtkinter.CTkButton(default_graph_frame, text="Load Graph", command=handle_load_graph)
    save_and_load_graph_button.pack(pady=(10,0), padx=10)
    
    def handle_export_result():
        if validate_input(mass_a_input.get('1.0', 'end-1c'), 'mass a must be a valid number!') is None:
            return
        if validate_input(mass_b_input.get('1.0', 'end-1c'), 'mass b must be a valid number!') is None:
            return
        if validate_input(mass_c_input.get('1.0', 'end-1c'), 'mass c must be a valid number!') is None:
            return
        if validate_input(mass_d_input.get('1.0', 'end-1c'), 'mass d must be a valid number!') is None:
            return
        if validate_input(gravity_input.get('1.0', 'end-1c'), 'gravity must be a valid number!') is None:
            return
        if validate_input(height_input.get('1.0', 'end-1c'), 'height must be a valid number!') is None:
            return

        mass_a = int(float(mass_a_input.get('1.0', 'end-1c')))
        mass_b = int(float(mass_b_input.get('1.0', 'end-1c')))
        mass_c = int(float(mass_c_input.get('1.0', 'end-1c')))
        mass_d = int(float(mass_d_input.get('1.0', 'end-1c')))
        g = float(gravity_input.get('1.0', 'end-1c'))
        height = float(height_input.get('1.0', 'end-1c'))
        
        current_datetime = datetime.now()
        current_datetime_str = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        ed.export_default_graph(mass_a,mass_b,mass_c,mass_d,g,height,current_datetime_str)
        
        messagebox.showinfo("Success", f'success export image as {current_datetime}.png')
    
    export_result_button = customtkinter.CTkButton(default_graph_frame, text="Export Result", command=handle_export_result)
    export_result_button.pack(pady=10, padx=10)
    
    return default_graph_frame