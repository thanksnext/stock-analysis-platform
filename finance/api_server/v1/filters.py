from company.models import Company
from django_filters import rest_framework as filters
from fundamentals.models import BalanceSheet, ComprehensiveIncome, YearSeasonTableInfo
from stock.models import Stock
from taiex.models import Taiex


def split_year_season(year_season_str):
    value_list = list(filter(None, year_season_str.split("-")))
    year = value_list[0]
    season = value_list[1]
    return year, season


def find_id_by_year_season(year, season, targetObj):
    for yearSeasonObj in targetObj:
        if (
            yearSeasonObj["fields"]["year"] == year
            and yearSeasonObj["fields"]["season"] == season
        ):
            return yearSeasonObj["pk"]
    return 0


def find_year_season_by_id(id, targetObj):
    for yearSeasonObj in targetObj:
        if yearSeasonObj["pk"] == id:
            return yearSeasonObj["fields"]["year"], yearSeasonObj["fields"]["season"]
    return 0, 0


class TaiexFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name="trade_date", lookup_expr="gte")
    end_date = filters.DateFilter(field_name="trade_date", lookup_expr="lte")

    class Meta:
        model = Taiex
        fields = ["start_date", "end_date"]


class IncomeFilter(filters.FilterSet):
    start_date_year_season = filters.CharFilter(method="filter_year_season_id")
    end_date_year_season = filters.CharFilter(method="filter_year_season_id")

    class Meta:
        model = ComprehensiveIncome
        fields = ["start_date_year_season", "end_date_year_season"]

    def filter_year_season_id(self, queryset, name, value):
        value_list = list(filter(None, value.split("-")))
        year = value_list[0]
        season = value_list[1]
        date_id = list(
            YearSeasonTableInfo.objects.filter(year=year).filter(season=season)
        )[0].id

        if name == "start_date_year_season":
            return queryset.filter(year_season_id__gte=date_id)
        else:
            return queryset.filter(year_season_id__lte=date_id)


class BalanceFilter(filters.FilterSet):
    start_date_year_season = filters.CharFilter(method="filter_year_season_id")
    end_date_year_season = filters.CharFilter(method="filter_year_season_id")

    class Meta:
        model = BalanceSheet
        fields = ["start_date_year_season", "end_date_year_season"]

    def filter_year_season_id(self, queryset, name, value):
        value_list = list(filter(None, value.split("-")))
        year = value_list[0]
        season = value_list[1]
        date_id = list(
            YearSeasonTableInfo.objects.filter(year=year).filter(season=season)
        )[0].id

        if name == "start_date_year_season":
            return queryset.filter(year_season_id__gte=date_id)
        else:
            return queryset.filter(year_season_id__lte=date_id)

    def filter_company_id(self, queryset, name, value):
        company_id = list(Company.objects.filter(company_code=value))[0].id
        return queryset.filter(company_id=company_id)


class StockFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name="trade_date", lookup_expr="gte")
    end_date = filters.DateFilter(field_name="trade_date", lookup_expr="lte")

    class Meta:
        model = Stock
        fields = ["start_date", "end_date"]
