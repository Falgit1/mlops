from segmentation.config.configuration import ConfigurationManager
from segmentation.components.training import Training
from segmentation.components.evaluation import Evaluation
from segmentation import logger

STAGE_NAME = "Evaluation Stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_evaluation_config()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        X, Y = training.data_preprocessing()
        evaluation = Evaluation(config=evaluation_config)
        evaluation.evaluation(X, Y)
        evaluation.save_score(file_path=evaluation_config.score_file)


if __name__ == '__main__':
    try:
        logger.info(f"======== Stage : {STAGE_NAME} started =========")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f"======== Stage : {STAGE_NAME} completed =========")
    except Exception as e:
        logger.exception(e)
        raise e
