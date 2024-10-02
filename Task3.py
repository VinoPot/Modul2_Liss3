car_input = input("Введите параметры автомобиля (например, “LADA 2010г 205000км 450000руб”): ")

brand, year, mileage, price = car_input.split()

print(f"Марка автомобиля: {brand}\nГод выпуска: {year}\nПробег: {mileage}\nЦена: {price}")