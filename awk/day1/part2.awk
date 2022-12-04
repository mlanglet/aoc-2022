BEGIN {
    CURRENT = 0
    TOP1 = 0
    TOP2 = 0
    TOP3 = 0
}
// {
    if(CURRENT > TOP1){
        TOP3 = TOP2
        TOP2 = TOP1
        TOP1 = CURRENT

    }
    CURRENT = 0
}
/[0-9]+/ {
    CURRENT += $0
}
END { print(TOP1 + TOP2 + TOP3) }