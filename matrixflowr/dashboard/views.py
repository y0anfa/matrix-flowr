from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from matrix.models import Matrix, Flow, Comment

# Create your views here.


@require_http_methods(["GET"])
@login_required
def view_dashboard(request):
    matrices = Matrix.objects.all().order_by("-created_at")
    for matrix in matrices:
        matrix.nb_active_flows = Flow.objects.filter(matrix=matrix.id).filter(is_active=True).count()
        matrix.nb_comments = Comment.objects.filter(matrix=matrix.id).count()

    return render(request, "dashboard/view_dashboard.html", {"matrices": matrices})