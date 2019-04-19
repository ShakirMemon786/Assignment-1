def remove_char(str, n):
        first_part = str[:n] 
        last_part = str[n+1:]
	return first_part + last_part
print(remove_char('shakir', 0))
print(remove_char('memon', 3))
print(remove_char('shakir', 5))
