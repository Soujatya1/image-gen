import streamlit as st
from langchain_groq import GroqCloud

# Streamlit App
st.title("AI-Powered Marketing Poster Generator")
st.write("Generate stunning marketing posters using GroqCloud's LLM.")

# User Inputs
description = st.text_area("Enter a description for your poster:")
style = st.selectbox("Choose a style:", ["Minimalistic", "Modern", "Vintage", "Creative"])
dimensions = st.text_input("Enter dimensions (e.g., 1024x1024):", "1024x1024")

# Generate Poster
if st.button("Generate Poster"):
    if description:
        st.write("Generating the poster using GroqCloud LLM...")

        # Initialize GroqCloud LLM
        groqcloud_llm = GroqCloud(api_key="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")

        # Pass input directly to GroqCloud for image generation
        response = groqcloud_llm.generate({
            "description": description,
            "style": style,
            "dimensions": dimensions,
            "task": "image_generation",  # Custom task identifier if supported
        })

        # Process and Display the Image
        if "image_url" in response:
            st.image(response["image_url"], caption="Generated Marketing Poster")
            st.download_button("Download Poster", response["image_url"])
        else:
            st.error("Failed to generate the image. Please try again later.")
    else:
        st.warning("Please enter a description for the poster.")
