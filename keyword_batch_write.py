import pandas as pd

def refresh_keywords(file_name = "test.txt"):
	df = pd.read_csv("keyword_database_alpha.csv")
	for i, row in df.iterrows():
		if row['parsed_bool'] == 1:
			df.loc[i, 'parsed_bool'] = 0

	df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
	df.to_csv("keyword_database_alpha.csv")


def write_next_keyword_batch(number_of_words_in_batch = 1, file_name = "test.txt"):
	df = pd.read_csv("keyword_database_alpha.csv")
	number_of_words_till_now = 0
	f = open('Stage1_search_to_PDFURL/'+file_name, "w+")
	for i, row in df.iterrows():

		if row['parsed_bool'] == 0:
			number_of_words_till_now += 1
			df.loc[i, 'parsed_bool'] = 1
			f.write(str(row['keyword']) + '\n')

			if number_of_words_till_now >= number_of_words_in_batch:
				break

	df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
	df.to_csv("keyword_database_alpha.csv")
	f.close()

# refresh_keywords()
write_next_keyword_batch()
