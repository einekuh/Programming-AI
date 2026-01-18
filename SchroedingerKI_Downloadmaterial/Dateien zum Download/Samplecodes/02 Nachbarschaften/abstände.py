import math
def euclidean_distance(point1, point2):
  return math.sqrt(sum((x - y)**2 for x, y in zip(point1, point2)))

def manhattan_distance(point1, point2):
    return sum(abs(x - y) for x, y in zip(point1, point2))

def cosine_similarity(vector1, vector2):    
    dot_product = sum(x * y for x, y in zip(vector1, vector2))
    magnitude1 = math.sqrt(sum(x ** 2 for x in vector1))
    magnitude2 = math.sqrt(sum(y ** 2 for y in vector2))
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0  # Ähnlichkeit ist 0, wenn einer der Vektoren ein Nullvektor ist
    
    return dot_product / (magnitude1 * magnitude2)

def cosine_distance(vector1, vector2):
    similarity = cosine_similarity(vector1, vector2)
    return 1 - similarity

p1 = (3,5)
p2 = (4,6)
print(euclidean_distance(p1, p2))
print(manhattan_distance(p1, p2))
print(cosine_distance(p1, p2))


print('3D')
p1 = (3,5,1)
p2 = (4,6,2)
print(euclidean_distance(p1, p2))
print(manhattan_distance(p1, p2))
print(cosine_distance(p1, p2))