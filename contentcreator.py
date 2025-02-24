import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = st.secrets["API_KEY"]

# Streamlit app layout
def main():
    # Title and description
    st.title("🎨 Creatify - Smart AI Content Generator")
    st.markdown("""
    Welcome to the **Creatify**! Your Smart AI Content Generator. This tool helps you generate creative marketing content for various fields. 
    Simply select your preferences below, provide details about your product or content, and let the AI do the rest!
    """)
    
    # Sidebar for navigation or additional info
    st.sidebar.header("About")
    st.sidebar.markdown("""
    💡 This app effortlessly generates creative, tailored marketing content in seconds. 
    Simply choose your field, tone, length, language, and even emoji preferences—watch your perfect content come to life! 🚀
    """)

    # User inputs
    st.header("🛠️ Customize Your Content")

    # Field selection
    field = st.selectbox(
        "Select Field",
        ["Education", "Healthcare", "Medical", "Food & Beverage", "Technology", "Fashion", "Travel", "Finance", "Real Estate"]
    )

    # Product/Content details input
    product_details = st.text_area(
        "Provide Product/Content Details",
        placeholder="Describe your product or content. For example: 'A new online course for learning Python programming.'",
        height=100
    )

    # Tone selection
    tone = st.selectbox(
        "Select Tone",
        ["Formal", "Joyful", "Professional", "Casual", "Inspirational", "Humorous", "Persuasive"]
    )

    # Language selection
    language = st.selectbox(
        "Select Language",
        ["English", "Chinese", "Malay"]
    )

    # Content length selection
    length = st.slider(
        "Select Content Length (in words)",
        min_value=50,
        max_value=500,
        value=150,
        step=50
    )

    # Emoji toggle
    include_emoji = st.checkbox("Include Emojis? 😊")

    # Generate content button
    if st.button("Generate Content"):
        # Validate inputs
        if not product_details.strip():
            st.error("Please provide product or content details.")
        else:
            with st.spinner("Generating your content... ✨"):
                try:
                    # Construct the prompt for OpenAI
                    prompt = (
                        f"Write a creative marketing content for the {field} field. "
                        f"The product or content is: {product_details}. "
                        f"The tone should be {tone}. "
                        f"The content should be approximately {length} words long. "
                        f"The language should be {language}. "
                        f"{'Include relevant emojis to make the content engaging.' if include_emoji else ''}"
                    )

                    # Call OpenAI API
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=length * 3,  # Adjust max_tokens for non-English languages
                        temperature=0.7  # Controls creativity (0.7 is a good balance)
                    )

                    # Display generated content
                    generated_content = response.choices[0].message.content.strip()
                    st.success("✅ Your content is ready!")
                    st.write(generated_content)

                    # Download button for the generated content
                    st.download_button(
                        label="Download Content as Text",
                        data=generated_content,
                        file_name="generated_content.txt",
                        mime="text/plain"
                    )

                except Exception as e:
                    st.error(f"An error occurred while generating content: {e}")

# Run the app
if __name__ == "__main__":
    main()
