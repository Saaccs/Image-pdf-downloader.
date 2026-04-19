import os
import time
import requests
from PIL import Image

CONTENT_ID = input("ID: ").strip()
BASE_URL = input("Base URL (ej: https://cache1.sitio.com/contents/): ").strip()
REFERER = input("Referer (ej: https://sitio.com/): ").strip()

DELAY = 0.7
MAX_FAILS = 5

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Referer": REFERER,
    "Accept": "image/webp,image/*,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8"
}

# -----------------------------

def download_content(content_id):
    print(f"\n📥 Descargando ID: {content_id}")

    folder = f"content_{content_id}"
    os.makedirs(folder, exist_ok=True)

    session = requests.Session()
    session.headers.update(HEADERS)

    images = []

    fails = 0
    page = 0

    while True:
        filename = f"{page:03}.webp"
        url = f"{BASE_URL}{content_id}/{filename}"
        path = os.path.join(folder, filename)

        try:
            r = session.get(url, timeout=10)

            if r.status_code == 200 and len(r.content) > 1000:
                with open(path, "wb") as f:
                    f.write(r.content)

                print(f"✅ {filename}")
                images.append(path)
                fails = 0
            else:
                fails += 1
                print(f"❌ {filename} ({r.status_code})")

            if fails >= MAX_FAILS:
                break

            page += 1
            time.sleep(DELAY)

        except Exception as e:
            print(f"⚠️ Error: {e}")
            fails += 1
            time.sleep(DELAY)

    if images:
        create_pdf(images, content_id, folder)
    else:
        print("\n❌ No se descargaron imágenes")


def create_pdf(image_paths, content_id, folder):
    print("\n📄 Creando PDF...")

    imgs = []

    for img_path in sorted(image_paths):
        try:
            img = Image.open(img_path).convert("RGB")
            imgs.append(img)
        except:
            print(f"⚠️ Error en {img_path}")

    if not imgs:
        print("❌ No hay imágenes")
        return

    pdf_path = f"{content_id}.pdf"

    imgs[0].save(
        pdf_path,
        save_all=True,
        append_images=imgs[1:]
    )

    print(f"🎉 PDF creado: {pdf_path}")

    # 🔥 LIMPIEZA
    print("\n🧹 Eliminando imágenes...")

    for img in image_paths:
        try:
            os.remove(img)
        except:
            pass
    try:
        os.rmdir(folder)
    except:
        pass

    print("✔️ Limpieza completada")

if __name__ == "__main__":
    download_content(CONTENT_ID)
