from rest_framework.views import APIView
from rest_framework.response import Response
import random
from utils import send_otp_code_register, send_otp_code_login
from .models import OtpCode, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from convert_numbers import persian_to_english
from .serializers import UserSerializer, OtpCodeRegisterSerializer, OtpCodeLoginSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserRegisterView(APIView):

    def post(self, request):
        """
        parameters:
        1. first_name
        2. last_name
        3. phone_number
        4. deaf
        """
        form = request.data
        ser_data = UserSerializer(data=form)
        if ser_data.is_valid():
            phone_number = persian_to_english(form['phone_number'])
            user = User.objects.filter(phone_number=phone_number).exists()
            if not user:
                request.session['register_information'] = {'first_name': form['first_name'],
                                                           'last_name': form['last_name'],
                                                           'phone_number': phone_number,
                                                           'deaf': form['deaf']}
                code = random.randint(10000, 99999)
                send_otp_code_register(form['phone_number'], code)
                if OtpCode.objects.filter(phone_number=phone_number).exists():
                    OtpCode.objects.get(phone_number=phone_number).delete()
                OtpCode.objects.create(phone_number=phone_number, code=code)
                return Response(data=(ser_data.data, {'massage': 'کد یکبار مصرف ارسال شد!'}), status=status.HTTP_200_OK)

        else:
            return Response(data=({'massage': 'این شماره تلفن قبلا ثبت شده است!'}), status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


class RegisterVerifyCodeView(APIView):
    # def get(self, request):
    #     phone_number = request.session['register_information']['phone_number']
    #     return Response(data={'phone_number': phone_number}, status=status.HTTP_200_OK)

    def post(self, request):
        """
        parameters:
        1. phone_number
        2. code
        3. first_name
        4. last_name
        5. deaf
        """
        form = request.data
        ser_data = OtpCodeRegisterSerializer(data=form)
        if ser_data.is_valid():
            # register_info = request.session['register_information']

            if not OtpCode.objects.filter(phone_number=form['phone_number']).exists():
                return Response(data={'massage': 'کد یکبار مصرف اشتباه است!', 'status': '203'}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            code_instance = OtpCode.objects.get(phone_number=form['phone_number'])
            if int(code_instance.code) == int(persian_to_english(form['code'])):
                User.objects.create_user(first_name=form['first_name'], last_name=form['last_name'],
                                         phone_number=form['phone_number'], deaf=form['deaf'])
                code_instance.delete()

                try:
                    user = User.objects.get(phone_number=form['phone_number'])
                    token_access = AccessToken.for_user(user)
                    token_refresh = RefreshToken.for_user(user)
                    return Response(data={'massage': 'ورود با موفقیت انجام شد!',
                                          'access': str(token_access),
                                          'refresh': str(token_refresh)},
                                    status=status.HTTP_200_OK)
                except:
                    user = None

                return Response(data=(ser_data.data, {'massage': 'ثبت نام با موفقیت انجام شد!', 'status': '201'}), status=status.HTTP_201_CREATED)
            else:
                return Response(data={'massage': 'کد یکبار مصرف اشتباه است!', 'status': '203'}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        else:
            return Response(data=({'massage': 'کد یکبار مصرف اشتباه است!', 'status': '203'}), status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


class UserLoginView(APIView):
    def post(self, request):
        """
        parameters:
        1. phone_number
        """
        form = request.data
        phone_number = persian_to_english(form['phone_number'])
        code = random.randint(10000, 99999)

        if User.objects.filter(phone_number=phone_number).exists():
            send_otp_code_login(phone_number=phone_number, code=code)
        else:
            return Response(data={'massage': 'این شماره تلفن ثبت نشده است!'}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        if OtpCode.objects.filter(phone_number=phone_number).exists():
            OtpCode.objects.get(phone_number=phone_number).delete()
        OtpCode.objects.create(phone_number=phone_number, code=code)
        request.session['phone_number'] = phone_number
        return Response(data={'massage': 'کد یکبار مصرف ارسال شد!', 'phone_number': phone_number}, status=status.HTTP_200_OK)


class UserLoginVerifyView(APIView):
    # def get(self, request):
    #     phone_number = request.session['phone_number']
    #     return Response(data={'phone_number': phone_number})

    def post(self, request):
        """
        parameters:
        1. phone_number
        2. code

        """
        form = request.data
        ser_data = OtpCodeLoginSerializer(data=form)
        if ser_data.is_valid():
            code = form['code']
            phone_number = persian_to_english(form['phone_number'])
            if not OtpCode.objects.filter(phone_number=phone_number).exists():
                return Response(data={'massage': 'کد یکبار مصرف اشتباه است!'}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            code_instance = OtpCode.objects.get(phone_number=phone_number)
            try:
                user = User.objects.get(phone_number=phone_number)
                if int(code_instance.code) == int(code):
                    token_access = AccessToken.for_user(user)
                    token_refresh = RefreshToken.for_user(user)
                    code_instance.delete()
                    return Response(data={'massage': 'ورود با موفقیت انجام شد!',
                                          'access': str(token_access),
                                          'refresh': str(token_refresh)},
                                    status=status.HTTP_200_OK)
                else:
                    return Response(data={'massage': 'کد یکبار مصرف اشتباه است!'}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            except:
                user = None

        return Response(data={'massage': 'کد یکبار مصرف اشتباه است!'}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


class UserLogout(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
