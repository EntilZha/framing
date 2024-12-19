import streamlit as st
import pandas as pd
from framing import calculate_margins
from PIL import Image
from ipycanvas import Canvas

st.set_page_config(layout="wide")
st.title("Photo Framing Tool")
st.header("Photo Framing Tool")
st.markdown("""
This tool helps you determine what frame and margins best fit a photo. To use it, you need:

- Photo Width/Height: This can be in pixels or any other unit. It is used to calculate the aspect ratio.
- Min Margin: This is the minimum margin (in same unit as frame size below) to use.
- Frame Width/Height: These should be frame sizes you are considering. It can be any unit, but must match the unit of the min margin
- You can enter multiple frame sizes

This tool will take all this information, then:

1. For each frame, calculate the margins assuming the smallest margin should be "Min Margin"
2. For each frame, display the calculated margins and what size the photos should be printed to.
""")

st.subheader("Enter your photo dimensions to calculate aspect ratio")
photo_width = st.number_input("Photo Width", value=1.0, min_value=1.0)
photo_height = st.number_input("Photo Height", value=1.0, min_value=1.0)
aspect_ratio = max(photo_height, photo_width) / min(photo_height, photo_width)
min_margin = st.number_input("Minimum Margin")

st.subheader("Add additional frame sizes here:")
frame_width = st.number_input("Frame Width", min_value=1.0)
frame_height = st.number_input("Frame Height", min_value=1.0)


def add_frame_size(width, height):
    st.session_state["frame_sizes"].append((width, height))


should_add_frame_size = st.button(
    "Add Frame Size", on_click=add_frame_size, args=[frame_width, frame_height]
)

if "frame_sizes" not in st.session_state:
    st.session_state["frame_sizes"] = []
frame_df = pd.DataFrame(st.session_state["frame_sizes"], columns=["height", "width"])
frame_df["ratio"] = frame_df["height"] / frame_df["width"]
frame_df["inverse_ratio"] = frame_df["width"] / frame_df["height"]
st.subheader("Current Frame Sizes")
st.table(frame_df)


st.text(
    "Based on the image aspect ratio, desired margin, and frame sizes, here are the calculated framing specs"
)

if len(st.session_state["frame_sizes"]) == 0:
    st.write("There are zero frame sizes, please add some")
else:
    rows = []
    for width, height in st.session_state["frame_sizes"]:
        specs = calculate_margins(
            frame_width=width,
            frame_height=height,
            image_aspect_ratio=aspect_ratio,
            min_margin=min_margin,
        )
        rows.append(specs.model_dump())
    st.table(rows)
