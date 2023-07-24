from PIL import Image

def generate(imagefile, outputfile):
    img = Image.open(imagefile)
    output = img.copy()
    output = output.resize((output.width * 3, output.height * 3))

    # Set alpha to 0
    output.putalpha(0)

    for x in range(img.width):
        for y in range(img.height):
            outx = x * 3 + 1
            outy = y * 3 + 1
            color = img.getpixel((x, y))
            output.putpixel((outx, outy), color)

    output.save(outputfile)
    print("done!")

generate('place.png', 'output.png')
generate('place.png', 'jahrein-output.png')
