from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

app=FastAPI()

class Cidade(BaseModel):
    id:int
    nome:str
    
cidades_list = [
  {'id': 1, 'nome': 'Teresina', 'uf': 'PI'},
  {'id': 2, 'nome': 'Altos', 'uf': 'PI'},
  {'id': 3, 'nome': 'Coelho Neto', 'uf': 'MA'},
  {'id': 4, 'nome': 'Pedro II', 'uf': 'PI'},
] #id será o parametro
cidades=[Cidade(id=1,nome='Teresina'),
        Cidade(id=2,nome='Coelho Neto')]

class NovaCidade(BaseModel):
    nome:str
    uf: str
@app.get('/cidades') 
def listar_cidades():
    return cidades_list
@app.get('/cidades2') 
def listar_cidades():
    
    return cidades
@app.get('/cidades/{id}')
def cidades_detail(id:int):
    for cidade in cidades:
        if cidade.id==id:
            return cidade
    return f'Cidade nao existe com id-->{id}'

@app.post('/cidades',status_code=201)
def cidades_create(nova_cidade:novaCidade):
    global proximo_id
    cidade=Cidade(id=proximo_id,
                  nome=nova_cidade.nome,
                  uf=nova_cidade.uf)
    proximo_id+=1
    cidades.append(cidade)
    return cidade
