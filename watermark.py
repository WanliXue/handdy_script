from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def Apply_Watermark(input, output, text):
    image = Image.open(input)
    font = ImageFont.truetype("arial.ttf", 120)

    image  = Image.open('hao.jpg')

    w, h = image.size
    draw = ImageDraw.Draw(image)




    text_w, text_h = draw.textsize(text, font)
    pos = w - text_w, (h - text_h) - 50
    watermark_text = Image.new('RGB', (text_w, (text_h)))
    draw = ImageDraw.Draw(watermark_text)

    draw.text((0, 0), text, font=font)
    watermark_text.putalpha(100)

    image.paste(watermark_text, pos, watermark_text)
    image.save(output)

Apply_Watermark('hao.jpg', 'watermark.jpg', 'WaterMark')