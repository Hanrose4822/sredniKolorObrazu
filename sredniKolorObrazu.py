
sciezka = # sciezka do pliku

def srednikolor(sciezka):
    from PIL import Image
    import io
    from io import BytesIO
    import numpy as np
    byteImgIO = io.BytesIO()
    obraz = Image.open(sciezka)
    obraz.save(byteImgIO, "PNG")
    byteImgIO.seek(0)
    obraz = byteImgIO.read()

    dataBytesIO = io.BytesIO(obraz)
    Image.open(dataBytesIO)

    obraz = Image.open(BytesIO(obraz))

    pixels = np.array(obraz)

    R = int(pixels[:, :, 0].mean())

    G = int(pixels[:, :, 1].mean())

    B = int(pixels[:, :, 2].mean())

    kolor = (R, G, B)
    print(kolor)


srednikolor(sciezka)
