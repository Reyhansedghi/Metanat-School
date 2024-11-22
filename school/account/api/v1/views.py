from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from account.models import User
from rest_framework.response import Response
from rest_framework import status, generics,permissions
from rest_framework_simplejwt.tokens import RefreshToken
from . serializers import (RegisterSerializer,ProfileSerializer)
from django.shortcuts import get_object_or_404
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        # Serialize داده‌های ورودی
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # ثبت‌نام کاربر و ذخیره آن در دیتابیس
            user = serializer.save()

            # ایجاد توکن برای کاربر جدید
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # Refresh ایجاد توکن
            refresh_token = str(refresh)

            return Response({
                "info": "user created and logged in",
                "access": access_token,
                "refresh": refresh_token 
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    #مشاهده اطلاعات کاربری،تغییر و دیلیت اکانت
    serializer_class=ProfileSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return get_object_or_404(User,id=user.id)
    
    def get(self, request, *args, **kwargs):
        user = self.get_queryset()
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        user = self.get_queryset()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = self.get_queryset()
        user.delete()
        return Response(status.HTTP_204_NO_CONTENT)