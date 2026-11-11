/* Escola Espaço Criativo · comportamento compartilhado
   Cada página define no <body>: data-base ("" na raiz, "../" nas pastas), data-pagina e, nas unidades, data-u ("sm" ou "me"). */
(function(){
var B=document.body.dataset.base||'', PAG=document.body.dataset.pagina||'', U=document.body.dataset.u||'';
var $=function(s,el){return (el||document).querySelector(s);}, $$=function(s,el){return [].slice.call((el||document).querySelectorAll(s));};
var brl=function(v){return v.toLocaleString('pt-BR',{style:'currency',currency:'BRL'});};

/* ===== Dados das unidades (mesmas informações dos catálogos) ===== */
var UN={
  sm:{nome:'Parque Santa Maria',curto:'Santa Maria',serie:'Berçário ao 9º ano',zap:'5585994071372',zapTxt:'(85) 99407-1372',
      end:'Rua Jorge da Veiga, 595 · Parque Santa Maria',mapa:'https://maps.google.com/?q=-3.858689,-38.501865',
      ig:'https://www.instagram.com/criativoespaco_sm/',logo:'img/logo.png',pag:'santa-maria/',
      turmas:['Berçário','Infantil I','Infantil II','Infantil III','Infantil IV','Infantil V','1º ano','2º ano','3º ano','4º ano','5º ano','6º ano','7º ano','8º ano','9º ano'],
      berc:[['Integral (7h às 18h)',1220],['Meio período (7h às 12h ou 13h às 18h)',720]],
      integral:[['Contraturno escolar',1030]],
      mensal:function(t){if(/^Infantil/.test(t))return 449;var n=parseInt(t,10);if(n>=1&&n<=5)return 471;if(n>=6)return 493;return 0;}},
  me:{nome:'Messejana',curto:'Messejana',serie:'Berçário ao 5º ano',zap:'5585974007393',zapTxt:'(85) 97400-7393',
      end:'Rua Santa Efigênia, 300 · Messejana (Colégio Maria de Fátima)',mapa:'https://maps.app.goo.gl/7UgxG8nRy4DjcvGP6',
      ig:'https://www.instagram.com/eecmessejana/',logo:'img/logo-messejana.png',pag:'messejana/',
      turmas:['Berçário','Infantil I','Infantil II','Infantil III','Infantil IV','Infantil V','1º ano','2º ano','3º ano','4º ano','5º ano'],
      berc:[['Integral (7h às 17h)',1750],['Integral (7h às 18h)',1900],['Meio período (7h às 12h ou 13h às 18h)',900]],
      integral:[['Tempo integral até as 17h',940],['Tempo integral até as 18h',1050]],
      mensal:function(t){if(/^Infantil/.test(t))return 650;var n=parseInt(t,10);if(n>=1&&n<=5)return 750;return 0;}}
};
var MAT_SM={'Infantil I':299,'Infantil II':439,'Infantil III':637.89,'Infantil IV':659.89,'Infantil V':802.89,'1º ano':1187.88,'2º ano':1301.88,'3º ano':1366.80,'4º ano':1426.80,'5º ano':1486.80,'6º ano':1928.40,'7º ano':1928.40,'8º ano':1928.40,'9º ano':1928.40};
var IDADE={0:'Berçário',1:'Infantil I',2:'Infantil II',3:'Infantil III',4:'Infantil IV',5:'Infantil V',6:'1º ano',7:'2º ano',8:'3º ano',9:'4º ano',10:'5º ano',11:'6º ano',12:'7º ano',13:'8º ano',14:'9º ano'};
/* Depoimentos reais das famílias. A seção só aparece com 3 ou mais. Formato: {nome:"Ana, mãe do João", unidade:"Messejana", nota:5, texto:"..."} */
var DEPOIMENTOS=[];

function wa(u,msg){return 'https://wa.me/'+UN[u].zap+'?text='+encodeURIComponent(msg);}
function msgVisita(u){return 'Olá! Vim pelo site da Escola Espaço Criativo e quero agendar uma visita na unidade '+UN[u].nome+'.';}
function msgOla(u){return 'Olá! Vim pelo site da Escola Espaço Criativo e quero informações sobre a unidade '+UN[u].nome+'.';}
function abrir(url){var a=document.createElement('a');a.href=url;a.target='_blank';a.rel='noopener';document.body.appendChild(a);a.click();a.remove();}
var ICO_ZAP='<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></svg>';
var ICO_IG='<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.4" cy="6.6" r="1.3" fill="currentColor"/></svg>';

/* ===== Topo, menu, barra e rodapé (iguais em todas as páginas) ===== */
var cur=function(p){return PAG===p?' aria-current="page"':'';};
var matHref=B+'matricula/'+(U?'?u='+U:'');
var logoTopo=U==='me'?UN.me.logo:'img/logo.png';
document.body.insertAdjacentHTML('afterbegin',
 '<a class="sr" href="#conteudo">Pular para o conteúdo</a>'+
 '<header class="topo"><div class="topo-in">'+
  '<a class="marca" href="'+B+'./"><img src="'+B+logoTopo+'" alt="" width="42" height="42"><span><b>Espaço Criativo</b><small>'+(U?'Unidade '+UN[U].nome:'Escola e Creche · Fortaleza')+'</small></span></a>'+
  '<nav class="topo-links" aria-label="Principal"><a href="'+B+'santa-maria/"'+cur('sm')+'>Santa Maria</a><a href="'+B+'messejana/"'+cur('me')+'>Messejana</a><a href="'+B+'historia/"'+cur('historia')+'>Nossa história</a></nav>'+
  '<a class="btn zap" href="'+matHref+'">Matricular</a>'+
  '<button class="hamb" type="button" aria-label="Abrir menu" aria-haspopup="dialog" data-abre="gaveta"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>'+
 '</div></header><div class="arco" aria-hidden="true"></div>'+
 '<dialog class="gaveta" id="gaveta" aria-label="Menu"><div class="gaveta-cab"><b>Menu</b><button class="x" type="button" data-fecha aria-label="Fechar">×</button></div>'+
  '<nav><a href="'+B+'./"'+cur('home')+'><span class="ico">🏠</span>Início</a>'+
  '<a href="'+B+'santa-maria/"'+cur('sm')+'><img src="'+B+'img/logo.png" alt=""><span>Unidade Santa Maria<small>Berçário ao 9º ano</small></span></a>'+
  '<a href="'+B+'messejana/"'+cur('me')+'><img src="'+B+'img/logo-messejana.png" alt=""><span>Unidade Messejana<small>Berçário ao 5º ano</small></span></a>'+
  '<a href="'+B+'historia/"'+cur('historia')+'><span class="ico">📖</span>Nossa história</a>'+
  '<a href="'+matHref+'"'+cur('matricula')+'><span class="ico">✏️</span>Matrícula e valores</a>'+
  '<a href="#rodape" data-fecha-ir><span class="ico">📞</span>Contato</a></nav>'+
  '<div class="rodape-gav"><a class="btn zap cheio" href="'+matHref+'">Quero matricular meu filho</a></div></dialog>'+
 '<dialog class="janela" id="escolha" aria-labelledby="esc-tit"><div class="j-cab"><b id="esc-tit">Escolha a unidade</b><button class="x" type="button" data-fecha aria-label="Fechar">×</button></div><div class="j-corpo" id="esc-corpo"></div></dialog>');

document.body.insertAdjacentHTML('beforeend',
 '<nav class="barra" aria-label="Ações rápidas">'+
  '<button type="button" class="zap-b" data-acao="zap"><span class="i">💬</span>WhatsApp</button>'+
  '<button type="button" data-acao="mapa"><span class="i">📍</span>Como chegar</button>'+
  '<button type="button" data-acao="visita"><span class="i">📅</span>Agendar visita</button></nav>'+
 '<footer class="rodape" id="rodape"><div class="wrap"><div class="cols">'+
  ['sm','me'].map(function(u){var x=UN[u];return '<div><h3>Unidade '+x.nome+'</h3><p>'+x.serie+'</p><p>'+x.end+'</p><p>WhatsApp <a href="https://wa.me/'+x.zap+'" target="_blank" rel="noopener">'+x.zapTxt+'</a></p><div class="links"><a href="'+x.mapa+'" target="_blank" rel="noopener">Como chegar</a><a href="'+x.ig+'" target="_blank" rel="noopener">Instagram</a><a href="'+B+x.pag+'">Ver a unidade</a></div></div>';}).join('')+
  '<div><h3>Escola Espaço Criativo</h3><p>Escola e creche desde 2002.</p><div class="links"><a href="'+B+'historia/">Nossa história</a><a href="'+B+'matricula/">Matrícula e valores</a><a href="https://escolaespacocriativo.com/" target="_blank" rel="noopener">escolaespacocriativo.com</a></div></div>'+
 '</div><p class="frase">Mais que uma escola, um lugar para pertencer!</p><p class="peq">Escola Espaço Criativo · Escola e Creche · desde 2002</p></div></footer>');

/* janelas */
$$('dialog').forEach(function(d){
  d.addEventListener('click',function(e){if(e.target===d)d.close();});
  $$('[data-fecha]',d).forEach(function(b){b.addEventListener('click',function(){d.close();});});
  new MutationObserver(function(){document.documentElement.classList.toggle('travado',!!$('dialog[open]'));}).observe(d,{attributes:true,attributeFilter:['open']});
});
$$('[data-abre]').forEach(function(b){b.addEventListener('click',function(){var d=document.getElementById(b.dataset.abre);if(d&&d.showModal)d.showModal();});});
$$('[data-fecha-ir]').forEach(function(a){a.addEventListener('click',function(){$('#gaveta').close();});});

/* ações rápidas: na página da unidade vão direto; nas outras perguntam a unidade */
var ACOES={
  zap:{tit:'Falar no WhatsApp',faz:function(u){abrir(wa(u,msgOla(u)));}},
  mapa:{tit:'Como chegar',faz:function(u){abrir(UN[u].mapa);}},
  visita:{tit:'Agendar uma visita',faz:function(u){abrir(wa(u,msgVisita(u)));}}
};
function acao(nome,u){
  if(u){ACOES[nome].faz(u);return;}
  var d=$('#escolha');$('#esc-tit').textContent=ACOES[nome].tit+': qual unidade?';
  var c=$('#esc-corpo');c.innerHTML='';
  ['sm','me'].forEach(function(k){var b=document.createElement('a');b.className='uni';b.href='#';b.style.setProperty('--c',k==='sm'?'#2e9e47':'#2f8fd0');
    b.innerHTML='<img src="'+B+UN[k].logo+'" alt=""><span><b>'+UN[k].nome+'</b><span>'+UN[k].serie+'</span></span><span class="seta">›</span>';
    b.addEventListener('click',function(e){e.preventDefault();d.close();ACOES[nome].faz(k);});c.appendChild(b);});
  if(d.showModal)d.showModal();
}
$$('[data-acao]').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();acao(b.dataset.acao,b.dataset.u||U);});});

/* ===== Vídeos curtos: tocam sem som quando aparecem na tela ===== */
$$('.vid').forEach(function(box){
  var v=$('video',box), s=$('.som',box); if(!v)return;
  if(s)s.addEventListener('click',function(){v.muted=!v.muted;if(!v.muted){v.currentTime=0;v.play();}s.textContent=v.muted?'🔇 Ligar som':'🔊 Desligar som';});
  if('IntersectionObserver' in window&&v.hasAttribute('data-auto')){
    new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var p=v.play();if(p&&p.catch)p.catch(function(){});}else v.pause();});},{threshold:.5}).observe(v);
  }
});

/* ===== Pontinhos dos carrosséis ===== */
$$('.trilho-h,.videos').forEach(function(t){
  var p=t.nextElementSibling; if(!p||!p.classList.contains('pontos'))return;
  var n=t.children.length; p.innerHTML=Array(n+1).join('<i></i>'); var is=$$('i',p); is[0]&&is[0].classList.add('on');
  t.addEventListener('scroll',function(){var w=t.children[0].getBoundingClientRect().width+14,k=Math.round(t.scrollLeft/w);is.forEach(function(x,j){x.classList.toggle('on',j===Math.min(k,n-1));});},{passive:true});
});

/* ===== Depoimentos (só com 3 ou mais) ===== */
var dep=$('#depoimentos');
if(dep){var lista=DEPOIMENTOS.filter(function(d){return !U||d.unidade===UN[U].nome||d.unidade===UN[U].curto;});
  if(lista.length>=3){dep.hidden=false;var t=$('.trilho-h',dep);
    lista.forEach(function(d){var f=document.createElement('figure');f.className='dep';f.innerHTML='<div class="est">'+'★'.repeat(d.nota||5)+'</div><blockquote></blockquote><figcaption></figcaption>';$('blockquote',f).textContent='“'+d.texto+'”';$('figcaption',f).textContent=d.nome+(d.unidade&&!U?' · '+d.unidade:'');t.appendChild(f);});}}

/* ===== Utilidades de formulário ===== */
function soDig(v){return (v||'').replace(/\D/g,'');}
function mascaraTel(v){v=soDig(v).slice(0,11);if(v.length<=2)return v.length?'('+v:'';if(v.length<=6)return '('+v.slice(0,2)+') '+v.slice(2);if(v.length<=10)return '('+v.slice(0,2)+') '+v.slice(2,6)+'-'+v.slice(6);return '('+v.slice(0,2)+') '+v.slice(2,7)+'-'+v.slice(7);}
function telOk(v){var d=soDig(v);return (d.length===11&&d[2]==='9')||d.length===10;}
$$('input[data-tel]').forEach(function(i){i.addEventListener('input',function(){i.value=mascaraTel(i.value);});});
function guarda(o){try{sessionStorage.setItem('ec-dados',JSON.stringify(o));}catch(e){}}
function pega(){try{return JSON.parse(sessionStorage.getItem('ec-dados')||'null');}catch(e){return null;}}

/* ===== Portão dos valores (página da unidade) ===== */
var portao=$('#portao');
if(portao){
  var g=pega(); if(g){$('#pt-resp').value=g.resp||'';$('#pt-zap').value=g.zap||'';$('#pt-aluno').value=g.crianca||'';}
  portao.addEventListener('submit',function(e){
    e.preventDefault();
    var resp=$('#pt-resp').value.trim(), zap=$('#pt-zap').value, aluno=$('#pt-aluno').value.trim(), irm=$('#pt-irmao').checked, f=[];
    if(!resp)f.push('o nome do responsável'); if(!telOk(zap))f.push('um WhatsApp válido com DDD'); if(!aluno)f.push('o nome do aluno');
    if(f.length){$('#pt-erro').textContent='Falta preencher: '+f.join(', ')+'.';return;}
    $('#pt-erro').textContent=''; guarda({resp:resp,zap:zap,crianca:aluno,irmao:irm});
    $$('#precos td[data-v]').forEach(function(td){var v=+td.dataset.v;td.innerHTML=irm?'<span class="riscado">'+brl(v)+'</span>'+brl(v-10):brl(v);});
    $('#pt-ola').textContent='Olá, '+resp.split(' ')[0]+'! Estes são os valores para '+aluno+' na unidade '+UN[U].nome+'.'+(irm?' Como são irmãos, já aparece o desconto de R$ 10,00 por aluno.':'');
    portao.hidden=true; $('#precos').hidden=false; $$('#precos details').forEach(function(d){d.open=true;});
    $('#precos').scrollIntoView({block:'start'});
  });
}

/* ===== Avaliação (página da unidade) ===== */
var av=$('#avaliar-form');
if(av){
  var nota=0, bts=$$('.estrelas button',av), a=$('#av-enviar');
  function monta(){var nome=$('#av-nome').value.trim(),txt=$('#av-txt').value.trim();
    if(nota&&nome&&txt){a.href=wa(U,'Olá! Quero deixar minha avaliação da Escola Espaço Criativo.\n\n*Nota:* '+'★'.repeat(nota)+' ('+nota+' de 5)\n*Nome:* '+nome+'\n*Unidade:* '+UN[U].nome+'\n*Comentário:* '+txt);a.setAttribute('aria-disabled','false');}
    else{a.href='#';a.setAttribute('aria-disabled','true');}}
  bts.forEach(function(b){b.addEventListener('click',function(){nota=+b.dataset.n;bts.forEach(function(x){x.classList.toggle('on',+x.dataset.n<=nota);x.setAttribute('aria-checked',+x.dataset.n===nota?'true':'false');});monta();});});
  $$('input,textarea',av).forEach(function(x){x.addEventListener('input',monta);});
  a.addEventListener('click',function(e){if(a.getAttribute('aria-disabled')==='true'){e.preventDefault();var f=[];if(!nota)f.push('a nota');if(!$('#av-nome').value.trim())f.push('seu nome');if(!$('#av-txt').value.trim())f.push('o comentário');$('#av-erro').textContent='Falta preencher: '+f.join(', ')+'.';}else $('#av-erro').textContent='';});
}

/* ===== Formulário de matrícula ===== */
var mat=$('#mat');
if(mat){
  var s={idade:$('#m-idade'),turma:$('#m-turma'),turno:$('#m-turno'),int:$('#m-int')};
  for(var i=0;i<=14;i++){var o=document.createElement('option');o.value=i;o.textContent=i===0?'Menos de 1 ano':i+(i===1?' ano':' anos');s.idade.appendChild(o);}
  var q=(location.search.match(/[?&]u=(sm|me)/)||[])[1]; if(q)$('#m-'+q).checked=true;
  var g2=pega(); if(g2){$('#m-resp').value=g2.resp||'';$('#m-zap').value=g2.zap||'';$('#m-crianca').value=g2.crianca||'';$('#m-irmao').checked=!!g2.irmao;}
  var un=function(){var r=$('input[name=unid]:checked',mat);return r?r.value:'';};
  function enche(sel,itens,vazio){sel.innerHTML='';if(vazio){var o=document.createElement('option');o.value='';o.textContent=vazio;sel.appendChild(o);}itens.forEach(function(it,k){var o=document.createElement('option');if(Array.isArray(it)){o.value=k;o.textContent=it[0]+' · '+brl(it[1]);}else{o.value=it;o.textContent=it;}sel.appendChild(o);});}
  function troca(){var u=un(),at=s.turma.value;enche(s.turma,u?UN[u].turmas:[],u?'Escolha a turma':'Escolha a unidade primeiro');if(u&&UN[u].turmas.indexOf(at)>-1)s.turma.value=at;if(u){enche(s.turno,UN[u].berc);enche(s.int,UN[u].integral,'Não, só meio período');}sugere(false);atualiza();}
  function sugere(forca){var u=un(),id=s.idade.value,d=$('#m-dica');d.textContent='';if(id==='')return;
    if(u==='me'&&+id>10){d.textContent='A unidade Messejana atende até o 5º ano. Para essa idade, escolha a unidade Santa Maria.';return;}
    if(u&&(forca||!s.turma.value)){s.turma.value=IDADE[id];d.textContent='Sugerimos a turma '+IDADE[id]+' pela idade. Você pode trocar se precisar.';}}
  function atualiza(){
    var u=un(),t=s.turma.value,berc=t==='Berçário',linhas=[],box=$('#m-valor'),irm=$('#m-irmao').checked,dsc=irm?10:0;
    $('#m-turno-box').hidden=!(u&&berc); $('#m-int-box').hidden=!(u&&t&&!berc);
    if(u&&t){if(berc){var b=UN[u].berc[s.turno.value||0];linhas.push(['Berçário · '+b[0],b[1]-dsc]);}
      else{linhas.push(['Mensalidade · '+t,UN[u].mensal(t)-dsc]);if(s.int.value!==''){var it=UN[u].integral[s.int.value];linhas.push([it[0],it[1]]);}}}
    var resp=$('#m-resp').value.trim(),cri=$('#m-crianca').value.trim(),zap=$('#m-zap').value,id=s.idade.value;
    if(linhas.length){var h='<b>Valor para '+t+' · '+UN[u].curto+'</b><ul>';linhas.forEach(function(l){h+='<li><span>'+l[0]+'</span><strong>'+brl(l[1])+'</strong></li>';});h+='</ul>';
      if(u==='me'){var base=linhas[0][1];h+='<p>Matrícula em novembro: 10% de desconto ('+brl(base*.9)+'). Em dezembro: 5% ('+brl(base*.95)+').</p><p>Material didático: consulte a escola.</p>';}
      else{if(MAT_SM[t])h+='<p>Material didático do '+t+': '+brl(MAT_SM[t])+'.</p>';h+='<p>Desconto pagando até o dia 05.</p>';}
      box.innerHTML=h;box.hidden=false;} else box.hidden=true;
    var ok=u&&resp&&telOk(zap)&&cri&&id!==''&&t&&!(u==='me'&&+id>10), a=$('#m-enviar');
    if(ok){guarda({resp:resp,zap:zap,crianca:cri,irmao:irm});
      var m=['Olá! Vim pelo site da Escola Espaço Criativo e quero fazer a matrícula.','','*Unidade:* '+UN[u].nome,'*Responsável:* '+resp,'*WhatsApp:* '+zap,'*Criança:* '+cri+' ('+(id==='0'?'menos de 1 ano':id+(id==='1'?' ano':' anos'))+')','*Turma:* '+t];
      if(irm)m.push('*Tem irmão estudando ou se matriculando:* sim');
      linhas.forEach(function(l){m.push('*'+l[0]+':* '+brl(l[1]));});
      a.href=wa(u,m.join('\n'));a.setAttribute('aria-disabled','false');}
    else{a.href='#';a.setAttribute('aria-disabled','true');}
  }
  $('#m-enviar').addEventListener('click',function(e){if(this.getAttribute('aria-disabled')==='true'){e.preventDefault();var f=[];if(!un())f.push('a unidade');if(!$('#m-resp').value.trim())f.push('o nome do responsável');if(!telOk($('#m-zap').value))f.push('um WhatsApp válido com DDD');if(!$('#m-crianca').value.trim())f.push('o nome da criança');if(s.idade.value==='')f.push('a idade');if(!s.turma.value)f.push('a turma');$('#m-erro').textContent=f.length?'Falta preencher: '+f.join(', ')+'.':'A unidade Messejana atende até o 5º ano.';}else $('#m-erro').textContent='';});
  $$('input[name=unid]',mat).forEach(function(r){r.addEventListener('change',troca);});
  s.idade.addEventListener('change',function(){sugere(true);atualiza();});
  [s.turma,s.turno,s.int,$('#m-irmao')].forEach(function(x){x.addEventListener('change',atualiza);});
  [$('#m-resp'),$('#m-crianca'),$('#m-zap')].forEach(function(x){x.addEventListener('input',atualiza);});
  mat.addEventListener('submit',function(e){e.preventDefault();});
  troca();
}
})();
