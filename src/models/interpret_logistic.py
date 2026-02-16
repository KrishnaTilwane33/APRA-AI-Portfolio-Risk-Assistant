import pandas as pd


def extract_coefficients(model, feature_cols):
    coef_df = pd.DataFrame(
        model.coef_,
        columns=feature_cols,
        index=model.classes_
    )
    return coef_df
