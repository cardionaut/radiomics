import hydra

from loguru import logger
from omegaconf import DictConfig, OmegaConf

from feature_extraction.radiomics import Radiomics


@hydra.main(version_base=None, config_path='.', config_name='config')
def main(config: DictConfig) -> None:
    radiomics = Radiomics(config)()
    

if __name__ == '__main__':
    main()