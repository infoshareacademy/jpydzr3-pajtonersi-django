from django.shortcuts import render


from med_doc.forms import VisitForm
from med_doc.models import Visit


def create_visit(request):
    template_name = 'med_doc/create_visit.html'
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            visit = Visit(**form.cleaned_data)
            visit.save()
            return render(request, template_name, context={'form': VisitForm()})
        return render(request, template_name, context={'form': VisitForm(request.POST)})

    elif request.method == 'GET':
        return render(request, template_name, context={'form': VisitForm()})
    else:
        raise Exception('Method not allowed')  #TODO: use proper error code
