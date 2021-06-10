import pandas as pd
import numpy as np


def rank_dataframe(
    dataframe, year=None, season=None, company_type=False, pct=False, skip_col=[]
):
    """Ranking the data of dataframe by year or season or both

    Args:
        dataframe(require): an pandas.DataFrame object

    Returns:
       check_series: Boolean. If the dataframe has nan, return True. Vice versa.
       check_signal: Pandas.Series. Shows whether each column contains nan.

    Raises:

    """
    init_skip_col = ["company_code", "company_type", "year", "season"]

    if skip_col:
        init_skip_col.extend(skip_col)

    ranked_df = pd.DataFrame()
    try:
        ranked_df = dataframe.loc[:, init_skip_col].copy()
        operable_columns = dataframe.drop(columns=init_skip_col).columns
    except:
        pass
    groupby_params = []

    if company_type:
        groupby_params.append("company_type")

    if year and season:
        groupby_params.extend(["year", "season"])
    elif year:
        groupby_params.extend(["year"])
    elif season:
        groupby_params.extend(["season"])

    if year or season:
        grouped_df = dataframe.groupby(groupby_params)
    else:
        grouped_df = dataframe

    for col in operable_columns:
        ranked_df[f"{str(col)}_rank"] = grouped_df[col].rank(method="min", pct=pct)

    return ranked_df


def check_dataframe_nan(dataframe):
    """Check whether there is nan in the data frame. If there is, it returns True. vice versa.

    Retrieves ckeck_signal and check_series, which react whether dataframe has nan values.

    Args:
        dataframe: an pandas.DataFrame object

    Returns:
       check_series: Boolean. If the dataframe has nan, return True. Vice versa.
       check_signal: Pandas.Series. Shows whether each column contains nan.

    Raises:
    """

    check_series = dataframe.isna().any()
    check_signal = check_series.any()

    return check_signal, check_series


def normalize_dataframe(
    dataframe,
    year=None,
    season=None,
    company_type=False,
    method="linear_scaling",
    skip_col=[],
):
    """Ranking the data of dataframe by year or season or both

    Args:
        dataframe(require): an pandas.DataFrame object

    Returns:
       check_series: Boolean. If the dataframe has nan, return True. Vice versa.
       check_signal: Pandas.Series. Shows whether each column contains nan.

    Raises:

    """
    init_skip_col = ["company_code", "company_type", "year", "season"]

    if skip_col:
        init_skip_col.extend(skip_col)

    normalized_df = pd.DataFrame()
    try:
        normalized_df = dataframe.loc[:, init_skip_col].copy()
        operable_columns = dataframe.drop(columns=init_skip_col).columns
    except:
        pass
    groupby_params = []

    if company_type:
        groupby_params.append("company_type")

    if year and season:
        groupby_params.extend(["year", "season"])
    elif year:
        groupby_params.extend(["year"])
    elif season:
        groupby_params.extend(["season"])

    if company_type or year or season:
        grouped_df = dataframe.groupby(groupby_params)

    if groupby_params:
        for col in operable_columns:

            normalized_df[col] = choose_normalized_method(
                grouped_df[col], method=method
            )
            # .apply(
            #     lambda x: (x - x.min()) / (x.max() - x.min())
            # )
    else:
        scaled_df = dataframe.drop(columns=init_skip_col)
        scaled_df = choose_normalized_method(scaled_df, method=method)
        # .apply(lambda x: (x - x.min()) / (x.max() - x.min()))
        normalized_df = pd.concat([normalized_df, scaled_df], axis=1)
    return normalized_df


def choose_normalized_method(dataframe, method="linear_scaling"):
    if method == "linear_scaling":
        dataframe = dataframe.apply(lambda x: (x - x.min()) / (x.max() - x.min()))
    elif method == "z_score":
        dataframe = dataframe.apply(lambda x: (x - x.mean()) / x.std())
    elif method == "log_scaling":
        dataframe = dataframe.apply(np.log)
    else:
        pass
    return dataframe
