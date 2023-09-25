units = input("Pounds(1) or Kilograms(2)?: ")
weight = float(input("Input Weight: "))


if units == "2" :
    weight = weight * 2.205


def round_25(balls) :
    a = balls / 25
    return round(a) * 25

h = round(0.866 * weight + 26.3)
a = round(1.44 * weight + 86.4)
t = round(1.77 * weight + 49.4)
m = round(2.52 * weight + 138)
a2= round(2.92 * weight + 147)
n = round(2.5 * weight + 379)
death = round(3.5 * weight + 470)

print(f"Threshold Effects: {h} mg ({round_25(h)} mg)")
print(f"Auditory Hallucinations: {a} ({round_25(a)}) mg")
print(f"Minor Audiovisual Hallucinations: {t} mg ({round_25(t)} mg)")
print(f"Major Audiovisual Hallucinations: {m} mg ({round_25(m)} mg)")
print(f"Mild Delirium: {a2} mg ({round_25(a2)} mg)")
print(f"Total Delirium: {n} mg ({round_25(n)} mg)")
print(f"/!\ EIRIEL: {death} mg ({round_25(death)} mg) WARNING : HIGH RISK OF DEATH DO NOT ATTEMPT!")


