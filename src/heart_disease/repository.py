from pathlib import Path
from catboost import CatBoostClassifier
from loguru import logger

class ModelRepository:
    def __init__(self, model=None):
        self.model = model
        self.logger = logger

    
    def get_model_path(self):
        current_dir = Path(__file__).resolve().parent
        project_root = current_dir.parent.parent
        model_path = project_root / "models" / "model.cbm"
        return str(model_path)

    
    def load_model(self):
        model_load_path = self.get_model_path()
        self.model = CatBoostClassifier().load_model(model_load_path)
        self.logger.info(f"Model loaded from {model_load_path}")

    def get_model(self):
        return self.model