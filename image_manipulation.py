from PIL import Image, ImageFilter, ImageEnhance

def manipulate_image(input__path, output__path):
    try:
        # Memuat gambar
        image = Image.open(input__path)
        print("✅ Gambar berhasil dimuat")

        # Operasi Cropping dengan validasi ukuran
        if image.width > 200 and image.height > 200:
            cropped_image = image.crop((10, 10, 200, 200))
            cropped_image.save('cropped_' + output__path)
            print("✅ Cropping berhasil")
        else:
            raise ValueError("Gambar terlalu kecil untuk di-crop ke ukuran 200x200")

        # Operasi Resizing dengan rasio aspek yang dipertahankan
        resized__image = cropped_image.resize((100, 100), Image.LANCZOS)
        resized__image.save('resized_' + output__path)
        print("✅ Resizing berhasil")

        # Operasi Filtering
        filtered__image = resized__image.filter(ImageFilter.BLUR)
        filtered__image.save('filtered_' + output__path)
        print("✅ Filtering berhasil")

        # Operasi Pengaturan Kecerahan
        enhancer = ImageEnhance.Brightness(filtered__image)
        bright__image = enhancer.enhance(1.5)
        bright__image.save('bright__' + output__path)
        print("✅ Pengaturan kecerahan berhasil")

        # Operasi Penggabungan Gambar
        combined_image = Image.blend(filtered__image, bright__image, alpha=0.5)
        combined_image.save('combined_' + output__path)
        print("✅ Penggabungan gambar berhasil")

    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    manipulate_image('example.jpg', 'result.jpg')