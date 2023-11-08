#importing qrcode library
import qrcode

#making the function for generator

def qr_generator(text):
    qr= qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size= 10,
        border= 4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img= qr.make_image(fill_color= "black",back_color= "white")
    img.save(f"{name}.png")

print("Welcome to QR code generator")
link= input("Enter your link")
name= input("enter file name ")
qr_generator(link)




