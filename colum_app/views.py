from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

#for test
def test(request):
    return render(request,'colum_app/ColumnPage_template.html')

def Primary(request):
    content={
        'PageTitle':'绿翔培训-小学基地',
        'StageName':'小学',
        'StageTitle':'全球最大小学联盟 优秀小学生的摇篮',
        'StageInfo':'我不说别的 以下几个学校和我们是一伙的(你信嘛)',
        'InfoA':'北京市第二实验小学',
        'InfoB':'上海市世界外国语小学',
        'InfoC':'广东省广州市华南师范大学附属小学',
        'Environment':'这个还用问嘛 当然是说环境优美 山清水秀德拉~~~',
        'Teacher':'就封面那几个货 也没谁了',
        'LogisticsTeam':'呃。。。洗洗睡吧',
        'Money':'最没钱的一个学院。。。人均工资也就三四万吧~~~',
        'Picture':'colum_app/picture/primary.png'
    }

    return render(request,'colum_app/ColumnPage_template.html',{'content':content})

def Middle(request):
    content={
        'PageTitle':'绿翔培训-初中基地',
        'StageName':'初中',
        'StageTitle':'全球最大初中联盟 高级初中生诞生的摇篮',
        'StageInfo':'讲道理 以下几个学校虽然和我们不是一伙的 但我们之间有套路啊',
        'InfoA':'湖北黄冈中学',
        'InfoB':'北京四中',
        'InfoC':'天津南开中学',
        'Environment':'景色设计别具匠心 具有复古韵味',
        'Teacher':'还就是封面那几个货 也没谁了。。。',
        'LogisticsTeam':'暂时咱家 还雇不起。。。',
        'Money':'第二穷的学院。。。该学院程序员表示很无奈',
        'Picture':'colum_app/picture/middle.png'
    }

    return render(request,'colum_app/ColumnPage_template.html',{'content':content})


def High(request):
    content={
        'PageTitle':'绿翔培训-高中基地',
        'StageName':'高中',
        'StageTitle':'全球最大高中联盟 炒鸡高中生诞生的摇篮',
        'StageInfo':'以下几个学校虽然和我们不是一伙的 但是他们和我们的关系八竿子打不着啊~',
        'InfoA':'北京人大附中',
        'InfoB':'湖北华中师大第一附中',
        'InfoC':'北京北师大实验中学',
        'Environment':'春夏秋冬，年年岁岁，时光荏苒',
        'Teacher':'就封面那几个货 还是不提了吧。。。',
        'LogisticsTeam':'唉 一脸无奈。。。',
        'Money':'第三穷的学院 没有之一',
        'Picture':'colum_app/picture/high.png'
    }

    return render(request,'colum_app/ColumnPage_template.html',{'content':content})


def University(request):
    content={
        'PageTitle':'绿翔培训-大学基地',
        'StageName':'大学',
        'StageTitle':'全球最大大学联盟',
        'StageInfo':'额。。。大学部粗了一点小小的问题那就是 咱家暂时还没获得办学资格捏 但是学校还是要列滴',
        'InfoA':'加里敦大学',
        'InfoB':'北京大学',
        'InfoC':'皇家理工大学',
        'Environment':'那肯定是世界第一好的喽~~~',
        'Teacher':'拥有加里敦大学首席终身荣誉教授',
        'LogisticsTeam':'那肯定是没有的喽 诶嘿嘿~~~',
        'Money':'学校还没建成 谈啥子资本呐',
        'Picture':'colum_app/picture/university.png'
    }

    return render(request,'colum_app/ColumnPage_template.html',{'content':content})


