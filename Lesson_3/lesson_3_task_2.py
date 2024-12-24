import smartphone

catalog = [smartphone.Smartphone("samsung", "galaxy", "+79243335577"),
           smartphone.Smartphone("Vivo", "G2", "+79258529674"),
           smartphone.Smartphone("Apple", "Apple12", "+79747891245"),
           smartphone.Smartphone("Nokia", "3310", "+79885694423"),
           smartphone.Smartphone("Xiomi", "Redmi note 8", "+79775896314")]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number} ")

