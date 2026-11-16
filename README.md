# LP Trânsito · Dra. Rebeka Paschoal Neves

Página estática pronta para o GitHub Pages: sem build e sem dependências externas, com as fontes hospedadas no próprio repositório.

## Publicar
1. Crie o repositório `lp-transito-rebeka` em `agenciapongui` e suba **todo o conteúdo desta pasta**, incluindo o `.nojekyll`.
2. Vá em Settings › Pages, escolha Branch `main` e pasta `/root`.
3. A página fica em `https://agenciapongui.github.io/lp-transito-rebeka/`.

Se a URL for outra, troque `BASE` no `build_site.py` e rode o script de novo, ou faça localizar/substituir de `https://agenciapongui.github.io/lp-transito-rebeka/` no `index.html`. Essa URL aparece no canonical, no `og:url`, na `og:image` e no schema.

## Estrutura
- `index.html`: página completa, com o CSS crítico inline, o schema LegalService e o FAQPage.
- `assets/img/`: imagens em WebP. O hero tem três tamanhos (1920, 1280 e mobile) e `og.jpg` é a imagem de compartilhamento.
- `assets/fonts/`: Montserrat (variável), Poppins 600/700 e Playfair Display 700, só com os caracteres latinos.

## Dados usados
- WhatsApp: +55 84 98757-1254. A mensagem já vem preenchida: "Olá, vim do google e gostaria de falar com a Advogada Especialista."
- Google: nota 5,0 e 177 avaliações. Os 12 depoimentos foram copiados do perfil do escritório no Google Maps em 16/11/2026.
