from django.shortcuts import render


def main(request):
    if request.method == 'GET':
        template = 'index.pug'
        return render(request, template, {})
