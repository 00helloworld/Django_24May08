from django.db import models

# Create your models here.



#管理员表
class gly(models.Model):
	
    yhm=models.CharField(max_length=40)#用户名
    mm=models.CharField(max_length=40)#密码
    xm=models.CharField(max_length=40)#姓名

#教师表
class jiaoshi(models.Model):
	
    yhm=models.CharField(max_length=40)#用户名
    mm=models.CharField(max_length=40)#密码
    xm=models.CharField(max_length=40)#姓名
    lxdh=models.CharField(max_length=40)#联系电话
    zc=models.CharField(max_length=40)#职称

#学生表
class xuesheng(models.Model):
	
    yhm=models.CharField(max_length=40)#用户名
    mm=models.CharField(max_length=40)#密码
    xm=models.CharField(max_length=40)#姓名
    lxdh=models.CharField(max_length=40)#联系电话
    zy=models.CharField(max_length=40)#专业

#教室信息表
class jsxx(models.Model):
	
    jsmc=models.CharField(max_length=40)#教室名称
    wz=models.CharField(max_length=40)#位置
    bz=models.CharField(max_length=40)#备注

#星期表
class xingqi(models.Model):
	
    xq=models.CharField(max_length=40)#星期

#时间段表
class sjd(models.Model):
	
    sjd=models.CharField(max_length=40)#时间段

#课程表
class kecheng(models.Model):
	
    kcmc=models.CharField(max_length=40)#课程名称
    rkjs=models.CharField(max_length=40)#任课教师
    sm=models.CharField(max_length=400)#说明

#上课时间表
class sksj(models.Model):
	
    lsh=models.CharField(max_length=40)#流水号
    xq=models.CharField(max_length=40)#星期
    sjd=models.CharField(max_length=40)#时间段
    kc=models.CharField(max_length=40)#课程
    js=models.CharField(max_length=40)#教室

#签到表
class qiandao_meta(models.Model):
    kc=models.CharField(max_length=40)#课程
    code = models.CharField(max_length=40)
    rq=models.CharField(max_length=40)#日期
    qdsj=models.CharField(max_length=40)#签到时间


class qiandao(models.Model):
	
    sksj=models.CharField(max_length=40)#上课时间
    xs=models.CharField(max_length=40)#学生
    zt=models.CharField(max_length=40)#状态
    rq=models.CharField(max_length=40)#日期
    qdsj=models.CharField(max_length=40)#签到时间
    qtsj=models.CharField(max_length=40)#签退时间
    kc=models.CharField(max_length=40)#课程

#教室借用表
class jsjy(models.Model):
	
    sqh=models.CharField(max_length=40)#申请号
    bt=models.CharField(max_length=40)#标题
    nr=models.CharField(max_length=4000)#内容
    js=models.CharField(max_length=40)#教室
    sqrq=models.CharField(max_length=40)#申请日期
    sjd=models.CharField(max_length=40)#时间段
    sqsj=models.CharField(max_length=40)#申请时间
    sqzt=models.CharField(max_length=40)#申请状态
    yh=models.CharField(max_length=40)#用户

 