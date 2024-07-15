from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from src.pipeline.prediction_pipeline import PredictionPipeline
import streamlit as st
import os
from pathlib import Path
import numpy as np


# this is for saving images and prediction
def save_image(uploaded_file):
    if uploaded_file is not None:
        save_path = os.path.join("images", "input.jpeg")
        os.makedirs('images', exist_ok=True)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())
        # st.success(f"Image saved to {save_path}")
        st.image(uploaded_file,)
        
        pred_pipeline = PredictionPipeline()
        model_path = pred_pipeline.run_pipeline()

        model = load_model(model_path)

        # test_image = image.load_img(Path("artifacts\img.jpeg"), target_size = (224,224))
        test_image = image.load_img(uploaded_file, target_size=(224, 224))

        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        # prediction = np.argmax(model.predict(test_image), axis=1)
        prediction = model.predict(test_image)

        print(prediction)

        if (prediction < 0.3):
            print('Normal')
            st.text_area(label="Prediction:", value="Normal", height=50)
        if (prediction >= 0.3):
            print('PNEUMONIA')
            st.text_area(label="Prediction:", value="PNEUMONIA", height=50)


if __name__ == "__main__":
    st.title("Medical Image Analysis")
    uploaded_file = st.file_uploader(
        "Upload an image", type=["jpg", "png", "jpeg"])
    save_image(uploaded_file)
