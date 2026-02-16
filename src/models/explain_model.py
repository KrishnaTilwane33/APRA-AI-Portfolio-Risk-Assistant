import pandas as pd
import numpy as np

def explain_logistic_model(model,feature_names, class_labels):
    coef = model.coef_

    coef_df = pd.DataFrame(
        coef,
        columns=feature_names,
        index=class_labels
    )

    return coef_df