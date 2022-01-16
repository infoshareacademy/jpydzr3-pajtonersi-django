from django.shortcuts import render


from med_doc.forms import VisitForm



def create_visit(request):
    template_name = ''
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template_name, context={'form': VisitForm()})
        return render(request, template_name, context={'form': VisitForm(request.POST)})

    elif request.mthod == 'GET':
        return render(request, template_name, context={'form': VisitForm()})
    else:
        raise Exception('Method not allowed')  #TODO: use proper error code