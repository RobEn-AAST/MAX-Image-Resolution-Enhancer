# Flask settings
DEBUG = False

# Flask-restplus settings
RESTPLUS_MASK_SWAGGER = False
SWAGGER_UI_DOC_EXPANSION = 'none'

# API metadata
API_TITLE = 'MAX Image Super-Resolution Generator'
API_DESC = 'Upscale low-resolution images by a factor of 4x. This model was trained on the OpenImagesV4 dataset.'
API_VERSION = '0.1'

# default model
MODEL_NAME = 'SRGAN'
DEFAULT_MODEL_PATH = 'assets/SRGAN/model'

MODEL_META_DATA = {
    'id': '{}_tensorflow'.format(MODEL_NAME.lower()),
    'name': 'Super-Resolution Generative Adversarial Network (SRGAN)',
    'description': 'SRGAN trained on the OpenImagesV4 dataset.',
    'type': 'Image-To-Image Translation Or Transformation',
    'source': 'https://developer.ibm.com/exchanges/models',
    'license': 'ApacheV2'
}