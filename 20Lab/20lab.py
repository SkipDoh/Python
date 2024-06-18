from PIL import Image, ImageDraw

# Создаем новое изображение
width, height = 2000, 2000
img = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(img)


# Функция для рисования буквы D
def draw_D(draw):
    draw.arc((100, 100, 300, 900), start=0, end=360, fill='black', width=20)
    draw.line([(100, 100), (100, 900)], fill='black', width=20)
    draw.line([(100, 100), (200, 100)], fill='black', width=20)
    draw.line([(100, 900), (200, 900)], fill='black', width=20)


# Функция для рисования буквы a
def draw_a(draw):
    draw.arc((300, 500, 500, 700), start=0, end=180, fill='black', width=20)
    draw.line([(400, 500), (400, 900)], fill='black', width=20)
    draw.line([(400, 700), (460, 700)], fill='black', width=20)


# Функция для рисования буквы N
def draw_N(draw):
    draw.line([(600, 100), (600, 900)], fill='red', width=20)
    draw.line([(600, 100), (750, 900)], fill='red', width=20)
    draw.line([(750, 900), (750, 100)], fill='red', width=20)


# Функция для рисования буквы i
def draw_i(draw):
    draw.line([(800, 100), (800, 900)], fill='black', width=20)


# Функция для рисования буквы L
def draw_L(draw):
    draw.line([(900, 100), (900, 900)], fill='blue', width=20)
    draw.line([(900, 900), (1050, 900)], fill='blue', width=20)


# Рисуем каждую букву
draw_D(draw)
draw_a(draw)
draw_N(draw)
draw_i(draw)
draw_L(draw)

# Сохраняем изображение
img.save('result.png')

# Показываем изображение
img.show()