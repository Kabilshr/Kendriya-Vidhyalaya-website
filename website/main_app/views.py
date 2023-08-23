from datetime import date
from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
import requests
from django.urls import reverse
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.conf import settings
import shutil
# Create your views here.
def index(request):
    # if a mail is submitted use send_mail to send it to kvkathmandueoi@gmail.com
    if request.method == 'POST':
        email=request.POST['email'] 
        phone=request.POST['phone']
        message=request.POST['message']
        send_mail(
            'Feedback form submitted',
            f"Message: {message} \nPhone Number:  {phone}  \nEmail Address:  {email} \nThis is an auto-generated message",
            email,
            ['eoikvkathmandu@gmail.com']
        )
        return HttpResponseRedirect(reverse('index'))
    # return normal page
    else:
        # get a quote from db and check if it was last updated today if not make an API call and update the database 
        quotes=quote.objects.get()
        if date.today() != quotes.last_updated:
            api_url = 'https://api.api-ninjas.com/v1/quotes?category=inspirational'
            response = requests.get(api_url, headers={'X-Api-Key': 'W0FQSDaLu2ED6wnd+pkcnA==KAQ9M2sJJyNPqYUL'})
            if response.status_code == requests.codes.ok:
                response=response.json()
                quote_to_be_displayed=response[0]['quote']
                author=response[0]['author']
                quotes.author=author
                quotes.quote=quote_to_be_displayed
                quotes.last_updated=date.today()
                quotes.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                print("Error:", response.status_code, response.text)
                return response
        else:
            # if date was updated today then send in carousel image and all the necessary data
            quote_to_be_displayed=quotes.quote
            author=quotes.author
            # send only the first 8 notices or 20 images and only one set of carousel images
            notice=Notice.objects.all()[::-1][:5]
            events=News_and_Events.objects.all()[::-1][:20]
            carousel_image=Carousel_image.objects.get()
            return render(request,"website/index.html",{
                "notice":notice,
                "carousel_image":carousel_image,
                "quote":quote_to_be_displayed,
                "author":author,
                "events":events
            })
def principal_message(request):
    message = principals_message.objects.get()
    return render(request,"website/principal_message.html",
                  {'message':message,
                   })
def about_kv(request):
    return render(request,"website/about_kv.html")
def contact_us(request):
    principal = member_list.objects.get(designation='APrincipal').name
    chairman= vmc_member.objects.get(post__iexact='chairman,vmc')
    print(chairman)
    return render(request,"website/contact_us.html",{
        'principal': principal,
        'chairman':chairman,
    })
def holidays(request):
    # get holidays according to their category
    holiday=Holiday.objects.filter(category='holiday')
    summer_vacation=Holiday.objects.filter(category='summer_vacation')
    winter_vacation=Holiday.objects.filter(category='winter_vacation')
    autum_vacation=Holiday.objects.filter(category='autum_vacation')
    return render(request,"website/holidays.html",{
                      'holiday':holiday,
                      'summer_vacation':summer_vacation,
                      'winter_vacation':winter_vacation,
                      'autum_vacation':autum_vacation,
                  })
def tc_issued(request):
    # if a search request is sent
    if request.method == "POST":
        name=request.POST['name']
        if not name:
            tcs_issued=TC.objects.all()[:200]
            return render(request,"website/tc_issued.html",{
                'tc':tcs_issued
            })
        try:
            # try getting the Student_Name,name of field that is used to search,that contains the search name and return 200
            tcs_issued=TC.objects.filter(Student_Name__contains=f'{name}')[:200]
            return render(request,"website/tc_issued.html",{
            'tc_search':tcs_issued
        })
            # if no objects are returned error is sent and a empty table is returned 
        except:
            tcs_issued=None  
            return render(request,"website/tc_issued.html",{
                'tc_search':tcs_issued
                })
    else:
        tcs_issued=TC.objects.all()[:200]
        return render(request,"website/tc_issued.html",{
            'tc':tcs_issued
        })
def vmc_members(request):
    vmc_members=vmc_member.objects.all()
    return render(request,"website/vmc_members.html",{
        'members':vmc_members
    })
def committees(request):
    committee=Committies.objects.all()
    return render(request,"website/committes.html",
                  {
                      "committee":committee
                  })
def notice(request):
    notice_data=Notice.objects.all()[::-1][:10]
    return render(request,"website/notice.html",{
        'notice_data':notice_data,
    })
def news_and_events(request):
    events = News_and_Events.objects.all()[::-1][:24]
    paginator=Paginator(events,8)
    page=request.GET.get("page") 
    events=paginator.get_page(page)
    return render(request,"website/news_and_events.html",{
        "events":events
    })
def other_class(request):
    data=Admissions.objects.all()
    return render(request,"website/other_class.html",{
        "data":data
    })
def alumni(request):
    # get form data and send email to request to add the alumnis data
    if request.method == 'POST':
        name=request.POST['name'] 
        phone=request.POST['phone']
        year_passed=request.POST['year']
        describe=request.POST['description']
        email=request.POST['email']
        send_mail(
            'Alumni form submitted',
            f"Name: {name} \nPhone Number:  {phone}  \nYear Passed:  {year_passed} \nCurrent Position: {describe} \nEmail: {email} \nAn Alumni form has been submitted to the website please contact the alumnus and add their data to the website \nThis is an auto-generated message",
            name,
            ['eoikvkathmandu@gmail.com']
        )
        return HttpResponseRedirect(reverse('index'))
    else:
        alumni_data=Alumni.objects.all()[::-1][:10]
        return render(request,"website/alumni.html",{
            'alumni_data':alumni_data,
        })
def achievements(request):
    achive=achievement.objects.all()[::-1][:10]
    return render(request,"website/achievement.html",{
        'achievements':achive
    })
def newsletter(request):
    news_letter=News_letter.objects.all()[::-1][:20]
    return render(request,"website/newsletter.html",{
        'news_letter':news_letter
    })
def members_list(request):
    # there is ABCD for sorting so Principal is Aprincipal and he comes in the first place
    members_list=member_list.objects.all().order_by("designation")
    return render(request,"website/members_list.html",{
        'members':members_list
    })
def vacancy(request):
    vacany_post=None
    vacany_present=False
    vacany_post=Vacancy.objects.all()
    if vacany_post:
        vacany_present=True
    return render(request,"website/vacancy.html",{
        "vacancy":vacany_post,
        "vacant":vacany_present
    })
def gallery(request):
    gallery = News_and_Events.objects.all()[::-1][:27]
    paginator=Paginator(gallery,9)
    page=request.GET.get("page") 
    gallery=paginator.get_page(page)
    return render(request,"website/gallery.html",{
        'gallery':gallery})
def fees(request):
    fee=Fee_structure.objects.get()
    return HttpResponseRedirect(f'{fee.file.url}')
def show_event(request,pk):
    return render(request,'website/show_event.html',{
        "event":News_and_Events.objects.get(pk=pk)
    })
def rickroll(request):
    # for people who get to into the weeds of the page
    return HttpResponseRedirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
def download(request):
    # check if super user is accessing the download page
    if request.user.is_authenticated:
        if request.user.is_superuser:
            shutil.make_archive("backup/media",'zip',f'{settings.BASE_DIR}/media')
            shutil.make_archive("backup/main_app",'zip',f'{settings.BASE_DIR}/main_app')
            shutil.make_archive("backup/website",'zip',f'{settings.BASE_DIR}/website')
            shutil.copyfile(f'{settings.BASE_DIR}/db.sqlite3', 'backup/db.sqlite3')
            shutil.copyfile(f'{settings.BASE_DIR}/manage.py', 'backup/manage.py')
            shutil.copyfile(f'{settings.BASE_DIR}/package-lock.json', 'backup/package-lock.json')
            shutil.copyfile(f'{settings.BASE_DIR}/package.json','backup/package.json')
            shutil.make_archive("backup",'zip',f'{settings.BASE_DIR}/backup')
            # rb is to make sure that everything is read 
            zip_file = open(f'{settings.BASE_DIR}/backup.zip', 'rb')
            response = HttpResponse(zip_file, content_type='application/force-download')
            response['Content-Disposition'] = 'attachment; filename="%s"' % 'backup.zip'
            return response
        else:
            return HttpResponseRedirect(reverse("rick"))
    else:
        return HttpResponseRedirect(reverse("rick"))
def disclosure(request):
    try:
        file=Disclosure.objects.get()
        return HttpResponseRedirect(f'{file.file.url}')
    except:
        return HttpResponseRedirect(reverse('index'))

def report(request):
    try:
        file=Affiliation.objects.get()
        return HttpResponseRedirect(f'{file.file.url}')
    except:
        return HttpResponseRedirect(reverse('index'))

def result(request):
    try:
        file=Result_Analysis.objects.get()
        return HttpResponseRedirect(f'{file.file.url}')
    except:
        return HttpResponseRedirect(reverse('index'))
def activity_calender(request):
    try:
        file=Calender_of_Activities.objects.get()
        return HttpResponseRedirect(f'{file.file.url}')
    except:
        return HttpResponseRedirect(reverse('index'))
def enrollment(request):
    try:
        file=Enrollment.objects.get()
        return HttpResponseRedirect(f'{file.file.url}')
    except:
        return HttpResponseRedirect(reverse('index'))
def teacher_achievement(request):
    achive=teachers_achievement.objects.all()[::-1][:10]
    return render(request,"website/teachers_achievement.html",{
        'achievements':achive
    })
def video_gallery(request):
    video_gallery = Video_gallery.objects.all()[::-1][:27]
    paginator=Paginator(video_gallery,9)
    page=request.GET.get("page") 
    video_gallery=paginator.get_page(page)
    return render(request,"website/video_gallery.html",{
        'video_gallery':video_gallery})

def archive(request):
    archive = News_and_Events.objects.all()
    paginator=Paginator(archive,9)
    page=request.GET.get("page") 
    archive=paginator.get_page(page)
    return render(request,"website/archive.html",{
        'gallery':archive})
