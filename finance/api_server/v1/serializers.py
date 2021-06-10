from collections import OrderedDict

from company.models import Company, CompanyType
from drf_queryfields import QueryFieldsMixin
from fundamentals.models import BalanceSheet, ComprehensiveIncome, YearSeasonTableInfo
from rest_framework import serializers
from stock.models import Stock
from taiex.models import Taiex


class TaiexSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Taiex
        fields = "__all__"


class YearSeasonSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = YearSeasonTableInfo
        exclude = ["id"]


class CompanyTypeSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = CompanyType
        fields = "__all__"


class CompanySerializer(QueryFieldsMixin, serializers.ModelSerializer):
    # company_type = CompanyTypeSerializer()

    class Meta:
        model = Company
        exclude = ["id"]
        depth = 1


class IncomeSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    year_season = YearSeasonSerializer()
    company = CompanySerializer()

    class Meta:
        model = ComprehensiveIncome
        exclude = ["id"]

    def to_representation(self, instance):
        result = super(IncomeSerializer, self).to_representation(instance)
        return OrderedDict(
            [(key, result[key]) for key in result if result[key] is not None]
        )


class BalanceSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    year_season = YearSeasonSerializer()
    company = CompanySerializer()

    class Meta:
        model = BalanceSheet
        exclude = ["id"]

    def to_representation(self, instance):
        result = super(BalanceSerializer, self).to_representation(instance)
        return OrderedDict(
            [(key, result[key]) for key in result if result[key] is not None]
        )


class StockSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Stock
        exclude = ["id", "company"]
