BEGIN { SCORE = 0}
/A X/ { SCORE += 3 }
/B X/ { SCORE += 1 }
/C X/ { SCORE += 2 }
/A Y/ { SCORE += 4 }
/B Y/ { SCORE += 5 }
/C Y/ { SCORE += 6 }
/A Z/ { SCORE += 8 }
/B Z/ { SCORE += 9 }
/C Z/ { SCORE += 7 }
END { print SCORE }