from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = [
        {
            'who_entered': x.passcard.owner_name,
            'entered_at': x.entered_at,
            'duration': x.format_duration()
        }
        for x in Visit.objects.all() if x.leaved_at == None
    ]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
