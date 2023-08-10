from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Matrix, Flow, Comment


class MatrixForm(ModelForm):
    class Meta:
        model = Matrix
        fields = ["name", "description", "vendor", "product"]
        labels = {
            "name": _("Name"),
            "description": _("Description"),
            "vendor": _("Product vendor"),
            "product": _("Product model")
        }
        error_messages = {
            "name": {
                "max_length": _("The matrix' name is too long.")
            },
            "vendor": {
                "max_length": _("The product's vendor name is too long.")
            },
            "product": {
                "max_length": _("The product's model name is too long.")
            }
        }


class FlowForm(ModelForm):
    class Meta:
        model = Flow
        fields = ["name", "description", "source", "destination", "is_opened"]
        labels = {
            "name": _("Name"),
            "description": _("Description"),
            "source": _("Source IP address"),
            "destination": _("Destination IP address"),
            "is_opened": _("Flow opened ?")
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        labels = {
            "content": _("Comment")
        }