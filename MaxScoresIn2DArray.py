pairwise_alignment_score = [["—", "85", "63", "74", "70", "84", "61", "57", "62", "70"], ["85", "—", "79", "73", "66", "59", "94", "61", "59", "51"], ["63", "79", "—", "75", "68", "60", "55", "85", "52", "65"], ["74", "73", "75", "—", "105", "54", "60", "78", "59", "53"], ["70", "66", "68", "105", "—", "40", "61", "79", "58", "39"], ["84", "59", "60", "54", "40", "—", "68", "45", "75", "78"], ["61", "94", "55", "60", "61", "68", "—", "64", "72", "42"], ["57", "61", "85", "78", "79", "45", "64", "—", "50", "70"], ["62", "59", "52", "59", "58", "75", "72", "50", "—", "81"], ["70", "51", "65", "53", "39", "78", "42", "70", "81", "—"]]

score_list = []
for row in pairwise_alignment_score:
    for record in row:
        score_list.append(record)

print(score_list)
int_score_list = []
for score in score_list:
    if score != '—':
        int_score_list.append(int(score))

# print(int_score_list.sort())
int_score_list.sort(reverse=True)
print(int_score_list)