

Este é o site pessoal e portfólio de **Erik Miyajima**, desenvolvido com **Python + Django**, com suporte a **internacionalização (i18n)** para múltiplos idiomas. O projeto reúne informações sobre mim, meus projetos, habilidades, redes sociais e canais de contato.


---

# Sobre o Projeto

Este portfólio digital foi criado para apresentar meu trabalho como **desenvolvedor autodidata, escritor e criador de projetos digitais com impacto social e educacional**. Com raízes no Japão e atuação voltada ao Brasil e ao mundo, busco unir tecnologia, literatura e transformação social.

---

# Tecnologias Utilizadas

- Python 3.10
- Django
- HTML5, CSS3
- Templates Django
- Suporte a Internacionalização (i18n)

---

# Como Executar Localmente

1. **Clone o repositório:**
    git clone https://github.com/ErikSM/nome-do-repositorio.git
    cd nome-do-repositorio


2. Crie um ambiente virtual (recomendado):
    python -m venv .venv
    source .venv/bin/activate   # Linux/macOS
    .venv\Scripts\activate      # Windows


3. Instale as dependências:
    pip install -r requirements.txt


4. Execute o projeto:
    python manage.py runserver

5. Acesse em: http://localhost:8000/

---


# Suporte a Idiomas
O site possui suporte completo para:
      🇧🇷 Português (pt)
      🇺🇸 Inglês (en)
  * Use o seletor de idiomas na interface para alternar entre os conteúdos traduzidos.

---

# Estrutura do Projeto

portfolio/

├── static/
│   └── img/                # Imagens do site
├── templates/
│   └── base.html           # Template base
│   └── index.html          # Página principal
├── locale/
│   └── pt/
│   └── en/
│       └── LC_MESSAGES/
│           └── django.po / .mo
├── site_pessoal/
│   └── views.py            # Lógica da página
├── manage.py
└── requirements.txt
