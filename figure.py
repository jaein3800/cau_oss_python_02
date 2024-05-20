"""
정사각형/원/정삼각형의 넓이 계산과 관련된 모듈
"""
import math

class Line:
    """
    외부에서 접근불가능한 필드 __length의 기본값은 1이며,
    생성자를 통해 초기 __length값을 지정할 수 있다.
    __length는 set_length와 get_length 메소드를 통해 접근할 수 있다.
    """
    __length = 1 # __length의 기본값은 1이다.

    def __init__(self, initial_length):
        """매개변수로 받은 값이 0보다 크고 정수, 혹은 실수인지 판단 후 __length의 초기값을 지정하는 함수
        Args:
            initial_length: __length의 초기 값
        Examples:
            >>> myline = figure.Line(10) # 초기 __length의 값을 10으로 지정
        """
        if type(initial_length) == float or int:
            if initial_length > 0:
                self.__length = initial_length
            else:
                pass
        else:
            pass

    def set_length(self, s_length):
        """매개변수로 받은 값이 0보다 크고 정수, 혹은 실수인지 판단 후 저장 중인 __length의 값을 변경하는 메소드
        Args:
            s_length: __length의 변경 값
        Examples:
            >>> myline.set_length(3) # 저장 중인 __length의 값을 3으로 변경한다.
        """
        if type(s_length) == float or int:
            if s_length > 0:
                self.__length = s_length
            else:
                pass
        else:
            pass

    def get_length(self):
        """현재 저장 중인 __length 값을 반환하는 메소드
        Returns:
            self.__length: 현재 저장 중인 __length 값
        Examples:
            >>> ret = myline.get_length()
        """
        return self.__length
    
def area_square(n):
    """매개변수로 전달받은 값이 Line클래스가 아닌 경우 숫자 0을 반환하고 이 외의 경우 정사각형의 넓이를 구하는 함수
    Args:
        n: 정사각형의 한 변의 길이
    Returns:
        int or float: 전달받은 값이 Line클래스 일 경우 n.get_length()**2
                      아닐 경우 숫자 0
    Examples:
        >>> myline = figure.Line(10); figure.area_square(myline) = 100
    """
    if type(n) != Line:
        return 0
    else:
        return n.get_length()**2

def area_circle(n):
    """매개변수로 전달받은 값이 Line클래스가 아닌 경우 숫자 0을 반환하고 이 외의 경우 원의 넓이를 구하는 함수
    Args:
        n: 원 반지름의 길이
    Returns:
        int or float: 전달받은 값이 Line클래스 일 경우 (n.get_length()**2)*math.pi
                      아닐 경우 숫자 0
    Examples:
        >>> myline = figure.Line(10); figure.area_circle(myline) = 314.1592653589793
    """
    if type(n) != Line:
        return 0
    else:
        return (n.get_length()**2)*math.pi

def area_regular_triangle(n):
    """매개변수로 전달받은 값이 Line클래스가 아닌 경우 숫자 0을 반환하고 이 외의 경우 정삼각형의 넓이를 구하는 함수
    Args:
        n: 정삼각형의 한 변의 길이
    Returns:
        int or float: 전달받은 값이 Line클래스 일 경우 (math.sqrt(3)/4)*(n.get_length()**2)
                      아닐 경우 숫자 0
    Examples:
        >>> myline = figure.Line(10); figure.area_triangle(myline) = 43.30127018922193
    """
    if type(n) != Line:
        return 0
    else:
        return (math.sqrt(3)/4)*(n.get_length()**2)