def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p in points:
            d = {}
            for q in points:
                f = p[0]-q[0]
                s = p[1]-q[1]
                d[f*f + s*s] = 1 + d.get(f*f + s*s, 0)
            for k in d:
                res += d[k] * (d[k] -1)
        return res


#Solution posted by lilixu
def numberOfBoomerangs(self, points):
        count = 0
        for i in range(len(points)):
            h = {}
            for j in range(len(points)):
                if i != j:
                    dt = pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2)
                    count += h.get(dt, 0)
                    h[dt] = h.get(dt, 0) + 1
        return count*2
