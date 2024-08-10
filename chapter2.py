from PIL import Image
from PIL import ImageFilter

# Memuat gambar
image = Image.open('example.jpg')

# Memotong gambar
cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('cropped_result.jpg')

# Mengubah ukuran gambar
resized_image = cropped_image.resize((100, 100))
resized_image.save('resized_result.jpg')

# Menerapkan filter blur
filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('filtered_result.jpg')

# Menyimpan gambar asli
image.save('result.jpg')
