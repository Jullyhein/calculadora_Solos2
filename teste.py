import logging
import os 
import pandas as pd
from flask import Flask, render_template, request

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def calculadora_mesas_teste(poste, fileira, grau, regiao, modulo, quantidade):
    # Caminho para o arquivo no diretório "downloads"
    downloads_folder = os.path.join(os.getcwd(), 'downloads')
    file_path = os.path.join(downloads_folder, 'PRECO-MODULO-JULLYEN.xlsx')

    # Verificar se o arquivo existe
    if not os.path.exists(file_path):
        logging.error(f"Arquivo não encontrado no caminho {file_path}")
        return {"error": f"Arquivo não encontrado no caminho {file_path}"}

    # Carregar o arquivo Excel
    try:
        df = pd.read_excel(file_path)
        logging.info("Arquivo Excel carregado com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao carregar o arquivo Excel: {e}")
        return {"error": f"Erro ao carregar o arquivo Excel: {e}"}

    # Padronizar os nomes das colunas
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    logging.debug(f"Colunas do DataFrame após padronização: {df.columns.tolist()}")

    # Verificar se as colunas necessárias existem
    required_columns = ['poste', 'fileiras', 'graus', 'região', 'módulo', 'preço_da_mesa_/módulo']
    if not all(col in df.columns for col in required_columns):
        logging.error(f"Colunas necessárias não encontradas. Colunas atuais: {df.columns.tolist()}")
        return {"error": f"Colunas necessárias não encontradas no arquivo."}

    # Tratar os parâmetros recebidos
    try:
        modulo = int(modulo) if str(modulo).isdigit() else modulo
        quantidade = int(quantidade) if str(quantidade).isdigit() else None

        # Filtrar o DataFrame para encontrar o preço correspondente
        resultado = df[
            (df['poste'] == poste) &
            (df['fileiras'] == fileira) &
            (df['graus'] == grau) &
            (df['região'] == regiao) &
            (df['módulo'] == modulo)
        ]

        logging.debug(f"Resultado do filtro:\n{resultado}")

        if not resultado.empty:
            # Obter o preço correspondente
            preco = float(resultado['preço_da_mesa_/módulo'].iloc[0])
            logging.info(f"Preço encontrado: {preco}")

            # Calcular o total
            if quantidade and quantidade > 0:
                total = preco * quantidade
                logging.info(f"Total calculado: {total}")
                return {
                    "postes": df['poste'].dropna().unique().tolist(),
                    "fileiras": df['fileiras'].dropna().unique().tolist(),
                    "graus": df['graus'].dropna().unique().tolist(),
                    "regioes": df['região'].dropna().unique().tolist(),
                    "modulos": df['módulo'].dropna().unique().tolist(),
                    "preco": preco,
                    "total": total,
                }
            else:
                logging.warning("Quantidade inválida fornecida.")
                return {"error": "Quantidade inválida. Insira um número positivo."}
        else:
            logging.warning("Nenhum resultado encontrado no filtro.")
            return {"error": "Nenhum resultado encontrado para os critérios selecionados."}

    except Exception as e:
        logging.error(f"Erro durante o cálculo: {e}")
        return {"error": f"Erro ao processar os dados: {e}"}


def tratar_coluna_preco(df, coluna):
    downloads_folder = os.path.join(os.getcwd(), 'downloads')
    file_path = os.path.join(downloads_folder, 'PRECO-MODULO-JULLYEN.xlsx')
    df = pd.read_excel(file_path)
    if coluna not in df.columns:
        raise ValueError(f"A coluna '{coluna}' não foi encontrada no DataFrame.")
    
    # Log inicial
    logging.info(f"Tratando a coluna '{coluna}'.")

    try:
        # Remover símbolos de dólar e vírgulas, e converter para float
        df[coluna] = (
            df[coluna]
            .astype(str)  # Converter para string (caso não esteja)
            .str.replace(r"[^0-9.,]", "", regex=True)  # Remove caracteres não numéricos
            .str.replace(",", "")  # Remove vírgulas
            .astype(float)  # Converte para float
        )
        logging.info(f"Coluna '{coluna}' tratada com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao tratar a coluna '{coluna}': {e}")
        raise

    return df


result = calculadora_mesas_teste(
    poste="Monoposte",
    fileira=2,
    grau=15,
    regiao=3,
    modulo=1303,
    quantidade=15
)

print(result)