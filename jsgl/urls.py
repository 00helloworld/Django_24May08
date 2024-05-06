"""jxc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import  views
urlpatterns = [
    path('admin/', admin.site.urls),

    # 测试初始化
    path('init_data', views.init_data),
    path('init_qiandao_data', views.init_qiandao_data),
    path('qiandao/qiandao_data', views.qiandao_data),

    #主页
    path('login/', views.login),
    path('out/', views.out),
    path('home', views.home),
    ###管理员维护
    #管理员添加
    path('gly/glyadd', views.glyadd),
    # 管理员列表
    path('gly/glylist', views.glylist),
    # 管理员修改页面
    path('gly/glymodify', views.glymodify),
    # 管理员详情页面
    path('gly/glydetail', views.glydetail),
    # 管理员删除
    path('gly/glydelete', views.glydelete),

    path('gly/glymod', views.glymod),
    ###教师维护
    #教师添加
    path('jiaoshi/jiaoshiadd', views.jiaoshiadd),
    # 教师列表
    path('jiaoshi/jiaoshilist', views.jiaoshilist),
    # 教师修改页面
    path('jiaoshi/jiaoshimodify', views.jiaoshimodify),
    # 教师详情页面
    path('jiaoshi/jiaoshidetail', views.jiaoshidetail),
    # 教师删除
    path('jiaoshi/jiaoshidelete', views.jiaoshidelete),
    path('jiaoshi/jiaoshimod', views.jiaoshimod),

    ###学生维护
    #学生添加
    path('xuesheng/xueshengadd', views.xueshengadd),
    # 学生列表
    path('xuesheng/xueshenglist', views.xueshenglist),
    # 学生修改页面
    path('xuesheng/xueshengmodify', views.xueshengmodify),
    # 学生详情页面
    path('xuesheng/xueshengdetail', views.xueshengdetail),
    # 学生删除
    path('xuesheng/xueshengdelete', views.xueshengdelete),

    path('xuesheng/xueshengmod', views.xueshengmod),

    ###教室信息维护
    #教室信息添加
    path('jsxx/jsxxadd', views.jsxxadd),
    # 教室信息列表
    path('jsxx/jsxxlist', views.jsxxlist),
    # 教室信息修改页面
    path('jsxx/jsxxmodify', views.jsxxmodify),
    # 教室信息详情页面
    path('jsxx/jsxxdetail', views.jsxxdetail),
    # 教室信息删除
    path('jsxx/jsxxdelete', views.jsxxdelete),

    path('jsxx/jsxxdata', views.jsxxdata),

    ###星期维护
    #星期添加
    path('xingqi/xingqiadd', views.xingqiadd),
    # 星期列表
    path('xingqi/xingqilist', views.xingqilist),
    # 星期修改页面
    path('xingqi/xingqimodify', views.xingqimodify),
    # 星期详情页面
    path('xingqi/xingqidetail', views.xingqidetail),
    # 星期删除
    path('xingqi/xingqidelete', views.xingqidelete),

    ###时间段维护
    #时间段添加
    path('sjd/sjdadd', views.sjdadd),
    # 时间段列表
    path('sjd/sjdlist', views.sjdlist),
    # 时间段修改页面
    path('sjd/sjdmodify', views.sjdmodify),
    # 时间段详情页面
    path('sjd/sjddetail', views.sjddetail),
    # 时间段删除
    path('sjd/sjddelete', views.sjddelete),

    ###课程维护
    #课程添加
    path('kecheng/kechengadd', views.kechengadd),
    # 课程列表
    path('kecheng/kechenglist', views.kechenglist),
    # 课程修改页面
    path('kecheng/kechengmodify', views.kechengmodify),
    # 课程详情页面
    path('kecheng/kechengdetail', views.kechengdetail),
    # 课程删除
    path('kecheng/kechengdelete', views.kechengdelete),

    ###上课时间维护
    #上课时间添加
    path('sksj/sksjadd', views.sksjadd),
    # 上课时间列表
    path('sksj/sksjlist', views.sksjlist),
# 上课时间列表
    path('sksj/kebiao', views.kebiao),
    # 上课时间修改页面
    path('sksj/sksjmodify', views.sksjmodify),
    # 上课时间详情页面
    path('sksj/sksjdetail', views.sksjdetail),
    # 上课时间删除
    path('sksj/sksjdelete', views.sksjdelete),

    # 上课时间列表
    path('sksj/sksjmylist', views.sksjmylist),




    ###签到维护
    #签到添加
    path('qiandao/qiandaoadd', views.qiandaoadd),
    path('qiandao/generate_qiandao', views.generate_qiandao),
    path('qiandao/add_qiandao', views.add_qiandao),
    # 签到列表
    path('qiandao/qiandaolist', views.qiandaolist),
    # 我的签到列表
    path('qiandao/qiandaomylist', views.qiandaomylist),
    # 签到修改页面
    path('qiandao/qiandaomodify', views.qiandaomodify),
    # 签到详情页面
    path('qiandao/qiandaodetail', views.qiandaodetail),
    # 签到删除
    path('qiandao/qiandaodelete', views.qiandaodelete),

    path('qiandao/qiandaoqiantui', views.qiandaoqiantui),

    ###教室借用维护
    #教室借用添加
    path('jsjy/jsjyadd', views.jsjyadd),
    # 教室借用列表
    path('jsjy/jsjylist', views.jsjylist),
# 教室借用列表
    path('jsjy/jsjymylist', views.jsjymylist),
    # 教室借用修改页面
    path('jsjy/jsjymodify', views.jsjymodify),
    # 教室借用详情页面
    path('jsjy/jsjydetail', views.jsjydetail),
    # 教室借用删除
    path('jsjy/jsjydelete', views.jsjydelete),

    path('jsjy/jsjyfinish', views.jsjyfinish),


    path('jsjy/jsjytj', views.jsjytj),

    path('', views.login),  # 当访问根URL时，将调用home视图
]
