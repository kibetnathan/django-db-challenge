from django.contrib import admin
from .models import Blog, Author, Subscriber

# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ("title", "author", "published_date")
#     search_fields = ("title", "text")
#     list_filter = ("published_date",)

# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ("name", "email", "age")
#     search_fields = ("name", "email")

# admin.site.register(Blog)
# admin.site.register(Author)
# admin.site.register(Subscriber)
# # admin.site.register(ContactForm)
