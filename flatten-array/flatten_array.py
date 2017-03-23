#SOFCOBBLED
def flatten(xs):
    res = []
    def loop(ys):
        for i in ys:
            if isinstance(i, list):
                loop(i)
            elif i == None or isinstance(i, tuple):
            	pass
            else:
                res.append(i)
    loop(xs)
    return res