print('{:=^40}'.format(' LOJAS GUANABARAS! '))
#o sinal circunflexo centraliza // # :=^40 --> quarenta espaço
preco = float(input('preço da  compra: R$'))
print(''' Formas de pagamento
      [01] à vista dinheiro/cheque
      [02] à vista cartão
      [03] 2x no cartão
      [04] 3x ou mais no cartão ''')
opcao = int(input('Qual é a opção: '))
if opcao == 1:
    total=preco-(preco * 0.10)
elif opcao == 2:
    total=preco-(preco * 0.05)
elif opcao == 3:
    total=preco
    parcelas=total/2
    print('Sua compra será parcelada em 2x de {:.2f} SEM JUROS'.format(parcelas))
elif opcao == 4:
    total=preco+(preco*0.20)
    totparc=int(input('quantas parcelas?'))
    parcelas = total / totparc
    print('sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc,parcelas))    
else:
    total = preco
    print('OPÇÃO INVALIDA de pagamento. Tente novamete!')
print('sua compra de R${:.2f} vai custa R${:.2f} no final.'.format(preco,total))               
      