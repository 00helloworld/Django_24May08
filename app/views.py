from django.shortcuts import render,HttpResponse,redirect
from app import models

import random
import string
import base64
from io import BytesIO
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

from django.db.models import Sum
from django.db.models import Count
from django.contrib import messages
# Create your views here.

from datetime import *

#系统首页
def main(request):
    return render(request, "main.html")

#登录首页
def login(request):
    if request.method == 'GET':
            return render(request, "login.html")
    if request.method == 'POST':
        yhm = request.POST.get('yhm')  # 用户名
        mm = request.POST.get('mm')  # 密码

        qx = request.POST.get('qx')  # 密码
        if qx == "学生":
            res = models.xuesheng.objects.filter(yhm=yhm, mm=mm).count()
        if qx == "教师":
            res = models.jiaoshi.objects.filter(yhm=yhm, mm=mm).count()
        if qx == "管理员":
            res = models.gly.objects.filter(yhm=yhm, mm=mm).count()
        if res == 0:
               messages.success(request, "操作失败、用户名和密码不匹配")
               return redirect('/login')
        elif res > 0:
            if qx == "学生":
                obj = models.xuesheng.objects.filter(yhm=yhm, mm=mm).first()
                request.session['id'] = obj.id
                request.session['yhm'] = yhm
            if qx == "教师":
                obj = models.jiaoshi.objects.filter(yhm=yhm, mm=mm).first()
                request.session['id'] = obj.id
                request.session['yhm'] = yhm
            if qx == "管理员":
                obj = models.gly.objects.filter(yhm=yhm, mm=mm).first()
                request.session['id'] = obj.id
            request.session['yhm'] = yhm
            request.session['mm'] = mm
            request.session['qx'] = qx


        return redirect('/sksj/kebiao')

def out(request):
    request.session['id'] = ''
    request.session['yhm'] = ""
    request.session['mm'] =""
    request.session['qx'] = ""
    request.session.flush()

    return redirect('/login')

#添加管理员
def glyadd(request):
   if request.method == 'GET':
       return render(request, "gly/glyadd.html")
   if request.method == 'POST':
        yhm = request.POST.get('yhm') #用户名
        mm = request.POST.get('mm') #密码
        xm = request.POST.get('xm') #姓名

        res = models.gly.objects.filter(yhm=yhm).count();
        if res > 0:
            messages.success(request, "操作失败、用户名重复")
        elif res == 0:
            messages.success(request, "操作成功")
            models.gly.objects.create(yhm=yhm, mm=mm, xm=xm, )


        #return render(request, "gly/glyadd.html")
        return redirect('/gly/glyadd')

#管理员列表
def glylist(request):
    print(request.method)
    global list
    if request.method == 'GET':

        yhm= request.GET.get('yhm')#用户名
        if not yhm:
            yhm = ""
        print(yhm)
        list = models.gly.objects.filter(yhm__icontains=yhm).all()  # 获取gly表所有的数据
    return render(request, "gly/glylist.html", {'list': list})
#修改管理员
def glymodify(request):
    # 获取要修改的数据的id
    if request.method == 'GET':
        id = request.GET.get('id')
        obj = models.gly.objects.get(id=id)
        return render(request, 'gly/glymodify.html', {'obj': obj})

    id = request.POST.get('id')
    yhm = request.POST.get('yhm') #用户名
    mm = request.POST.get('mm') #密码
    xm = request.POST.get('xm') #姓名
    messages.success(request, "操作成功")
    ret = models.gly.objects.filter(id=id).update(yhm=yhm,mm=mm,xm=xm, )

    return redirect('/gly/glylist')

#修改管理员
def glymod(request):
    # 获取要修改的数据的id
    if request.method == 'GET':
        id = request.session.get('id')
        obj = models.gly.objects.get(id=id)
        return render(request, 'gly/modify.html', {'obj': obj})

    id = request.POST.get('id')
    yhm = request.POST.get('yhm') #用户名
    mm = request.POST.get('mm') #密码
    xm = request.POST.get('xm') #姓名
    messages.success(request, "操作成功")
    ret = models.gly.objects.filter(id=id).update(yhm=yhm,mm=mm,xm=xm, )

    return redirect('/gly/glymod')

# 管理员详情
def glydetail(request):
    # 获取要修改的数据的id
    id = request.GET.get('id')
    obj = models.gly.objects.get(id=id)
    return render(request, 'gly/glydetail.html', {'obj': obj})

#管理员删除
def glydelete(request):
    # 获取要删除数据的id
    id = request.GET.get('id')
    # 查询数据库是否存在
    obj = models.gly.objects.get(id=id)
    if obj:
        # 在数据库中删除
        obj.delete()
        messages.success(request, "操作成功")
        return redirect('/gly/glylist')
    return HttpResponse("删除失败")

#添加教师
def jiaoshiadd(request):
   if request.method == 'GET':
       return render(request, "jiaoshi/jiaoshiadd.html")
   if request.method == 'POST':
        yhm = request.POST.get('yhm') #用户名
        mm = request.POST.get('mm') #密码
        xm = request.POST.get('xm') #姓名
        lxdh = request.POST.get('lxdh') #联系电话
        zc = request.POST.get('zc') #职称

        res = models.jiaoshi.objects.filter(yhm=yhm).count();
        if res > 0:
            messages.success(request, "操作失败、用户名重复")
        elif res == 0:
            messages.success(request, "操作成功")
            models.jiaoshi.objects.create(yhm=yhm, mm=mm, xm=xm, lxdh=lxdh, zc=zc, )


        #return render(request, "jiaoshi/jiaoshiadd.html")
        return redirect('/jiaoshi/jiaoshiadd')

#教师列表
def jiaoshilist(request):
    print(request.method)
    global list
    if request.method == 'GET':

        yhm= request.GET.get('yhm')#用户名
        if not yhm:
            yhm = ""
        print(yhm)
        list = models.jiaoshi.objects.filter(yhm__icontains=yhm).all()  # 获取jiaoshi表所有的数据
    return render(request, "jiaoshi/jiaoshilist.html", {'list': list})
#修改教师
def jiaoshimodify(request):
    # 获取要修改的数据的id
    if request.method == 'GET':
        id = request.GET.get('id')
        obj = models.jiaoshi.objects.get(id=id)
        return render(request, 'jiaoshi/jiaoshimodify.html', {'obj': obj})

    id = request.POST.get('id')
    yhm = request.POST.get('yhm') #用户名
    mm = request.POST.get('mm') #密码
    xm = request.POST.get('xm') #姓名
    lxdh = request.POST.get('lxdh') #联系电话
    zc = request.POST.get('zc') #职称
    messages.success(request, "操作成功")
    ret = models.jiaoshi.objects.filter(id=id).update(yhm=yhm,mm=mm,xm=xm,lxdh=lxdh,zc=zc, )

    return redirect('/jiaoshi/jiaoshilist')


#修改教师 个人信息修改
def jiaoshimod(request):
    # 获取要修改的数据的id
    if request.method == 'GET':
        id = request.session.get('id')
        obj = models.jiaoshi.objects.get(id=id)
        return render(request, 'jiaoshi/modify.html', {'obj': obj})

    id = request.POST.get('id')
    yhm = request.POST.get('yhm') #用户名
    mm = request.POST.get('mm') #密码
    xm = request.POST.get('xm') #姓名
    lxdh = request.POST.get('lxdh') #联系电话
    zc = request.POST.get('zc') #职称
    messages.success(request, "操作成功")
    ret = models.jiaoshi.objects.filter(id=id).update(yhm=yhm,mm=mm,xm=xm,lxdh=lxdh,zc=zc, )

    return redirect('/jiaoshi/jiaoshimod')

# 教师详情
def jiaoshidetail(request):
    # 获取要修改的数据的id
    id = request.GET.get('id')
    obj = models.jiaoshi.objects.get(id=id)
    return render(request, 'jiaoshi/jiaoshidetail.html', {'obj': obj})

#教师删除
def jiaoshidelete(request):
    # 获取要删除数据的id
    id = request.GET.get('id')
    # 查询数据库是否存在
    obj = models.jiaoshi.objects.get(id=id)
    if obj:
        # 在数据库中删除
        obj.delete()
        messages.success(request, "操作成功")
        return redirect('/jiaoshi/jiaoshilist')
    return HttpResponse("删除失败")

#添加学生
def xueshengadd(request):
   if request.method == 'GET':
       return render(request, "xuesheng/xueshengadd.html")
   if request.method == 'POST':
        yhm = request.POST.get('yhm') #用户名
        mm = request.POST.get('mm') #密码
        xm = request.POST.get('xm') #姓名
        lxdh = request.POST.get('lxdh') #联系电话
        zy = request.POST.get('zy') #专业

        res = models.xuesheng.objects.filter(yhm=yhm).count();
        if res > 0:
            messages.success(request, "操作失败、用户名重复")
        elif res == 0:
            messages.success(request, "操作成功")
            models.xuesheng.objects.create(yhm=yhm, mm=mm, xm=xm, lxdh=lxdh, zy=zy, )


        #return render(request, "xuesheng/xueshengadd.html")
        return redirect('/xuesheng/xueshengadd')

#学生列表
def xueshenglist(request):
    print(request.method)
    global list
    if request.method == 'GET':

        yhm= request.GET.get('yhm')#用户名
        if not yhm:
            yhm = ""
        print(yhm)
        list = models.xuesheng.objects.filter(yhm__icontains=yhm).all()  # 获取xuesheng表所有的数据
    return render(request, "xuesheng/xueshenglist.html", {'list': list})
#修改学生
def xueshengmodify(request):
    # 获取要修改的数据的id
    if request.method == 'GET':
        id = request.GET.get('id')
        obj = models.xuesheng.objects.get(id=id)
        return render(request, 'xuesheng/xueshengmodify.html', {'obj': obj})

    id = request.POST.get('id')
    yhm = request.POST.get('yhm') #用户名
    mm = request.POST.get('mm') #密码
    xm = request.POST.get('xm') #姓名
    lxdh = request.POST.get('lxdh') #联系电话
    zy = request.POST.get('zy') #专业
    messages.success(request, "操作成功")
    ret = models.xuesheng.objects.filter(id=id).update(yhm=yhm,mm=mm,xm=xm,lxdh=lxdh,zy=zy, )

    return redirect('/xuesheng/xueshenglist')
#修改学生
def xueshengmod(request):
    # 获取要修改的数据的id
    if request.method == 'GET':
        id = request.session.get('id')
        obj = models.xuesheng.objects.get(id=id)
        return render(request, 'xuesheng/modify.html', {'obj': obj})

    id = request.POST.get('id')
    yhm = request.POST.get('yhm') #用户名
    mm = request.POST.get('mm') #密码
    xm = request.POST.get('xm') #姓名
    lxdh = request.POST.get('lxdh') #联系电话
    zy = request.POST.get('zy') #专业
    messages.success(request, "操作成功")
    ret = models.xuesheng.objects.filter(id=id).update(yhm=yhm,mm=mm,xm=xm,lxdh=lxdh,zy=zy, )

    return redirect('/xuesheng/xueshengmod')

# 学生详情
def xueshengdetail(request):
    # 获取要修改的数据的id
    id = request.GET.get('id')
    obj = models.xuesheng.objects.get(id=id)
    return render(request, 'xuesheng/xueshengdetail.html', {'obj': obj})

#学生删除
def xueshengdelete(request):
    # 获取要删除数据的id
    id = request.GET.get('id')
    # 查询数据库是否存在
    obj = models.xuesheng.objects.get(id=id)
    if obj:
        # 在数据库中删除
        obj.delete()
        messages.success(request, "操作成功")
        return redirect('/xuesheng/xueshenglist')
    return HttpResponse("删除失败")

#添加教室信息
def jsxxadd(request):
   if request.method == 'GET':
       return render(request, "jsxx/jsxxadd.html")
   if request.method == 'POST':
        jsmc = request.POST.get('jsmc') #教室名称
        wz = request.POST.get('wz') #位置
        bz = request.POST.get('bz') #备注

        res = models.jsxx.objects.filter(jsmc=jsmc).count();
        if res > 0:
            messages.success(request, "操作失败、教室名称重复")
        elif res == 0:
            messages.success(request, "操作成功")
            models.jsxx.objects.create(jsmc=jsmc, wz=wz, bz=bz, )

        #return render(request, "jsxx/jsxxadd.html")
        return redirect('/jsxx/jsxxadd')

#教室信息列表
def jsxxlist(request):
    print(request.method)
    global list
    if request.method == 'GET':

        jsmc= request.GET.get('jsmc')#教室名称
        if not jsmc:
            jsmc = ""
        print(jsmc)
        list = models.jsxx.objects.filter(jsmc__icontains=jsmc).all()  # 获取jsxx表所有的数据
    return render(request, "jsxx/jsxxlist.html", {'list': list})
#修改教室信息
def jsxxmodify(request):
    # 获取要修改的数据的id
    if request.method == 'GET':
        id = request.GET.get('id')
        obj = models.jsxx.objects.get(id=id)
        return render(request, 'jsxx/jsxxmodify.html', {'obj': obj})

    id = request.POST.get('id')
    jsmc = request.POST.get('jsmc') #教室名称
    wz = request.POST.get('wz') #位置
    bz = request.POST.get('bz') #备注
    messages.success(request, "操作成功")
    ret = models.jsxx.objects.filter(id=id).update(jsmc=jsmc,wz=wz,bz=bz, )

    return redirect('/jsxx/jsxxlist')

# 教室信息详情
def jsxxdetail(request):
    # 获取要修改的数据的id
    id = request.GET.get('id')
    obj = models.jsxx.objects.get(id=id)
    return render(request, 'jsxx/jsxxdetail.html', {'obj': obj})

#教室信息删除
def jsxxdelete(request):
    # 获取要删除数据的id
    id = request.GET.get('id')
    # 查询数据库是否存在
    obj = models.jsxx.objects.get(id=id)
    if obj:
        # 在数据库中删除
        obj.delete()
        messages.success(request, "操作成功")
        return redirect('/jsxx/jsxxlist')
    return HttpResponse("删除失败")

#添加星期
def xingqiadd(request):
   if request.method == 'GET':
       return render(request, "xingqi/xingqiadd.html")
   if request.method == 'POST':
        xq = request.POST.get('xq') #星期
        messages.success(request, "操作成功")
        models.xingqi.objects.create(xq=xq, )
        #return render(request, "xingqi/xingqiadd.html")
        return redirect('/xingqi/xingqiadd')

#星期列表
def xingqilist(request):
    print(request.method)
    global list
    if request.method == 'GET':

        xq= request.GET.get('xq')#星期
        if not xq:
            xq = ""
        print(xq)
        list = models.xingqi.objects.filter(xq__icontains=xq).all()  # 获取xingqi表所有的数据
    return render(request, "xingqi/xingqilist.html", {'list': list})
#修改星期
def xingqimodify(request):
    # 获取要修改的数据的id
    if request.method == 'GET':
        id = request.GET.get('id')
        obj = models.xingqi.objects.get(id=id)
        return render(request, 'xingqi/xingqimodify.html', {'obj': obj})

    id = request.POST.get('id')
    xq = request.POST.get('xq') #星期
    messages.success(request, "操作成功")
    ret = models.xingqi.objects.filter(id=id).update(xq=xq, )

    return redirect('/xingqi/xingqilist')

# 星期详情
def xingqidetail(request):
    # 获取要修改的数据的id
    id = request.GET.get('id')
    obj = models.xingqi.objects.get(id=id)
    return render(request, 'xingqi/xingqidetail.html', {'obj': obj})

#星期删除
def xingqidelete(request):
    # 获取要删除数据的id
    id = request.GET.get('id')
    # 查询数据库是否存在
    obj = models.xingqi.objects.get(id=id)
    if obj:
        # 在数据库中删除
        obj.delete()
        messages.success(request, "操作成功")
        return redirect('/xingqi/xingqilist')
    return HttpResponse("删除失败")

#添加时间段
def sjdadd(request):
   if request.method == 'GET':
       return render(request, "sjd/sjdadd.html")
   if request.method == 'POST':
        sjd = request.POST.get('sjd') #时间段
        messages.success(request, "操作成功")
        models.sjd.objects.create(sjd=sjd, )
        #return render(request, "sjd/sjdadd.html")
        return redirect('/sjd/sjdadd')

#时间段列表
def sjdlist(request):
    print(request.method)
    global list
    if request.method == 'GET':

        sjd= request.GET.get('sjd')#时间段
        if not sjd:
            sjd = ""
        print(sjd)
        list = models.sjd.objects.filter(sjd__icontains=sjd).all()  # 获取sjd表所有的数据
    return render(request, "sjd/sjdlist.html", {'list': list})
#修改时间段
def sjdmodify(request):
    # 获取要修改的数据的id
    if request.method == 'GET':
        id = request.GET.get('id')
        obj = models.sjd.objects.get(id=id)
        return render(request, 'sjd/sjdmodify.html', {'obj': obj})

    id = request.POST.get('id')
    sjd = request.POST.get('sjd') #时间段
    messages.success(request, "操作成功")
    ret = models.sjd.objects.filter(id=id).update(sjd=sjd, )

    return redirect('/sjd/sjdlist')

# 时间段详情
def sjddetail(request):
    # 获取要修改的数据的id
    id = request.GET.get('id')
    obj = models.sjd.objects.get(id=id)
    return render(request, 'sjd/sjddetail.html', {'obj': obj})

#时间段删除
def sjddelete(request):
    # 获取要删除数据的id
    id = request.GET.get('id')
    # 查询数据库是否存在
    obj = models.sjd.objects.get(id=id)
    if obj:
        # 在数据库中删除
        obj.delete()
        messages.success(request, "操作成功")
        return redirect('/sjd/sjdlist')
    return HttpResponse("删除失败")

#添加课程
def kechengadd(request):
   if request.method == 'GET':
       jslist = models.jiaoshi.objects.all()  # 获取分类表所有的数据
       return render(request, "kecheng/kechengadd.html",{'jslist':jslist})
   if request.method == 'POST':
        kcmc = request.POST.get('kcmc') #课程名称
        rkjs = request.POST.get('rkjs') #任课教师
        sm = request.POST.get('sm') #说明

        res = models.kecheng.objects.filter(kcmc=kcmc).count();
        if res > 0:
            messages.success(request, "操作失败、教室名称重复")
        elif res == 0:
            messages.success(request, "操作成功")
            models.kecheng.objects.create(kcmc=kcmc, rkjs=rkjs, sm=sm, )


        #return render(request, "kecheng/kechengadd.html")
        return redirect('/kecheng/kechengadd')

#课程列表
def kechenglist(request):
    print(request.method)
    global list
    if request.method == 'GET':

        kcmc= request.GET.get('kcmc')#课程名称
        if not kcmc:
            kcmc = ""
        print(kcmc)
        list = models.kecheng.objects.filter(kcmc__icontains=kcmc).all()  # 获取kecheng表所有的数据
    return render(request, "kecheng/kechenglist.html", {'list': list})
#修改课程
def kechengmodify(request):
    # 获取要修改的数据的id
    if request.method == 'GET':
        id = request.GET.get('id')
        obj = models.kecheng.objects.get(id=id)
        jslist = models.jiaoshi.objects.all()  # 获取分类表所有的数据
        return render(request, 'kecheng/kechengmodify.html', {'obj': obj,'jslist':jslist})

    id = request.POST.get('id')
    kcmc = request.POST.get('kcmc') #课程名称
    rkjs = request.POST.get('rkjs') #任课教师
    sm = request.POST.get('sm') #说明
    messages.success(request, "操作成功")
    ret = models.kecheng.objects.filter(id=id).update(kcmc=kcmc,rkjs=rkjs,sm=sm, )

    return redirect('/kecheng/kechenglist')

# 课程详情
def kechengdetail(request):
    # 获取要修改的数据的id
    id = request.GET.get('id')
    obj = models.kecheng.objects.get(id=id)
    return render(request, 'kecheng/kechengdetail.html', {'obj': obj})

#课程删除
def kechengdelete(request):
    # 获取要删除数据的id
    id = request.GET.get('id')
    # 查询数据库是否存在
    obj = models.kecheng.objects.get(id=id)
    if obj:
        # 在数据库中删除
        obj.delete()
        messages.success(request, "操作成功")
        return redirect('/kecheng/kechenglist')
    return HttpResponse("删除失败")

#添加上课时间
def sksjadd(request):
   if request.method == 'GET':
       curr_time = datetime.now()
       timestamp = datetime.strftime(curr_time, '%Y%m%d%H%M%S')
       #print(timestamp)
       xqlist = models.xingqi.objects.all()  # 获取星期表所有的数据
       sjdlist = models.sjd.objects.all()  # 获取时间段表所有的数据
       kclist=models.kecheng.objects.all()#课程
       jsxxlist=models.jsxx.objects.all()#教师
       return render(request, "sksj/sksjadd.html",{'lsh':timestamp,'xqlist':xqlist,'sjdlist':sjdlist,'kclist':kclist,'jsxxlist':jsxxlist})
   if request.method == 'POST':
        lsh = request.POST.get('lsh') #流水号
        xq = request.POST.get('xq') #星期
        sjd = request.POST.get('sjd') #时间段
        kc = request.POST.get('kc') #课程
        js = request.POST.get('js') #教室

        flg="操作成功"

        num1=models.sksj.objects.filter(xq=xq,sjd=sjd,js=js).count();#判断 同一时间下 教室使用是否冲突

        num2 = models.sksj.objects.filter(xq=xq, sjd=sjd, kc=kc).count();  # 判断 同一时间下课程上课是否冲突

        if num1>0 or num2>0 :
            flg="同一时间下 教室或课程 冲突";

        else:
            models.sksj.objects.create(lsh=lsh, xq=xq, sjd=sjd, kc=kc, js=js, )

        messages.success(request, flg)


        #return render(request, "sksj/sksjadd.html")
        return redirect('/sksj/sksjadd')

   # 添加上课时间
def kebiao(request):

    curr_time = datetime.now()
    timestamp = datetime.strftime(curr_time, '%Y%m%d%H%M%S')
    # print(timestamp)
    xqlist = models.xingqi.objects.all()  # 获取星期表所有的数据
    sjdlist = models.sjd.objects.all()  # 获取时间段表所有的数据
    kclist = models.kecheng.objects.all()  # 课程
    jsxxlist = models.jsxx.objects.all()  # 教师
    sksjlist=models.sksj.objects.all() #上课时间
    return render(request, "sksj/kebiao.html",
                    {'lsh': timestamp, 'xqlist': xqlist, 'sjdlist': sjdlist, 'sksjlist': sksjlist,
                    'jsxxlist': jsxxlist})



#上课时间列表
def sksjlist(request):
    print(request.method)
    global list
    if request.method == 'GET':

        lsh= request.GET.get('lsh')#流水号
        if not lsh:
            lsh = ""
        print(lsh)
        list = models.sksj.objects.filter(lsh__icontains=lsh).all()  # 获取sksj表所有的数据
    return render(request, "sksj/sksjlist.html", {'list': list})

#上课时间列表
def sksjmylist(request):
    print(request.method)
    global list
    if request.method == 'GET':

        lsh= request.GET.get('lsh')#流水号
        if not lsh:
            lsh = ""
        print(lsh)
        curr_time = datetime.now()

        times = datetime.strftime(curr_time, '%Y-%m-%d')
        # 将字符串转换为datetime对象
        date = datetime.strptime(times, "%Y-%m-%d")
        # 获取星期几
        weekday = date.weekday()

        # 打印结果，星期几以数字形式打印（0-6）
        print(weekday)

        # 如果想要以星期几的名字形式打印，可以使用以下映射
        weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']

        xq = weekdays[weekday]

        list = models.sksj.objects.filter(lsh__icontains=lsh,xq=xq).all()  # 获取sksj表所有的数据
    return render(request, "sksj/sksjmylist.html", {'list': list})
#修改上课时间
def sksjmodify(request):
    # 获取要修改的数据的id
    if request.method == 'GET':
        id = request.GET.get('id')
        obj = models.sksj.objects.get(id=id)
        return render(request, 'sksj/sksjmodify.html', {'obj': obj})

    id = request.POST.get('id')
    lsh = request.POST.get('lsh') #流水号
    xq = request.POST.get('xq') #星期
    sjd = request.POST.get('sjd') #时间段
    kc = request.POST.get('kc') #课程
    js = request.POST.get('js') #教室
    messages.success(request, "操作成功")
    ret = models.sksj.objects.filter(id=id).update(lsh=lsh,xq=xq,sjd=sjd,kc=kc,js=js, )

    return redirect('/sksj/sksjlist')

# 上课时间详情
def sksjdetail(request):
    # 获取要修改的数据的id
    id = request.GET.get('id')
    obj = models.sksj.objects.get(id=id)
    return render(request, 'sksj/sksjdetail.html', {'obj': obj})

#上课时间删除
def sksjdelete(request):
    # 获取要删除数据的id
    id = request.GET.get('id')
    # 查询数据库是否存在
    obj = models.sksj.objects.get(id=id)
    if obj:
        # 在数据库中删除
        obj.delete()
        messages.success(request, "操作成功")
        return redirect('/sksj/sksjlist')
    return HttpResponse("删除失败")

def generate_qiandao(request):
    if request.method == 'GET':
        curr_time = datetime.now()
        timestamp = datetime.strftime(curr_time, '%Y%m%d%H%M%S')
        kclist=models.kecheng.objects.all()#课程
        return render(request, "qiandao/generate_qiandao.html",{'lsh':timestamp,'sjdlist':sjdlist,'kclist':kclist,'jsxxlist':jsxxlist})
    if request.method == 'POST':
        kclist=models.kecheng.objects.all()#课程
        curr_time = datetime.now()
        timestamp = datetime.strftime(curr_time, '%Y%m%d%H%M%S')
        kc = request.POST.get('kc') #课程
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        rq = datetime.strftime(curr_time, '%Y%m%d')
        qdsj = timestamp

        latest_data = models.qiandao_meta.objects.filter(kc=kc).order_by('-qdsj').first()
        if latest_data:
            old_qdsj = latest_data.qdsj
            old_time = datetime.strptime(old_qdsj, '%Y%m%d%H%M%S')
            time_diff = abs(curr_time - old_time)
            if time_diff > timedelta(minutes=60):
                models.qiandao_meta.objects.create(code=code, rq=rq, qdsj=qdsj, kc=kc, )
            else:
                code = latest_data.code
        else:
            models.qiandao_meta.objects.create(code=code, rq=rq, qdsj=qdsj, kc=kc, )
        
        return render(request, "qiandao/generate_qiandao.html",{'lsh':timestamp,'sjdlist':sjdlist,'kclist':kclist,'jsxxlist':jsxxlist, 'code':code, 'course':kc})


def add_qiandao(request):
    if request.method == 'GET':
        curr_time = datetime.now()
        timestamp = datetime.strftime(curr_time, '%Y%m%d%H%M%S')
        kclist=models.kecheng.objects.all()#课程
        return render(request, "qiandao/add_qiandao.html",{'lsh':timestamp,'sjdlist':sjdlist,'kclist':kclist,'jsxxlist':jsxxlist})
    if request.method == 'POST':
        xs=request.session.get('yhm')#学生
        kclist=models.kecheng.objects.all()#课程
        curr_time = datetime.now()
        timestamp = datetime.strftime(curr_time, '%Y%m%d%H%M%S')
        kc = request.POST.get('kc') #课程
        code = request.POST.get('code')
        rq = datetime.strftime(curr_time, '%Y%m%d')
        qdsj = timestamp

        latest_data = models.qiandao_meta.objects.filter(kc=kc).order_by('-qdsj').first()
        if latest_data:
            old_qdsj = latest_data.qdsj
            old_time = datetime.strptime(old_qdsj, '%Y%m%d%H%M%S')
            time_diff = abs(curr_time - old_time)
            if time_diff > timedelta(minutes=60):
                # 签到过期
                messages.success(request, "签到过期")
                pass
            elif code != latest_data.code:
                # 签到码错误
                messages.success(request, "签到码错误")
                pass
            else:
                qiandao = models.qiandao.objects.filter(kc=kc, xs=xs).order_by('-qdsj').first()
                if qiandao:
                    # 已经签到
                    messages.success(request, "已经签到")
                    pass
                else:
                    # 签到成功
                    xs=request.session.get('yhm')#学生
                    zt='签到'#状态
                    qtsj='no'#签退时间
                    models.qiandao.objects.create(sksj=qdsj, xs=xs, zt=zt, rq=rq, qdsj=qdsj, qtsj=qtsj, kc=kc, )
                    messages.success(request, "签到成功")
        else:
            # 签到成功
            xs=request.session.get('yhm')#学生
            zt='签到'#状态
            qtsj='no'#签退时间
            models.qiandao.objects.create(sksj=qdsj, xs=xs, zt=zt, rq=rq, qdsj=qdsj, qtsj=qtsj, kc=kc, )
            messages.success(request, "签到成功")

        return render(request, "qiandao/add_qiandao.html",{'lsh':timestamp,'sjdlist':sjdlist,'kclist':kclist,'jsxxlist':jsxxlist})





#添加签到
def qiandaoadd(request):
   if request.method == 'GET':
       sjd=request.GET.get("sjd")
       kc = request.GET.get("kc")
       curr_time = datetime.now()

       times = datetime.strftime(curr_time, '%Y-%m-%d')
       curr_time = datetime.now()
       timestamp = datetime.strftime(curr_time, '%Y%m%d%H%M%S')
       sj = datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')

       return render(request, "qiandao/qiandaoadd.html",{'sjd':sjd,'kc':kc,'rq':times,'qdsj':sj})
   if request.method == 'POST':
        sksj = request.POST.get('sksj') #上课时间
        xs = request.POST.get('xs') #学生
        zt = request.POST.get('zt') #状态
        rq = request.POST.get('rq') #日期
        qdsj = request.POST.get('qdsj') #签到时间
        qtsj = request.POST.get('qtsj') #签退时间
        kc = request.POST.get('kc') #课程

        res = models.qiandao.objects.filter(xs=xs,sksj=sksj,kc=kc).count();
        if res > 0:
            messages.success(request, "操作失败、当日课程已经被签到")
        elif res == 0:
            messages.success(request, "签到成功")
            models.qiandao.objects.create(sksj=sksj, xs=xs, zt=zt, rq=rq, qdsj=qdsj, qtsj=qtsj, kc=kc, )



        #return render(request, "qiandao/qiandaoadd.html")
        return redirect('/sksj/sksjmylist')

#签到列表
def qiandaolist(request):
    print(request.method)
    global list
    if request.method == 'GET':

        sksj= request.GET.get('sksj')#上课时间
        if not sksj:
            sksj = ""
        print(sksj)
        kc = request.GET.get('kc')  # 上课时间
        if not kc:
            kc = ""
        print(kc)
        list = models.qiandao.objects.filter(sksj__icontains=sksj,kc__icontains=kc).all()  # 获取qiandao表所有的数据
    return render(request, "qiandao/qiandaolist.html", {'list': list})


#签到列表
def qiandaomylist(request):
    print(request.method)
    global list
    if request.method == 'GET':

        sksj= request.GET.get('sksj')#上课时间
        if not sksj:
            sksj = ""
        print(sksj)
        kc = request.GET.get('kc')  # 上课时间
        if not kc:
            kc = ""
        print(kc)
        xs=request.session.get("yhm")
        list = models.qiandao.objects.filter(sksj__icontains=sksj,kc__icontains=kc,xs=xs).all()  # 获取qiandao表所有的数据
    return render(request, "qiandao/qiandaomylist.html", {'list': list})
#修改签到
def qiandaomodify(request):
    # 获取要修改的数据的id
    if request.method == 'GET':
        id = request.GET.get('id')
        obj = models.qiandao.objects.get(id=id)
        return render(request, 'qiandao/qiandaomodify.html', {'obj': obj})

    id = request.POST.get('id')
    sksj = request.POST.get('sksj') #上课时间
    xs = request.POST.get('xs') #学生
    zt = request.POST.get('zt') #状态
    rq = request.POST.get('rq') #日期
    qdsj = request.POST.get('qdsj') #签到时间
    qtsj = request.POST.get('qtsj') #签退时间
    kc = request.POST.get('kc') #课程
    messages.success(request, "操作成功")
    ret = models.qiandao.objects.filter(id=id).update(sksj=sksj,xs=xs,zt=zt,rq=rq,qdsj=qdsj,qtsj=qtsj,kc=kc, )

    return redirect('/qiandao/qiandaolist')
#修改签到
def qiandaoqiantui(request):
    # 获取要修改的数据的id
    id = request.GET.get('id')
    zt = "已完成" #状态
    curr_time = datetime.now()
    sj = datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
    qtsj = sj #签退时间
    kc = request.POST.get('kc') #课程
    messages.success(request, "操作成功")
    ret = models.qiandao.objects.filter(id=id).update(zt=zt,qtsj=qtsj )

    return redirect('/qiandao/qiandaomylist')

# 签到详情
def qiandaodetail(request):
    # 获取要修改的数据的id
    id = request.GET.get('id')
    obj = models.qiandao.objects.get(id=id)
    return render(request, 'qiandao/qiandaodetail.html', {'obj': obj})

#签到删除
def qiandaodelete(request):
    # 获取要删除数据的id
    id = request.GET.get('id')
    # 查询数据库是否存在
    obj = models.qiandao.objects.get(id=id)
    if obj:
        # 在数据库中删除
        obj.delete()
        messages.success(request, "操作成功")
        return redirect('/qiandao/qiandaolist')
    return HttpResponse("删除失败")

#添加教室借用
def jsjyadd(request):
   if request.method == 'GET':
       curr_time = datetime.now()
       timestamp = datetime.strftime(curr_time, '%Y%m%d%H%M%S')
       times = datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
       sjdlist = models.sjd.objects.all()  # 获取时间段表所有的数据

       jsxxlist = models.jsxx.objects.all()  # 教师
       return render(request, "jsjy/jsjyadd.html",{'sqh':timestamp,'sqsj':times,'sjdlist':sjdlist,'jsxxlist':jsxxlist})
   if request.method == 'POST':
        sqh = request.POST.get('sqh') #申请号
        bt = request.POST.get('bt') #标题
        nr = request.POST.get('nr') #内容
        js = request.POST.get('js') #教室
        sqrq = request.POST.get('sqrq') #申请日期
        sjd = request.POST.get('sjd') #时间段
        sqsj = request.POST.get('sqsj') #申请时间
        sqzt = request.POST.get('sqzt') #申请状态
        yh = request.POST.get('yh') #用户



        # 将字符串转换为datetime对象
        date = datetime.strptime(sqrq, "%Y-%m-%d")

        # 获取星期几
        weekday = date.weekday()

        # 打印结果，星期几以数字形式打印（0-6）
        print(weekday)

        # 如果想要以星期几的名字形式打印，可以使用以下映射
        weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']

        xq=weekdays[weekday]

        print("xq="+xq)

        num1=models.jsjy.objects.filter(js=js,sqrq=sqrq,sjd=sjd).count()#教室已经被别人预约

        num2=models.sksj.objects.filter(js=js,sjd=sjd,xq=xq).count()#查看教室是否在上课


        if num1>0:
            messages.success(request, "操作失败了、该教室已经被别人预约")
        elif num2 > 0:
            messages.success(request, "操作失败了、该教室当天有课")
        else:
            messages.success(request, "操作成功")
            models.jsjy.objects.create(sqh=sqh,bt=bt,nr=nr,js=js,sqrq=sqrq,sjd=sjd,sqsj=sqsj,sqzt=sqzt,yh=yh, )
        #return render(request, "jsjy/jsjyadd.html")
        return redirect('/jsjy/jsjyadd')

#教室借用列表
def jsjylist(request):
    print(request.method)
    global list
    if request.method == 'GET':

        sqh= request.GET.get('sqh')#申请号
        if not sqh:
            sqh = ""
        print(sqh)

        list = models.jsjy.objects.filter(sqh__icontains=sqh).all()  # 获取jsjy表所有的数据
    return render(request, "jsjy/jsjylist.html", {'list': list})




#教室借用列表
def jsjymylist(request):
    print(request.method)
    global list
    if request.method == 'GET':

        sqh= request.GET.get('sqh')#申请号
        if not sqh:
            sqh = ""
        yhm=request.session.get('yhm')#用户名
        if not yhm:
            yhm = ""
        print(sqh)
        list = models.jsjy.objects.filter(sqh__icontains=sqh,yh=yhm).all()  # 获取jsjy表所有的数据
    return render(request, "jsjy/list.html", {'list': list})
#修改教室借用
def jsjymodify(request):
    # 获取要修改的数据的id
    if request.method == 'GET':
        id = request.GET.get('id')
        obj = models.jsjy.objects.get(id=id)
        return render(request, 'jsjy/jsjymodify.html', {'obj': obj})

    id = request.POST.get('id')
    sqh = request.POST.get('sqh') #申请号
    bt = request.POST.get('bt') #标题
    nr = request.POST.get('nr') #内容
    js = request.POST.get('js') #教室
    sqrq = request.POST.get('sqrq') #申请日期
    sjd = request.POST.get('sjd') #时间段
    sqsj = request.POST.get('sqsj') #申请时间
    sqzt = request.POST.get('sqzt') #申请状态
    yh = request.POST.get('yh') #用户
    messages.success(request, "操作成功")
    ret = models.jsjy.objects.filter(id=id).update(sqh=sqh,bt=bt,nr=nr,js=js,sqrq=sqrq,sjd=sjd,sqsj=sqsj,sqzt=sqzt,yh=yh, )

    return redirect('/jsjy/jsjylist')




#修改教室借用
def jsjyfinish(request):
    # 获取要修改的数据的id

    id = request.GET.get('id')



    sqzt = "完成" #申请状态

    messages.success(request, "操作成功")
    ret = models.jsjy.objects.filter(id=id).update(sqzt=sqzt, )

    return redirect('/jsjy/jsjylist')

# 教室借用详情
def jsjydetail(request):
    # 获取要修改的数据的id
    id = request.GET.get('id')
    obj = models.jsjy.objects.get(id=id)
    return render(request, 'jsjy/jsjydetail.html', {'obj': obj})

# 教师借用使用统计
def jsjytj(request):
    # 获取要修改的数据的id
    global list
    list = models.jsjy.objects.values('js').annotate(
        num=Count('id'))
    return render(request, 'jsjy/jsjytongji.html', {'list': list})

#教室借用删除
def jsjydelete(request):
    # 获取要删除数据的id
    id = request.GET.get('id')
    # 查询数据库是否存在
    obj = models.jsjy.objects.get(id=id)
    if obj:
        # 在数据库中删除
        obj.delete()
        messages.success(request, "操作成功")
        return redirect('/jsjy/jsjylist')
    return HttpResponse("删除失败")


def qiandao_data(request):
    kclist=models.kecheng.objects.all()#课程
    if request.method == 'POST':
        kc = request.POST.get('kc')
        qiandao = models.qiandao.objects.filter(kc=kc).all()
        student = models.xuesheng.objects.all()
        ratios = [round(len(qiandao)/len(student), 1), round(1-len(qiandao)/len(student), 1)]
        categories = ['Present', 'Absent']
        matplotlib.use('Agg')  # 不出现画图的框
        # plt.rcParams['font.sans-serif'] = ['SimHei']  # 这两行用来显示汉字
        # plt.rcParams['axes.unicode_minus'] = False
        # plt.title('签到情况')
        plt.pie(ratios, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # 保持图形是圆形

        sio = BytesIO()
        plt.savefig(sio, format='png', bbox_inches='tight', pad_inches=0.0)
        data = base64.encodebytes(sio.getvalue()).decode()
        src = 'data:image/png;base64,' + str(data)
        # 记得关闭，不然画出来的图是重复的
        plt.close()
        print(ratios, kc)
        return render(request, 'qiandao/qiandao_data.html', {'kc': kc,'src': src, 'kclist':kclist})
    return render(request, 'qiandao/qiandao_data.html', {'kclist':kclist})

    # matplotlib.use('Agg')  # 不出现画图的框
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 这两行用来显示汉字
    # plt.rcParams['axes.unicode_minus'] = False
    # sns.boxplot([133,123,899,198,849,180,844])  # 箱线图
    # plt.title('title', loc='center')
    # sio = BytesIO()
    # plt.savefig(sio, format='png', bbox_inches='tight', pad_inches=0.0)
    # data = base64.encodebytes(sio.getvalue()).decode()
    # src = 'data:image/png;base64,' + str(data)
    # # 记得关闭，不然画出来的图是重复的
    # plt.close()
    # return render(request, 'qiandao/qiandao_data.html', {'src': src})



 
def init_data(request):
    # admin
    yhm = 'admin' #用户名
    mm = '123' #密码
    xm = 'admin' #姓名
    res = models.gly.objects.filter(yhm=yhm).count()
    if res == 0:
        models.gly.objects.create(yhm=yhm, mm=mm, xm=xm, )
    # teacher
    for i in range(2):
        yhm = f'teacher_{i}' #用户名
        mm = '123' #密码
        xm = yhm #姓名
        lxdh = '123456789' #联系电话
        zc = 'dasfdsgdsa' #职称
        res = models.jiaoshi.objects.filter(yhm=yhm).count()
        if res == 0:
            models.jiaoshi.objects.create(yhm=yhm, mm=mm, xm=xm, lxdh=lxdh, zc=zc, )
    # student
    for i in range(100):
        yhm = f'student_{i}' #用户名
        mm = '123' #密码
        xm = yhm #姓名
        lxdh = '12368768574' #联系电话
        zy = 'cdsagsdga' #专业

        res = models.xuesheng.objects.filter(yhm=yhm).count()
        if res == 0:
            models.xuesheng.objects.create(yhm=yhm, mm=mm, xm=xm, lxdh=lxdh, zy=zy, )
    # week
    for i in ['一', '二', '三', '四', '五', '六', '日']:
        xq = i #星期
        res = models.xingqi.objects.filter(xq=xq).count()
        if res == 0:
            models.xingqi.objects.create(xq=xq, )
    # time
    for i in ['上午8-10', '上午10-12', '下午1-3', '下午3-5']:
        sjd = i #时间段
        res = models.sjd.objects.filter(sjd=sjd).count()
        if res == 0:
            models.sjd.objects.create(sjd=sjd, )

    # classroom
    for i in range(100):
        jsmc = f'classroom_{i+1}' #教室名称
        wz = '主楼' #位置
        bz = '备注信息' #备注

        res = models.jsxx.objects.filter(jsmc=jsmc).count()
        if res == 0:
            models.jsxx.objects.create(jsmc=jsmc, wz=wz, bz=bz, )

    # course

    return HttpResponse("初始化数据成功")


def init_qiandao_data(request):
    kclist=models.kecheng.objects.all()
    students = models.xuesheng.objects.all()

    sksj = '20240428001025'
    zt = '已完成'
    rq = '20240428'
    qdsj = sksj
    qtsj = '2024-04-28 00:10:41'

    for kcs in kclist:
        kc = kcs.kcmc
        for student in students:
            xs = student.xm
            if random.randint(1, 10)>9:
                continue
            else:
                qiandao = models.qiandao.objects.filter(kc=kc, xs=xs).count()
                if qiandao == 0:
                    models.qiandao.objects.create(sksj=qdsj, xs=xs, zt=zt, rq=rq, qdsj=qdsj, qtsj=qtsj, kc=kc, )
    return HttpResponse("初始化数据成功")
