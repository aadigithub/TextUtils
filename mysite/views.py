from django.http import HttpResponse
from django.shortcuts import render,redirect

def index(request):
    return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # get value from checkbox
    removepunc1 = request.POST.get('removepunc', 'off')
    fullcaps1 =request.POST.get('fullcaps','off')
    spaceremove1 =request.POST.get('removespace', 'off')
    charcount1 = request.POST.get('charcount', 'off')
    # Check which checkbox is on

    if removepunc1 == 'on':
        punc = '''!()[]{};"'\,<>.?/@#$%^&*~'''
        analyze1 = ''
        for char in djtext:
            if char not in punc:
                analyze1 = analyze1 + char
        param = {'purpose':'Removed punctuations','analyzed_text': analyze1}
        djtext = analyze1

    if fullcaps1 == 'on':
        analyze1 =''
        for char in djtext:
            analyze1 =  analyze1 + char.upper()
        param = {'purpose': 'Captalized Text', 'analyzed_text': analyze1}
        djtext = analyze1

    if spaceremove1 == 'on':
        analyze1 = ''
        for char in djtext:
            analyze1 = analyze1 + char.strip()
        param = {'purpose': 'Remove space', 'analyzed_text': analyze1}
        djtext = analyze1


    if charcount1 == 'on':
        char_count = 0
        for char in djtext:
            if char.isspace() != True:
                char_count = char_count +1
        param = {'purpose': 'No of character', 'analyzed_text': char_count}

        if (removepunc1 != 'on' and charcount1 != 'on' and spaceremove1 != 'on' and fullcaps1 != 'on'):
            return render(request, 'error.html')
    return render(request, 'analyze.html', param)
    # Analyze the text



