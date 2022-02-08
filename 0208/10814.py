t = int(input())
m_list = []
for i in range(t):
    age, name = input().split()
    age = int(age)
    m_list.append((age,name))

m_list.sort(key = lambda x : x[0])

for member in m_list:
    print(member[0],member[1])
