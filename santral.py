from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

# Telefon ilk açıldığında çalışacak karşılama menüsü
@app.route("/voice", methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()
    
    # Kullanıcıdan tek haneli tuşlama bekliyoruz
    gather = Gather(num_digits=1, action='/menu', method='POST')
    
    # Kesin Türkçe olması için 'Polly.Burcu-Neural' veya 'Polly.Filiz' kullanıyoruz
    gather.say(
        "Yusuf'un sesli yanıt sistemine hoş geldiniz. "
        "Hermes iki sıfır şarkısını dinlemek için lütfen bir tuşuna, "
        "Hızlı Sokaklar iki sıfır şarkısını dinlemek için lütfen iki tuşuna basınız.",
        voice="Polly.Filiz",
        language="tr-TR"
    )
    
    response.append(gather)
    
    # Tuşlama yapılmazsa menüyü tekrarlatıyoruz
    response.redirect('/voice')
    return str(response)

# Kullanıcı tuşa bastıktan sonra çalışacak kısım
@app.route("/menu", methods=['GET', 'POST'])
def menu():
    response = VoiceResponse()
    
    # Basılan tuşu alıyoruz
    selected_option = request.values.get('Digits', None)
    
    if selected_option == '1':
        response.say("Hermes iki sıfır oynatılıyor.", voice="Polly.Filiz", language="tr-TR")
        response.play("https://www.image2url.com/r2/default/audio/1784044764478-fd34e470-40be-4b28-b51f-06103222d12a.mp3")
        
    elif selected_option == '2':
        response.say("Hızlı Sokaklar iki sıfır oynatılıyor.", voice="Polly.Filiz", language="tr-TR")
        # Buraya kendi bulduğun Hızlı Sokaklar linkini veya test amaçlı bir hızlı ritimli müzik linkini koyabilirsin
        response.play("https://www.image2url.com/r2/default/audio/1784045664647-90e43cf3-72ea-4880-becd-b0c978bb2fdd.mp3")
        
    else:
        response.say("Geçersiz bir tuşlama yaptınız. Lütfen tekrar deneyiniz.", voice="Polly.Filiz", language="tr-TR")
        response.redirect('/voice')
        
    return str(response)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
