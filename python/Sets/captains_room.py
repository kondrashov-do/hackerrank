number_of_people_in_room = int(input()) 
hotel_room_numbers = list(map(int, input().split())) 
print( (sum(set(hotel_room_numbers))*number_of_people_in_room - sum(hotel_room_numbers))//(number_of_people_in_room-1) ) 
