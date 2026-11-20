print ("---The Codemother ROI calculator---")

uren_tekst = input("Uren per week kwijt aan deze taak?")
uren_per_week = float(uren_tekst)
uurloon_tekst =input("uurloon van de medewerker?")
uurloon= float(uurloon_tekst)
efficientie_tekst =input("Procent opgelost door AI?:")
efficientie =float(efficientie_tekst)
investering = float(input("Wat zijn de eenmalige kosten om de AI Agent te bouwen?"))

kosten_per_week = uren_per_week * uurloon
besparing_per_week = kosten_per_week * (efficientie/100)
besparing_per_maand = besparing_per_week * 4.33
besparing_per_jaar = besparing_per_maand * 52
weken_terugverdiend = investering/ besparing_per_week


print(f"\n[Resultaat]")
print(f"Besparing per week:{besparing_per_week:.2f} Euro")
print(f"Besparing per maand:{besparing_per_maand:.2f} Euro")
print(f"Besparing per jaar:{besparing_per_jaar:.2f} Euro")
print(f"De klant heeft de investeringterugverdiendin: {weken_terugverdiend:.1f} weken!")