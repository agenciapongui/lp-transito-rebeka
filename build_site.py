import json,re,unicodedata,urllib.parse,html,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
BASE='https://agenciapongui.github.io/lp-transito-rebeka/'
PHONE='5584987571254'
MSG='Olá, vim do google e gostaria de falar com a Advogada Especialista.'
WA='https://wa.me/%s?text=%s'%(PHONE,urllib.parse.quote(MSG))
MAPS='https://maps.google.com/?cid=261626645182001391'
TOTAL=177
G='<svg class="g" viewBox="0 0 48 48" aria-hidden="true"><path fill="#FFC107" d="M43.6 20.5H42V20H24v8h11.3C33.7 32.7 29.2 36 24 36c-6.6 0-12-5.4-12-12s5.4-12 12-12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 12.9 4 4 12.9 4 24s8.9 20 20 20 20-8.9 20-20c0-1.3-.1-2.4-.4-3.5z"/><path fill="#FF3D00" d="m6.3 14.7 6.6 4.8C14.7 15.1 19 12 24 12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 16.3 4 9.7 8.3 6.3 14.7z"/><path fill="#4CAF50" d="M24 44c5.2 0 9.9-2 13.4-5.2l-6.2-5.2C29.2 35.1 26.7 36 24 36c-5.2 0-9.6-3.3-11.3-8l-6.5 5C9.5 39.6 16.2 44 24 44z"/><path fill="#1976D2" d="M43.6 20.5H42V20H24v8h11.3c-.8 2.2-2.2 4.2-4.1 5.6l6.2 5.2C37 39.2 44 34 44 24c0-1.3-.1-2.4-.4-3.5z"/></svg>'
WAI='<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.7-.8-2-.9-.3-.1-.5-.1-.7.1-.2.3-.8.9-.9 1.1-.2.2-.3.2-.6.1-.3-.1-1.2-.5-2.3-1.4-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.5.1-.6l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.4s1 2.8 1.2 3c.1.2 2 3.1 4.9 4.3.7.3 1.2.5 1.6.6.7.2 1.3.2 1.8.1.6-.1 1.7-.7 1.9-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.6-.3M12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4C2.7 15.6 2.2 13.8 2.2 12 2.2 6.6 6.6 2.2 12 2.2S21.8 6.6 21.8 12 17.4 21.8 12 21.8M12 0C5.4 0 0 5.4 0 12c0 2.1.6 4.2 1.6 6L0 24l6.2-1.6C8 23.4 10 24 12 24c6.6 0 12-5.4 12-12S18.6 0 12 0"/></svg>'
CHECK='<svg class="check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>'
TRUST='<div class="trust">%s<span><span class="stars" aria-hidden="true">★★★★★</span> <b>5,0 no Google</b> · %d avaliações<br>Contato via WhatsApp · 100%% seguro</span></div>'%(G,TOTAL)
rv=json.load(open('avaliacoes.json'))
def slug(n): return re.sub(r'[^a-z0-9]+','-',unicodedata.normalize('NFKD',n).encode('ascii','ignore').decode().lower()).strip('-')
def card(r,hidden):
    n,d,txt,_=r; e=html.escape
    ah=' aria-hidden="true"' if hidden else ''
    return f'<article class="rv"{ah}><div class="rv-head"><img src="assets/img/av-{slug(n)}.webp" width="96" height="96" alt="" decoding="async"><div class="rv-who"><b>{e(n)}</b><small>{e(d)}</small></div>{G}</div><span class="stars" role="img" aria-label="5 de 5 estrelas">★★★★★</span><p>{e(txt)}</p></article>'
a,b=rv[:6],rv[6:]
row=lambda xs:''.join(card(x,False) for x in xs)+''.join(card(x,True) for x in xs)
faq=[("Como funciona o atendimento?","Ao tocar em qualquer botão da página, você é direcionado para o WhatsApp do escritório. A advogada conversa com você, entende o seu problema e avalia o caso. Se for preciso, solicita os documentos para concluir a análise. Em seguida, apresenta a solução para o seu caso."),
("Preciso ir ao escritório?","Não. O atendimento é 100% online, pelo WhatsApp, para motoristas de todo o Brasil."),
("Quanto vou gastar?","Somente depois de conversar com você e entender o seu problema é possível formular uma proposta adequada à sua necessidade. Exponha seu caso para a nossa equipe."),
("Preciso de um advogado para resolver meu problema?","Sim. O advogado é o profissional habilitado para assessorar você quando o problema é jurídico. Em questões de trânsito, contar com uma advogada especialista é fundamental para apresentar a melhor defesa.")]
FAQ=''.join(f'<details{" open" if i==0 else ""}><summary><span class="ic" aria-hidden="true">+</span>{html.escape(q)}</summary><div class="ans">{html.escape(a_)}</div></details>' for i,(q,a_) in enumerate(faq))
schema={"@context":"https://schema.org","@graph":[
 {"@type":"LegalService","@id":BASE+"#escritorio","name":"Paschoal Neves Advogados","description":"Advocacia especializada em Direito de Trânsito: suspensão e cassação de CNH, Lei Seca, recusa ao bafômetro e PPD.","url":BASE,"image":BASE+"assets/img/og.jpg","logo":BASE+"assets/img/logo.webp","telephone":"+55 84 98757-1254","areaServed":{"@type":"Country","name":"Brasil"},"hasMap":MAPS,
  "address":{"@type":"PostalAddress","streetAddress":"Av. Engenheiro Roberto Freire, 1962","addressLocality":"Natal","addressRegion":"RN","postalCode":"59082-095","addressCountry":"BR"},
  "founder":{"@type":"Person","name":"Rebeka Paschoal Neves","jobTitle":"Advogada especialista em Direito de Trânsito","identifier":"OAB/RN 16.550"}},
 {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a_}} for q,a_ in faq]}]}
t=open('template.html',encoding='utf-8').read()
rep={'{{BASE}}':BASE,'{{SCHEMA}}':json.dumps(schema,ensure_ascii=False,separators=(',',':')),'{{WA}}':html.escape(WA),'{{WAICON}}':WAI,'{{GICON}}':G,'{{CHECK}}':CHECK,'{{TRUST}}':TRUST,'{{MAPS}}':MAPS,'{{TOTAL}}':str(TOTAL),'{{ROW1}}':row(a),'{{ROW2}}':row(b),'{{FAQ}}':FAQ}
for k,v in rep.items(): t=t.replace(k,v)
left=re.findall(r'\{\{[^}]+\}\}',t); assert not left,left
open('index.html','w',encoding='utf-8').write(t)
print('ok',len(t), 'multa' in t.lower())
