import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import plotly.graph_objs as go
import plotly.io as pio
import io
import random



# Create a Tkinter window
root = tk.Tk()
root.title("Tkinter with Plotly XY Plot Image")

# Generate random data for the XY plot
x_values = [random.uniform(1, 10) for _ in range(50)]
y_values = [random.uniform(1, 10) for _ in range(50)]

# Create a Plotly XY plot with random data
fig = go.Figure(data=go.Scatter(x=x_values, y=y_values, mode='markers', name='XY Plot'))

# Update the layout of the graph to hide the title
fig.update_layout(margin=dict(l=50, r=50, t=20, b=20))

# Export the Plotly graph as a PNG image
image_bytes = pio.to_image(fig, format='png')

# Convert the image bytes to a PIL Image
pil_image = Image.open(io.BytesIO(image_bytes))

# Convert the PIL Image to a Tkinter PhotoImage
tk_image = ImageTk.PhotoImage(pil_image)

# Create a Tkinter label to display the image
label = tk.Label(root, image=tk_image)
label.pack()

# Function to change the theme of the plot
def change_theme(event):
    selected_theme = theme_combobox.get()
    fig.update_layout(template=selected_theme)
    # Export the updated Plotly graph as a PNG image
    updated_image_bytes = pio.to_image(fig, format='png')
    updated_pil_image = Image.open(io.BytesIO(updated_image_bytes))
    updated_tk_image = ImageTk.PhotoImage(updated_pil_image)
    label.configure(image=updated_tk_image)
    label.image = updated_tk_image

# Create a combobox to select the theme
themes = ['plotly_dark', 'plotly_white', 'plotly']
theme_combobox = ttk.Combobox(root, values=themes, state="readonly")
theme_combobox.current(0)  # Set the default selected theme
theme_combobox.bind("<<ComboboxSelected>>", change_theme)
theme_combobox.pack()

# Start the Tkinter event loop
root.mainloop()