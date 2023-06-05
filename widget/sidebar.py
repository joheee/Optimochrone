import customtkinter

def SidebarWidget(app, default_graph_frame, custom_graph_frame, learn_more_frame):
    # Create the sidebar frame
    sidebar_frame = customtkinter.CTkFrame(master=app, width=150,corner_radius=0)
    sidebar_frame.pack(side='left', fill='y')

    def handle_default_graph():
        default_graph_frame.pack()
        custom_graph_frame.pack_forget()
        learn_more_frame.pack_forget()

    def handle_custom_graph():
        default_graph_frame.pack_forget()
        custom_graph_frame.pack()
        learn_more_frame.pack_forget()

    def handle_learn_more():
        default_graph_frame.pack_forget()
        custom_graph_frame.pack_forget()
        learn_more_frame.pack()
    
    label = customtkinter.CTkLabel(sidebar_frame, text="Optimochrone")
    label.pack(pady=(10,0))
    
    # Create sidebar options
    default_graph_button = customtkinter.CTkButton(sidebar_frame, text="Default Graphs", command=handle_default_graph)
    default_graph_button.pack(pady=(10,0), padx=10)

    custom_graph_button = customtkinter.CTkButton(sidebar_frame,text='Custom Graphs', command=handle_custom_graph)
    custom_graph_button.pack(pady=(10,0), padx=10)

    learn_more_button = customtkinter.CTkButton(sidebar_frame,text='Learn More',command=handle_learn_more)
    learn_more_button.pack(pady=10, padx=10)