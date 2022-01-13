import os
import sys
from google.cloud import vision
import io

"""sys.argv[1] = C:\\Users\\jonat\\OneDrive\\Documents\\EBCS Research\\ChecksOctoberJonathanLaurent (pictures of 
checks folder) 
sys.argv[2] = C:\\Users\\jonat\\GoogleAPIParserKey """


def get_image_paths(folder):
    re = []
    for filename in os.listdir(folder):
        re.append(os.path.join(folder, filename))
    return re


def detect_text(path, text_file_path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    text_doc = ""

    for text in texts:
        text_doc += text.description + " "
    file_name = os.path.basename(path).split(".")[0]
    with open(text_file_path + file_name + '.txt', 'w', encoding='utf-8') as f:
        f.write(text_doc)
    return text_doc


if __name__ == '__main__':
    folder_images_path = "C:\\Users\\jonat\\OneDrive\\Documents\\EBCS Research\\ChecksOctoberJonathanLaurent"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\jonat\\GoogleAPIParserKey"
    img_paths = get_image_paths(folder_images_path)
    dirs = folder_images_path.split("/")
    get_root_dir_img = "/".join([dirs[i] for i in range(0, len(dirs) - 1)])
    if not os.path.exists(get_root_dir_img + "/DL-textfiles"):
        os.makedirs(get_root_dir_img + "/DL-textfiles")
    for img_path in img_paths:
        detect_text(img_path, get_root_dir_img + "/DL-textfiles/")

