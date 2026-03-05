class calculator:
    """
Write a calculator class that is able to do calculations (dot product,
addition, subtraction) of 2 vectors.
Vector will always have identical sizes, no error handling.
Its up to you to find a decorator that can help you to use the Methods of the
calculator class without instantiating this class.
"""
    @staticmethod
    def dotproduct(V1, V2):
        result = 0
        for i in range(len(V1)):
            result += V1[i] * V2[i]
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1, V2):
        result = []
        for i in range(len(V1)):
            result.append(float(V1[i] + V2[i]))
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1, V2):
        result = []
        for i in range(len(V1)):
            result.append(float(V1[i] - V2[i]))
        print(f"Sous Vector is: {result}")
