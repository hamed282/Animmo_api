import requests
# from adminpanel.models import IndexModel, SocialSettingModel
# from home.models import FeedbackModel, CategoryModel, HitsCountModel, TotalHitsModel
from uuid import getnode as get_mac_address
from datetime import timedelta
from django.utils import timezone


def send_otp_code_register(phone_number, code):
    url = "https://api.ghasedak.me/v2/verification/send/simple"
    payload = f"receptor={phone_number}&template=register&type=1&param1={code}"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'apikey': "36ff2f2d9fdeb043ccd9e71e54b29231f9910c831ad96fdc8df1b8b43f661ad8",
        'cache-control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


def send_otp_code_login(phone_number, code):
    url = "https://api.ghasedak.me/v2/verification/send/simple"
    payload = f"receptor={phone_number}&template=login&type=1&param1={code}"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'apikey': "36ff2f2d9fdeb043ccd9e71e54b29231f9910c831ad96fdc8df1b8b43f661ad8",
        'cache-control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# def hits_count(request):
#     ip = get_client_ip(request)
#     mac = get_mac_address()
#     try:
#         count = HitsCountModel.objects.get(ip=ip, mac=mac)
#         if count.updated + timedelta(hours=12) < timezone.now():
#             count.count += 1
#             count.save()
#         try:
#             total_count = TotalHitsModel.objects.get(date=timezone.now().date())
#             total_count.hits += 1
#             total_count.save()
#         except:
#             TotalHitsModel.objects.create(hits=1, date=timezone.now().date())
#     except:
#         HitsCountModel.objects.create(ip=ip, mac=mac, count=1)
#         try:
#             total_count = TotalHitsModel.objects.get(date=timezone.now().date())
#             total_count.hits += 1
#             total_count.save()
#         except:
#             TotalHitsModel.objects.create(hits=1, date=timezone.now().date())
#
#     # ip = get_client_ip(request)
#     # mac = get_mac_address()
#     # count = HitsCountModel.objects.get(ip=ip, mac=mac, created=datetime.now(), updated=datetime.now())
#     # print(count.updated)
#     # print(datetime.now())
#     # if (count.updated + timedelta(hours=12)) < datetime.now():
#     #     print(datetime.now())

