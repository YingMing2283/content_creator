import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = st.secrets["API_KEY"]

# Streamlit app layout
def main():
    # Title and description
    st.title("🎨 AI Creative Content Bot")
    st.markdown("""
    Welcome to the **AI Creative Content Bot**! This tool helps you generate creative marketing content for various fields. 
    Simply select your preferences below, and let the AI do the rest!
    """)

    # Sidebar for navigation or additional info
    st.sidebar.header("About")
    st.sidebar.markdown("""
    This app uses OpenAI's GPT-3.5 Turbo to generate creative marketing content tailored to your needs. 
    Choose the field, tone, length, and whether to include emojis, and get your content in seconds!
    """)

    # User inputs
    st.header("🛠️ Customize Your Content")

    # Field selection
    field = st.selectbox(
        "Select Field",
        ["Education", "Healthcare", "Medical", "Food & Beverage", "Technology", "Fashion", "Travel", "Finance", "Real Estate"]
    )

    # Tone selection
    tone = st.selectbox(
        "Select Tone",
        ["Formal", "Joyful", "Professional", "Casual", "Inspirational", "Humorous", "Persuasive"]
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
        with st.spinner("Generating your content... ✨"):
            # Construct the prompt for OpenAI
            prompt = (
                f"Write a creative marketing content for the {field} field. "
                f"The tone should be {tone}. "
                f"The content should be approximately {length} words long. "
                f"{'Include relevant emojis to make the content engaging.' if include_emoji else ''}"
            )

            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=length * 2,  # Adjust max_tokens based on word count
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

# Run the app
if __name__ == "__main__":
    main()
