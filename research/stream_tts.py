import asyncio
import time
import edge_tts

TEXT = "Hello I’m a virtual entity designed to interact with humans in a conversational and engaging manner. I can understand natural language, generate responses, and even adapt to the context of our conversation. My visual representation is created using computer-generated imagery (CGI), so I can have a face and body to make our interactions feel more human-like."

VOICE = "en-GB-SoniaNeural"
OUTPUT_FILE = "test1.mp3"


async def amain(text, voice, output_file) -> None:
    """Main function"""
    communicate = edge_tts.Communicate(text, voice)
    with open(output_file, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                print(f"WordBoundary: {chunk}")


if __name__ == "__main__":
    start = time.time()
    asyncio.run(amain(TEXT, VOICE, OUTPUT_FILE))
    print("Conversion Time:", time.time()-start)