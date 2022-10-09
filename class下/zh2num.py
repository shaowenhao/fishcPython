class ZH_INT:
    def __init__(self,num):
        self.num = num
    def __int__(self):
        try:
            return int(self.num)
        except ValueError:
            zh = {"零":0,"五":5,"二":2}
            result = 0
            for each in self.num:
                if each in zh:
                    result += zh[each]
                else:
                    result += int(each)
                result *= 10

            return result // 10


