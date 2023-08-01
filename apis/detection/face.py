from flask_restx import Resource, Namespace
from werkzeug.datastructures import FileStorage
from PIL import Image
import numpy as np

face_detect = Namespace("Face Detection","Yolov7 face detection")


upload_parser = face_detect.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)


@face_detect.route('/upload/')
@face_detect.expect(upload_parser)
class Upload(Resource):
    def post(self):
        args = upload_parser.parse_args()
        uploaded_file = args['file']  # This is FileStorage instance
        img = np.array(Image.open(uploaded_file))
        return {'size': img.shape, "task":"detection"}, 201