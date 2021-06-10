from company.models import Company, CompanyType
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from fundamentals.models import BalanceSheet, ComprehensiveIncome
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    # api_view,
    permission_classes,
    # renderer_classes,
    # parser_classes,
)

# from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from stock.models import Stock
from taiex.models import Taiex

# from django.shortcuts import render
from .filters import BalanceFilter, IncomeFilter, StockFilter, TaiexFilter
from .serializers import (
    BalanceSerializer,
    CompanySerializer,
    CompanyTypeSerializer,
    IncomeSerializer,
    StockSerializer,
    TaiexSerializer,
)


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_summary="Taiex index",
        operation_description="Return the info. of Taiex",
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_summary="Taiex by date",
        operation_description="Return  a specified trading date of taiex ",
    ),
)
class TaiexViewSet(ReadOnlyModelViewSet):
    queryset = Taiex.objects.all().order_by("trade_date")
    serializer_class = TaiexSerializer
    # permission_classes = (IsAuthenticated,)
    filterset_class = TaiexFilter


@permission_classes([IsAuthenticated])
class IncomeViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = IncomeSerializer
    filterset_class = IncomeFilter

    @swagger_auto_schema(
        operation_summary="Comprehensive income",
        operation_description="Return the comprehensive income info. of a specified company",
    )
    def list(self, request, company_code, *args, **kwargs):
        self.queryset = ComprehensiveIncome.objects.filter(
            company__company_code=company_code
        )
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class BalanceViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = BalanceSerializer
    filterset_class = BalanceFilter

    @swagger_auto_schema(
        operation_summary="Balance sheet",
        operation_description="Return the balance sheet info. of a specified company",
    )
    def list(self, request, company_code, *args, **kwargs):
        self.queryset = BalanceSheet.objects.filter(company__company_code=company_code)
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_summary="Company",
        operation_description="Return a list of company",
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_summary="A specified company",
        operation_description="Return a specified company",
    ),
)
class CompanyViewSet(ReadOnlyModelViewSet):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = "company_code"
    filterset_fields = ["company_type"]
    # permission_classes = (IsAuthenticated,)


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_summary="Company type",
        operation_description="Return a list of company type",
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_summary="A specified company type",
        operation_description="Return a specified company type",
    ),
)
class CompanyTypeViewSet(ReadOnlyModelViewSet):

    queryset = CompanyType.objects.all()
    serializer_class = CompanyTypeSerializer
    # permission_classes = (IsAuthenticated,)


# class StockViewSet(ListAPIView):
class StockViewSet(GenericViewSet):

    serializer_class = StockSerializer
    filterset_class = StockFilter
    # permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_summary="Stock index",
        operation_description="Return the stock info of a specified company",
    )
    def list(self, request, company_code, *args, **kwargs):
        self.queryset = Stock.objects.filter(company__company_code=company_code)
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
