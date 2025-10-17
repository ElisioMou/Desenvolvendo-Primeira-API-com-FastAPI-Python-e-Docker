run:
	@uvicorn workout_api.main:app --reload

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(d)

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head


# pyenv local 3.11.4 (Ativa versão do Python)
# .\venv\Scripts\Activate.ps1 (Ativa ambiente de desenvolvimento)
# docker-compose up db -d (Ativa o docker compose)
# Start-Sleep -Seconds 20 (Inicializa o MySQL)
# docker-compose exec db mysql -h 127.0.0.1 -P 3306 -u root -proot -e "SHOW DATABASES;"
# docker-compose exec db ping -c 3 db  (Teste conectividade interna)
# docker-compose run --rm migration (Executa as migrations)