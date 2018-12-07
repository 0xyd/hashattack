import csv
import hashlib

# Transform source data to training dataset
hash_f = dict()
hash_f['md5'] = hashlib.md5
hash_f['sha1'] = hashlib.sha1
hash_f['sha224'] = hashlib.sha224
hash_f['sha256'] = hashlib.sha256

raw_data_files = [
	'bt4-password.txt', 
	'cirt-default-passwords.txt', 
	'darkweb2017-top10000.txt', 
	'Keyboard-Combinations.txt',
	'Most-Popular-Letter-Passes.txt',
	'openwall.net-all.txt',
	'probable-v2-top12000.txt']

train_data_files = [
	'bt4-password.csv', 
	'cirt-default-passwords.csv', 
	'darkweb2017-top10000.csv', 
	'Keyboard-Combinations.csv',
	'Most-Popular-Letter-Passes.csv',
	'openwall.net-all.csv',
	'probable-v2-top12000.csv'
]

input_path  = 'data'
output_path = 'training_data'

def transfer2hash(message, hash_names):

	data = []
	for name in hash_names:
		data.append(hash_f[name](message.encode('utf8')).hexdigest())

	return data

headers = ['password', 'md5', 'sha1', 'sha224', 'sha256']

for input_file, output_file in zip(raw_data_files, train_data_files):

	read_file = open('data/'+input_file, 'rb')

	with open('training_data/'+output_file, 'w') as csv_file:

		csv_writer = csv.writer(csv_file, delimiter=',')
		csv_writer.writerow(headers)

		while True:

			pwd = read_file.readline()
			if pwd == '':
				break
			pwd = pwd.decode('utf8', errors='ignore').strip()
			row = [pwd]
			row.extend(transfer2hash(pwd, ['md5', 'sha1', 'sha224', 'sha256']))
			csv_writer.writerow(row)
			break
	read_file.close()
