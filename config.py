class Config:
    # Banco de dados SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'  # Caminho para o arquivo SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False        # Desativa o monitoramento de modificações
    HOST = 'localhost'                            # Endereço de hospedagem
    PORT = 5000                                   # Porta de execução
    DEBUG = True  