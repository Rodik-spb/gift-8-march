import streamlit as st
import os
import base64

# 1. Настройка страницы
st.set_page_config(page_title="тест-подарок", page_icon="🎁")

# 2. ТЕМНЫЙ ГРАДИЕНТ И УЛУЧШЕННЫЙ БЕЛЫЙ ТЕКСТ (CSS)
st.markdown("""
<style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {padding-top: 2rem; }
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1a0624 0%, #3d0c45 50%, #1a0624 100%);
    }
    h1, h2, h3, p, label, span, .stMarkdown, [data-testid="stMarkdownContainer"] p {
        color: #ffffff !important;
    }
    .streamlit-expanderHeader {
        background-color: rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px;
        color: white !important;
    }
    div[data-testid="stRadio"] label {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Функция для отображения ГИФОК и картинок (теперь с поддержкой анимации)
def safe_image(file_name, width=300):
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            data = f.read()
            encoded = base64.b64encode(data).decode()

        if file_name.lower().endswith(".gif"):
            mime_type = "image/gif"
        elif file_name.lower().endswith(".png"):
            mime_type = "image/png"
        else:
            mime_type = "image/jpeg"

        st.markdown(
            f'<img src="data:{mime_type};base64,{encoded}" width="{width}">',
            unsafe_allow_html=True
        )
    else:
        st.warning(f"⚠️ Файл '{file_name}' не найден.")
# --- ЛОГИКА ПАРОЛЯ ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def check_password():
    # ЗДЕСЬ МОЖНО ИЗМЕНИТЬ ПАРОЛЬ
    correct_passwords = ["29 июля"]
    user_input = st.session_state["password_input"].strip().lower()
    if user_input in correct_passwords:
        st.session_state["authenticated"] = True
        del st.session_state["password_input"]
    else:
        st.error("❌ Неверно! Попробуй еще раз")

# Если пользователь еще не прошел проверку
if not st.session_state['authenticated']:
    st.title("🔐 Доступ ограничен")
    st.write("Негодяев не пускаем, сначала пройдите проверку")
    st.info("💡 **Наводящий вопрос:** Когда мы начали встречаться?")
    st.text_input("Введи секретное слово:", type="password", key="password_input", on_change=check_password)
    st.stop()  # Останавливает выполнение кода здесь, пока пароль не верный


# --- ЗАГОЛОВОК ---
st.title("С праздником тебя, Дашулька!")
st.write("Ответь на все вопросы правильно, чтобы стать ближе к подарку!")

# Главный котик (проверка связи)
safe_image("chonguk.png", width=90)

# 3. Список вопросов
questions = [
    {"q": "Какая песня играла на Зените, когда мы познакомились?",
     "o": ["Гроза", "Молния", "Вспышка"],
     "a": "Молния",
     "h_img": "molniya.png"},

    {"q": "Кто автор песни Флешмоб?",
     "o": ["Три дня дождя", "Kizaru", "Lida"],
     "a": "Три дня дождя",},

    {"q": "Какое число написано у меня на футболке?",
     "o": ["13", "69", "68"],
     "a": "68"},

    {"q": "Какое отчество у моего папы?",
     "o": ["Михайлович", "Денисович", "Викторович"],
     "a": "Викторович",
     "h_img": "tsoy.png"},

    {"q": "А у мамы?",
     "o": ["Викторовна", "Михайловна", "Николаевна"],
     "a": "Викторовна",
     "h_img": "tsoy.png"},

    {"q": "Что написано на подвеске, которую ты мне подарила?",
     "o": ["I LOVE LIDA", "I HATE LIDA", "LIDA ONE LOVE"],
     "a": "I HATE LIDA"},

]

correct_count = 0

# 4. ЦИКЛ ВОПРОСОВ
for i, item in enumerate(questions):
    st.subheader(f"Вопрос №{i + 1}")
    if item.get("q_img"):
       safe_image(item["q_img"], width=400)
    user_choice = st.radio(item["q"], item["o"], key=f"q{i}", index=None)

    h_text, h_img = item.get("h_text"), item.get("h_img")
    if h_text or h_img:
        with st.expander("💡 Подсказка"):
            if h_text: st.write(h_text)
            if h_img: safe_image(h_img, width=250)

    if user_choice == item["a"]:
        correct_count += 1

st.divider()

# 5. ФИНАЛ
st.subheader("🔥 Финальный вопрос")
col_text, col_gif = st.columns([2, 1])

with col_text:
    user_final = st.text_input("Ты меня любишь?")

with col_gif:
    safe_image("pocoyo.gif", width=160)


final_artist = "Да"

if user_final:
    if final_artist.lower() in user_final.lower():
        if correct_count == len(questions):
            st.balloons()
            st.success("Все ответы верны! 🎉")
            st.link_button("🎟 ЗАБРАТЬ ПОДАРОК", "https://drive.google.com/drive/u/0/folders/1AG_NiuMDQAKNaeg8AuC2xAHBj9_Ds5IS")
            st.snow()
        else:
            st.error(f"Правильный! Но в тесте есть ошибки. Правильно отвечено на {correct_count} из {len(questions)}")
    else:
        st.warning("Ответ: Да?")




















