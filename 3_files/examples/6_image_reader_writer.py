from files.files import JPEG_FILE_PATH

with open(JPEG_FILE_PATH, "rb") as file:
    img = file.read()
    with open('temp_image.jpeg', "wb") as new_file:
        new_file.write(img)

    with open('temp_image.jpeg', "rb") as new_file:
        img_res = file.read()

    assert img == img_res

with open(JPEG_FILE_PATH, "rb") as file:
    img = file.read()
    with open('temp_image.jpeg', "wb") as new_file:
        new_file.write(img)

    with open('temp_image.jpg', "rb") as new_file:
        img_res = file.read()

    assert img == img_res

# from files.files import PNG_FILE_PATH
#
# with open(PNG_FILE_PATH, "rb") as file:
#     img = file.read()
#     with open('temp_image.png', "wb") as new_file:
#         new_file.write(img)
#
# from files.files import JPG_FILE_PATH
#
# with open(JPG_FILE_PATH, "rb") as file:
#     img = file.read()
#     with open('temp_image.jpg', "wb") as new_file:
#         new_file.write(img)