a = input('Nhap so luong chai: ')
for bot in range(int(a),0,-1):
	if bot == 1 :
		print(bot ,"bottle of beer on the wall," , bot , "bottle of beer")
		print("Go to the store and buy some more," ,len(range(int(a))) ,"bottles of beer on the wall.")
	else:
		print(bot ,"bottles of beer on the wall," , bot , "bottles of beer")
		print("Take one down and pass it around," ,bot-1, "bottles of beer on the wall.")

