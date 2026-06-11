from django.shortcuts import render

MODELS = {
    'budslive': {
        'name': 'Samsung Galaxy Buds Live',
        'description': 'Бездротові навушники з активним шумозаглушенням та унікальним дизайном «бобів».',
        'price': '≈ 150 USD'
    },
    'airpods': {
        'name': 'Apple AirPods',
        'description': 'Популярні бездротові навушники з автоматичним підключенням та підтримкою Siri.',
        'price': '≈ 160 USD'
    },
    'sonywf1000xm4': {
        'name': 'Sony WF-1000XM4',
        'description': 'Флагманські TWS-навушники з найкращим шумозаглушенням та підтримкою LDAC.',
        'price': '≈ 280 USD'
    },
    'boseqc': {
        'name': 'Bose QuietComfort Earbuds',
        'description': 'Комфортні навушники з преміальним шумозаглушенням та глибоким басом.',
        'price': '≈ 270 USD'
    },
    'jbltune': {
        'name': 'JBL Tune 230NC',
        'description': 'Доступні навушники з активним шумозаглушенням та потужним звуком JBL Pure Bass.',
        'price': '≈ 100 USD'
    }
}

def show_model(request):
    model = request.GET.get('model', '').lower()
    info = MODELS.get(model) if model else None
    return render(request, 'headphones/model.html', {'info': info, 'models': MODELS})
