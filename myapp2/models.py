from django.db import models


# Create your models here.
class UserInfo(models.Model):
    # id列是自动生成的，自增的，默认是主键
    # id = models.AutoField()
    username = models.CharField(verbose_name="姓名", max_length=20)
    # password是后添加的一列，需要默认以前的数据这列是可以为空，或者设置为默认值
    # 不设置默认值或者为空，直接执行的话，会有提示 1.django提示你输入默认值，2.退出
    password = models.CharField(verbose_name="密码", max_length=10, default=None)
    age = models.IntegerField(verbose_name="年龄", null=True)
    phonenum = models.IntegerField(verbose_name="手机号", null=True)
    email = models.CharField(verbose_name="邮箱", max_length=255, null=True)
    # 表关联  级联删除 on_delete=models.CASCADE    级联为空 on_delete=models.SET_NULL,null=True,blank=True
    depart = models.ForeignKey(verbose_name="关联部门", to="Depart", on_delete=models.CASCADE)


"""
新增
    新增单条
    models.UserInfo.objects.creat(name="xx",password="xx",..)
    models.UserInfo.objects.creat(**{"name":"xx","password":"xx",..})
    #新增多条
    depat_list = [
        models.Depart(departid=2,departname="新增部门2",count=30),
        models.Depart(departid=3, departname="新增部门3", count=40)
    ]
    models.Depart.objects.bulk_create(depat_list)
查询
    v1 = models.UserInfo.objects.filter(name="xx",age=xx)
    查询结果 v1 = [obj,obj..]

    v2 = models.UserInfo.objects.all()
    查询结果 v2 = [obj,obj..]
    注意：未查询到数据时候返回空列表，IF 判断空列表依然返回 FALSE

    v3 = models.UserInfo.objects.filter(name="xx",age=xx).first()
    查询结果为单条数据  v3 = obj
    注意：未查询到数据时候返回None

删除
    models.UserInfo.all().delete()
    models.UserInfo.objects.filter(name="xx",age=xx).delete()

修改
    models.UserInfo.all().update(age=19)
    models.UserInfo.objects.filter(name="xx",age=xx).update(age=19)
"""


class Depart(models.Model):
    departid = models.IntegerField(primary_key=True)
    departname = models.CharField(verbose_name="部门名称", max_length=50)
    count = models.IntegerField(verbose_name="人数")
