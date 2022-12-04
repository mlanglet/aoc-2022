BEGIN {
    CURRENT = 0
    MAX = 0
}
/^$/ {
    if(CURRENT > MAX){
        MAX = CURRENT
    }
    CURRENT = 0
}
/[0-9]+/ {
    CURRENT += $0
}
END { print MAX }