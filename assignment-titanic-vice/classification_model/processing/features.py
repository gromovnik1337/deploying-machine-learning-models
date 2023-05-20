from sklearn.base import BaseEstimator, TransformerMixin


class ExtractLetterTransformer(BaseEstimator, TransformerMixin):
    # Extract fist letter of variable

    def __init__(self, variables):
        
        if not isinstance(variables, list):
            raise ValueError('variables should be a list')
        
        self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        X = X.copy()
        for features in self.variables:
            X[features] = X[features].str[0]

        return X
