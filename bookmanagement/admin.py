from django.contrib import admin
from .models import BookOwner,Author,Book,BookTransactionModel,QuotationFromBook,Comments
# Register your models here.



admin.site.register(BookOwner)
admin.site.register(Author)
admin.site.register(BookTransactionModel)
admin.site.register(Book)
admin.site.register(Comments)

