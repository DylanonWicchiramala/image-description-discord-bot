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

    model = ImageDescriptor('img/13f03c70-0116-4627-8490-dd98f97d70b0.jpg')
    txt = model.get_description()
    print(txt)