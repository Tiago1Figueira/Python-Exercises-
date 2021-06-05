while True:
    print('=' * 50, 'FÓRMULA PARA CÁLCULO DO TRAPÉZIO', '=' * 50)
    basemaior = float(input('Informe a base menor do trapézio:'))
    basemenor = float(input('Informe a base maior do trapézio:'))
    altura = float(input('Informe a altura do trapézio:'))
    trapezio = (basemaior + basemenor) * altura / 2
    print(f'A área do trapézio é {trapezio}!')

