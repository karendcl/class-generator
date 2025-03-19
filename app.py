import streamlit as st
import google.generativeai as genai
import json

from context import get_context_default


# from css import *

def get_api_key():
    with open("key.json") as f:
        data = json.load(f)
    return data["API_KEY"]

# Set up the Gemini API
genai.configure(api_key=get_api_key())

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Streamlit app
with st.sidebar:
    st.header("Context Information")
    role, skills, objectives, to_create = get_context_default()
    role = st.text_area(
        "About You (e.g., role, industry):",
        help="Provide some information about yourself.",
        value=role,
        height=200,
    )

    uploaded_file = st.file_uploader("Upload a Markdown file for context", type=["md"])
    md_content = ""
    if uploaded_file is not None:
        md_content += uploaded_file.read().decode("utf-8")
        st.write("### Uploaded Markdown Content")
        st.markdown(md_content)
    skills = st.text_area(
        "Skills/Experience:",
        help="Mention any skills or experience the students have.",
        value=skills,
    )

    objectives = st.text_area(
        "Class Objectives:",
        help="Describe the objectives of the class.",
        value=objectives,
    )

    to_create = st.text_area(
        "Instructions:",
        help="Provide detailed instructions on what to create.",
        value=to_create,
        height = 300
    )

# Main content area
st.header("Generate Content")

# User input for prompt
user_prompt = st.text_area("Enter your prompt here:", height=150, value="Taking into account the context provided "
                                                                              "above, design a structured class plan. "
                                                                        "Remember it is only one lesson and not the "
                                                                        "whole course.")

# Button to generate response
if st.button("Generate Response"):
    if user_prompt:
        with st.spinner("Generating response..."):
            try:
                if md_content:
                    skills += f"These are the previous classes that have been taught:\n\n{md_content}\n\n"
                # Combine context and prompt
                full_prompt = (
                    f"{role}\n\n{skills}\n\n{objectives}\n\n{to_create}\n\n{user_prompt}"
                )

                # Generate response using the Gemini API
                response = model.generate_content(full_prompt)
                st.success("Response generated successfully!")

                # Display the response
                st.subheader("Generated Content:")
                st.write(response.text)

                markdown_content = f"{response.text}"

                st.download_button(
                    label="Download as Markdown",
                    data=markdown_content,
                    file_name=f"class.md",
                    mime="text/markdown",
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt to generate a response.")
