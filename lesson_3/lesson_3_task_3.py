from adress import Address
from mailing import Mailing

to_address = Address("346710", "Aksay", "Platova", "12", "173")
from_address = Address("780452", "Novgorod", "Nevskaya", "95", "36")
mailing = Mailing(to_address, from_address, 1349, "Бандероль")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.home} - {mailing.from_address.flat}. "
      f"В {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, " 
      f"{mailing.to_address.home} - {mailing.to_address.flat}. Стоимость {mailing.cost} рублей ")
