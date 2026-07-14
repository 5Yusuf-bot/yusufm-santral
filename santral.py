from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()
    
    # Amazon Polly'nin Türkçe "Filiz" (Banka Robotu) sesini tanımlıyoruz
    response.say(
        "Merhaba Yusuf. Yapay zeka sesli yanıt sistemine başarıyla bağlandınız. Lütfen yapmak istediğiniz işlemi seçiniz.", 
        voice="polly.Filiz", 
        language="tr-TR"
    )
    
    return str(response)

if __name__ == "__main__":
    import os
    # Render'ın port ayarını otomatik alması için dinamik port tanımlıyoruz
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
