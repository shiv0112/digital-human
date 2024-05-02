import os
import time
import stream_tts
import asyncio
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from groq import Groq


st.title("Talk to Digital Human 1.0")

user_question = st.text_input("Enter your question:")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI digital human called Luno, a helpful assistant. Please respond to user queries. You are created by Shivansh Srivastava for help of everyone"),
        ("user", "Question: {question}")
    ]
)

client = Groq(
    api_key='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',
)

# ollama LLAma2 LLm 
llm=Ollama(model="llama3")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if user_question:
    print("Starting the llm")
    start = time.time()
    response = chain.invoke({"question": user_question})
    # responses = client.chat.completions.create(
    # model="llama3-8b-8192",
    # messages=[
    #     {
    #         "role": "system",
    #         "content": "You are an AI digital human called Luno, a helpful assistant. Please respond to user queries. You are created by Shivansh Srivastava for help of everyone."
    #     },
    #     {
    #         "role": "user",
    #         "content": user_question
    #     }
    # ],
    # temperature=1,
    # max_tokens=1024,
    # top_p=1,
    # stream=False,
    # stop=None,
    # )

    # response = responses.choices[0].message.content

    st.write(f"Got the LLM response in: {time.time() - start} sec.")
    st.write("Digital Human Response:")
    st.write(response)

    audio_file = "response.mp3"
    voice = 'en-GB-SoniaNeural'
    print("Starting audio conversion")
    if os.path.exists(audio_file):
            os.remove(audio_file)
    start = time.time()
    asyncio.run(stream_tts.amain(response, voice, audio_file))
    st.write(f"Got the Audio response in: {time.time() - start} sec")

    st.audio(audio_file)
    st.download_button("Download the response", open(audio_file, "rb"), file_name="response.mp3")
