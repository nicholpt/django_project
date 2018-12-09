from django.conf.urls import url
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views
from shop import views as shop_views

#url.py is needed for django to know what url directs to which module/function/class
urlpatterns = [
    url(r'^$', PostListView.as_view(), name='store-home'),
    url(r'home/$', PostListView.as_view(), name='store-home'),
    url(r'about/$', views.about, name='store-about'),
    url(r'shop/$', shop_views.product_list),
]
