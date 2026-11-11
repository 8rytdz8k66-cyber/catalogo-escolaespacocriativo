# Gera santa-maria/index.html e messejana/index.html a partir do mesmo modelo.
# Uso: python3 assets/gerar_unidades.py  (rodar na raiz do repositório)
import os

HEAD = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titulo}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0d0f74">
<meta property="og:type" content="website">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://8rytdz8k66-cyber.github.io/catalogo-escolaespacocriativo/{logo}">
<meta property="og:url" content="https://8rytdz8k66-cyber.github.io/catalogo-escolaespacocriativo/{pasta}/">
<link rel="icon" href="../{logo}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Nunito:wght@400;600;700;800&family=Caveat:wght@700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/site.css">
</head>
'''

UN = {
 'sm': dict(
  pasta='santa-maria', classe='', nome='Parque Santa Maria', serie='Berçário ao 9º ano',
  titulo='Espaço Criativo · Unidade Parque Santa Maria', logo='img/logo.png',
  desc='Escola Espaço Criativo, unidade Parque Santa Maria: berçário ao 9º ano na Rua Jorge da Veiga, 595, em Fortaleza. Veja a escola por dentro, as turmas e os valores.',
  lead='A primeira unidade da Espaço Criativo, onde tudo começou em 2002. Do berçário ao 9º ano, com opção de tempo integral.',
  end='Rua Jorge da Veiga, 595 · Parque Santa Maria, Fortaleza', zap='(85) 99407-1372', zapn='5585994071372',
  mapa='https://maps.google.com/?q=-3.858689,-38.501865', ig='https://www.instagram.com/criativoespaco_sm/',
  video='santa-maria-por-dentro', vtxt='Veja os espaços e as salas de aula da unidade.',
  selos=['Desde 2002', 'Berçário ao 9º ano', 'Tempo integral'],
  grupos=[('var(--vermelho)','Berçário','Integral (7h às 18h) ou meio período (7h às 12h ou 13h às 18h)'),
          ('var(--laranja)','Educação Infantil','Infantil I ao Infantil V'),
          ('var(--verde)','Fundamental I','1º ao 5º ano'),
          ('var(--azul)','Fundamental II','6º ao 9º ano'),
          ('var(--lilas)','Contraturno escolar','Para quem precisa de tempo integral'),
          ('var(--amarelo)','Diárias','Integral ou meio período, quando precisar')],
  jeito=[('var(--azul)','🤗','Cada criança no seu tempo','Do aluno com dificuldade de aprendizagem à criança atípica, cada um é acompanhado com acolhimento e respeito ao seu ritmo.'),
         ('var(--laranja)','🎓','O aluno que virou professor','Um aluno do 9º ano quase desistiu de estudar. Uma educadora o incentivou a continuar. Hoje ele é professor de Educação Física na própria escola.'),
         ('var(--lilas)','🏡','Família de verdade','Uma escola conduzida por duas irmãs, presente no dia a dia e parceira das famílias no desenvolvimento de cada criança.')],
  promo='',
  precos='''
        <details class="abre" style="--c:var(--vermelho)"><summary>Mensalidade</summary><div class="corpo">
          <table class="tab"><tr><td>Educação Infantil</td><td data-v="449">R$ 449,00</td></tr><tr><td>Fundamental I</td><td data-v="471">R$ 471,00</td></tr><tr><td>Fundamental II</td><td data-v="493">R$ 493,00</td></tr></table>
        </div></details>
        <details class="abre" style="--c:var(--verde)"><summary>Berçário e integral</summary><div class="corpo">
          <table class="tab">
            <tr><td>Berçário integral<small>7h às 18h</small></td><td data-v="1220">R$ 1.220,00</td></tr>
            <tr><td>Berçário meio período<small>7h às 12h ou 13h às 18h</small></td><td data-v="720">R$ 720,00</td></tr>
            <tr><td>Contraturno escolar</td><td>R$ 1.030,00</td></tr>
            <tr><td>Diária integral</td><td>R$ 120,00</td></tr>
            <tr><td>Diária meio período</td><td>R$ 70,00</td></tr>
          </table>
        </div></details>
        <details class="abre" style="--c:var(--azul)"><summary>Material didático</summary><div class="corpo">
          <table class="tab">
            <tr><td>Infantil I</td><td>R$ 299,00</td></tr><tr><td>Infantil II</td><td>R$ 439,00</td></tr><tr><td>Infantil III</td><td>R$ 637,89</td></tr><tr><td>Infantil IV</td><td>R$ 659,89</td></tr><tr><td>Infantil V</td><td>R$ 802,89</td></tr>
            <tr><td>1º ano</td><td>R$ 1.187,88</td></tr><tr><td>2º ano</td><td>R$ 1.301,88</td></tr><tr><td>3º ano</td><td>R$ 1.366,80</td></tr><tr><td>4º ano</td><td>R$ 1.426,80</td></tr><tr><td>5º ano</td><td>R$ 1.486,80</td></tr><tr><td>6º ao 9º ano</td><td>R$ 1.928,40</td></tr>
          </table>
        </div></details>
        <div class="selos"><span>Desconto pagando até o dia 05</span><span>Agenda digital: R$ 60,00</span><span>Irmãos: R$ 10,00 a menos cada</span></div>''',
  outra=('me','messejana','Messejana','Berçário ao 5º ano','img/logo-messejana.png','#2f8fd0')),
 'me': dict(
  pasta='messejana', classe=' class="me"', nome='Messejana', serie='Berçário ao 5º ano',
  titulo='Espaço Criativo · Unidade Messejana', logo='img/logo-messejana.png',
  desc='Escola Espaço Criativo, unidade Messejana (Colégio Maria de Fátima): berçário ao 5º ano na Rua Santa Efigênia, 300, em Fortaleza. Veja a escola por dentro, as turmas e os valores.',
  lead='Educação que desenvolve mente, coração e conexões para a vida. O capítulo mais novo da Espaço Criativo, no Colégio Maria de Fátima.',
  end='Rua Santa Efigênia, 300 · Messejana, Fortaleza', zap='(85) 97400-7393', zapn='5585974007393',
  mapa='https://maps.app.goo.gl/7UgxG8nRy4DjcvGP6', ig='https://www.instagram.com/eecmessejana/',
  video='messejana-por-dentro', vtxt='Veja o pátio, o parquinho e a quadra coberta.',
  selos=['Colégio Maria de Fátima', 'Berçário ao 5º ano', 'Inglês na prática'],
  grupos=[('var(--vermelho)','Berçário','Integral (7h às 17h ou às 18h) ou meio período (7h às 12h ou 13h às 18h)'),
          ('var(--laranja)','Educação Infantil','Infantil I ao Infantil V'),
          ('var(--verde)','Fundamental I','1º ao 5º ano'),
          ('var(--azul)','Tempo integral','Até as 17h ou até as 18h')],
  jeito=[('var(--azul)','🤗','Acolhimento que abraça','Cada criança é chamada pelo nome e acompanhada no seu tempo, do berçário em diante.'),
         ('var(--vermelho)','💛','Desenvolvimento socioemocional','Além do conteúdo, a criança aprende a conviver, a lidar com o que sente e a confiar em si.'),
         ('var(--laranja)','🏡','Parceria com as famílias','Escola presente no dia a dia, que conversa com os pais e caminha junto com eles.'),
         ('var(--verde)','🌎','Inglês integrado na prática','O inglês entra na rotina de um jeito natural, brincando e vivendo a língua.')],
  promo='<div class="promo"><b>10%</b><p>Matrícula em novembro com 10% de desconto. Em dezembro, 5%.</p></div>',
  precos='''
        <details class="abre" style="--c:var(--vermelho)"><summary>Mensalidade</summary><div class="corpo">
          <table class="tab"><tr><td>Educação Infantil<small>Infantil I ao V</small></td><td data-v="650">R$ 650,00</td></tr><tr><td>Fundamental I<small>1º ao 5º ano</small></td><td data-v="750">R$ 750,00</td></tr></table>
        </div></details>
        <details class="abre" style="--c:var(--verde)"><summary>Berçário</summary><div class="corpo">
          <table class="tab">
            <tr><td>Integral<small>7h às 17h</small></td><td data-v="1750">R$ 1.750,00</td></tr>
            <tr><td>Integral<small>7h às 18h</small></td><td data-v="1900">R$ 1.900,00</td></tr>
            <tr><td>Meio período<small>7h às 12h ou 13h às 18h</small></td><td data-v="900">R$ 900,00</td></tr>
          </table>
        </div></details>
        <details class="abre" style="--c:var(--azul)"><summary>Tempo integral</summary><div class="corpo">
          <table class="tab">
            <tr><td>Integral até as 17h<small>Infantil e Fundamental I</small></td><td>R$ 940,00</td></tr>
            <tr><td>Integral até as 18h<small>Infantil e Fundamental I</small></td><td>R$ 1.050,00</td></tr>
          </table>
        </div></details>
        <div class="selos"><span>Novembro: 10% de desconto</span><span>Dezembro: 5% de desconto</span><span>Material didático: consulte a escola</span><span>Irmãos: R$ 10,00 a menos cada</span></div>''',
  outra=('sm','santa-maria','Parque Santa Maria','Berçário ao 9º ano','img/logo.png','#2e9e47')),
}

def pagina(k, d):
    grupos = '\n'.join(f'      <div class="turma" style="--c:{c}"><span><b>{t}</b><span>{s}</span></span></div>' for c,t,s in d['grupos'])
    jeito = '\n'.join(f'      <div class="mini" style="--c:{c}"><span class="ic" aria-hidden="true">{i}</span><h3>{t}</h3><p>{p}</p></div>' for c,i,t,p in d['jeito'])
    selos = ''.join(f'<span>{s}</span>' for s in d['selos'])
    o = d['outra']
    return HEAD.format(**d) + f'''<body data-base="../" data-pagina="{k}" data-u="{k}"{d['classe']}>
<main id="conteudo">

<section class="hero" aria-labelledby="titulo">
  <div class="bolinhas" aria-hidden="true">
    <i style="width:110px;height:110px;background:var(--acc);right:-46px;top:-40px;opacity:.9"></i>
    <i style="width:26px;height:26px;background:var(--amarelo);right:16%;bottom:24px"></i>
  </div>
  <div class="wrap">
    <div>
      <h1 id="titulo">Unidade <span>{d['nome']}</span></h1>
      <p class="lead">{d['lead']}</p>
      <div class="botoes">
        <a class="btn zap" href="../matricula/?u={k}">Quero matricular meu filho</a>
        <a class="btn contorno" href="#valores">Ver valores</a>
      </div>
      <div class="selos-hero">{selos}</div>
    </div>
    <img class="hero-logo" src="../{d['logo']}" alt="Logo da unidade {d['nome']}" width="250" height="250" fetchpriority="high">
  </div>
</section>

<section class="claro" aria-labelledby="t-dentro">
  <div class="wrap video-un">
    <div class="vid"><video data-auto muted loop playsinline preload="metadata" poster="../img/{d['video']}.jpg" aria-label="Vídeo: a unidade {d['nome']} por dentro"><source src="../img/{d['video']}.mp4" type="video/mp4"></video><button type="button" class="som">🔇 Ligar som</button></div>
    <div>
      <div class="cab"><small style="--c:var(--azul)">Por dentro</small><h2 id="t-dentro">Já passou na frente, mas nunca entrou?</h2><p>{d['vtxt']} Toque em “Ligar som” para ouvir.</p></div>
      <div class="botoes"><button type="button" class="btn zap" data-acao="visita">Agendar uma visita</button><button type="button" class="btn contorno-escuro" data-acao="mapa">📍 Como chegar</button></div>
    </div>
  </div>
</section>

<section aria-labelledby="t-turmas">
  <div class="wrap">
    <div class="cab"><small style="--c:var(--laranja)">Turmas e horários</small><h2 id="t-turmas">{d['serie']}</h2></div>
    <div class="lista-turmas">
{grupos}
    </div>
  </div>
</section>

<section class="claro" aria-labelledby="t-jeito">
  <div class="wrap">
    <div class="cab"><small style="--c:var(--verde)">Nosso jeito</small><h2 id="t-jeito">O que seu filho encontra aqui</h2></div>
    <div class="trilho-h" style="--cols:{len(d['jeito'])}">
{jeito}
    </div>
    <div class="pontos" aria-hidden="true"></div>
  </div>
</section>

<section id="valores" aria-labelledby="t-valores">
  <div class="wrap" style="max-width:720px">
    <div class="cab"><small style="--c:var(--lilas)">Valores</small><h2 id="t-valores">Investimento na educação</h2></div>
    {d['promo']}
    <form class="form" id="portao" novalidate>
      <h3>Veja os valores</h3>
      <p class="nota">Preencha para ver as mensalidades. Seus dados só vão para a escola se você enviar pelo WhatsApp.</p>
      <label for="pt-resp">Nome do pai, mãe ou responsável</label><input id="pt-resp" type="text" autocomplete="name" placeholder="Ex.: Ana Souza" required>
      <label for="pt-zap">WhatsApp do responsável</label><input id="pt-zap" data-tel type="text" inputmode="tel" autocomplete="tel" placeholder="(85) 99999-9999" maxlength="15" required>
      <label for="pt-aluno">Nome do aluno</label><input id="pt-aluno" type="text" placeholder="Ex.: João" required>
      <div class="irmao"><p>Tem mais de 1 filho? <span>Estudando juntos, economizam!</span></p><label><input type="checkbox" id="pt-irmao"> Sim</label></div>
      <p class="erro" id="pt-erro" role="alert"></p>
      <button type="submit" class="btn zap cheio">Ver valores</button>
    </form>
    <div id="precos" hidden>
      <p class="ola" id="pt-ola"></p>
{d['precos']}
      <div class="botoes" style="margin-top:16px"><a class="btn zap cheio" href="../matricula/?u={k}">Calcular o valor da turma e matricular</a></div>
    </div>
  </div>
</section>

<section id="depoimentos" class="claro" hidden aria-labelledby="t-dep">
  <div class="wrap">
    <div class="cab"><small style="--c:#b07a00">Depoimentos</small><h2 id="t-dep">O que os pais dizem</h2></div>
    <div class="trilho-h" style="--cols:3"></div>
  </div>
</section>

<section class="escuro" aria-labelledby="t-local">
  <div class="wrap">
    <div class="cab"><small style="--c:var(--amarelo)">Como chegar</small><h2 id="t-local">Venha conhecer a unidade</h2></div>
    <div class="local" style="grid-template-columns:1fr">
      <div class="card">
        <h3>Unidade {d['nome']}</h3>
        <p>{d['end']}<br>WhatsApp {d['zap']}</p>
        <div class="botoes">
          <a class="btn zap" href="https://wa.me/{d['zapn']}" target="_blank" rel="noopener">{'{ZAP}'}WhatsApp</a>
          <a class="btn branco" href="{d['mapa']}" target="_blank" rel="noopener">📍 Mapa</a>
          <a class="ig" href="{d['ig']}" target="_blank" rel="noopener" aria-label="Instagram da unidade {d['nome']}">{'{IG}'}</a>
        </div>
      </div>
    </div>
    <details class="abre" style="margin-top:18px;--c:var(--amarelo)" id="avaliar"><summary>Já é da escola? Deixe sua avaliação</summary><div class="corpo">
      <div class="form" id="avaliar-form" style="box-shadow:none;padding:0;border:0">
        <div class="estrelas" role="radiogroup" aria-label="Nota de 1 a 5">{''.join(f'<button type="button" role="radio" aria-checked="false" data-n="{n}" aria-label="{n} estrela{"s" if n>1 else ""}">★</button>' for n in range(1,6))}</div>
        <label for="av-nome">Seu nome</label><input id="av-nome" type="text" placeholder="Ex.: Ana, mãe do João">
        <label for="av-txt">Seu comentário</label><textarea id="av-txt" rows="3" placeholder="Conte como é a experiência da sua família com a escola"></textarea>
        <p class="erro" id="av-erro" role="alert"></p>
        <a class="btn zap cheio" id="av-enviar" href="#" target="_blank" rel="noopener" aria-disabled="true">Enviar avaliação pelo WhatsApp</a>
      </div>
    </div></details>
  </div>
</section>

</main>
<script src="../assets/site.js"></script>
</body>
</html>
'''

ZAP = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></svg>'
IG = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.4" cy="6.6" r="1.3" fill="currentColor"/></svg>'
for k, d in UN.items():
    os.makedirs(d['pasta'], exist_ok=True)
    html = pagina(k, d).replace('{ZAP}', ZAP).replace('{IG}', IG)
    open(os.path.join(d['pasta'], 'index.html'), 'w').write(html)
    print('ok', d['pasta'])
