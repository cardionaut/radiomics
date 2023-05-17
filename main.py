import hydra

from loguru import logger
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path='.', config_name='config')
def main(config: DictConfig) -> None:
    pass

if __name__ == '__main__':
    main()