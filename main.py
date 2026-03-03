from fastapi import FastAPI
from fastapi import HTTPException
app=FastAPI()
cidades_list = [
  {'id': 1, 'nome': 'Teresina', 'uf': 'PI'},
  {'id': 2, 'nome': 'Altos', 'uf': 'PI'},
  {'id': 3, 'nome': 'Coelho Neto', 'uf': 'MA'},
  {'id': 4, 'nome': 'Pedro II', 'uf': 'PI'},
] #id será o parametro
@app.get('/cidades') #cidades?
def listar_cidades():
    return cidades_list

# EndPoints (rota) de um API REST
@app.get('/cidades/{id}')
def detalhes_cidade(id: int):
  for cidade in cidades_list:
    if cidade['id'] == id:
      return cidade
  raise HTTPException(status_code=404, detail="Não encontrado")

@app.delete('/cidades/{id}')
def remover_cidade(id: int):
  for index, cidade in enumerate(cidades_list):
    if cidade['id'] == id:
      cidades_list.pop(index)
      return 

#teste api
#http://localhost:8000/cidades
#terminal: http://localhost:8000/cidades