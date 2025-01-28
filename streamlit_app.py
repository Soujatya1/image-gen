import streamlit as st
from openrouter import ChatCompletion
import requests

# Streamlit App
st.title("AI-Powered Marketing Poster Generator")
st.write("Generate stunning marketing posters using OpenRouter's LLM.")

# User Inputs
description = st.text_area("Enter a description for your poster:")
style = st.selectbox("Choose a style:", ["Minimalistic", "Modern", "Vintage", "Creative"])
dimensions = st.text_input("Enter dimensions (e.g., 1024x1024):", "1024x1024")

# Generate Poster
if st.button("Generate Poster"):
    if description:
        st.write("Generating the poster using OpenRouter LLM...")

        # Initialize OpenRouter ChatCompletion
        api_key = "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"
        client = ChatCompletion(api_key=api_key)

        try:
            # Create the prompt for the OpenRouter model
            text_prompt = (
                f"Generate a marketing poster in {style.lower()} style. "
                f"Description: {description}. Ensure the dimensions are {dimensions}. "
                f"Return an image URL."
            )

            # Send the request to OpenRouter
            response = client.create(
                model="deepseek/deepseek-r1-distill-llama-70b",
                messages=[
                    {"role": "system", "content": "You are an AI that generates images for marketing posters."},
                    {"role": "user", "content": text_prompt},
                ]
            )

            # Debug the response
            st.write("OpenRouter Response:", response)

            # Check for image URL in the response
            if "choices" in response and response["choices"]:
                image_url = response["choices"][0]["message"]["content"]
                st.image(image_url, caption="Generated Marketing Poster")
                st.download_button("Download Poster", image_url)
            else:
                st.error("Failed to retrieve an image URL from the OpenRouter response.")
        except Exception as e:
            st.error(f"Error during generation: {e}")
    else:
        st.warning("Please enter a description for the poster.")
