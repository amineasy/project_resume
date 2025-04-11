from random import random

from django.contrib.auth import get_user_model
from django.core.signing import TimestampSigner
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from yaml import serializer
from project_resume.apps.accounts.serializers.admin import *
from django.core.mail import send_mail


User = get_user_model()

class RegisterApiView(APIView):


    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)









class SendEmailPassword(APIView):
    def post(self, request):
        serializer = PasswordRestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'چنین ایمیلی برای کاربر پیدا نشد'},status=status.HTTP_404_NOT_FOUND)


            code = random.randint(10000, 99999)



            send_mail(
                'کد تایید بازیابی رمز عبور',
                f'کد تایید شما: {code}',
                'amineasydjango@gmail.com',
                [email],
                fail_silently=False
            )

            request.session['reset_code'] = code
            request.session['reset_email'] = email
            return Response({'message': 'کد تایید به ایمیل ارسال شد'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











class VerifyRestCode(APIView):
    def post(self, request):
        code = request.session.get('reset_code')
        email = request.session.get('reset_email')
        serializer = VerifyCodeSerializer(data=request.data)
        if serializer.is_valid():
            entered_code = serializer.validated_data['code']
            if str(entered_code) == str(code):
                request.session.pop('reset_code', None)  # حذف برای امنیت
                request.session['allow_password_reset'] = True
                return Response({'message': 'کد تایید صحیح است، حالا می‌تونی رمزتو عوض کنی'}, status=200)
            else:
                return Response({'error': 'کد تایید اشتباهه'}, status=400)

        return Response(serializer.errors, status=400)




class NewPassword(APIView):
    pass
