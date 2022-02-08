n = int(input())
card = []
result = []
for i in range(n):
    card.append(i+1)

while len(card) > 1:
    result.append(card[0])
    card.remove(card[0])
    card.append(card[0])
    card.remove(card[0])
result.append(card[0])

for re in result:
    print(re,end = ' ')