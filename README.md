# Ecommerce_Edinho_Variedades
Projeto proposto pelo nosso professor da faculdade de Análise e Desenvolvimento de Sistemas (ADS) para aprendizado e também obtenção de nota na matéria. A seguir terá instruções para a instalação e execução do projeto. Obs.: antes de tentar rodar o projeto, certifique-se que você está com o python mais recente instalado.

Ao baixar o projeto, exclua a VENV presente e crie uma nova no terminal com o seguinte comando:

Windows - python -m venv 'nome da venv da sua preferência'
Linux - python3 -m venv 'nome da venv da sua preferência'

Depois disso inslale o django pelo terminal com o seguinte comando:

Terminal - pip install django

faça as migrações com os seguintes comandos no terminal:

Windows - python manage.py makemigrations
Linux - python3 manage.py makemigrations

Windows - python manage.py migrate
Linux - python3 manage.py migrate

Depois de fazer as migrações você poderá rodar o projeto com o seguinte comando no terminal:

Windows - python manage.py runserver
Linux - python3 manage.py runserver


Obs.: o projeto está configurado para rodar com o banco de dados MySql, se você não tiver instalado o MySql WorkBench na sua máquina, baixe-o no site oficial pelo link a seguir (https://dev.mysql.com/downloads/workbench/). Também não esqueça de ter instalado o MySql Client pelo terminal.
