from smartphone import Smartphone

catalog = []

tel1 = Smartphone("Nokia", "3310", "+79884561212")
tel2 = Smartphone("Xiaomi", "CHFA", "+79451234565")
tel3 = Smartphone("Siemens", "A50", "+79188975522")
tel4 = Smartphone("HONOR", "10Lite Plus", "+79284445873")
tel5 = Smartphone("Motorola", "Opossum2", "+79283219874")

catalog.append(tel1)
catalog.append(tel2)
catalog.append(tel3)
catalog.append(tel4)
catalog.append(tel5)

for tel in catalog:
    print(f"{tel.marka} - {tel.model}, {tel.number} ")
