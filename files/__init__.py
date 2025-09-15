import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


TXT_FILE_PATH = get_path(filename="example.txt")
CSV_FILE_PATH = get_path(filename="users.csv")
JSON_FILE_PATH = get_path(filename="example.json")
SQLITE_FILE_PATH = get_path(filename="data.sqlite")
PDF_FILE_PATH = get_path(filename="example.pdf")
EXCEL_FILE_PATH = get_path(filename="qa.xlsx")
JPG_FILE_PATH = get_path(filename="jpg.jpg")
JPEG_FILE_PATH = get_path(filename="example.jpeg")
PNG_FILE_PATH = get_path(filename="example_small.png")
