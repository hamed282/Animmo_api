from django.db import models
from accounts.models import User
from course.models import CourseModel


class UserCourseModel(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_user')
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='rel_course')
    spotplayer_license = models.CharField(max_length=512)
    price = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    # referral_code = models.ForeignKey(DiscountModel, on_delete=models.CASCADE, related_name='rel_discount')

    def __str__(self):
        return f'{self.user} - {self.course}'
