from flask_restx import Resource, Namespace
from werkzeug.datastructures import FileStorage
from PIL import Image
import numpy as np
from logger import logger

face_classif = Namespace("Face Classification","Yolov7 face classification")


upload_parser = face_classif.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)


@face_classif.route('/upload/')
@face_classif.expect(upload_parser)
class Upload(Resource):
    def post(self):
        args = upload_parser.parse_args()
        uploaded_file = args['file']  # This is FileStorage instance
        img = np.array(Image.open(uploaded_file))
        logger.info({'filename':uploaded_file.filename,'size': img.shape, "task":"classification"})
        return {'size': img.shape, "task":"classification"}, 201