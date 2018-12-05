from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from search_indexes.viewsets import ProdDocumentView

router = DefaultRouter()
router.register(r'^',
                        ProdDocumentView,
                        base_name='proddocument')

urlpatterns = [
    url(r'^', include(router.urls)),
]