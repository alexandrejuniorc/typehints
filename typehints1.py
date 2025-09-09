from typing import List, Union, Tuple, Dict, Any, NewType, Callable, Sequence, Iterable

# Primitivos
numero: int = 10
flutuante: float = 10.5 
booleano: bool = False 
string: str = "Alexandre Junior" 

# Sequências
lista: List[int] = [1, 2, 3] # Lista de inteiros
lista_str_int: List[Union[int, str]] = [1,2,3,"Alexandre"] # Lista de inteiros e strings
tupla: Tuple[int, int, int, str] = (1, 2, 3, "Alexandre") # Tupla de inteiros e string

# Dicionários e conjuntos
pessoa: Dict[str, Union[str,int]] = {"nome": "Alexandre", "sobrenome": "Junior", "idade": 30} # Dicionário com chaves
pessoa2: Dict[str, Any] = {"nome": "Alexandre", "sobrenome": "Junior", "idade": 30, "notas": [10, 8, 9]} # Dicionário com qualquer valor
pessoa3: Dict[str, Union[str, int, List[int]]] = {'nome': 'Alexandre', 'sobrenome': 'Junior', 'idade': 30, 'notas': [10, 8, 9]} # Dicionário com lista

# Meu tipo
MeuDict = Dict[str, Union[str, int, List[int]]] # Definindo um novo tipo ou alias
pessoa4: MeuDict = {'nome': 'Alexandre', 'sobrenome': 'Junior', 'idade': 30, 'notas': [10, 8, 9]} # Usando o novo tipo

# Meu outro tipo
UserId = NewType('UserId', str) # Definindo um novo tipo
user_id = UserId('123') # Usando o novo tipo

def retorna_funcao(funcao: Callable[[int,int], int]) -> Callable:
  return funcao

# def fala_oi():
#   print('Oi')
  
def soma(x: int,y: int) -> int:
  return x + y
  
# retorna_funcao(fala_oi)()
print(retorna_funcao(soma)(10,20))

# Classes

class Pessoa:
  def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
    self.nome: str = nome
    self.sobrenome: str = sobrenome
    self.idade: int = idade

  def falar(self) -> str:
    return f'{self.nome} está falando...'

  def comer(self, alimento: str) -> str:
    return f'{self.nome} está comendo {alimento}.'

  def beber(self, bebida: str) -> str:
    return f'{self.nome} está bebendo {bebida}.'
  
p1 = Pessoa('Alexandre', 'Junior', 30)
print(p1.falar())
print(p1.comer('maçã'))
print(p1.beber('água'))

# Sequenciais
def iterar(sequencia: Sequence[int]) -> List[int]:
  return [x * 2 for x in sequencia]

def iterar2(sequencia: Iterable[int]) -> List[int]:
  return [x  for x in sequencia]

print(iterar([1,2,3]))
print(iterar2([1,2,3]))