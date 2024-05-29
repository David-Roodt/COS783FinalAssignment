#converts input image to ela applied image
from PIL import Image, ImageChops, ImageEnhance


def convert_to_ela_image(filename,quality):

    Original_Image = Image.open(filename).convert('RGB')

    Compressed_Image_filename = 'resaved_image.jpg'
    Original_Image.save(Compressed_Image_filename,'JPEG',quality=quality)
    Compressed_Image = Image.open(Compressed_Image_filename)

    ELA_Image = ImageChops.difference(Original_Image,Compressed_Image)
    
    #scaling factors are calculated from pixel extremas
    extrema = ELA_Image.getextrema()
    max_difference = max([pix[1] for pix in extrema])
    if max_difference ==0:
        max_difference = 1
    scale = 350.0 / max_difference
    
    ELA_Image = ImageEnhance.Brightness(ELA_Image).enhance(scale)

    ELA_Image.save("ela_image.png")
    return ELA_Image