import address
import mailing


to_address = address.Address("12345", "Чита", "Ул. Ленина", "10", "12")
from_address = address.Address("67890", "Волгоград", "Ул.Бабушкина", "1", "5")

mailo = mailing.Mailing(to_address, from_address, "2500", "1452")
print(f"{mailo.track} из {mailo.from_address.index}, {mailo.from_address.city}, {mailo.from_address.street}, "
      f"{mailo.from_address.house} - {mailo.from_address.apartment} в {mailo.to_address.index}, "
      f"{mailo.to_address.city}, {mailo.to_address.street}, {mailo.to_address.house} - {mailo.to_address.apartment}."
      f" Стоимость {mailo.cost} рублей.")


