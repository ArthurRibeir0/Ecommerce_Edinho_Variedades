# Ecommerce_Edinho_Variedades
Projeto proposto pelo nosso professor da faculdade de Análise e Desenvolvimento de Sistemas (ADS) para aprendizado e também obtenção de nota na matéria. A seguir terá instruções para a instalação e execução do projeto. Obs.: antes de tentar rodar o projeto, certifique-se que você está com o python mais recente instalado.

Ao baixar o projeto, exclua a VENV presente e crie uma nova no terminal com o seguinte comando:

No windows - python -m venv 'nome da venv da sua preferência'
No linux - python3 -m venv 'nome da venv da sua preferência'

Agora execute esta venv com o seguite comando:

No windows - 'nome da venv'/Scripts/Activate
No linux - source 'nome da venv'/bin/activate

Depois disso inslale o django com o seguinte comando:

No terminal - pip install django

faça as migrações com os seguintes comandos no terminal:

No windows - python manage.py makemigrations
No linux - python3 manage.py makemigrations

No windows - python manage.py migrate
No linux - python3 manage.py migrate

Depois de fazer as migrações você poderá rodar o projeto com o seguinte comando no terminal:

No windows - python manage.py runserver
No linux - python3 manage.py runserver


Obs.: o projeto está configurado para rodar com o banco de dados MySql, se você não tiver instalado o MySql WorkBench na sua máquina, baixe-o no site oficial pelo link a seguir (https://dev.mysql.com/downloads/workbench/). Também não esqueça de ter instalado o MySql Client pelo terminal.
