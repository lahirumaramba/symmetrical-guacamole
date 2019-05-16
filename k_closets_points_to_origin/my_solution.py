from operator import itemgetter

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        point_distance = []
        result = []
        
        def distance_from_origin(point):
            x = point[0]
            y = point[1]
            
            return  math.sqrt((x*x) + (y*y))
        
        for point in points:
            distance = distance_from_origin(point)
            point_distance.append((point, distance))
            
            
        point_distance.sort(key=itemgetter(1))
        
        i = 0
        while i<K:
            point = point_distance[i][0]
            result.append(point)
            i += 1
            
        return result
