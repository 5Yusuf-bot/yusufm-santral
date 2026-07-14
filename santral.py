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
    response.play("https://www.image2url.com/r2/default/audio/1784045664647-90e43cf3-72ea-4880-becd-b0c978bb2fdd.mp3")
    
    return str(response)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
