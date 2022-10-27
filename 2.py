literka= input('Podaj litere')

if len(literka)>1 or len(literka)==0:
    print('Nieprawidlowe')
if 'a'<= literka >='z':
    print('literka jest mala')
elif 'A' <= literka >='Z':
    print('literkaj jest duza')
else:
    print('to nie jest literka')