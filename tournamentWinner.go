// Statement
// Given an array of pairs representing the teams that have competed against each
// other and an array containing the results of each competition, write a function that returns the winner of the tournament. 
// Competitions array has 2 strings, ["homeTeam" "awayTeam"], if the result of a match is 0, homeTeam loses, if its 1, homeTeam wins

// Solution:
// As a brute force approach we could create a array with winners based on the results, then we just return the most repeated string inside that array. 
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
