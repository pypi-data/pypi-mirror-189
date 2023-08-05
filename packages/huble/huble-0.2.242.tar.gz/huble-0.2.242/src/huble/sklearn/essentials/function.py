from sklearn.model_selection import train_test_split  # type: ignore
import pandas as pd
from ...error.decorators import function_error_handling

@function_error_handling("train_test_split")
def train_test_split(**params):
    data = params['data']
    train_dataset, test_dataset = train_test_split(data=data, test_size=0.33, random_state=42)
    return train_dataset, test_dataset


@function_error_handling("train_model")
def train_model(**params):
    data = params['data']
    y = data[(params['column'])]
    X = data.drop(y, axis=1)
    model = params['model']
    Model =  model.fit(X, y)
    return Model
