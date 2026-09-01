# ვქმნით საწყის ცვლადს
time = 10

# ციკლით სათითაოდ ვიღებთ რიცხვებს: 0, 1, 2
for i in range(3):
    time = time - i  # ყოველ ბიჯზე ვაკლებთ i-ს მნიშვნელობას

# ვბეჭდავთ საბოლოო შედეგს
print(time)

# საწყისი ცვლადების შექმნა
runner_a = 0
runner_b = 0

# ციკლი 0-იდან 5-ის ჩათვლით რიცხვების მისამატებლად
for i in range(6):
    runner_a = runner_a + i
    runner_b = runner_b + i

# საბოლოო შედეგების დაბეჭდვა ტერმინალში
print("Runner A:", runner_a)
print("Runner B:", runner_b)
