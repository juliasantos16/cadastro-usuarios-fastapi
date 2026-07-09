class ContextoSimples:
    def __enter__(self):
        print('iniciar conexão...')
        return self

    def __exit__ (self, exc_type, exc_val, exc_tb):
        print('execuções em banco de dados.')

with ContextoSimples() as cs:
    print('fechando conexão com segurança.')
