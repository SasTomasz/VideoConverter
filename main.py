import streamlit as st
from PIL import Image


def convert_to_gray(image):
    with Image.open(image) as im:
        gray_image = im.convert("L")
    return gray_image


def main():
    uploaded_file = st.file_uploader("Upload image")

    with st.expander("Video"):
        picture = st.camera_input("Camera")

    if uploaded_file:
        gray_image = convert_to_gray(uploaded_file)
        st.image(gray_image)
    elif picture:
        gray_image = convert_to_gray(picture)
        st.image(gray_image)


if __name__ == "__main__":
    main()
