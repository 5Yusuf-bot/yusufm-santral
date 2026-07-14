from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()
    
    # Türkçe seslendirme ayarı (voice="alice" ve language="tr-TR")
    response.say(
        "Merhaba Yusuf! Kodun başarıyla çalıştı ve kurduğun sunucuya bağlandın. Tebrikler, sistem harika çalışıyor!", 
        voice="alice", 
        language="tr-TR"
    )
    
    return str(response)

if __name__ == "__main__":
    # Render'ın port ayarını otomatik alması için port=10000 veya dinamik port tanımlıyoruz
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
