from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from matrix.models import Matrix, Flow, Comment

# Create your views here.

@login_required
def view_dashboard(request):
    matrices = Matrix.objects.all().order_by("-created_at")
    for matrix in matrices:
        matrix.nb_active_flows = Flow.objects.filter(matrix=matrix.id).filter(is_active=True).count()
        matrix.nb_comments = Comment.objects.filter(matrix=matrix.id).count()

    return render(request, "dashboard/index.html", {"matrices": matrices})