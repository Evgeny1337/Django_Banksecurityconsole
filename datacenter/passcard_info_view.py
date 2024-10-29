from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = [
        {
            'entered_at': x.entered_at,
            'duration': x.format_duration(),
            'is_strange': x.is_visit_long()
        }
        for x in Visit.objects.filter(passcard=passcard)
    ]
    # Программируем здесь
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
