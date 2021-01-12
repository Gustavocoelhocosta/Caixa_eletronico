from sistema import Caixa_eletronico

c = Caixa_eletronico()

c.registrar_abastecimento(100,2)
c.registrar_abastecimento(50,2)
c.registrar_abastecimento(20,2)
c.registrar_abastecimento(10,2)

c.mostrar_saldo()
y = c.aprovar_saque(10)[0]
x = c.aprovar_saque(10)[1]

print(f"{x[100]} - {x[50]} - {x[20]} - {x[10]}")
print(y)
c.mostrar_saldo()
