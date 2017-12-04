from __future__ import print_function
import os
import time
from mailmerge import MailMerge
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from accounts import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
)
from django.contrib.auth.decorators import login_required
from accounts.forms import FancyFormPzsBozpPo
from accounts.models import Document, ProcessedDocument
from accounts.forms import DocumentForm
from django.conf import settings
# Create your views here.
from jk.settings import MEDIA_DIR, BASE_DIR


class SignUpToOurJKPortal(CreateView):
    form_class = forms.UserCreationForm
    """
        success_url has a special function so
        when someone has sucessfully sign up 
        for our web page application then 
        use reverse_lazy function and send him/her 
        to 'login' page :)
    """
    success_url = reverse_lazy('login')
    template_name = 'accounts/SignUpToOurJKPortal.html'


class DocumentDeleteView(LoginRequiredMixin, DeleteView):

    model = Document
    success_url = reverse_lazy('accounts:list_document')


class ProcessedDocumentDeleteView(LoginRequiredMixin, DeleteView):

    model = ProcessedDocument
    success_url = reverse_lazy('accounts:list_document')


# class SelectProcessView(LoginRequiredMixin, ListView):
#     """
#     This section will allow us to pick particular
#     previously uploaded documents in form of checkboxes
#     """
#     model = Document
#     template_name = 'accounts/SelectProcessView.html'

@login_required()
def SelectProcessView(request):
    form_class = FancyFormPzsBozpPo
    # form2 = Document.objects.all()
    form2 = Document.objects.filter(user=request.user)

    return render(request, 'accounts/SelectProcessView.html', {'form1': form_class, 'form2': form2})


@login_required()
def collect_templates(request):

    if request.method == 'POST':
        custom_name = request.POST.getlist('custom_name')
        list_of_selected_paths = request.POST.getlist('identifier_for_my_class')
        mandant_obchodne_meno = request.POST.getlist('mandant_obchodne_meno')
        mandant_sidlo = request.POST.getlist('mandant_sidlo')
        mandant_ICO = request.POST.getlist('mandant_ICO')
        mandant_DIC = request.POST.getlist('mandant_DIC')
        mandant_IC_DPH = request.POST.getlist('mandant_IC_DPH')
        mandant_zapis = request.POST.getlist('mandant_zapis')
        mandant_zastupenie = request.POST.getlist('mandant_zastupenie')
        mandant_email = request.POST.getlist('mandant_email')
        mandant_telefon = request.POST.getlist('mandant_telefon')
        suma_pzs = request.POST.getlist('suma_pzs')
        suma_po = request.POST.getlist('suma_po')
        suma_bozp = request.POST.getlist('suma_bozp')
        datum = request.POST.getlist('datum')
        miesto = request.POST.getlist('miesto')

        filled_dict = {"mandant_obchodne_meno":mandant_obchodne_meno[0],
                       "mandant_sidlo":mandant_sidlo[0],
                       "mandant_ICO":mandant_ICO[0],
                       "mandant_DIC":mandant_DIC[0],
                       "mandant_IC_DPH":mandant_IC_DPH[0],
                       "mandant_zapis":mandant_zapis[0],
                       "mandant_zastupenie":mandant_zastupenie[0],
                       "mandant_email":mandant_email[0],
                       "mandant_telefon":mandant_telefon[0],
                       "suma_pzs":suma_pzs[0],
                       "suma_po":suma_po[0],
                       "suma_bozp":suma_bozp[0],
                       "datum":datum[0],
                       "miesto":miesto[0]}

        def process_with_mail_merge(input_file, _filled_dict, user_defined_name):
            original_path = input_file
            #print('funkcia: {}'.format(BASE_DIR + input_file))
            input_file = BASE_DIR + input_file
            document = MailMerge(input_file)
            _out_name = original_path.strip('.docx') + user_defined_name + '.docx'
            document.merge(**_filled_dict)
            document.write(BASE_DIR + _out_name)
            return _out_name

        '''
        user_id_list => simply stores my USER ID 
        for example: Jano has been signed up for this page as the first person after admin user 
                     that's why it has USER ID: 2
        '''
        user_id_list = []
        currently_processed_files = []
        for i in list_of_selected_paths:

            user_idx = Document.objects.get(doc_file=i.strip('/media/')).user_id
            user_id_list.append(user_idx)
            userx = Document.objects.get(doc_file=i.strip('/media/')).user
            doc_filex = Document.objects.get(doc_file=i.strip('/media/')).doc_file
            namex = Document.objects.get(doc_file=i.strip('/media/')).name
            idx = Document.objects.get(doc_file=i.strip('/media/')).id
            # #print('\nbase_dir+i: {}\nselected file: {}\nuser_idx: {}\nuserx: {}\ndoc_filex: {}\nnamex: {}\nidx:{}'.format(BASE_DIR + i, i, user_idx, userx, doc_filex, namex, idx))
            # #print('*************')

            # doc_filex: user_2/pracovna_zdravotna_sluzba_mfMZhiJ.docx
            # oi = process_with_mail_merge(i, filled_dict, namex.replace(' ', '_'))
            oi = process_with_mail_merge(i, filled_dict, time.strftime("%Y.%m.%d.%H.%M.%S")+'_'+ namex + '_' + custom_name[0])
            display_name = time.strftime("%Y.%m.%d.%H.%M.%S")+'_'+ namex + '_' + custom_name[0]
            ProcessedDocument(user_id=user_idx, display_name=display_name,
                              path_to_processed_file=oi).save()
            currently_processed_files.append(display_name)

        # for i in ProcessedDocument.objects.all().values(): #print(i)
        # {'id': 1, 'user_id': 2, 'display_name': 'pzs jano', 'path_to_processed_file': 'some_path.docx',
        #  'date_upload': datetime.date(2017, 11, 15)}
        #print(currently_processed_files)
        try:
            processed_documents = ProcessedDocument.objects.filter(display_name__in=currently_processed_files)
        except ProcessedDocument.DoesNotExist:
            processed_documents = ProcessedDocument.objects.all()

        return render(request,
                      'accounts/success.html',
                      {'processed_documents': processed_documents})
    else:
        return render(request,
                      'accounts/success.html',
                      {'documents': 'something is wrong!', 'rendered_docs': []})


@login_required()
def list_document(request):

    if request.method == 'POST':

        form = DocumentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            # NEW CODE
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

    else:
        form = DocumentForm()

    '''
    This section only searches through the database tables
    '''
    # documents_data = Document.objects.all()
    documents_data = Document.objects.filter(user=request.user)
    # processed_document_data = ProcessedDocument.objects.all()
    processed_document_data = ProcessedDocument.objects.filter(user=request.user)

    return render(
        request,
        'accounts/list_document.html',
        {'documents_data': documents_data, 'processed_document_data': processed_document_data, 'form': form},

    )


@login_required()
def generate_table(request):

    table = []
    for i in range(0,5):
        a = dict(name='name',
                 weight='20g',
                 lipid='3',
                 saturated='2',
                 sacharides='10',
                 sugar='0',
                 protein='12',
                 salt='5',
                 desc='some text')
        table.append(a)
    
    #print('BASE_DIR: {}'.format(BASE_DIR))
    return render(
        request,
        'accounts/initial_table.html',
        {'table_data': table, 'base_dir': BASE_DIR},
    )

