import os
import six

import SimpleITK as sitk
import pandas as pd
from loguru import logger
from radiomics import featureextractor, getTestCase

class Radiomics:
    def __init__(self, config) -> None:
        self.config = config
        self.root_dir = config.root_dir
        self.extractor = featureextractor.RadiomicsFeatureExtractor(config)

    def __call__(self, ) -> None:
        imageName, maskName = getTestCase('brain1', self.root_dir)
        features = self.extractor.execute(imageName, maskName)  # label=
        features = pd.DataFrame(features, columns=features.keys())
        logger.debug(features)
