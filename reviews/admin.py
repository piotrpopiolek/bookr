from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book, BookContributor, Review)

class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn', 'isbn13')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn', 'publisher__name__startswith')

def initialled_name(obj):
    """ obj.first_names='Jerome David', obj.last_names='Salinger'
        => 'Salinger, JD' """
    initials = ''.join([name[0] for name in obj.first_names.split(' ')])
    return "{}, {}".format(obj.last_names, initials)

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names','initialled_name')
    list_filter = ('last_names',)
    search_fields = ('last_names__startswith', 'first_names')

class ReviewAdmin(admin.ModelAdmin):
    exclude = ('date_edited',)
    fieldsets = (('Łącza', {'fields': ('creator', 'book')}), ('Zawartość recenzji', {'fields': ('content', 'rating')}))

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)
