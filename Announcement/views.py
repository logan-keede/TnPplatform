from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Announcement
# Create your views here.

def announcements_list(request):
    announcements = Announcement.objects.all()
    paginator = Paginator(announcements, 10) # Show 10 announcements per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'announcements.html', {'page_obj': page_obj})