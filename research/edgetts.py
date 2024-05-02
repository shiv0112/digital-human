import asyncio
import time
import edge_tts

language_dict = {
 'English-Jenny (Female)': 'en-US-JennyNeural',
 'English-Guy (Male)': 'en-US-GuyNeural',
 'English-Ana (Female)': 'en-US-AnaNeural',
 'English-Aria (Female)': 'en-US-AriaNeural',
 'English-Christopher (Male)': 'en-US-ChristopherNeural',
 'English-Eric (Male)': 'en-US-EricNeural',
 'English-Michelle (Female)': 'en-US-MichelleNeural',
 'English-Roger (Male)': 'en-US-RogerNeural',
 'English (Australia)-Natasha- (Female)': 'en-AU-NatashaNeural',
 'English (Australia)-William- (Male)': 'en-AU-WilliamNeural',
 'English (Canada)-Clara- (Female)': 'en-CA-ClaraNeural',
 'English (Canada)-Liam- (Male)': 'en-CA-LiamNeural',
 'English (UK)-Libby- (Female)': 'en-GB-LibbyNeural',
 'English (UK)-Maisie- (Female)': 'en-GB-MaisieNeural',
 'English (UK)-Ryan- (Male)': 'en-GB-RyanNeural',
 'English (UK)-Sonia- (Female)': 'en-GB-SoniaNeural',
 'English (UK)-Thomas- (Male)': 'en-GB-ThomasNeural',
 'English (Hong Kong)-Sam- (Male)': 'en-HK-SamNeural',
 'English (Hong Kong)-Yan- (Female)': 'en-HK-YanNeural',
 'English (Ireland)-Connor- (Male)': 'en-IE-ConnorNeural',
 'English (Ireland)-Emily- (Female)': 'en-IE-EmilyNeural',
 'English (India)-Neerja- (Female)': 'en-IN-NeerjaNeural',
 'English (India)-Prabhat- (Male)': 'en-IN-PrabhatNeural',
 'English (Kenya)-Asilia- (Female)': 'en-KE-AsiliaNeural',
 'English (Kenya)-Chilemba- (Male)': 'en-KE-ChilembaNeural',
 'English (Nigeria)-Abeo- (Male)': 'en-NG-AbeoNeural',
 'English (Nigeria)-Ezinne- (Female)': 'en-NG-EzinneNeural',
 'English (New Zealand)-Mitchell- (Male)': 'en-NZ-MitchellNeural',
 'English (Philippines)-James- (Male)': 'en-PH-JamesNeural',
 'English (Philippines)-Rosa- (Female)': 'en-PH-RosaNeural',
 'English (Singapore)-Luna- (Female)': 'en-SG-LunaNeural',
 'English (Singapore)-Wayne- (Male)': 'en-SG-WayneNeural',
 'English (Tanzania)-Elimu- (Male)': 'en-TZ-ElimuNeural',
 'English (Tanzania)-Imani- (Female)': 'en-TZ-ImaniNeural',
 'English (South Africa)-Leah- (Female)': 'en-ZA-LeahNeural',
 'English (South Africa)-Luke- (Male)': 'en-ZA-LukeNeural'
}

TEXT = "Hm Hello I’m a virtual entity designed to interact with humans in a conversational and engaging manner. I can understand natural language, generate responses, and even adapt to the context of our conversation. My visual representation is created using computer-generated imagery (CGI), so I can have a face and body to make our interactions feel more human-like."

VOICE = language_dict.get("English (India)-Neerja- (Female)': 'en-IN-NeerjaNeural","en-GB-SoniaNeural")
OUTPUT_FILE = "test.mp3"


async def amain() -> None:
    """Main function"""
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(amain())
    print("Conversion Time:", time.time()-start)