from fastapi import FastAPI
from loguru import logger


from heart_disease.processor import Processor
from heart_disease.repository import ModelRepository
from heart_disease.validation import InputModel

app = FastAPI()

logger.add("logs/app.log", level="INFO")

repository = ModelRepository()
repository.load_model()

@app.get("/ping")
def root():
    logger.info("Принят запрос на проверку работоспособности")
    return {"message": "Pong"}


@app.post("/prediction")
def prediction(input_model: InputModel):
    logger.info("Принят запрос на предсказание")
    logger.debug(f"Входной X-вектор: {input_model.model_dump()}")

    processor = Processor(repository)
    output = processor.predict(input_model)
    logger.debug(f"Выходной Y-вектор: {output}")

    return {"result": output}


