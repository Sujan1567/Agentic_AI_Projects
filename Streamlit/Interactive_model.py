import streamlit as st
from openai import OpenAI

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Nepal Travel Assistant",
    page_icon="🇳🇵",
    layout="centered"
)

# -----------------------------
# OpenAI Client for Ollama
# -----------------------------
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

# -----------------------------
# Model
# -----------------------------
MODEL = "travel-nepal:latest"

# -----------------------------
# System Prompt
# -----------------------------
SYSTEM_PROMPT = """
You are a terse travel assistant for Nepal.

You can answer questions related to:
- Nepal travel
- Tourism
- Destinations
- Trekking
- Hotels
- Transportation
- Itineraries
- Attractions
- Travel costs
- Permits and visas
- Food recommendations for travelers

Keep your answers clear, useful, and concise.
"""

# -----------------------------
# Page Title
# -----------------------------
st.title("Nepal Travel Assistant")
st.caption("Powered by Ollama - service provider to traveller in nepal.")

# -----------------------------
# Initialize Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display Previous Messages
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# User Input
# -----------------------------
user_input = st.chat_input(
    "Ask me anything about travelling in Nepal..."
)

if user_input:

    # Add user message to chat history
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Prepare messages for Ollama
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    # Add conversation history
    messages.extend(st.session_state.messages)

    # Generate assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = client.chat.completions.create(
                    model=MODEL,
                    messages=messages,
                    temperature=0
                )

                answer = response.choices[0].message.content

                st.markdown(answer)

                # Save assistant response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as e:

                st.error(
                    f"Unable to connect to Ollama.\n\n"
                    f"Error: {e}"
                )