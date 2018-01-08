from django.shortcuts import render, HttpResponse, Http404
from django.template.loader import render_to_string
from functionality.scrapper import get_rates_by_name


# 1-BTC, 2-ETH, 3-LTC
gpus_abilities = {
    'GTX1070': [0.001, 0.002, 0.003],
    'GTX1050TI': [0.0006, 0.0025, 0.0027],
    'AMD580RX': [0.0008, 0.0015, 0.0035],
}

currencies = ['Bitcoin', 'Ethereum', 'Litecoin']


def index(request):
    return render(request, 'functionality/index.html')


def calculations(request):
    if request.is_ajax():
        id = int(request.POST['currency'])
        GTX1070 = int(request.POST['GTX1070'])
        GTX1050TI = int(request.POST['GTX1050TI'])
        AMD580RX = int(request.POST['AMD580RX'])

        rates = get_rates_by_name(currencies[id])
        current_rate = round(rates[0], 3)
        previous_rate = round(current_rate - rates[1], 3)

        crypt_result = round(gpus_abilities['GTX1070'][id] * GTX1070 +
                 gpus_abilities['GTX1050TI'][id] * GTX1050TI +
                 gpus_abilities['AMD580RX'][id] * AMD580RX, 6)

        usd_result = round(crypt_result * current_rate, 3)

        context = {'cur_rate': current_rate, 'prev_rate': previous_rate,
                   'crypt_result': crypt_result, 'usd_result': usd_result,
                   'crypt_name': currencies[id]}
        html = render_to_string('functionality/_results.html', context)
        return HttpResponse(html)
    else:
        raise Http404