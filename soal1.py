def hitung_rating():
    input_data = input("Masukkan rating (pisahkan dengan koma): ")
    data_list = list(map(float, input_data.split(',')))
    
    min_rating = min(data_list)
    max_rating = max(data_list)
    avg_rating = round(sum(data_list) / len(data_list), 1)
    
    if min_rating.is_integer():
        min_rating = int(min_rating)
    if max_rating.is_integer():
        max_rating = int(max_rating)
    if avg_rating.is_integer():
        avg_rating = int(avg_rating)
    
    return min_rating, max_rating, avg_rating

hasil = hitung_rating()

print(hasil)
