import pandas as pd
from heart_disease.repository import ModelRepository
from heart_disease.validation import InputModel


class Processor:

    MAPPING_OUTPUT = ['no disease', 'disease']
    def __init__(self, model_repository: ModelRepository):
        self.model_repository = model_repository

    def predict(self, input_model: InputModel) -> str:
        model = self.model_repository.get_model()
        predicted_output = model.predict(self._process_input_data(input_model))
        return self._process_output_data(predicted_output)
    
    def _process_input_data(self, input_model: InputModel) -> pd.Series:
        return pd.Series(input_model.model_dump())

    def _process_output_data(self, output: pd.Series) -> str:
        return self.MAPPING_OUTPUT[int(output)]