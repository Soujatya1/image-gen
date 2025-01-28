import streamlit as st
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

        # OpenRouter API details
        api_key = "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"  # Replace with your OpenRouter API key
        api_url = "https://openrouter.ai/"  # Base endpoint for OpenRouter

        # Create the prompt
        text_prompt = (
            f"Generate a marketing poster in {style.lower()} style. "
            f"Description: {description}. Ensure the dimensions are {dimensions}. "
            f"Return the image URL."
        )

        # Set up request headers and body
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": "deepseek/deepseek-r1-distill-llama-70b",  # Replace with the correct model
            "messages": [
                {"role": "system", "content": "You are an AI that generates marketing posters."},
                {"role": "user", "content": text_prompt},
            ],
        }

        try:
            # Send POST request to OpenRouter API
            response = requests.post(api_url, json=payload, headers=headers)

            # Handle response
            if response.status_code == 200:
                result = response.json()
                st.write("OpenRouter Response:", result)

                # Extract image URL if available
                if "choices" in result and result["choices"]:
                    image_url = result["choices"][0]["message"]["content"]
                    st.image(image_url, caption="Generated Marketing Poster")
                    st.download_button("Download Poster", image_url)
                else:
                    st.error("No image URL found in the response.")
            else:
                st.error(f"API call failed with status code {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a description for the poster.")
