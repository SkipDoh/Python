from PIL import Image, ImageDraw

# Создаем новое изображение
width, height = 400, 200
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Нарисуем березовый фон
for x in range(width):
    for y in range(height):
        if y < height//2:
            draw.point((x, y), (122, 197, 205))
        else:
            draw.point((x, y), (122, 197, 205))

# Нарисуем зеленый квадрат
draw.polygon([(50, 50), (200, 50), (200, 200), (50, 200)], fill='green')

# Нарисуем синюю крышу
draw.polygon([(50, 50), (125, 25), (200, 50)], fill='blue')

# Нарисуем двуступенчатую красную лестницу
draw.rectangle([(200, 110), (250, 200)], fill='red')
draw.rectangle([(250, 150), (300, 200)], fill='red')

# Нарисуем желтый круг
draw.ellipse((300, 0, 400, 100), fill='yellow')

# Отобразим изображение
image.show()