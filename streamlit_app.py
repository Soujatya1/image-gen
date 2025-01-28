import streamlit as st
from langchain_groq import ChatGroq

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
        groqcloud_llm = ChatGroq(
            api_key="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", 
            model_name="Llama3-70b-8192"
        )

        # Create a combined text prompt
        prompt = (
            f"Create a {style.lower()} marketing poster based on the following description: "
            f"'{description}'. Ensure the dimensions are {dimensions}."
        )

        # Pass the prompt directly to GroqCloud
        try:
            response = groqcloud_llm.generate_image(prompt)
            # Check if the response includes an image URL
            if isinstance(response, dict) and "image_url" in response:
                st.image(response["image_url"], caption="Generated Marketing Poster")
                st.download_button("Download Poster", response["image_url"])
            else:
                st.error("Failed to generate the image. Please check the response format.")
        except Exception as e:
            st.error(f"Error during generation: {e}")
    else:
        st.warning("Please enter a description for the poster.")
