def seq_nummer():
    num = 0
    while True:
        num += 1
        yield num

seq_num = seq_nummer()

def moveTower(height, fromPole, toPole, withPole):
    print("seq: %d" % seq_num.next())
    print("height: %d, fromPole: %s, toPole: %s, withPole: %s" % (height, fromPole, toPole, withPole))
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

moveTower(3,"A","B","C")