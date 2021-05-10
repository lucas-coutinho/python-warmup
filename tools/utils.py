
__all__ = ['cos_sim', 'diff', 'pearson_corr']

def cos_sim(point1, point2) -> float:
    def dot(point1,  point2) -> float:
        pointwise_mult=[point1[a]*point2[a] for a in range(len(point1))]
        return pointwise_mult

    def mod(point) -> float:
        return (sum([x**2 for x in point]))**(1/2)

    return sum(dot(point1, point2))/(mod(point1)*mod(point2))

def diff(point1, point2) -> float:
    return sum([point1[i] - point2[i] for i in range(len(point1))])

def pearson_corr(point1, point2) -> float:
    def dot(point1,  point2) -> float:
        u1 = mean(point1)
        u2 = mean(point2)
        pointwise_mult=[(point1[a] - u1)  * ( point2[a] - u2) for a in range(len(point1))]
        return pointwise_mult

    def mod(point) -> float:
        u = mean(point)
        return (sum([(x - u)**2 for x in point]))**(1/2)

    return sum(dot(point1, point2))/(mod(point1)*mod(point2))
