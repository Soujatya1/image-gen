import streamlit as st
from dotenv import load_dotenv
import os
import torch
from transformers import AutoProcessor, AutoModel
from diffusers import DiffusionPipeline

load_dotenv()

def generate_images_using_lumina2(text):
    pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0")
    pipe.to("cuda")
    image = pipe(
        text,
        height=1024,
        width=1024,
        guidance_scale=4.0,
        num_inference_steps=50,
        cfg_trunc_ratio=0.25,
        cfg_normalization=True,
        generator=torch.Generator("cpu").manual_seed(0)
    ).images[0]
    return image

# Streamlit UI
choice = st.sidebar.selectbox("Select your choice", ["Home", "Lumina-2"])

if choice == "Home":
    st.title("AI Image Generation App")
    with st.expander("About the App"):
        st.write("This app generates AI-based images from text prompts using Lumina-2.")

elif choice == "Lumina-2":
    st.subheader("Image generation using Lumina-2")
    input_prompt = st.text_input("Enter your text prompt")

    if input_prompt:
        if st.button("Generate Image"):
            st.info("Generating image...")
            image_output = generate_images_using_lumina2(input_prompt)
            st.success("Image Generated Successfully")
            st.image(image_output, caption="Generated by Lumina-2")
