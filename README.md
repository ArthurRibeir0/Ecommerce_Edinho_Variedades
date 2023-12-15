Antes de tentar rodar o projeto, certifique-se que você está com o python mais recente instalado.


Ao baixar o projeto, exclua a VENV presente e crie uma nova no terminal com o seguinte comando: "python -m venv 'nome da venv da sua preferência'" (em windows), "python3 -m venv 'nome da venv da sua preferência'" (em linux).

Depois disso inslale o django pelo terminal com o seguinte comando: "pip install django".

faça as migrações com os seguintes comandos no terminal: "python manage.py makemigrations" (em windows), "python3 manage.py makemigrations" (em linux) - "python manage.py migrate" (em windows), "python3 manage.py migrate" (em linux)

Depois de fazer as migrações você poderá rodar o projeto com o seguinte comando no terminal: "python manage.py runserver" (em windows), "python3 manage.py runserver" (em linux)



Obs.: o projeto está configurado para rodar com o banco de dados MySql, se você não tiver instalado o MySql WorkBench na sua máquina, baixe-o no site oficial pelo link a seguir (https://dev.mysql.com/downloads/workbench/). Também não esqueça de ter instalado o MySql Client pelo terminal.
