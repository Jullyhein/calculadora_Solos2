
## Documentação da API Calculadora de Mesas

## Rota: `/`

### Descrição
Esta rota é responsável por retornar uma página inicial onde o usuário pode:
- Selecionar um **estado**.
- Filtrar os **municípios** disponíveis para o estado selecionado.
- Filtrar as **regiões** disponíveis com base no estado e município selecionados.

Se todos os critérios forem preenchidos (estado, município, e região), a aplicação:
1. Filtra os dados correspondentes no DataFrame.
2. Grava os critérios selecionados no banco de dados usando o modelo `Pesquisa`.

---

### **Endpoints**

#### `GET /`
Retorna uma página HTML com um formulário para o usuário selecionar os filtros.

#### `POST /`
Processa os filtros selecionados (estado, município, e região) enviados pelo formulário e grava os resultados no banco de dados.

---

### **Parâmetros de Requisição**

#### POST
| Parâmetro     | Tipo     | Obrigatório | Descrição                                                                 |
| :------------ | :------- | :---------- | :----------------------------------------------------- |
| `estado`      | `string` | Sim         | O estado a ser selecionado. Exemplo: `SP`.                                |
| `municipio`   | `string` | Sim         | O município associado ao estado selecionado. Exemplo: `São Paulo`.        |
| `regiao`      | `string` | Sim         | A região filtrada com base no estado e município selecionados. Exemplo: `1`. |

---

## Rota: `/mesas`

### Descrição
Essa rota é responsável por:
- Exibir uma interface para selecionar parâmetros relacionados a postes, fileiras, graus, região, módulos e quantidade.
- Calcular o preço total de uma mesa com base nos parâmetros selecionados e no conteúdo de uma planilha processada.
- Salvar os resultados no banco de dados SQLite usando o modelo `Mesa`.

---

### **Endpoints**

#### `GET /mesas`
Retorna uma página HTML que permite selecionar os seguintes parâmetros:
- Poste
- Fileiras
- Graus
- Região
- Módulo
- Quantidade

#### `POST /mesas`
Recebe os parâmetros enviados pelo formulário e realiza o cálculo do preço total com base nos dados da planilha. Salva o resultado no banco de dados.

![image](https://github.com/user-attachments/assets/9633f7d4-ca5d-4fbd-83b7-c21644fba7d0)


---

### **Parâmetros de Requisição**

#### POST
| Parâmetro     | Tipo       | Obrigatório | Descrição                                                                 |
| :------------ | :--------- | :---------- | :------------------------------------------------------------------------ |
| `poste`       | `string`   | Sim         | O tipo de poste. Exemplo: `padrão`.                                       |
| `fileiras`    | `string`   | Sim         | Número de fileiras. Exemplo: `2`.                                         |
| `graus`       | `string`   | Sim         | Grau de inclinação. Exemplo: `45`.                                        |
| `regiao`      | `string`   | Sim         | A região selecionada. Exemplo: `Sul`.                                     |
| `modulo`      | `string`   | Sim         | O tipo de módulo. Exemplo: `M1`.                                          |
| `quantidade`  | `integer`  | Sim         | A quantidade de mesas/módulos. Exemplo: `10`.                             |

---

![image](https://github.com/user-attachments/assets/39be72e7-78a6-4bab-8240-0ccff12f8e51)

### **Exemplo de Requisição HTTP**

#### `GET /mesas`
```http
GET /mesas HTTP/1.1
Host: localhost:5000/mesas



