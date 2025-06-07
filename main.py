from Plant_class import logger
from Plant_class.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from Plant_class.pipeline.stage02_prepare_base_model import BaseModelTrainingPipeline
from Plant_class.pipeline.stage03_prepare_callbacks import CallbacksTrainingPipeline

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

# STAGE_NAME = "Prepare Callbacks Stage"
#
# try:
#     logger.info(f"======== Stage : {STAGE_NAME} started =========")
#     obj = CallbacksTrainingPipeline()
#     obj.main()
#     logger.info(f"======== Stage : {STAGE_NAME} completed =========")
# except Exception as e:
#     logger.exception(e)
#     raise e

