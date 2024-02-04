from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class AuthMiddleware(MiddlewareMixin):
    """
        测试中间件，理解中间件原理
    """

    def process_request(self, request):
        # 如果是登录的页面，直接向后运行. ps 有些框架会组织静态文件的加载
        if request.path_info in ("/login/", "/static/"):
            return
        # 无返回值或返回None，继续向前走
        # 有返回值 redirect render httpre
        info_dict = request.session.get('info')
        if info_dict:
            # 将后面常用的用户信息直接存储在session中 后面使用用户信息直接  request.info即可获取用户信息
            request.info = info_dict
            return
        return redirect('/login/')
