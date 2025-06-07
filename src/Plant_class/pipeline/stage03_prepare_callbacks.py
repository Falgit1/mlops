from Plant_class.config.configuration import ConfigurationManager
from Plant_class.components.prepare_callbacks import PrepareCallbacks
from Plant_class import logger

STAGE_NAME = "Prepare Callbacks Stage"


class CallbacksTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()


if __name__ == '__main__':
    try:
        logger.info(f"======== Stage : {STAGE_NAME} started =========")
        obj = CallbacksTrainingPipeline()
        obj.main()
        logger.info(f"======== Stage : {STAGE_NAME} completed =========")
    except Exception as e:
        logger.exception(e)
        raise e
