from __future__ import print_function
import os ,io
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'image-description-344713-24cbf65711ff.json'

class ImageDescriptor:
    
    def __init__(self, path):
        # self.img_url = img_url
        self.img_path = path
        client = vision.ImageAnnotatorClient()
        
        with io.open(self.img_path, 'rb') as image_file:
            content = image_file.read()
        
        image = vision.Image(content=content)
        # image.source.image_uri = self.img_url
        
        response = client.label_detection(image=image)
        
        self.desc = ''
        
        for label in response.label_annotations:
            self.desc += str(label.description) + ' '
        
    def get_description(self, Language = 'Thai') -> str:
        return self.desc


if __name__ == '__main__':
    image_uri = 'gs://cloud-samples-data/vision/using_curl/shanghai.jpeg'

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = image_uri

    response = client.label_detection(image=image)
    print(response.label_annotations[0].description)