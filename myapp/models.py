from django.db import models

# Create your models here.

# quản lý tài khoản


# tài khoản
class TaiKhoan(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    link_anh_dai_dien = models.CharField(max_length=200)
    ngay_sinh = models.DateField()
    ngay_tao = models.DateField()

# TaiKhoan.objects.create(username='son12', password='123', link_anh_dai_dien='234234sf', ngay_sinh='2002-2-2', ngay_tao='2001-2-2')



# quản lý bạn bè

# quản lý sở thích,

# quản lý tương tác

#1 nhiều
# 1 sinh viên có thể có nhiều điểm
#nhiều nhiều
# 1 sinh viên có thể học nhiều lớp 1 lớp thì  có nhiều sinh viên học

#no sql



