import copy
class Room:
	def _init_(self, floor, room_no, capacity, start_time, end_time):
		self.floor = floor
		self.room_no = room_no
		self.capacity = capacity
		self.start_time = start_time
		self.end_time = end_time

	def _str_(self):
		return "ROOM:- floor : " + str(self.floor) + ", room_no : " + str(self.room_no) + ", capacity : " + str(self.capacity) + ", start_time : " + str(self.start_time) + ", end_time : " + str(self.end_time)


room_dict = {}

f = open("rooms.txt", "r")
f1 = f.readlines()
f.close()


list_rooms = []
for line in f1:
	room_details = line.split(",")
	index = 0
	# print "room_details : " + str(room_details)
	# print "size : " + str(len(room_details))
	for entry in room_details:
		if index == 0:
			floor_room = entry.split(".")
			floor = int(floor_room[0])
			room_no = int(floor_room[1])
		elif index == 1:
			capacity = int(entry)
		elif index%2 == 0:
			start_time_string = entry.replace(":",".")
			try:
				start_time = float(start_time_string)
			except:
				raise Exception("INCORRECT INPUT FORMAT!")
		elif index%2 == 1:
			end_time_string = entry.replace(":",".")
			try:
				end_time = float(end_time_string)
			except:
				raise Exception("INCORRECT INPUT FORMAT!")
			# print "index : " + str(index) + ", floor : " + str(floor) + ", room_no : " + str(room_no) + ", capacity : " + str(capacity) + ", start_time : " + str(start_time) + ", end_time : " + str(end_time)
			room = Room(floor, room_no, capacity, start_time, end_time)
			list_rooms.append(room)
		index += 1

# for list_room in list_rooms:
# 	print str(list_room)


input_file = open("input.txt", "r")
input_room_details = input_file.readlines()
input_file.close()
for input_room_detail in input_room_details:
	output_list = []
	input_room = input_room_detail.split(",")
	members = int(input_room[0])
	current_floor = int(input_room[1])
	try:
		input_start_time = float(input_room[2].replace(":","."))
	except:
		raise Exception("INCORRECT INPUT FORMAT!")
	try:
		input_end_time = float(input_room[3].replace(":","."))
	except:
		raise Exception("INCORRECT INPUT FORMAT!")
	duration = input_end_time - input_start_time
	while (duration>0):
		current_room = None
		for room in list_rooms:
			if room.capacity>=members and room.start_time<=input_start_time and room.end_time>input_start_time:
				if current_room is None:
					current_room = room
				else:
					if abs(current_floor-room.floor)<=abs(current_floor-current_room.floor):
						if abs(current_floor-room.floor)==abs(current_floor-current_room.floor):
							if current_room.end_time<room.end_time:
								current_room = room
						else:
							current_room = room
		if not (current_room is None):
			# Getting the last inserted room and checking if it can be bypassed
			while output_list:
				last_room = output_list[-1]
				if input_start_time>=current_room.start_time and last_room.end_time<=current_room.end_time:
					# print "REMOVING : " + str(last_room)
					output_list.pop()
			output_list.append(current_room)
			duration = duration - (current_room.end_time - input_start_time)
			input_start_time = current_room.end_time
		else:
			break
	print "For input : " + input_room_detail
	if duration>0:
		print "NO ROOM IS AVAILABLE"
	else:
		for room in output_list:
			print str(room)
