import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import DictConfig, OmegaConf
from dataclasses import dataclass

@dataclass
class TableConfig:
    rows: int = 1
    cols: int = 2

@dataclass
class DatabaseConfig:
    driver: str = "postgresql"
    user: str = "user"
    password: str = "password"
    table_cfg: TableConfig = TableConfig()

@dataclass
class ModelConfig:
    data_source: TableConfig = TableConfig()

@dataclass
class ServerConfig:
    db: DatabaseConfig
    model: ModelConfig

cs = ConfigStore.instance()
cs.store(name="database", node=DatabaseConfig, group="db")
cs.store(name="server", node=ServerConfig)

@hydra.main(version_base=None, config_path="conf", config_name="config")
def my_app(cfg : DictConfig) -> None:
    """Should print:
    db:
        driver: postgresql
        user: user
        password: password
        table_cfg:
            rows: 1
            cols: 2
    model:
        data_source: ${db.table_cfg}
    """
    print(OmegaConf.to_yaml(cfg))
    # Should print 1
    print(cfg.model.data_source.rows)

if __name__ == "__main__":
    my_app()