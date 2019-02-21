from django.forms import ModelForm
from cms.models import Book, Impression
from requests import request
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'content')

class ImpressionForm(ModelForm):
    class Meta:
        model = Impression
        fields = ('comment',)

