from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request,"website/index.html")
def principal_message(request):
    message = principals_message.objects.get()
    return render(request,"website/principal_message.html",
                  {'message':message,
                   })
def about_kv(request):
    return render(request,"website/about_kv.html")
def facilities(request):
    return render(request,"website/facilities.html")
def ict(request):
    return render(request,"website/ict.html")
def milestone(request):
    return render(request,"website/milestone.html")
def contact_us(request):
    return render(request,"website/contact_us.html")
def sport_and_games(request):
    return render(request,"website/sport_and_games.html")
def holidays(request):
    holiday=Holiday.objects.all()
    return render(request,"website/holidays.html",{
                      'holiday':holiday
                  })
def tc_issued(request):
    if request.method == "POST":
        name=request.POST['name']
        if not name:
            tcs_issued=TC.objects.all()
            return render(request,"website/tc_issued.html",{
                'tc':tcs_issued
            })
        try:
            tcs_issued=TC.objects.filter(name__contains=f'{name}')
            return render(request,"website/tc_issued.html",{
            'tc_search':tcs_issued
        })
        except:
            tcs_issued=None  
            return render(request,"website/tc_issued.html",{
                'tc_search':tcs_issued
                })
    else:
        tcs_issued=TC.objects.all()
        return render(request,"website/tc_issued.html",{
            'tc':tcs_issued
        })
def vmc_members(request):
    vmc_members=vmc_member.objects.all()
    return render(request,"website/vmc_members.html",{
        'members':vmc_members
    })
def committees(request):
    return render(request,"website/committes.html")
def administrative_notice(request):
    try:
        notice_data=Administrative_Notice.objects.all()[::-1][:10]
    except:
        notice_data=None
    return render(request,"website/administrative_notice.html",{
        'notice_data':notice_data,
    })
def academic_notice(request):
    try:
        notice_data=Administrative_Notice.objects.all()[::-1][:10]
    except:
        notice_data=None
    finally:
            return render(request,"website/academic_notice.html",{
            'notice_data':notice_data,
        })
def class_1(request):
    return render(request,"website/class_1.html")
def class_11(request):
    return render(request,"website/class_11.html")
def other_class(request):
    return render(request,"website/other_class.html")
def alumni(request):
    try:
        alumni_data=Alumni.objects.all()[::-1][:5]
    except:
        alumni_data=Alumni.objects.all()
    return render(request,"website/alumni.html",{
        'alumni_data':alumni_data,
    })
def achievement(request):
    return render(request,"website/achievement.html")
def newsletter(request):
    news_letter=News_letter.objects.all()
    return render(request,"website/newsletter.html",{
        'news_letter':news_letter
    })
def members_list(request):
    members_list=member_list.objects.all()
    return render(request,"website/members_list.html",{
        'members':members_list
    })
def vacancy(request):
    vacany_post=None
    vacany_present=False
    try:
        vacany_post=Vacancy.objects.all()
        vacany_present=True
    except:
        vacany_present=False
    return render(request,"website/vacancy.html",{
        "vacancy":vacany_post,
        "vacant":vacany_present
    })