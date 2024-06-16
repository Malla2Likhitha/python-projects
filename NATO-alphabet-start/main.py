import pandas

# TODO 1. Create a dictionary in this format:
nato_df = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(nato_df.to_dict())
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
# print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    name = input('Your name: ').upper()
    try:
        nato_name = [nato_dict[i] for i in name]
    except KeyError:
        print('Only alphabets please..')
        continue
    else:
        print(nato_name)
        break

