import requests
import time
from PIL import Image, ImageFont, ImageDraw

# Настройка API
API_KEY = "YOUR_API_KEY"

# Настройка NZXT Kraken 360
SCREEN_WIDTH = 360
SCREEN_HEIGHT = 240

# Настройка цветов
BACKGROUND_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)

# Настройка шрифтов
FONT_PATH = "fonts/pixel.ttf"
FONT_SIZE = 16

# Функция для получения курса криптовалюты
def get_crypto_price(currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={currency}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[currency]["usd"]

# Функция для отображения курса на экране
def display_price(currency, price):
    # Создаем изображение
    image = Image.new("RGB", (SCREEN_WIDTH, SCREEN_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(image)

    # Отображаем название криптовалюты
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    text_width, text_height = draw.textsize(currency, font=font)
    draw.text((SCREEN_WIDTH / 2 - text_width / 2, 10), currency, font=font, fill=TEXT_COLOR)

    # Отображаем курс
    text = f"{price:.2f} USD"
    text_width, text_height = draw.textsize(text, font=font)
    draw.text((SCREEN_WIDTH / 2 - text_width / 2, SCREEN_HEIGHT - 20), text, font=font, fill=TEXT_COLOR)

    # Отображаем изображение на экране
    image.show()

# Цикл обновления курса
while True:
    # Получаем курс биткоина
    bitcoin_price = get_crypto_price("bitcoin")

    # Получаем курс эфириума
    ethereum_price = get_crypto_price("ethereum")

    # Отображаем курс биткоина
    display_price("Bitcoin", bitcoin_price)

    # Отображаем курс эфириума
    display_price("Ethereum", ethereum_price)

    # Задержка 1 секунда
    time.sleep(1)
