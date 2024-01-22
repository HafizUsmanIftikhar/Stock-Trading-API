"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.schemas import get_schema_view
from app.views import *


from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Stock Trading API",
        default_version='v1',
        description="API endpoints for stock trading",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('users/', CreateUserView.as_view(),name='create_user'),
    path('users/<str:username>/', GetUserView.as_view(),name='get_user'),
    path('stocks/', IngestStockDataView.as_view(),name='get_all_stock_data'),
    path('stocks/ingest/', get_all_stock_data,name='ingest_stock_data'),
    path('stocks/<str:ticker>/', get_stock_data,name='get_stock_data'),
    path('transactions/', CreateTransactionView.as_view(),name='create_transaction'),
    path('transactions/<int:user_id>/', GetUserTransactionsView.as_view(),name='get_user_transactions'),
    path('transactions/<int:user_id>/<str:start_timestamp>/<str:end_timestamp>/', get_user_transactions_by_timestamp,name='get_user_transactions_by_timestamp'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]