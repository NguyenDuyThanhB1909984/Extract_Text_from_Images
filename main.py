pip install opencv-python-headless
import streamlit as st
import cv2
import pytesseract
import numpy as np 

st.set_option('deprecation.showfileUploaderEncoding', False)

st.title("Trích xuất văn bản từ hình ảnh")

# Upload image file
uploaded_file = st.file_uploader("Chọn hình ảnh...", type=["jpg", "jpeg", "png"])

# Extract text from uploaded image
if uploaded_file is not None:
    # Display uploaded image
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
    st.image(image, caption='Hình ảnh đã tải lên', use_column_width=True)

    # Extract text from image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang='vie')

    # Display extracted text
    st.subheader('Văn bản trích xuất')
    st.write(text)
