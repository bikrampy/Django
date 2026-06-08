from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  return render(request, 'index.html')

def analyzetext(request):
    userText = request.POST.get('userText', '')
    operation = request.POST.get('operation', 'off')
    if userText != "" and operation == "removepunc":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzedText = ""
        for char in userText:
            if char not in punctuations:
                analyzedText += char
        params = {'purpose': 'After Removing Punctuations', 'analyzed_text': analyzedText}
        return render(request, 'analyze.html', params)
    
    elif userText != "" and operation == "toUppercase":
        analyzedText = ""
        for char in userText:
            analyzedText += char.upper()
        params = {'purpose': 'After Caonverting to Uppercase', 'analyzed_text': analyzedText}
        return render(request, 'analyze.html', params)
    
    elif userText != "" and operation == "newlineremover":
        analyzedText = ""
        for char in userText:
            if char != '\n' and char != '\r':
                analyzedText += char
        print(analyzedText)
        params = {'purpose': 'After Removing New Letter', 'analyzed_text': analyzedText}
        return render(request, 'analyze.html', params)
    
    elif userText != "" and operation == "spaceremover":
        analyzedText = ""
        prev_char = ""
        for char in userText:
            if not (char == " " and prev_char == " "):
                analyzedText += char
            prev_char = char
        params = {'purpose': 'After Removing Extra Space', 'analyzed_text': analyzedText}
        return render(request, 'analyze.html', params)
    
    elif userText != "" and operation == "charactercount":
        analyzedText = 0
        for char in userText:
            if char != "\r" and char != "\n" and char != " ":
                analyzedText += 1
        params = {'purpose': 'After Counting Characters', 'analyzed_text': analyzedText}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')
