package main

func TournamentWinner(competitions [][]string, results []int) string {
    var winners []string
	for i := 0; i < len(results); i++ {
        if results[i] == 0 {
            winners = append(winners, competitions[i][1])
        } else if results[i] == 1 {
            winners = append(winners, competitions[i][0])
        }
    }
	return mostRepeatedString(winners)
}

func mostRepeatedString(strs []string) string {
    freq := make(map[string]int)
    mostRepeated := strs[0]
    for _, str := range strs {
        freq[str]++
    }
    for _, str := range strs {
        if freq[str] > freq[mostRepeated] {
            mostRepeated = str
        }
    }

    return mostRepeated
}
