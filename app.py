import streamlit as st

st.set_page_config(page_title="CatNet Simple Browser", layout="wide")

st.markdown("""
<style>
    /* Google tarzı basit stil */
    .search-box {
        max-width: 600px;
        margin: 30px auto;
    }
    .result {
        border-bottom: 1px solid #ddd;
        padding: 10px 0;
    }
    .result-title {
        font-size: 18px;
        color: #1a0dab;
        margin-bottom: 5px;
        text-decoration: none;
    }
    .result-link {
        color: #006621;
        font-size: 14px;
        margin-bottom: 3px;
    }
    .result-desc {
        color: #545454;
        font-size: 13px;
    }
    .answer-box {
        background: #f8f9fa;
        border: 1px solid #dadce0;
        padding: 15px;
        max-width: 600px;
        margin: 0 auto 30px auto;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

st.title("CatNet Simple Browser")

with st.form("search_form", clear_on_submit=False):
    query = st.text_input("Arama yap veya URL gir", key="input")
    submitted = st.form_submit_button("Ara")

if submitted and query.strip():
    # Sabit asıl cevap (normalde burası API veya scraping ile gerçek cevaba dönebilir)
    answer = (
        f"**Asıl Cevap:**\n\n"
        f"\"{query}\" hakkında genel bilgi: Bu örnek uygulamada gerçek arama yapılmamaktadır, "
        f"ancak burada gerçek Google gibi öne çıkan tek bir cevap gösterilebilir."
    )
    
    # Sabit 10 tane örnek sonuç listesi
    example_results = [
        {"title": "Site 1 Başlık", "url": "https://site1.com", "desc": "Site 1 kısa açıklama burada yer alır."},
        {"title": "Site 2 Başlık", "url": "https://site2.com", "desc": "Site 2 hakkında bilgi burada."},
        {"title": "Site 3 Başlık", "url": "https://site3.com", "desc": "Site 3 açıklaması örneği."},
        {"title": "Site 4 Başlık", "url": "https://site4.com", "desc": "Site 4 ile ilgili kısa bilgi."},
        {"title": "Site 5 Başlık", "url": "https://site5.com", "desc": "Site 5 tanıtım metni."},
        {"title": "Site 6 Başlık", "url": "https://site6.com", "desc": "Site 6 içeriği hakkında açıklama."},
        {"title": "Site 7 Başlık", "url": "https://site7.com", "desc": "Site 7 ile ilgili kısa özet."},
        {"title": "Site 8 Başlık", "url": "https://site8.com", "desc": "Site 8 tanıtım yazısı."},
        {"title": "Site 9 Başlık", "url": "https://site9.com", "desc": "Site 9 hakkında kısa bilgi."},
        {"title": "Site 10 Başlık", "url": "https://site10.com", "desc": "Site 10 açıklaması burada yer alır."},
    ]
    
    # Asıl cevabı göster
    st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)
    
    # Sonuçları listele
    st.markdown('<div class="search-box">', unsafe_allow_html=True)
    for res in example_results:
        st.markdown(
            f'<div class="result">'
            f'<a href="{res["url"]}" target="_blank" class="result-title">{res["title"]}</a><br>'
            f'<span class="result-link">{res["url"]}</span><br>'
            f'<span class="result-desc">{res["desc"]}</span>'
            f'</div>',
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.write("Lütfen yukarıdaki kutuya arama terimi girip 'Ara' butonuna basın.")

# Cat CPT AI'ye git butonu (alt kısımda)
if st.button("Cat CPT AI'ye Git"):
    st.markdown("[Cat CPT AI Linki](https://u7d-vsupbr8wh-42h8-cgr9opjrtf4t6zmw79vm2s.streamlit.app/)")
