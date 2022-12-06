BEGIN { SCORE = 0 }
/A X/ { SCORE += 4 }
/B X/ { SCORE += 1 }
/C X/ { SCORE += 7 }
/A Y/ { SCORE += 8 }
/B Y/ { SCORE += 5 }
/C Y/ { SCORE += 2 }
/A Z/ { SCORE += 3 }
/B Z/ { SCORE += 9 }
/C Z/ { SCORE += 6 }
END { print SCORE }