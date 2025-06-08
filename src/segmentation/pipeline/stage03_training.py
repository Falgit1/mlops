from segmentation.config.configuration import ConfigurationManager
from segmentation.components.prepare_callbacks import PrepareCallbacks
from segmentation.components.training import Training
from segmentation import logger

STAGE_NAME = "Training Stage"


class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        X, Y = training.data_preprocessing()
        training.train(X, Y,
                       callback_list=callback_list
                       )


if __name__ == '__main__':
    try:
        logger.info(f"======== Stage : {STAGE_NAME} started =========")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f"======== Stage : {STAGE_NAME} completed =========")
    except Exception as e:
        logger.exception(e)
        raise e
