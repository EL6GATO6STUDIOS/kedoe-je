import streamlit as st

st.set_page_config(page_title="Cat Programmer Ai", layout="centered")
st.title("🤖 Cat Programmer Ai (Tam Entegre Sürüm)")

def is_daily_expression(message):
    selamlar = ["merhaba", "selam", "günaydın", "iyi akşamlar", "nasılsın", "bay bay", "hoşça kal", "teşekkür", "sağ ol"]
    return any(phrase in message.lower() for phrase in selamlar)

def is_question(message):
    return "?" in message or any(x in message.lower() for x in ["nedir", "nasıl", "neden", "niye", "hangi", "kim", "ne", "mı", "mu"])

def is_analytic_expression(message):
    analiz_kelimeler = ["iyi mi", "kötü mü", "mantıklı mı", "doğru mu", "yanlış mı", "sence", "ne düşünüyorsun", "değer mi", "gerekli mi"]
    return any(phrase in message.lower() for phrase in analiz_kelimeler)

def is_code_question(message):
    kodlama_kelime = [
        "kodla", "yaz", "örnek ver", "nasıl yapılır", "nasıl yazılır",
        "python", "html", "javascript", "java", "css", "kod örneği",
        "script", "function", "kod", "yazılım", "değişken", "fonksiyon", "loop", "döngü",
        "kodla bunu", "programla", "algoritma"
    ]
    return any(word in message.lower() for word in kodlama_kelime)

def is_modeling_question(message):
    keywords = ["model", "şekil", "grafik", "çiz", "renkli", "3d", "svg", "figür", "şekil çiz", "çizim", "tasarla", "çizgi", "objekt"]
    return any(word in message.lower() for word in keywords)

def is_game_question(message):
    game_keywords = [
        "oyun", "game", "level", "karakter", "boss", "puan", "kazanma", "kazandım",
        "nasıl geçilir", "gizemli orman", "görev", "gta", "minecraft", "valorant",
        "fortnite", "cod", "pubg", "legend", "hile", "kasıt", "online oyun"
    ]
    return any(word in message.lower() for word in game_keywords)

def generate_code_response(message):
    msg = message.lower()
    if "python ile hesap makinesi" in msg or "python hesap makinesi" in msg:
        return """
```python
def hesapla():
    print("Basit Hesap Makinesi")
    sayi1 = float(input("1. sayıyı gir: "))
    islem = input("İşlem seç (+, -, *, /): ")
    sayi2 = float(input("2. sayıyı gir: "))

    if islem == '+':
        print("Sonuç:", sayi1 + sayi2)
    elif islem == '-':
        print("Sonuç:", sayi1 - sayi2)
    elif islem == '*':
        print("Sonuç:", sayi1 * sayi2)
    elif islem == '/':
        print("Sonuç:", sayi1 / sayi2)
    else:
        print("Geçersiz işlem.")

hesapla()
