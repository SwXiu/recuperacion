from django.shortcuts import render, get_object_or_404, redirect
from .models import Poema


# Create your views here.
def listaPoemas(request, categoria):
    categorias = ["Romantico", "Tragico", "Drama"]

    categoriaSeleccionada = categoria

    if categoriaSeleccionada:
        poemas = Poema.objects.filter(categoria__icontains = categoriaSeleccionada)
    else:
        poemas = Poema.objects.all()

    return render(request, "index.html", {
        "categorias": categorias,
        "poemas": poemas,
        "categoriaSeleccionada": categoriaSeleccionada
    })

def likePoema(request, poema_id):
    poema = get_object_or_404(Poema, id=poema_id)
    poema.likes += 1
    poema.save()
    return redirect('poemas:listaPoemas', categoria=poema.categoria)