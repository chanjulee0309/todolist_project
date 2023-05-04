from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class TodoView(APIView):
    def get(self, request, pk=None):
        return Response({'message':'get 요청입니다!'})

    def post(self, request):
        return Response({'message':'post 요청입니다!'})

    def put(self, request):
        return Response({'message':'put 요청입니다!'})

    def delete(self, request):
        return Response({'message':'delete 요청입니다!'})

class TodoCompletView(APIView):
    def put(self, request):
        return Response({'message':'todo 완료'})
