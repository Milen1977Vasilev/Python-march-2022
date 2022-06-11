groups_count = int(input())
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_people = 0

for groups in range(1, groups_count + 1):
    people = int(input())
    if people < 6:
        musala += people
        total_people += people
    elif people < 13:
        monblan += people
        total_people += people
    elif people < 26:
        kilimanjaro += people
        total_people += people
    elif people < 41:
        k2 += people
        total_people += people
    else:
        everest += people
        total_people += people
per_musala = musala / total_people * 100
per_monblan = monblan / total_people * 100
per_kilimanjaro = kilimanjaro / total_people * 100
per_k2 = k2 / total_people * 100
per_everest = everest / total_people * 100
print(f"{per_musala:.2f}%")
print(f"{per_monblan:.2f}%")
print(f"{per_kilimanjaro:.2f}%")
print(f"{per_k2:.2f}%")
print(f"{per_everest:.2f}%")