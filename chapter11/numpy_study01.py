import numpy as np
def seq_array():
    data1 = list(range(0, 10))
    print(type(data1), data1)
    a1 = np.array(data1)
    print(type(a1), a1.dtype, a1)

    data2 = [0.1, 5, 4, 12, 0.5]
    a2 = np.array(data2)
    print(a2.dtype, a2)


def two_dimension_array():
    a3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(a3.dtype, a3)


def range_array():
    print("np.arange(0, 10, 2): ", np.arange(0, 10, 2))
    print("np.arange(1, 10): ", np.arange(1, 10))
    print("np.arange(5) : ", np.arange(5))

    b1 = np.arange(12).reshape(4, 3)
    print("b1.shape : ", b1.shape)
    print("np.arange(12).reshape(4,3) : ", b1)

    print("np.arange(5): {}\nnp.arange(5) : {}".format(np.arange(5), np.arange(5).shape))


def num_array():
    n1 = np.linspace(1, 10, 10)
    print("np.linspace(1,10,10) : {}, dtype : {}".format(n1, n1.dtype))
    n2 = np.linspace(0, np.pi, 20)
    print("np.linspace(0,np.pi,20) : {}, dtype : {}".format(n2, n2.dtype))

    print(np.zeros(10))
    print(np.zeros((3, 4)))
    print(np.ones(5))
    print(np.ones((3, 5)))
    print(np.eye(5))


def type_conversion():
    str_array = np.array(['1.5', '0.62', '2', '3.14', '3.141592'])
    print(str_array,str_array.dtype)
    float_array = str_array.astype(float)
    print(float_array, float_array.dtype)


def rand_array():
    print(np.random.rand(2,3))
    print(np.random.rand())
    print(np.random.rand(2,3,4))

    print(np.random.randint(10,size =(3,4)))
    print(np.random.randint(1,30))


def array_cal():
    arr1 = np.array([10,20,30,40])
    arr2 = np.array([1,2,3,4])

    print("arr1 + arr2 = {}".format(arr1+arr2))
    print("arr1 - arr2 =",arr1-arr2)
    print("arr * 2 =",arr2*2)
    print("arr1 * arr2 = ",arr1*arr2)
    print("arr1 / arr2 = ",arr1/arr2)
    print("arr1 / (arr2 ** 2) =",arr1/(arr2**2))
    print("arr1 > 20 =",arr1>20)

    print("==================")
    arr3 = np.arange(5)
    print("arr 3 =",arr3)
    print("arr3.sum() = {}, arr3.mean() = {}".format(arr3.sum(),arr3.mean()))
    print("arr3.std() = {}, arr3.var() = {}".format(arr3.std(),arr3.var()))
    print("arr3.min() = {}, arr3.max() = {}".format(arr3.min(),arr3.max()))
    arr4 = np.arange(1,5)
    print("arr4 = ",arr4)
    print("arr4.cumsum() = {}, arr4.cumprod() = {}".format(arr4.cumsum(),arr4.cumprod()))

def matrix_ex():
    A = np.array([0,1,2,3]).reshape(2,2)
    B = np.array([3,2,0,1]).reshape(2,2)
    print("A = \n{}\nB = \n{}".format(A,B))
    print("A.dot(B) =\n",A.dot(B))
    print("np.dot(A,B) = \n",np.dot(A,B))
    print("np.transpose(A) = =\n",np.transpose(A))
    print("A.transpose() = \n",A.transpose())
    print("np.linalg.inv(A) = \n",np.linalg.inv(A))
    print("np.linalg.det(A) = ",np.linalg.det(A))



if __name__ == "__main__":
    seq_array()
    print("==================")
    two_dimension_array()
    print("==================")
    range_array()
    print("==================")
    num_array()
    type_conversion()
    print("==================")
    rand_array()
    print("==================")
    array_cal()
    print("==================")
    matrix_ex()