from django.db.models import Count, F
from django.shortcuts import get_object_or_404, render

from .models import Atleta, Equipe, Modalidade


def index(request):
    equipes = Equipe.objects.annotate(
        total_atletas=Count("atletas", distinct=True),
        tecnico_nome=F("tecnico__nome"),
    ).order_by("nome")
    modalidades = Modalidade.objects.all()
    return render(request, "jogos/index.html", {"equipes": equipes, "modalidades": modalidades})


def equipe(request, id):
    equipe = get_object_or_404(
        Equipe.objects.annotate(
            total_atletas=Count("atletas", distinct=True),
            tecnico_nome=F("tecnico__nome"),
            tecnico_email=F("tecnico__email"),
            tecnico_telefone=F("tecnico__telefone"),
        ),
        pk=id,
    )
    atletas = Atleta.objects.filter(equipe=equipe).prefetch_related("modalidades").order_by("nome")
    return render(request, "jogos/equipe.html", {"equipe": equipe, "atletas": atletas})


def modalidade(request, id):
    modalidade = get_object_or_404(
        Modalidade.objects.annotate(total_atletas=Count("atletas", distinct=True)),
        pk=id,
    )
    atletas = (
        Atleta.objects.filter(modalidades=modalidade)
        .select_related("equipe")
        .prefetch_related("modalidades")
        .distinct()
        .order_by("nome")
    )
    return render(request, "jogos/modalidade.html", {"modalidade": modalidade, "atletas": atletas})
