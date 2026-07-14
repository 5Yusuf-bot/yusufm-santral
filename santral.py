from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()
    
    # Giriş robotu (Banka robotu sesiyle)
    response.say(
        "Bağlantı başarılı. Seçtiğiniz parça oynatılıyor, lütfen bekleyiniz.", 
        voice="polly.Filiz", 
        language="tr-TR"
    )
    
    # Senin gönderdiğin doğrudan MP3 linkini çalıyoruz!
    response.play("https://www.image2url.com/r2/default/audio/1784044764478-fd34e470-40be-4b28-b51f-06103222d12a.mp3")
    
    return str(response)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
