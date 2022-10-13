import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="conf", config_name="config_non_structured")
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
        rows: ${db.table_cfg}
    """
    print(OmegaConf.to_yaml(cfg))
    # Should print 1
    print(cfg.model.data_source.rows)

if __name__ == "__main__":
    my_app()