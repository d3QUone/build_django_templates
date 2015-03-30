#
# Vladimir Kasatkin. April, 2015
#

from config import SOURCE_DIRS, TARGET_DIR, TARGET_FILES
from os import listdir, remove
import sys

# 
# just put filename in tag insted of your include. This file will be searching in the same 
# folder with current "Target-File", example: 
# 
# [[[ "question__block.html" ]]]
#

def parse_base_file(folder, filename):
	try:
		f = open(folder + filename, "r")
		copy = f.read()
		f.close()

		# create empty file:
		f = open(TARGET_DIR + filename, "w")
		f.close()

		# open it for writing at the end:
		f = open(TARGET_DIR + filename, "a")

		left_t = 0
		right_t = 0
		ins = 0  # just stats

		# move 'left' side of file in new file adding nessesary insertions 
		while True:
			left_t = copy.find("[[[")

			if left_t == -1:
				print """File "{0}" complete with {1} insertions""".format(TARGET_DIR + filename, ins)

				# insert what left!!!
				f.write(copy)
				f.close()

				# if ins == 0:
				# 	print "No updates"
				# 	remove(TARGET_DIR + filename)

				break  # will be the last cycle 

			buf = copy[:left_t]

			f.write(buf)

			copy = copy[left_t + 3:]  # cut that,  len("[[[") = 3, that is flexible

			right_t = copy.find("]]]")

			include = copy[:right_t].replace('"', '').replace(' ', '')

			copy = copy[right_t + 3:]

			print 'Found "{0}"'.format(include)

			# open include, add content....
			try:
				include_file = open(folder + include, "r")
				include_content = include_file.read()
				include_file.close()

				f.write(include_content)
			except:
				print "No matching file found..."
				f.close()
				# delete target file...
				remove(TARGET_DIR + filename)
				break

			ins += 1

	except Exception as e:
		print "Error (parse_base_file): {0}".format(e)


if __name__ == "__main__":
	for targ_file in TARGET_FILES:
		for folder in SOURCE_DIRS:
			all_files = listdir(folder)

			if targ_file in all_files:
				parse_base_file(folder, targ_file)
				print "--"*40
				break
