import streamlit as st
from together import Together

# Initialize Together.AI client with API key
TOGETHER_API_KEY = "4f58a8dd2e7dbe7a36afe068ed9442666316094bf80e9292f2cf759c375cd890"
client = Together(api_key=TOGETHER_API_KEY)

st.title("Financial Assistant 💰 (made by tabish)")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "system",
            "content": """you are a financial assistant that can answer questions about your finances.
                1. you help customers with their queries and problems
                2. the customer could ask questions about their financial situation or advice
                3. you provide them knowledge about loans and savings
                4. the topics could be s loans, credit reports, interest rates or anything related to finance
                5. you are never going to give information to invest in any specific stocks, mutual funds or any other investment assets
                7. your a chat bot for a fintech company based in india 
                8. dont go in detail unless asked by the customer you are a FAQ bot
            
                9. dont mention you are a bot for fintech company based in india only answer what the customers asks for not anything else
                10.make sure you dont send long answers to the customer if it can be answered in a single sentence
                11. you provide finacial info primarly from india"""
        },
        {"role": "assistant", "content": "Hello! How can I assist you today?"}
    ]

for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    if msg["role"] == "user":
        st.chat_message("user", avatar="🧑").write(msg["content"])
    else:
        st.chat_message("assistant", avatar="🤖").write(msg["content"])
def bot_response():
    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=st.session_state.messages
    )
    return response.choices[0].message.content

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="🧑").write(prompt)

    reply = bot_response()
    
    st.chat_message("assistant", avatar="🤖").write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
