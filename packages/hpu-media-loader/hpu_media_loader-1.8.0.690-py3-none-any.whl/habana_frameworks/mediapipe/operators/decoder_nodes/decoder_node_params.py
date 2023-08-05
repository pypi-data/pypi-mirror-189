from habana_frameworks.mediapipe.media_types import ftype as ft
from habana_frameworks.mediapipe.media_types import randomCropType as rct
from habana_frameworks.mediapipe.media_types import decoderStage as ds

# INFO: Here we will give params and its default arguments order doesnt matter
# INFO: if any parameter is not set here it will be set to zero

image_decoder_params = {
    'output_format': 'rgb-i',
    'resize': [0, 0],  # for height,width
    'resampling_mode': ft.BI_LINEAR,
    'random_crop_type': rct.NO_RANDOM_CROP,
    'scale_min': 0,
    'scale_max': 0,
    'ratio_min': 0,
    'ratio_max': 0,
    'decoder_stage': ds.ENABLE_ALL_STAGES,
    'seed': 0}
