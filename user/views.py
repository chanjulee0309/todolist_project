from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer


class UserView(APIView):
    def get(self, request):
        return Response(UserSerializer(request.user).data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def put(self, request):
        return Response({'message':'put 요청입니다!'})

    def delete(self, request):
        return Response({'message':'delete 요청입니다!'})

class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(**request.data)

        if not user:
            return Response({'message': '존재하지 않는 아이디 혹은 잘못된 비밀번호를 입력하셨습니다.'})

        login(request, user)

        return Response({'message':'로그인 성공!!'})

class UserLogoutView(APIView):
    def post(self, request):

        logout(request)

        return Response({'message':'logout 요청입니다!'})
