import numpy as np
from PIL import Image
import streamlit as st


def calculate_use_percent(uploaded_file):
    img = Image.open(uploaded_file).convert("L")
    img_data = np.array(img)

    white_pixels = np.sum(img_data == 255)
    total_pixels = img_data.size
    filled_pixels = total_pixels - white_pixels
    percentage = (filled_pixels / total_pixels) * 100

    st.write("Percent of the image that is not blank:", percentage)
    st.write("Number of White Pixels:", white_pixels)
    st.write("Number of filled pixels:", filled_pixels)


def main():
    st.title("Image Percentage Calculator")
    uploaded_file = st.file_uploader("Upload a File...", type="jpg")
    if uploaded_file is not None:
        calculate_use_percent(uploaded_file)
        st.divider()
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        st.divider()


if __name__ == "__main__":
    main()
