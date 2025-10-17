from fastapi import FastAPI

app = FastAPI(
    title="Workout API",
    version="1.0.0",
    description="API para gerenciamento de treinos e exercícios 🏋️‍♂️"
)

@app.get("/")
def root():
    return {"message": "🏋️‍♂️ Workout API está rodando com sucesso!"}
