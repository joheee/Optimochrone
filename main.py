import customtkinter
import page.default_graph as pd
import page.custom_graph as pc
import page.learn_more as pl
import widget.sidebar as sid

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title('Optimochrone')
app.resizable(False, False)

# instance the default graph page
default_graph_frame = pd.default_graph(app) 
custom_graph_frame = pc.custom_graph(app)
learn_more_frame = pl.learn_more(app)

sid.SidebarWidget(app, default_graph_frame, custom_graph_frame, learn_more_frame)

default_graph_frame.pack()

app.mainloop()