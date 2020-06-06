from django.shortcuts import render
from .models import Project, Author


def portfolio(request):
    if request.method == 'POST':

        if request._post['button'] == 'Crear':
            try:
                autor = Author.objects.get(name='Fernando')
                print('El autor ya existe')
            except:
                autor = Author.objects.create(name='Fernando')
                autor.save()

        elif request._post['button'] == 'Borrar':
            try:
                autor = Author.objects.get(name='Fernando')
                autor.delete()
            except:
                print("El autor no existe")
        elif request._post['button'] == 'Post':
            print(type(request._post))

        projects = Project.objects.all()
        return render(request, 'portfolio/portfolio.html', {'projects':projects})

    else:
        projects = Project.objects.all()
        print(type(projects))
        return render(request, 'portfolio/portfolio.html', {'projects':projects})

# def create_author():

    # autor = Author.objects.create(name="Ferandndo")
    # autor.save()


# ****** NOTAS RELACIONADAS CON REQUEST ******

        # print(request._post)

        # diccionario = list(i for i in request.__dict__)
        # for i in diccionario:
        #     print(i, request.__dict__[i])

        # for i in request.__dict__:
        #     print(i)

        # autor = Author.objects.create(name="prueba")
        # autor.save()
