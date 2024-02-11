import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import plotly.graph_objs as go
import plotly.io as pio
import io
import random

class PlotlyXYPlot:
    def __init__(self, root, x_values, y_values):
        self.root = root
        self.x_values = x_values
        self.y_values = y_values
        self.fig = go.Figure(data=go.Scatter(x=self.x_values, y=self.y_values, mode='markers', name='XY Plot'))
        self.fig.update_layout(margin=dict(l=50, r=50, t=20, b=20))
        self.image_bytes = pio.to_image(self.fig, format='png')
        self.pil_image = Image.open(io.BytesIO(self.image_bytes))
        self.tk_image = ImageTk.PhotoImage(self.pil_image)
        self.label = tk.Label(self.root, image=self.tk_image)
        self.label.pack()
        self.theme_combobox = ttk.Combobox(self.root, values=['plotly_dark', 'plotly_white', 'plotly'], state="readonly")
        self.theme_combobox.current(0)  # Set the default selected theme
        self.theme_combobox.bind("<<ComboboxSelected>>", self.change_theme)
        self.theme_combobox.pack()

    def change_theme(self, event):
        selected_theme = self.theme_combobox.get()
        self.fig.update_layout(template=selected_theme)
        updated_image_bytes = pio.to_image(self.fig, format='png')
        updated_pil_image = Image.open(io.BytesIO(updated_image_bytes))
        updated_tk_image = ImageTk.PhotoImage(updated_pil_image)
        self.label.configure(image=updated_tk_image)
        self.label.image = updated_tk_image

    def start(self):
        self.root.mainloop()