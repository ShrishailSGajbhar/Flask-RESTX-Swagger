from flask_restx import Api
from flask import Blueprint

from .classification import face_classif
from .detection import face_detect

documents = Blueprint("Api",__name__,url_prefix='/docs')

api = Api(
    documents,
    title='MY REST Api',
    version='1.0',
    description='A Computer Vision REST API for detection and classification',
)

api.add_namespace(face_detect)
api.add_namespace(face_classif)