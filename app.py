import streamlit as st

st.set_page_config(page_title="CatNet Simple Browser", layout="wide")

st.title("CatNet Simple Browser")

# Arama / URL girişi
query = st.text_input("Arama yap veya URL gir", "")

if query:
    if query.startswith("http://") or query.startswith("https://"):
        url = query
    elif "." in query:
        url = "http://" + query
    else:
        # Arama terimi ise Google arama linki oluştur
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

    st.write(f"**Açılan sayfa:** [{url}]({url})")

    # Sayfa gösterimi için iframe (bazı sitelerde çalışmayabilir)
    st.components.v1.iframe(url, height=700, scrolling=True)
else:
    st.write("Lütfen yukarıdaki kutuya arama terimi veya URL girin.")

# Cat CPT AI'ye git butonu
if st.button("Cat CPT AI'ye Git"):
    st.markdown("[Cat CPT AI Linki](https://u7d-vsupbr8wh-42h8-cgr9opjrtf4t6zmw79vm2s.streamlit.app/)")
