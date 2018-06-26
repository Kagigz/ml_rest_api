import logging
from http import HTTPStatus
from flask_restplus import Api
from ml_rest_api.settings import settings

log = logging.getLogger(__name__)

api = Api(version='0.1', 
          title='Godel ML REST API',
          description='A RESTful API to return predictions from a trained ML model, built with Python 3 and Flask-RESTplus',
          default='health',
          default_label='Basic health check methods',)


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings['FLASK_DEBUG']:
        return {'message': message}, HTTPStatus.INTERNAL_SERVER_ERROR
