sequences = ["EJG", "GEECG", "CGJEE", "JJGECCG"]
elements = ["E", "G", "C", "J"]
numbered_sequences = []
for seq in sequences:
    numbered_sequence = ""
    for char in seq:
        numbered_sequence += str(elements.index(char))
    numbered_sequences.append(numbered_sequence)

print(numbered_sequences)

S = [[9, -4, 2, 2], [-4, 9, -5, -5], [2, -5, 10, 7], [2, -5, 7, 10]]

for row in range(len(numbered_sequences)):
    for col in range(row + 1, len(numbered_sequences)):
        # print(numbered_sequences[i])
        # print(numbered_sequences[j])
        sequence1 = numbered_sequences[row]
        sequence2 = numbered_sequences[col]
        gap_penalty = -3
        pairwise_alignment_scores = []

        for i in range(len(sequence1) + 1):
            pairwise_alignment_scores.append([0] * (len(sequence2) + 1))

        # print(pairwise_alignment_scores)
        for i in range(1, len(sequence1) + 1):
            pairwise_alignment_scores[i][0] = pairwise_alignment_scores[i - 1][0] + gap_penalty
        for j in range(1, len(sequence2) + 1):
            pairwise_alignment_scores[0][j] = pairwise_alignment_scores[0][j - 1] + gap_penalty

        # print (pairwise_alignment_scores)
        for i in range(1, len(sequence1) + 1):
            for j in range(1, len(sequence2) + 1):
                # print(pairwise_alignment_scores[i - 1][j] + gap_penalty)
                # print(pairwise_alignment_scores[i][j - 1] + gap_penalty)
                # print(pairwise_alignment_scores[i - 1][j - 1] + S[int(sequence1[i - 1])][int(sequence2[j - 1])])
                pairwise_alignment_scores[i][j] = max(pairwise_alignment_scores[i - 1][j] + gap_penalty,
                                                pairwise_alignment_scores[i][j - 1] + gap_penalty,
                                                pairwise_alignment_scores[i - 1][j - 1] + S[int(sequence1[i - 1])][int(sequence2[j - 1])]
                                                )
        new_sequence1 = ""
        new_sequence2 = ""
        for pos in sequence1:
            new_sequence1 += elements[int(pos)]
        for pos in sequence2:
            new_sequence2 += elements[int(pos)]
        print("pairwise alignment score for sequence", new_sequence1, "and", new_sequence2, "is ")
        print(pairwise_alignment_scores)
