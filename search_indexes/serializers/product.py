import json

from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from search_indexes.product import ProductDoc

class ProdDocumentSerializer(DocumentSerializer):
    """Serializer for the Prod document."""

    class Meta(object):
        """Meta options."""

        # Specify the correspondent document class
        document = ProductDoc

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'category',
            'name',
            'slug',
            'description',
            'price',
            'stock',
        )