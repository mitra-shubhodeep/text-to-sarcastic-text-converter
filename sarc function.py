text = input('Enter text: ')
sar_text=""
l=len(text)
for i in range(l):
    if i%2==0:
        sar_text+=text[i].lower()
    else:
        sar_text+=text[i].upper()

print(sar_text)
