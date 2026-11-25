"""Gera as páginas de cada unidade (messejana/ e santa-maria/) a partir da página principal.

O design fica idêntico ao da página principal (index.html); só o conteúdo muda para a unidade.
Uso, na raiz do repositório:  python3 assets/gerar_unidades_2027.py
"""
import importlib.util
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = "https://8rytdz8k66-cyber.github.io/catalogo-escolaespacocriativo/"

# Respostas da Eli por unidade (sem preços), já usadas antes
_spec = importlib.util.spec_from_file_location("g", os.path.join(RAIZ, "assets", "gerar_catalogo_2027.py"))
_g = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_g)

UNI = {
    "messejana": {
        "nome": "Messejana", "nome_longo": "Unidade Messejana", "faixa": "Berçário ao 5º ano",
        "zap": "5585974007393", "zap_txt": "(85) 97400-7393",
        "insta": "https://www.instagram.com/eecmessejana/",
        "mapa": "https://maps.app.goo.gl/7UgxG8nRy4DjcvGP6",
        "logo_mf": True,
        "lead": "Estamos no coração de Messejana, Fortaleza/CE. Venha conhecer a nossa unidade.",
        "dif_local": ("No coração de Messejana", "Rua Santa Efigênia, 300"),
        "dif_etapas": ("Do Berçário ao 5º ano", "com tempo integral"),
        "etapas_h2": "Do Berçário ao 5º ano, no mesmo caminho",
        "sem_fund2": True,
        "nota_etapas": "Tempo integral disponível no contraturno.",
        "unid_h2": "No coração de Messejana",
        "card": 0,
        "galeria": None,
        "por_dentro": None,
        "rodape_unid": [("Messejana", "Rua Santa Efigênia, 300")],
        "og_img": "img/ref-messejana.jpg",
        "hist2": "Hoje, aqui na Unidade Messejana, seguimos com a mesma tradição de cuidar: a direção, com Evanisse e Elienice, conhece cada aluno e cada família pelo nome. Somos uma alternativa às grandes redes, para famílias que querem uma educação forte com afeto de verdade.",
        "eli_hist": "A Espaço Criativo nasceu em 2002, do sonho de duas irmãs, filhas de professora: Elienice e Evanisse. São mais de 23 anos de tradição em Fortaleza, e aqui na Unidade Messejana a direção conhece cada aluno e cada família pelo nome 💙",
        "desc": "Escola Espaço Criativo, Unidade Messejana (Rua Santa Efigênia, 300, Fortaleza/CE). Do Berçário ao 5º ano, com Programa Bilíngue e Educação Socioemocional. Matrículas 2027.",
    },
    "santa-maria": {
        "nome": "Parque Santa Maria", "nome_longo": "Unidade Parque Santa Maria", "faixa": "Berçário ao 9º ano",
        "zap": "5585994071372", "zap_txt": "(85) 99407-1372",
        "insta": "https://www.instagram.com/criativoespaco_sm/",
        "mapa": "https://maps.google.com/?q=-3.858689,-38.501865",
        "logo_mf": False,
        "lead": "Estamos no Parque Santa Maria, Fortaleza/CE. Venha conhecer a nossa unidade.",
        "dif_local": ("No Parque Santa Maria", "onde a nossa história começou"),
        "dif_etapas": ("A partir de 2 anos até o 9º ano do Ensino Fundamental", "com tempo integral"),
        "etapas_h2": "Do Berçário ao 9º ano, no mesmo caminho",
        "sem_fund2": False,
        "nota_etapas": "Tempo integral disponível. A Creche Espaço Brincar fica ao lado, na Rua Jorge da Veiga, 620.",
        "unid_h2": "No Parque Santa Maria, onde a nossa história começou",
        "card": 1,
        "galeria": [("sm-sala", "Sala de aula", "Sala de aula com crianças nas mesinhas"),
                    ("sm-brinquedoteca", "Brinquedoteca", "Brinquedoteca com escorregadores e piso colorido"),
                    ("sm-corredor", "Corredor colorido", "Corredor com piso colorido e amarelinha das vogais"),
                    ("sm-parquinho", "Parquinho", "Parquinho de areia com casinha de madeira"),
                    ("sm-patio", "Pátio coberto", "Pátio coberto com pebolim")],
        "por_dentro": ("Conheça os espaços da Unidade Parque Santa Maria",
                       "Fotos reais da unidade onde a Espaço Criativo nasceu, em 2002."),
        "rodape_unid": [("Parque Santa Maria", "Rua Jorge da Veiga, 595"),
                        ("Creche Espaço Brincar", "Rua Jorge da Veiga, 620")],
        "og_img": "img/ref-santa-maria-parcial.jpg",
        "hist2": "Foi aqui no Parque Santa Maria que tudo começou, e a tradição de cuidar continua: a direção, com Evanisse e Elienice, conhece cada aluno e cada família pelo nome. Somos uma alternativa às grandes redes, para famílias que querem uma educação forte com afeto de verdade.",
        "eli_hist": "A Espaço Criativo nasceu em 2002, aqui no Parque Santa Maria, do sonho de duas irmãs, filhas de professora: Elienice e Evanisse. Começou numa casa adaptada, com quatro salas, e já são mais de 23 anos de tradição em Fortaleza. A direção conhece cada aluno e cada família pelo nome 💙",
        "desc": "Escola Espaço Criativo, Unidade Parque Santa Maria (Rua Jorge da Veiga, 595, Fortaleza/CE). Do Berçário ao 9º ano, com Programa Bilíngue e Educação Socioemocional. Matrículas 2027.",
    },
}


def troca(s, a, b, n=1):
    achou = s.count(a)
    assert achou == n, f"esperava {n}x, achei {achou}x: {a[:90]!r}"
    return s.replace(a, b)


def entre(s, ini, fim, novo):
    i = s.index(ini)
    j = s.index(fim, i) + len(fim)
    return s[:i] + novo + s[j:]


def gerar(chave, u):
    s = open(os.path.join(RAIZ, "index.html"), encoding="utf-8").read()
    nl, nome, faixa = u["nome_longo"], u["nome"], u["faixa"]

    # Metadados
    s = troca(s, "<title>Escola Espaço Criativo · Matrículas 2027</title>",
              f"<title>Escola Espaço Criativo · {nl} · Matrículas 2027</title>")
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{u["desc"]}">', s, count=1)
    s = troca(s, 'content="Escola Espaço Criativo · Mais que uma escola, um lugar para pertencer!"',
              f'content="Escola Espaço Criativo · {nl} · Mais que uma escola, um lugar para pertencer!"')
    s = troca(s, 'content="Matrículas 2027 · vagas para o Berçário ao 9º ano em Messejana e no Parque Santa Maria, Fortaleza/CE."',
              f'content="Matrículas 2027 · vagas para o {faixa} na {nl}, Fortaleza/CE."')
    s = troca(s, f'<meta property="og:image" content="{URL}img/ref-messejana.jpg">',
              f'<meta property="og:image" content="{URL}{u["og_img"]}">')
    s = troca(s, f'<meta property="og:url" content="{URL}">', f'<meta property="og:url" content="{URL}{chave}/">')

    # Cabeçalho: o logo do Colégio Maria de Fátima é da unidade Messejana
    if not u["logo_mf"]:
        s = troca(s, '\n      <img class="mf" src="img/logo-mf-ref.png" alt="Colégio Maria de Fátima" width="135" height="141">', "")

    # Topo
    s = troca(s, "vagas para o Berçário ao 9º ano</span>", f"vagas para o {faixa}</span>")
    s = troca(s, '<p class="lead">Estamos no coração de Messejana e no Parque Santa Maria, Fortaleza/CE. Venha conhecer as nossas unidades.</p>',
              f'<p class="lead">{u["lead"]}</p>')
    s = troca(s, "<li><b>Messejana e Parque Santa Maria</b><span>duas unidades perto de você</span></li>",
              f"<li><b>{u['dif_local'][0]}</b><span>{u['dif_local'][1]}</span></li>")
    s = troca(s, "<li><b>A partir de 2 anos até o 9º ano do Ensino Fundamental</b><span>com tempo integral</span></li>",
              f"<li><b>{u['dif_etapas'][0]}</b><span>{u['dif_etapas'][1]}</span></li>")

    # Nosso jeito e etapas
    s = troca(s, "Quatro compromissos que valem nas duas unidades, do Berçário ao 9º ano.",
              f"Quatro compromissos que valem todos os dias na {nl}, do {faixa}.")
    s = troca(s, '<h2 class="h2">Do Berçário ao 9º ano, no mesmo caminho</h2>', f'<h2 class="h2">{u["etapas_h2"]}</h2>')
    if u["sem_fund2"]:
        s = troca(s, '\n      <article class="ecard"><small>6º ao 9º ano</small><h3>Fundamental II</h3><p>Projetos, interclasses e vagas também no turno da tarde.</p></article>', "")
        s = troca(s, "<option>Fundamental II (6º ao 9º)</option>", "")
    s = troca(s, '<p class="nota">Tempo integral disponível. Consulte as etapas oferecidas em cada unidade.</p>',
              f'<p class="nota">{u["nota_etapas"]}</p>')

    # Unidade: só o card desta unidade
    s = troca(s, '<span class="eyebrow">Unidades</span>\n    <h2 class="h2">Em Messejana e no Parque Santa Maria</h2>',
              f'<span class="eyebrow">Unidade</span>\n    <h2 class="h2">{u["unid_h2"]}</h2>')
    s = troca(s, "Escolha a unidade e fale direto com a gente. A mensagem já chega dizendo qual unidade você quer conhecer.",
              "Venha conhecer de perto: fale direto com a coordenação da unidade e agende a sua visita.")
    i = s.index('<div class="ucards">')
    j = s.index("</div>\n  </div>\n</section>", i)
    bloco = s[i:j]
    cards = bloco.split('<article class="ucard">')
    manter = cards[1 + u["card"]].rstrip()
    if not manter.endswith("</article>"):
        manter = manter[: manter.rindex("</article>") + len("</article>")]
    s = s[:i] + '<div class="ucards">\n      <article class="ucard">' + manter + "\n    " + s[j:]
    s = troca(s, f"Olá! Vim pelo catálogo e quero agendar uma visita na {nl}.", f"Olá! Vim pelo site e quero agendar uma visita na {nl}.")

    # Galeria
    if u["galeria"]:
        tit, txt = u["por_dentro"]
        s = troca(s, '<h2 class="h2">Conheça os espaços da Unidade Messejana</h2>', f'<h2 class="h2">{tit}</h2>')
        s = troca(s, "Fotos reais da unidade: estrutura nova, pensada para o Berçário e a Educação Infantil.", txt)
        figs = "\n".join(f'      <figure><img src="img/{a}.jpg" alt="{alt}" width="440" height="550" loading="lazy"><figcaption>{c}</figcaption></figure>'
                         for a, c, alt in u["galeria"])
        s = entre(s, '<div class="gal">', "\n    </div>", '<div class="gal">\n' + figs + "\n    </div>")

    # História: só a unidade desta página
    s = troca(s, "<p>Hoje são duas unidades, em Messejana e no Parque Santa Maria, e a mesma tradição de cuidar: a direção, com Evanisse e Elienice, conhece cada aluno e cada família pelo nome. Somos uma alternativa às grandes redes, para famílias que querem uma educação forte com afeto de verdade.</p>",
              f"<p>{u['hist2']}</p>")

    # Formulário: unidade já definida
    s = troca(s, '<form class="form" id="form-visita" novalidate>', f'<form class="form" id="form-visita" data-unidade="{nome}" novalidate>')
    s = re.sub(r'\n      <label for="f-unid">Unidade</label>\n      <select id="f-unid"[^\n]*</select>', "", s, count=1)
    assert 'id="f-unid"' not in s

    # Avaliações: só desta unidade
    notas = re.findall(r'      <a class="nota-g"[^\n]*</a>', s)
    assert len(notas) == 2
    fica = [n for n in notas if (">Messejana</b>" in n) == (chave == "messejana")]
    sai = [n for n in notas if n not in fica]
    s = troca(s, "\n" + sai[0], "")

    # Rodapé
    s = troca(s, "Do Berçário ao 9º ano, preparando para o presente e inspirando o futuro.",
              f"Do {faixa}, preparando para o presente e inspirando o futuro.")
    lis = re.findall(r'          <li><a href="https://www.instagram.com/[^\n]*</li>\n', s)
    assert len(lis) == 2
    s = troca(s, "".join(lis), f'          <li><a href="{u["insta"]}" target="_blank" rel="noopener">Instagram</a></li>\n')
    s = entre(s, "<h4>Unidades</h4>", "</ul>",
              "<h4>Unidade</h4>\n        <ul>\n" + "\n".join(f"          <li><b>{a}</b><span>{b}</span></li>" for a, b in u["rodape_unid"]) + "\n        </ul>")
    s = troca(s, "© 2026 Escola Espaço Criativo · Fortaleza (CE)", f"© 2026 Escola Espaço Criativo · {nl} · Fortaleza (CE)")

    # WhatsApp da unidade e mensagens dizendo de onde a pessoa veio
    s = s.replace("5585994071372", u["zap"]).replace("(85) 99407-1372", u["zap_txt"])
    s = s.replace("Vim pelo catálogo da Escola Espaço Criativo", f"Vim pelo site da {nl} da Escola Espaço Criativo")
    s = s.replace("Vim pelo catálogo", f"Vim pelo site da {nl}")

    # Eli com as informações desta unidade (sem preços e sem falar da outra unidade)
    base = [it for it in _g.eli_base(_g.UNIDADES[chave]) if it["id"] != "outra"]
    for it in base:
        if it["id"] == "historia":
            it["r"] = u["eli_hist"]
            it["chaves"] = [c for c in it["chaves"] if c != "anos"] + ["anos de escola", "quantos anos"]
    i = s.index("var BASE=") + len("var BASE=")
    j = s.index(";\n", i)
    s = s[:i] + json.dumps(base, ensure_ascii=False) + s[j:]
    s = troca(s, "a assistente virtual da Escola Espaço Criativo 😊 Posso te ajudar com turmas, unidades, Programa Bilíngue, visita e matrícula 2027.",
              f"a assistente virtual da Escola Espaço Criativo, {nl} 😊 Posso te ajudar com turmas, endereço, Programa Bilíngue, visita e matrícula 2027.")

    # Na Eli, o botão de endereço abre o mapa da unidade
    s = troca(s, "else if(acao==='mapa'){a.href='#unidades';a.textContent='Ver as unidades';a.addEventListener('click',fechar);}",
              "else if(acao==='mapa'){a.href='" + u["mapa"] + "';a.target='_blank';a.rel='noopener';a.textContent='Ver no mapa';}")

    # Telas grandes: um card só ocupa a largura toda (no celular nada muda)
    css_unidade = (
        "@media (min-width:760px){"
        ".ucards.uma{grid-template-columns:1fr}"
        ".ucards.uma .ucard{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr)}"
        ".ucards.uma .ucard img{height:100%;min-height:340px;aspect-ratio:auto}"
        ".ucards.uma .ucard .in{padding:36px 36px 34px;align-self:center}"
        ".notas.uma{grid-template-columns:minmax(0,520px)}"
        "}"
        "@media (min-width:1080px){.ecards.tres{grid-template-columns:repeat(3,1fr)}}\n"
    )
    s = troca(s, "</style>", css_unidade + "</style>")
    s = troca(s, '<div class="ucards">', '<div class="ucards uma">')
    s = troca(s, '<div class="notas">', '<div class="notas uma">')
    if u["sem_fund2"]:
        s = troca(s, '<div class="ecards">', '<div class="ecards tres">')

    # Caminhos relativos para a subpasta
    s = s.replace('src="img/', 'src="../img/').replace("url(fonts/", "url(../fonts/")
    s = s.replace('href="img/', 'href="../img/').replace("this.src='img/", "this.src='../img/")
    assert '"img/' not in s and "'img/" not in s and "(fonts/" not in s

    os.makedirs(os.path.join(RAIZ, chave), exist_ok=True)
    with open(os.path.join(RAIZ, chave, "index.html"), "w", encoding="utf-8") as f:
        f.write(s)
    print("ok", chave, len(s))


if __name__ == "__main__":
    for k, v in UNI.items():
        gerar(k, v)
