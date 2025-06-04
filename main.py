from Plant_class import logger
from Plant_class.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"======== Stage : {STAGE_NAME} started =========")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"======== Stage : {STAGE_NAME} completed =========")
except Exception as e:
    logger.exception(e)
    raise e
