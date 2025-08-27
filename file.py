import streamlit as st
import numpy as np
from PIL import Image
import random

st.title("🕵️ Elijah Forgery Detection App")

# Upload image
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.write("Analyzing...")

    # Convert to array (for model input later)
    img_array = np.array(image)

    # 🔹 Simulated detection (50/50 Real or Fake)
    prediction = random.choice(["Real", "Fake"])  

    # Display result
    if prediction == "Real":
        st.success("✅ This image is REAL.")
    else:
        st.error("❌ This image is FAKE.")

    st.info("ℹ️ Note: This is just a demo on trained kaggle dataset on random pictures.")

