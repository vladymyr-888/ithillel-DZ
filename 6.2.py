input_numbers = int(input('Enter numbers 0 - 8640000'))
days , seconds = divmod(input_numbers,84600)
hours , seconds = divmod(seconds,3600)
minute , second = divmod(seconds,60)
format = 'день' if days == 1 else 'дня'
print(f'{days} {format},{str(hours).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}')