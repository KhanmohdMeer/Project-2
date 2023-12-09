import pyqrcode
from PIL import Image

# Create a QR code instance
url = pyqrcode.create('LINK HERE')

# Save the QR code as an image file
url.png('MyProfile.png', scale=8)

# Display the QR code
image = Image.open('MyProfile.png')
image.show()