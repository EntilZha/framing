import streamlit as st
import pandas as pd
from framing import calculate_margins
from PIL import Image
from ipycanvas import Canvas

st.title("Photo Framing Tool")
st.header("Photo Framing Tool")


st.subheader("Enter your photo dimensions to calculate aspect ratio")
photo_width = st.number_input("Photo Width", value=1, min_value=1)
photo_height = st.number_input("Photo Height", value=1, min_value=1)
aspect_ratio = max(photo_height, photo_width) / min(photo_height, photo_width)
min_margin = st.number_input("Minimum Margin")

if "frame_sizes" not in st.session_state:
    st.session_state["frame_sizes"] = [
        [19, 13],
        [14, 11],
        [5, 4],
    ]
frame_df = pd.DataFrame(st.session_state["frame_sizes"], columns=["height", "width"])
frame_df["ratio"] = frame_df["height"] / frame_df["width"]
frame_df["inverse_ratio"] = frame_df["width"] / frame_df["height"]
st.subheader("Current Frame Sizes")
st.table(frame_df)

st.subheader("Add additional frame sizes here:")
frame_width = st.number_input("Frame Width", min_value=1)
frame_height = st.number_input("Frame Height", min_value=1)


def add_frame_size(width, height):
    st.session_state["frame_sizes"].append((width, height))


should_add_frame_size = st.button(
    "Add Frame Size", on_click=add_frame_size, args=[frame_width, frame_height]
)


st.text(
    "Based on the image aspect ratio, desired margin, and frame sizes, here are the calculated framing specs"
)


for width, height in st.session_state["frame_sizes"]:
    specs = calculate_margins(
        frame_width=width,
        frame_height=height,
        image_aspect_ratio=aspect_ratio,
        min_margin=min_margin,
    )
    st.write(specs)
