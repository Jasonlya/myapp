from django.shortcuts import render, redirect
from django import forms
from django.core.validators import RegexValidator
from myapp2 import models
from django.views.decorators.clickjacking import xframe_options_exempt


# Create your views here.
class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "请输入用户名"}),
        validators=[RegexValidator(r'^\w{3,}$', '用户名格式错误')]
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "请输入密码"})
    )

    # 默认get请求


def login(request):
    """ 例如：用户名、密码 -> 数据库校验"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 校验成功拿到字典 form.cleaned_data -> {'username': '3213', 'password': '12321'}
        # 去数据库中校验，用户名和密码的合法性
        # user_object = models.UserInfo.objects.filter(name=form.cleaned_data['username'],password=form.cleaned_data['password']).first()
        user_object = models.UserInfo.objects.filter(**form.cleaned_data).first()
        if user_object:
            # 如果成功
            """
                1.生成随机字符串
                2.返回到用户浏览器的cookie中
                3.存储到网站的session中 随机字符串+用户标识
            """
            request.session["info"] = {"id": user_object.id, "name": user_object.username}
            return redirect('/home/')
        else:
            # 如果失败，展示错误信息
            return render(request, "login.html", {"form": form, 'error': "用户名或密码错误"})
    else:
        return render(request, 'login.html', {'form': form})
    """老方法，改进为上面form表单方法"""
    # # 判断是get请求还是post请求
    # if request.method == "POST":
    #     # 去请求体中获取数据，再进行校验
    #     username = request.POST.get('username')
    #     password = request.POST.get('pwd')
    #     # 去数据库中校验，用户名和密码的合法性
    #     user_object = models.UserInfo.objects.filter(name=username, password=password).first()
    #     if user_object:
    #         # 如果成功
    #         """
    #             1.生成随机字符串
    #             2.返回到用户浏览器的cookie中
    #             3.存储到网站的session中 随机字符串+用户标识
    #         """
    #         request.session["info"] = {"id": user_object.id, "name": user_object.name}
    #         return redirect('/index/')
    #     else:
    #         # 如果失败，展示错误信息
    #         return render(request, "login.html", {"error": "用户名或密码错误"})
    # return render(request, "login.html")


def home(request):
    return render(request, 'home.html')


def testdatas(request):
    return render(request, 'testdatas.html')
