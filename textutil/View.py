
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request, 'index.html')



def analyze(request):
   # Get the text
   djname = request.POST.get('text', 'default')
   removepunc = request.POST.get('analyze', 'off')
   spaceremover = request.POST.get('spaceremover', 'off')
   newlineremover = request.POST.get('newlineremover', 'off')
   upper = request.POST.get('upper', 'off')

    #which button is cheacked:
   if removepunc=="on":
      punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
      analyzed = ""
      for char in djname:
         if char not in punctuations:
            analyzed = analyzed + char
      params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
      djname = analyzed

   if newlineremover == 'on':
       analyzed = ''
       for char in djname:
           if char != '\n' and char != '\r':
             analyzed = analyzed + char
       params = {'purpose': 'newlineremover', 'analyzed_text': analyzed}
       djname = analyzed

   if upper == 'on':
       analyzed = ""
       for char in djname:
           analyzed = analyzed + char.upper()
       params = {'purpose': 'upper', 'analyzed_text': analyzed}
       djname = analyzed

   if spaceremover=='on':
       analyzed =""
       for index, char in enumerate(djname):
           if not(djname[index] == " " and djname[index+1] == " "):
               analyzed = analyzed + char
       params = {'purpose': 'Spaceremover', 'analyzed_text': analyzed}

   if (removepunc != "on" and newlineremover != "on" and spaceremover != "on" and upper != "on"):
    return HttpResponse("please select any operation and try again")

   return render(request, 'punctuation.html', params)

def about(request):
    return render(request, 'about1.html')




