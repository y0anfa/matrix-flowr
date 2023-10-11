from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.utils.text import slugify

from .models import Matrix, Flow, Comment
from .forms import MatrixForm, FlowForm, CommentForm

# Create your views here.


@require_http_methods(["GET"])
@login_required
def matrices_list(request):
    matrices = Matrix.objects.all().order_by("-created_at")
    for matrix in matrices:
        matrix.nb_active_flows = Flow.objects.filter(matrix=matrix.id).filter(is_active=True).count()
        matrix.nb_comments = Comment.objects.filter(matrix=matrix.id).count()

    return render(request, "matrix/matrices_list.html", {"matrices": matrices})


@require_http_methods(["GET"])
@login_required
def view_matrix(request, id):
    matrix = Matrix.objects.get(id=id)
    flows = Flow.objects.filter(matrix=id)
    comments = Comment.objects.filter(matrix=id).order_by("-created_at")

    return render(request, "matrix/view_matrix.html", {"matrix": matrix, "flows": flows, "comments": comments})


@require_http_methods(["GET", "POST"])
@login_required
def create_matrix(request):
    if request.method == "POST":
        form = MatrixForm(request.POST)

        if form.is_valid():
            new_matrix = form.save(commit=False)

            new_matrix.slug = slugify(new_matrix.name)
            new_matrix.created_by = request.user
            new_matrix.updated_by = request.user
            new_matrix.save()

            form.save_m2m()

            return redirect("matrices_list")

    else:
        return render(request, "matrix/create_matrix.html")


@require_http_methods(["GET", "POST"])
@login_required
def edit_matrix(request, id):
    matrix = Matrix.objects.get(id=id)

    if request.method == "POST":
        form = MatrixForm(request.POST, instance=matrix)

        if form.is_valid():
            form.slug = slugify(form.cleaned_data['name'])
            form.updated_by = request.user

            form.save()

            return redirect("view_matrix", matrix.id)

    else:
        return render(request, "matrix/edit_matrix.html", {"matrix": matrix})


@require_http_methods(["GET"])
@login_required
def confirm_delete_matrix(request, id):
    matrix = Matrix.objects.get(id=id)
    return render(request, "matrix/confirm_delete_matrix.html", {"matrix": matrix})


@require_http_methods(["GET"])
@login_required
def delete_matrix(request, id):
    matrix = Matrix.objects.get(id=id)
    matrix.delete()
    return redirect("matrices_list")


@require_http_methods(["GET", "POST"])
@login_required
def create_flow(request, matrix_id):
    if request.method == "POST":
        form = FlowForm(request.POST)

        if form.is_valid():
            new_flow = form.save(commit=False)
            matrix = Matrix.objects.get(id=matrix_id)

            new_flow.slug = slugify(new_flow.name)
            new_flow.matrix = matrix
            if request.POST.get("is_opened") == "on":
                new_flow.is_opened = True
            else:
                new_flow.is_opened = False
            new_flow.created_by = request.user
            new_flow.updated_by = request.user
            new_flow.save()

            form.save_m2m()

            return redirect("view_matrix", matrix_id)

    else:
        return render(request, "matrix/create_flow.html", {"matrix_id": matrix_id})


@require_http_methods(["GET", "POST"])
@login_required
def edit_flow(request, matrix_id, flow_id):
    flow = Flow.objects.get(id=flow_id)
    matrix = Matrix.objects.get(id=matrix_id)

    if request.method == "POST":
        form = FlowForm(request.POST, instance=flow)

        if form.is_valid():
            form.slug = slugify(form.cleaned_data['name'])
            form.updated_by = request.user

            form.save()

            return redirect("view_matrix", matrix_id)

    else:
        return render(request, "matrix/edit_flow.html", {"matrix": matrix, "flow": flow})


@require_http_methods(["GET"])
@login_required
def toggle_flow(request, matrix_id, flow_id):
    flow = Flow.objects.get(id=flow_id)
    flow.is_active = not flow.is_active
    flow.save()
    return redirect("view_matrix", matrix_id)


@require_http_methods(["GET"])
@login_required
def confirm_delete_flow(request, matrix_id, flow_id):
    matrix = Matrix.objects.get(id=matrix_id)
    flow = Flow.objects.get(id=flow_id)
    return render(request, "matrix/confirm_delete_flow.html", {"matrix": matrix, "flow": flow})


@require_http_methods(["GET"])
@login_required
def delete_flow(request, matrix_id, flow_id):
    flow = Flow.objects.get(id=flow_id)
    flow.delete()
    return redirect("view_matrix", matrix_id)


@require_http_methods(["POST"])
@login_required
def create_comment(request, matrix_id):
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)

            matrix = Matrix.objects.get(id=matrix_id)

            new_comment.author = request.user
            new_comment.matrix = matrix

            new_comment.save()

            form.save_m2m()

            return redirect("view_matrix", matrix_id)

    else:
        return Http404()


@require_http_methods(["GET"])
@login_required
def delete_comment(request, matrix_id, comment_id):
    comment = Comment.objects.get(id=comment_id)

    if comment.author == request.user:
        comment.delete()
        return redirect("view_matrix", matrix_id)
    else:
        return HttpResponse(status=401)
