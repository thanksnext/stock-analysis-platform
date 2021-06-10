import pytest
import pandas as pd
import numpy as np
from utils import normalize_dataframe
from pandas._testing import assert_frame_equal


test_df = pd.DataFrame(
    np.array(
        [
            [1000, 20, 102, 1, 1, 1, 1],
            [1000, 20, 102, 2, 2, 2, 2],
            [1000, 20, 102, 3, 3, 3, 3],
            [1000, 20, 103, 1, 1, 1, 1],
            [1000, 20, 103, 2, 2, 2, 2],
            [1000, 20, 103, 3, 3, 3, 3],
            [1001, 20, 102, 1, 4, 4, 4],
            [1001, 20, 102, 2, 5, 5, 5],
            [1001, 20, 102, 3, 6, 6, 6],
            [1001, 20, 103, 1, 4, 4, 4],
            [1001, 20, 103, 2, 5, 5, 5],
            [1001, 20, 103, 3, 6, 6, 6],
            [2303, 21, 102, 1, 7, 7, 7],
            [2303, 21, 102, 2, 8, 8, 8],
            [2303, 21, 102, 3, 9, 9, 9],
            [2303, 21, 103, 1, 7, 7, 7],
            [2303, 21, 103, 2, 8, 8, 8],
            [2303, 21, 103, 3, 9, 9, 9],
        ]
    ),
    columns=[
        "company_code",
        "company_type",
        "year",
        "season",
        "price_change",
        "test_col_1",
        "test_col_2",
    ],
)


class TestNormalizeDataframe:
    def test_normailze_dateframe_default(self):

        validate_df = pd.DataFrame(
            np.array(
                [
                    [1000, 20, 102, 1, 1, 0, 0],
                    [1000, 20, 102, 2, 2, 0.125, 0.125],
                    [1000, 20, 102, 3, 3, 0.25, 0.25],
                    [1000, 20, 103, 1, 1, 0, 0],
                    [1000, 20, 103, 2, 2, 0.125, 0.125],
                    [1000, 20, 103, 3, 3, 0.25, 0.25],
                    [1001, 20, 102, 1, 4, 0.375, 0.375],
                    [1001, 20, 102, 2, 5, 0.5, 0.5],
                    [1001, 20, 102, 3, 6, 0.625, 0.625],
                    [1001, 20, 103, 1, 4, 0.375, 0.375],
                    [1001, 20, 103, 2, 5, 0.5, 0.5],
                    [1001, 20, 103, 3, 6, 0.625, 0.625],
                    [2303, 21, 102, 1, 7, 0.75, 0.75],
                    [2303, 21, 102, 2, 8, 0.875, 0.875],
                    [2303, 21, 102, 3, 9, 1, 1],
                    [2303, 21, 103, 1, 7, 0.75, 0.75],
                    [2303, 21, 103, 2, 8, 0.875, 0.875],
                    [2303, 21, 103, 3, 9, 1, 1],
                ]
            ),
            columns=[
                "company_code",
                "company_type",
                "year",
                "season",
                "price_change",
                "test_col_1",
                "test_col_2",
            ],
        )

        result_df = normalize_dataframe(test_df, skip_col=["price_change"])

        assert_frame_equal(validate_df, result_df, check_dtype=False)

    def test_normailze_dateframe_groupby_company_type(self):

        validate_df = pd.DataFrame(
            np.array(
                [
                    [1000, 20, 102, 1, 1, 0, 0],
                    [1000, 20, 102, 2, 2, 0.2, 0.2],
                    [1000, 20, 102, 3, 3, 0.4, 0.4],
                    [1000, 20, 103, 1, 1, 0, 0],
                    [1000, 20, 103, 2, 2, 0.2, 0.2],
                    [1000, 20, 103, 3, 3, 0.4, 0.4],
                    [1001, 20, 102, 1, 4, 0.6, 0.6],
                    [1001, 20, 102, 2, 5, 0.8, 0.8],
                    [1001, 20, 102, 3, 6, 1, 1],
                    [1001, 20, 103, 1, 4, 0.6, 0.6],
                    [1001, 20, 103, 2, 5, 0.8, 0.8],
                    [1001, 20, 103, 3, 6, 1, 1],
                    [2303, 21, 102, 1, 7, 0, 0],
                    [2303, 21, 102, 2, 8, 0.5, 0.5],
                    [2303, 21, 102, 3, 9, 1, 1],
                    [2303, 21, 103, 1, 7, 0, 0],
                    [2303, 21, 103, 2, 8, 0.5, 0.5],
                    [2303, 21, 103, 3, 9, 1, 1],
                ]
            ),
            columns=[
                "company_code",
                "company_type",
                "year",
                "season",
                "price_change",
                "test_col_1",
                "test_col_2",
            ],
        )

        result_df = normalize_dataframe(
            test_df, company_type=True, skip_col=["price_change"]
        )

        assert_frame_equal(validate_df, result_df, check_dtype=False)

    def test_normailze_dateframe_groupby_year(self):

        validate_df = pd.DataFrame(
            np.array(
                [
                    [1000, 20, 102, 1, 1, 0, 0],
                    [1000, 20, 102, 2, 2, 0.125, 0.125],
                    [1000, 20, 102, 3, 3, 0.25, 0.25],
                    [1000, 20, 103, 1, 1, 0, 0],
                    [1000, 20, 103, 2, 2, 0.125, 0.125],
                    [1000, 20, 103, 3, 3, 0.25, 0.25],
                    [1001, 20, 102, 1, 4, 0.375, 0.375],
                    [1001, 20, 102, 2, 5, 0.5, 0.5],
                    [1001, 20, 102, 3, 6, 0.625, 0.625],
                    [1001, 20, 103, 1, 4, 0.375, 0.375],
                    [1001, 20, 103, 2, 5, 0.5, 0.5],
                    [1001, 20, 103, 3, 6, 0.625, 0.625],
                    [2303, 21, 102, 1, 7, 0.75, 0.75],
                    [2303, 21, 102, 2, 8, 0.875, 0.875],
                    [2303, 21, 102, 3, 9, 1, 1],
                    [2303, 21, 103, 1, 7, 0.75, 0.75],
                    [2303, 21, 103, 2, 8, 0.875, 0.875],
                    [2303, 21, 103, 3, 9, 1, 1],
                ]
            ),
            columns=[
                "company_code",
                "company_type",
                "year",
                "season",
                "price_change",
                "test_col_1",
                "test_col_2",
            ],
        )

        result_df = normalize_dataframe(test_df, year=True, skip_col=["price_change"])

        assert_frame_equal(validate_df, result_df, check_dtype=False)

    def test_normailze_dateframe_groupby_season(self):

        validate_df = pd.DataFrame(
            np.array(
                [
                    [1000, 20, 102, 1, 1, 0, 0],
                    [1000, 20, 102, 2, 2, 0, 0],
                    [1000, 20, 102, 3, 3, 0, 0],
                    [1000, 20, 103, 1, 1, 0, 0],
                    [1000, 20, 103, 2, 2, 0, 0],
                    [1000, 20, 103, 3, 3, 0, 0],
                    [1001, 20, 102, 1, 4, 0.5, 0.5],
                    [1001, 20, 102, 2, 5, 0.5, 0.5],
                    [1001, 20, 102, 3, 6, 0.5, 0.5],
                    [1001, 20, 103, 1, 4, 0.5, 0.5],
                    [1001, 20, 103, 2, 5, 0.5, 0.5],
                    [1001, 20, 103, 3, 6, 0.5, 0.5],
                    [2303, 21, 102, 1, 7, 1, 1],
                    [2303, 21, 102, 2, 8, 1, 1],
                    [2303, 21, 102, 3, 9, 1, 1],
                    [2303, 21, 103, 1, 7, 1, 1],
                    [2303, 21, 103, 2, 8, 1, 1],
                    [2303, 21, 103, 3, 9, 1, 1],
                ]
            ),
            columns=[
                "company_code",
                "company_type",
                "year",
                "season",
                "price_change",
                "test_col_1",
                "test_col_2",
            ],
        )

        result_df = normalize_dataframe(test_df, season=True, skip_col=["price_change"])

        assert_frame_equal(validate_df, result_df, check_dtype=False)

    def test_normailze_dateframe_groupby_year_season(self):

        validate_df = pd.DataFrame(
            np.array(
                [
                    [1000, 20, 102, 1, 1, 0, 0],
                    [1000, 20, 102, 2, 2, 0, 0],
                    [1000, 20, 102, 3, 3, 0, 0],
                    [1000, 20, 103, 1, 1, 0, 0],
                    [1000, 20, 103, 2, 2, 0, 0],
                    [1000, 20, 103, 3, 3, 0, 0],
                    [1001, 20, 102, 1, 4, 0.5, 0.5],
                    [1001, 20, 102, 2, 5, 0.5, 0.5],
                    [1001, 20, 102, 3, 6, 0.5, 0.5],
                    [1001, 20, 103, 1, 4, 0.5, 0.5],
                    [1001, 20, 103, 2, 5, 0.5, 0.5],
                    [1001, 20, 103, 3, 6, 0.5, 0.5],
                    [2303, 21, 102, 1, 7, 1, 1],
                    [2303, 21, 102, 2, 8, 1, 1],
                    [2303, 21, 102, 3, 9, 1, 1],
                    [2303, 21, 103, 1, 7, 1, 1],
                    [2303, 21, 103, 2, 8, 1, 1],
                    [2303, 21, 103, 3, 9, 1, 1],
                ]
            ),
            columns=[
                "company_code",
                "company_type",
                "year",
                "season",
                "price_change",
                "test_col_1",
                "test_col_2",
            ],
        )

        result_df = normalize_dataframe(
            test_df, year=True, season=True, skip_col=["price_change"]
        )

        assert_frame_equal(validate_df, result_df, check_dtype=False)

    def test_normailze_dateframe_groupby_company_type_year_season(self):

        validate_df = pd.DataFrame(
            np.array(
                [
                    [1000, 20, 102, 1, 1, 0, 0],
                    [1000, 20, 102, 2, 2, 0, 0],
                    [1000, 20, 102, 3, 3, 0, 0],
                    [1000, 20, 103, 1, 1, 0, 0],
                    [1000, 20, 103, 2, 2, 0, 0],
                    [1000, 20, 103, 3, 3, 0, 0],
                    [1001, 20, 102, 1, 4, 1, 1],
                    [1001, 20, 102, 2, 5, 1, 1],
                    [1001, 20, 102, 3, 6, 1, 1],
                    [1001, 20, 103, 1, 4, 1, 1],
                    [1001, 20, 103, 2, 5, 1, 1],
                    [1001, 20, 103, 3, 6, 1, 1],
                    [2303, 21, 102, 1, 7, np.nan, np.nan],
                    [2303, 21, 102, 2, 8, np.nan, np.nan],
                    [2303, 21, 102, 3, 9, np.nan, np.nan],
                    [2303, 21, 103, 1, 7, np.nan, np.nan],
                    [2303, 21, 103, 2, 8, np.nan, np.nan],
                    [2303, 21, 103, 3, 9, np.nan, np.nan],
                ]
            ),
            columns=[
                "company_code",
                "company_type",
                "year",
                "season",
                "price_change",
                "test_col_1",
                "test_col_2",
            ],
        )

        result_df = normalize_dataframe(
            test_df,
            company_type=True,
            year=True,
            season=True,
            skip_col=["price_change"],
        )

        assert_frame_equal(validate_df, result_df, check_dtype=False)
