from rest_framework.views import APIView
from rest_framework.response import Response

from todo.serializers import TodoSerializer
from todo.models import Todo

# Create your views here.
class TodoView(APIView):
    def get(self, request, pk=None):
        """pk 값의 유무에 따라 todo 목록 혹은 todo의 상세 정보를 response 합니다."""
        if pk:
            obj = Todo.objects.get(pk=pk)
            return Response(TodoSerializer(obj).data)
        
        queryset = Todo.objects.filter(user=request.user)
        return Response(TodoSerializer(queryset, many=True).data)

    def post(self, request):
        """내용을 입력받아 todo를 생성합니다."""
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data)

    def put(self, request, pk):
        """todo를 수정합니다."""
        obj = Todo.objects.get(pk=pk)
        serializer = TodoSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message':'put 요청입니다!'})

    def delete(self, request):
        """Todo를 삭제합니다."""
        Todo.objects.get(pk=pk).delete()

        return Response({'message':'delete 요청입니다!'})

class TodoCompletView(APIView):
    def put(self, request, pk):
        """지정 된 todo를 complete 합니다."""
        obj = Todo.objects.get(pk=pk)
        obj.complete()

        return Response({'message':'todo 완료'})
