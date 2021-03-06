from orangecontrib.recommendation import Learner, Model

import numpy as np

__all__ = ["LearnerRecommendation", "ModelRecommendation"]


class ModelRecommendation(Model):

    def predict_on_range(self, predictions):
        # Just for modeling ratings with latent factors
        try:
            if self.min_rating is not None:
                predictions[predictions < self.min_rating] = self.min_rating

            if self.max_rating is not None:
                predictions[predictions > self.max_rating] = self.max_rating
        except AttributeError:
            pass
        finally:
            return predictions

    def compute_objective(self):
        pass


class LearnerRecommendation(Learner):
    __returns__ = ModelRecommendation

    def __init__(self, preprocessors=None, verbose=False, min_rating=None,
                 max_rating=None):
        self.min_rating = min_rating
        self.max_rating = max_rating
        super().__init__(preprocessors=preprocessors, verbose=verbose)

    def fit_model(self):
        pass

    def fit_base(self, data):
        """This function calls the fit method.

        Args:
            data: Orange.data.Table

        Returns:
            Model

        """

        model = self.fit_model(data)
        model.min_rating = self.min_rating
        model.max_rating = self.max_rating

        return model
