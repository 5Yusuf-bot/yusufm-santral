from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

# Buraya 1'den 8'e kadar çalacak şarkıların MP3 linklerini koyduk.
# Bunlar test için internetteki örnek telifsiz şarkılardır.
# Daha sonra kendi istediğin şarkıların .mp3 linkleriyle burayı güncelleyebilirsin!
SARKI_LISTESI = {
    "1": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "2": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "3": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
    "4": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
    "5": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3",
    "6": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3",
    "7": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3",
    "8": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3"
}

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()
    
    # Kullanıcıdan tek basamaklı bir tuşlama bekliyoruz (0-8 arası)
    gather = response.gather(num_digits=1, action='/play-song')
    
    # Telefon açıldığında robotun okuyacağı Türkçe karşılama metni
    karasılama_metni = (
        "Yusuf Em Şarkı Merkezine hoş geldiniz! "
        "Birbirinden sıkı parçaları dinlemek için lütfen bir ile sekiz arasında bir rakamı tuşlayınız. "
        "Müşteri hizmetlerine bağlanmak için lütfen sıfırı tuşlayınız."
    )
    gather.say(karasılama_metni, language="tr-TR")
    
    # Eğer hiçbir şeye basılmazsa menüyü tekrar oynatır
    response.redirect('/voice')
    return str(response)

@app.route("/play-song", methods=['GET', 'POST'])
def play_song():
    response = VoiceResponse()
    digit_pressed = request.values.get('Digits', None)
    
    # 0'a basılırsa: Şaka amaçlı eğlenceli bir telesekreter mesajı
    if digit_pressed == '0':
        response.say("Şu anda tüm müşteri temsilcilerimiz diğer müzik severlerle ilgilenmektedir. Lütfen daha sonra tekrar deneyiniz.", language="tr-TR")
        response.redirect('/voice')
        
    # 1-8 arası bir tuşa basılırsa: Şarkıyı çal
    elif digit_pressed in SARKI_LISTESI:
        response.say(f"{digit_pressed} numaralı parça oynatılıyor, keyifli dinlemeler!", language="tr-TR")
        response.play(SARKI_LISTESI[digit_pressed])
        
    # Hatalı tuşlama yapılırsa:
    else:
        response.say("Hatalı bir tuşlama yaptınız. Lütfen tekrar deneyin.", language="tr-TR")
        response.redirect('/voice')
        
    return str(response)

if __name__ == "__main__":
    # Kodumuz bilgisayarında 5000 portunda çalışacak
    app.run(port=5000)