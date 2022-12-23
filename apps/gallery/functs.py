from functools import partial
from shared.functions.get_path import get_upload_path as _get_upload_path


get_upload_path = partial(_get_upload_path, app_name='gallery')



