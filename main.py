class StudentsinMLOPS:
    def __init__(self, initial_strength=0):
        self.total_strength = 0

    def enrollStudents(self, count):
        self.total_strength += count

    def dropStudents(self, count):
        self.total_strength -= count

    def getTotalStrength(self):
        return self.total_strength

    def getClassName(self):
        return "StudentsinMLOPS"


if __name__ == '__main__':
    mlopsclass = StudentsinMLOPS()
    mlopsclass.enrollStudents(5)

    print(mlopsclass.getTotalStrength())