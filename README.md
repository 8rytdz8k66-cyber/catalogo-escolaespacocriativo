# Escola Espaço Criativo · Matrículas 2027

Sites da escola no GitHub Pages:

- Geral (as duas unidades): https://8rytdz8k66-cyber.github.io/catalogo-escolaespacocriativo/
- Unidade Messejana: https://8rytdz8k66-cyber.github.io/catalogo-escolaespacocriativo/messejana/
- Unidade Parque Santa Maria: https://8rytdz8k66-cyber.github.io/catalogo-escolaespacocriativo/santa-maria/

## Como atualizar

1. Edite a página geral, `index.html`. O visual das três páginas sai dela.
2. Gere as páginas das unidades de novo:

```
python3 assets/gerar_unidades_2027.py
```

Os dados de cada unidade (WhatsApp, endereço, etapas, fotos, Instagram, mapa) ficam no começo de `assets/gerar_unidades_2027.py`. As respostas da Eli ficam em `assets/gerar_catalogo_2027.py`. A Eli nunca informa preços: para valores, ela sempre manda falar com a coordenação.
