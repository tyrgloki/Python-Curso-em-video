# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

variable = input('Digite algo: ')

print(f'Tipo: {type(variable)}'
      f'isNum: {variable.isnumeric()}\n'
      f'isAlpha: {variable.isalpha()}\n'
      f'isAlphaNum: {variable.isalnum()}\n'
      f'isLower: {variable.islower()}\n'
      f'isUpper: {variable.isupper()}\n'
      f'isTitle: {variable.istitle()}\n'
      f'Len: {len(variable)}')
