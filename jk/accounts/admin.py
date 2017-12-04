from django.contrib import admin
from accounts import models
# Register your models here.


class DocumentAdmin(admin.ModelAdmin):

    ''' order of fields '''
    fields = ['doc_file', 'date_upload', 'name', 'user']

    ''' search bar in admin portal '''
    search_fields = ['doc_file', 'date_upload', 'name', 'user']

    ''' adding filterable fields '''
    list_filter = ['doc_file', 'date_upload', 'name', 'user']

    '''  '''
    list_display = ['doc_file', 'date_upload', 'name', 'user']

    ''' editable fileds has to be also in 'list_display'  '''
    # list_editable = ['length']


class ProcessedDocumentAdmin(admin.ModelAdmin):

    ''' order of fields '''
    fields = ['path_to_processed_file', 'date_upload', 'user', 'display_name']

    ''' search bar in admin portal '''
    search_fields = ['path_to_processed_file', 'date_upload', 'user', 'display_name']

    ''' adding filterable fields '''
    list_filter = ['path_to_processed_file', 'date_upload', 'user', 'display_name']

    '''  '''
    list_display = ['path_to_processed_file', 'date_upload', 'user', 'display_name']

    ''' editable fileds has to be also in 'list_display'  '''
    # list_editable = ['length']


admin.site.register(models.Document, DocumentAdmin)
admin.site.register(models.ProcessedDocument, ProcessedDocumentAdmin)


