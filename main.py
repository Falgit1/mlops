from segmentation import logger
from segmentation.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from segmentation.pipeline.stage02_prepare_base_model import BaseModelTrainingPipeline
from segmentation.pipeline.stage03_training import TrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"======== Stage : {STAGE_NAME} started =========")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"======== Stage : {STAGE_NAME} completed =========")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info(f"======== Stage : {STAGE_NAME} started =========")
    obj = BaseModelTrainingPipeline()
    obj.main()
    logger.info(f"======== Stage : {STAGE_NAME} completed =========")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training Stage"

try:
    logger.info(f"======== Stage : {STAGE_NAME} started =========")
    obj = TrainingPipeline()
    obj.main()
    logger.info(f"======== Stage : {STAGE_NAME} completed =========")
except Exception as e:
    logger.exception(e)
    raise e
