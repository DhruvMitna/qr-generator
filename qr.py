# Importing the necessary functions from modules.
from qrcode import QRCode
from qrcode.constants import ERROR_CORRECT_H

try:

    # Getting the user input.
    Data = input("Enter the text or link that you want to show: ")
    size = float(input("Enter the size of the qrcode (default = 15): "))
    borderSize = float(input("Enter the size of the border of the qrcode: "))
    Fit = input("Enter yes if you want the qrcode size to be responsive: ").lower()

# If the user enters a string where an integer was required, this message is printed out instead of the program crashing.
except ValueError:

    print("Please enter a valid value.")

# Generating the qrcode.
qr = QRCode(error_correction = ERROR_CORRECT_H, box_size = size, border = borderSize)
qr.add_data(Data)

if Fit != "no":

    qr.make(fit = True)

else:

    qr.make()

bg = input("Enter the background color: ").lower()
fg = input("Enter the foreground color: ").lower()

try:

    img = qr.make_image(fill = fg, back_color = bg)

    fileName = input("Enter the name of the image file of the qrcode: ").lower()

    # saving the image.
    img.save(f"output/{fileName}.png")

# If the user enters an unsupported colour, this message is printed out instead of the program crashing.
except (ValueError, NameError) :

    print("Colour not supported.")