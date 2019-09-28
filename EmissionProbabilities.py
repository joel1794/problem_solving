msa = [["A", "-", "A", "B", "-", "B", "A", "F", "C", "D", "-", "B", "-", "A", "A", "E", "A", "0", "A", "C", "E", "D", "A", "-", "E", "Q", "-", "-", "-", "A", "-", "A", "B", "C", "D", "B", "A", "L", "F", "4", "-", "B", "B", "A", "S", "B", "-", "-", "-", "A", "A", "A", "A", "F", "B"],
["A", "-", "A", "B", "N", "B", "A", "F", "C", "D", "-", "B", "-", "A", "A", "E", "A", "A", "B", "C", "E", "D", "A", "-", "E", "Q", "-", "C", "D", "A", "B", "A", "B", "-", "-", "B", "A", "-", "F", "4", "N", "B", "B", "M", "-", "B", "T", "Y", "B", "A", "A", "A", "A", "-", "-"],
["A", "-", "A", "B", "-", "B", "A", "F", "C", "D", "A", "B", "-", "A", "-", "E", "A", "A", "-", "C", "E", "D", "C", "D", "E", "Q", "A", "-", "-", "A", "B", "F", "B", "A", "N", "-", "-", "-", "F", "4", "-", "B", "B", "A", "F", "B", "T", "Y", "B", "A", "A", "A", "A", "-", "-"],
["2", "A", "A", "B", "-", "B", "A", "F", "C", "D", "A", "B", "-", "A", "-", "E", "A", "A", "B", "C", "E", "D", "C", "D", "E", "Q", "F", "C", "D", "A", "B", "A", "-", "A", "P", "A", "L", "-", "F", "4", "-", "B", "B", "A", "-", "-", "S", "B", "A", "A", "A", "A", "A", "-", "-"],
["C", "D", "A", "B", "-", "B", "A", "F", "C", "D", "B", "1", "-", "A", "A", "E", "A", "A", "-", "C", "E", "D", "A", "-", "E", "Q", "-", "C", "D", "A", "B", "A", "B", "A", "B", "A", "L", "-", "F", "4", "L", "B", "B", "A", "F", "B", "S", "B", "A", "A", "A", "A", "A", "-", "-"],
["C", "D", "A", "B", "A", "A", "A", "-", "-", "-", "-", "B", "-", "A", "-", "E", "A", "-", "A", "C", "E", "D", "C", "D", "E", "Q", "-", "-", "-", "A", "-", "A", "B", "C", "D", "-", "A", "-", "F", "4", "-", "B", "B", "A", "S", "B", "-", "-", "-", "A", "A", "A", "A", "F", "B"],
["C", "D", "A", "B", "-", "-", "A", "-", "C", "D", "A", "B", "-", "A", "-", "E", "A", "A", "-", "C", "E", "D", "A", "-", "E", "Q", "-", "C", "D", "A", "B", "C", "D", "C", "D", "A", "A", "-", "F", "4", "M", "B", "B", "-", "-", "A", "T", "Y", "B", "A", "A", "A", "A", "-", "-"],
["-", "-", "A", "A", "-", "B", "A", "-", "C", "D", "B", "-", "-", "A", "A", "E", "A", "A", "-", "C", "E", "D", "C", "D", "E", "Q", "-", "C", "D", "A", "B", "P", "B", "A", "-", "A", "B", "-", "F", "4", "-", "B", "B", "A", "F", "B", "S", "B", "M", "A", "A", "A", "A", "-", "-"],
["C", "D", "A", "B", "-", "-", "R", "B", "A", "F", "A", "B", "P", "A", "A", "E", "A", "-", "A", "C", "E", "D", "C", "D", "E", "Q", "A", "A", "B", "C", "D", "A", "F", "A", "L", "-", "-", "-", "F", "4", "N", "B", "B", "A", "S", "B", "-", "-", "-", "A", "A", "A", "A", "M", "B"],
["A", "-", "A", "B", "A", "A", "-", "-", "-", "-", "-", "B", "-", "A", "A", "E", "A", "-", "A", "C", "E", "D", "C", "D", "E", "Q", "A", "A", "B", "A", "F", "A", "-", "-", "-", "-", "-", "-", "F", "4", "B", "N", "B", "A", "S", "B", "-", "-", "-", "A", "A", "A", "A", "F", "B"]]

distinct_elements = []
for sequence in msa:
    for element in sequence:
        if element not in distinct_elements:
            distinct_elements.append(element)

# print(len(distinct_elements))
distinct_elements.remove('-')
# print(len(distinct_elements))
distinct_elements_count = len(distinct_elements)
match_indexes = []
insert_indexes = []

for i in range(len(msa[0])):
    count = 0
    for j in range(len(msa)):
        if msa[j][i] == '-':
            count += 1
    if count > 5:
        insert_indexes.append(i)
    else:
        match_indexes.append(i)

print(insert_indexes)
print(match_indexes)

emission_probability = {}
match_state_count = 0

# for element in distinct_elements:
#     emission_probability[element] = 0
#
# print(emission_probability)
print("Match state and insert state emission probabilities are as follows")
elements_in_insert_state = 0

for element in distinct_elements:
    emission_probability[element] = 0
for element in emission_probability:
    emission_probability[element] = 1 / distinct_elements_count

print("I", match_state_count, emission_probability)

for i in range(len(msa[0])):
    if i in match_indexes:
        for element in distinct_elements:
            emission_probability[element] = 0
        for j in range(len(msa)):
            if msa[j][i] != '-':
                emission_probability[msa[j][i]] += 1
        for element in emission_probability:
            emission_probability[element] = (emission_probability[element] + 1) / (len(msa) + distinct_elements_count)
        match_state_count += 1
        print("M", match_state_count, emission_probability)

    if i in insert_indexes:
        elements_in_insert_state = 0
        for element in distinct_elements:
            emission_probability[element] = 0
        for j in range(len(msa)):
            if msa[j][i] != '-':
                emission_probability[msa[j][i]] += 1
                elements_in_insert_state += 1
        for element in emission_probability:
            emission_probability[element] = (emission_probability[element] + 1) / (elements_in_insert_state + distinct_elements_count)
        print("I", match_state_count, emission_probability)
    elif i + 1 not in insert_indexes:
        for element in distinct_elements:
            emission_probability[element] = 0
        for element in emission_probability:
            emission_probability[element] = 1 / distinct_elements_count
        print("I", match_state_count, emission_probability)

