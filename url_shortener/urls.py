from django.urls import path, include
from .views import UrlList, UrlDetail, FindOriginalUrl, UrlDelete

urlpatterns = [
    path('', UrlList.as_view(), name='main_page'),
    path('<str:short_url>/', FindOriginalUrl.as_view(), name='find_original_url'),
    path('detail/<int:pk>/', UrlDetail.as_view(), name='url_detail'),
    path('delete/<int:pk>/', UrlDelete.as_view(), name='url_delete'),
]