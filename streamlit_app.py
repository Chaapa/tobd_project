import streamlit as st
from PIL import Image

# Функция для загрузки изображений
def load_image(image_path):
    return Image.open(image_path)

# Настройка страницы
st.set_page_config(page_title="Предсказания", layout="centered")

# Заголовок приложения
st.title("Предсказания будущего")

# Подзаголовок
st.subheader("Выберите категорию предсказания, чтобы увидеть изображение")

# Категории
categories = {
    "На завтра": "images/tomorrow_prediction.jpg",
    "На неделю вперед": "images/week_prediction.jpg",
    "На месяц вперед": "images/month_prediction.jpg"
}

# Выбор категории
selected_category = st.radio("Категории предсказаний:", list(categories.keys()))

# Показ изображения
if selected_category:
    image_path = categories[selected_category]
    image = load_image(image_path)
    st.image(image, caption=selected_category, use_container_width=True)

