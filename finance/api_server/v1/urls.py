from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from .views import (
    BalanceViewSet,
    CompanyTypeViewSet,
    CompanyViewSet,
    IncomeViewSet,
    StockViewSet,
    TaiexViewSet,
)

stock_list = StockViewSet.as_view({"get": "list"})
income_list = IncomeViewSet.as_view({"get": "list"})
balance_list = BalanceViewSet.as_view({"get": "list"})


router = DefaultRouter()
router.register("taiex", TaiexViewSet)
router.register("company", CompanyViewSet, basename="company")
router.register("company_type", CompanyTypeViewSet, basename="company_type")

urlpatterns = [
    path("", include(router.urls)),
    # path("stock/<int:company_code>/", StockViewSet.as_view(), name="stock-list"),
    path("stock/<int:company_code>/", stock_list, name="stock-list"),
    path("income/<int:company_code>/", income_list, name="income-list"),
    path("balance/<int:company_code>/", balance_list, name="balance-list"),
]

schema_view = get_schema_view(
    openapi.Info(
        title="TAIEX Fundamental Data API",
        default_version="v1",
        description="description",
        terms_of_service="localhost:8000/",
        contact=openapi.Contact(email="kent_chen@finance.com"),
        license=openapi.License(name="NAN"),
    ),
    patterns=[
        path("api/v1/auth/", include("djoser.urls")),
        path("api/v1/auth/", include("djoser.urls.jwt")),
        path("api/v1/", include("api_server.v1.urls")),
    ],
    public=True,
    # permission_classes=(permissions.AllowAny,),
)
urlpatterns += [
    path(
        r"swagger<format>",
        schema_view.with_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        r"swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
