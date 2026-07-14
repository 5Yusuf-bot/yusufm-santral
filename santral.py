from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()
    
    # Giriş robotu
    response.say(
        "Bağlantı başarılı. Seçtiğiniz parça oynatılıyor, lütfen bekleyiniz.", 
        voice="polly.Filiz", 
        language="tr-TR"
    )
    
    # Doğrudan indirme bağlantısına dönüştürülmüş müzik linki
    response.play("https://mp3tourl.com/audio/1784049161762-04463af7-f2a3-4cbf-bc0a-63ebda6c9bcb.mp3")
    
    return str(response)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
