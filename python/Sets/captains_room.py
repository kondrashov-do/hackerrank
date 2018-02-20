number_of_people_in_rooms = int(input()) 
hotel_room_numbers = list(map(int, input().split())) 
print( (sum(set(hotel_room_numbers))*number_of_people_in_rooms - sum(hotel_room_numbers))//(number_of_people_in_rooms-1) ) 