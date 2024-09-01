import streamlit as st
from PIL import Image
import google.generativeai as genai
import os

# Configure Google Gemini with API key
API_KEY = 'AIzaSyBhDvhO1z_j-977fOuRJixhqLqnG4yyCsc'
genai.configure(api_key=API_KEY)

# Set up the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Setting page configuration
st.set_page_config(page_title="Image Analysis Med", page_icon=":robot:")

# Set logo
st.image("doctor_img.png", width=200)

# Set title and subtitle
st.title("This is an AI Doctor of Nepal🧑‍⚕️")
st.subheader("This web app assists village people with medical diagnosis")

# Provide user with the text area for symptoms input
symptoms = st.text_area("Enter your symptoms:", placeholder="Describe your symptoms here...")

if st.button("Analyze Symptoms"):
    if symptoms:
        try:
            # Call Google Gemini for analysis
            prompt = f"Summarize the possible medical conditions based on the following symptoms: {symptoms}"
            response = model.generate_content(prompt)
            result = response.text.strip()
            
            # Limit response to one paragraph and add warning
            result = f"Based on your symptoms, the AI suggests the following conditions: {result}."
            result += "\n\n**Warning:** This information is not a substitute for professional medical advice. Please consult a healthcare professional for accurate diagnosis and treatment."
            st.write(result)
            
            # Provide a clickable link to find a doctor
            st.write("For further inquiries, you can find a doctor [here](https://www.google.com/maps/search/doctors+near+me).")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please enter your symptoms for analysis.")

# Developer Section
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; font-size: 18px;">
        <h4 style="color: #6c63ff;">Meet the Developer: Peshal Parajuli</h4>
        <p style="font-style: italic;">"Technology should serve humanity, and every project is an opportunity to make lives better."</p>
        <p>Follow the journey, reach out for collaborations, or simply say hello at: <a href="mailto:peshalparajuli2006@gmail.com" style="color: #FF6F61;">peshalparajuli2006@gmail.com</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
