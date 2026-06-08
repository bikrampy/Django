from django.shortcuts import redirect, render

def home(request):
    return render(
        request,
        "home.html",
        {
            "name": "Bikram",
            'age': 23,
            'about': "He is a passionate web developer currently focusing on learning Django web framework",
            'favMovies': {
                'YJHD': 2009,
                "Barfi": 2010
            },
            'skills': ['Django', "Nodejs", 'Reactjs']
        }
    )