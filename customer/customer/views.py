
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.conf import settings
from django.template import engines
from django.http import HttpResponse


@staff_member_required(login_url='/admin/login/')
def dashboard(request):

    users = User.objects.all().order_by('-date_joined')[:8]

    context = {
        'username': request.user.username,
        'total_users': User.objects.count(),
        'users': users,
    }

    template = engines['django'].from_string(
        settings.ADMIN_DASHBOARD_HTML
    )

    html = template.render(context, request)

    return HttpResponse(html)

