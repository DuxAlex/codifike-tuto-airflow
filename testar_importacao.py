try:
    #digite a bibliteca que deseja testar se já esta no projeto
    import operators
    print("O módulo está disponível para importação.")
except ImportError:
    print("O módulo NÃO está disponível.")