import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO
import json

# Function to send image to your API and get the processed image
def process_image(image):
    url = 'http://45.55.105.200/image_backgroung_remove'
    files = {'img_file': ('image.jpg', image, 'image/jpeg')}
    data = {'model_type': '1'}

    response = requests.post(url, files=files, data=data)

    if response.status_code == 200:
        # Assuming the response contains a base64-encoded image
        response_data = response.json()
        imgdata = base64.b64decode(response_data['file_base64'])
        return imgdata
    else:
        st.error(f"Error: {response.status_code}, {response.text}")
        return None

# Streamlit UI
st.title('Image Background Remover')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    with st.spinner('Processing image...'):
        processed_image = process_image(uploaded_file.getvalue())
        if processed_image:
            # Display processed image
            processed_image = Image.open(BytesIO(processed_image))
            st.image(processed_image, caption='Processed Image', use_column_width=True)
