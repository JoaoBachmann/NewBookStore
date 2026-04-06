from rest_framework.viewsets import ModelViewSet

from core.models.livro import Livro
from core.serializers.livro import LivroListRetrieveSerializer, LivroListSerializer, LivroSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return LivroListSerializer
        elif self.action == 'retrieve':
            return LivroListRetrieveSerializer
        return LivroSerializer
