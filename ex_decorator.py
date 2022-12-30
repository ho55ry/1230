# ------------------------------------------------------------------------------------------
# 데코레이터(Decorator) 
# - 메서드에 의미 명확한 부여
# - 형식 : @xxxx
# ------------------------------------------------------------------------------------------
# 클래스 및 메서드 종류
# - 완성된 클래스 => 클래스
# - 미완성 클래스 => 추상클래스(Abstract Class)
#                   미구현(코드 없는 메서드) 메서드를 가지고 있는 클래스 => 구현되게 오버라이딩
#                   abc모듈 포함해서 사용함
# ------------------------------------------------------------------------------------------
# 메서드 종류
# - 객체 생성해야만 사용가능한 메서드 => self
#   : 인스턴스 메서드
# - 객체 생성없이 사용가능한 메서드 => cls
#   : 정적 메서드 -> 객체없이 사용 가능
#   : 클래스 메서드 -> 클래스 정보(cls) 가진 객체 없이 사용 가능
# ------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------
# 학생 정보 클래스
# - 클래스명: Student
# - 속    성
#      - 클래스 속성 : school
#      - 인스턴스 속성 : name, number, grade
# - 메서드
#      - 학교명 출력 
# ------------------------------------------------------------------------------------------
class Student:
    school='아양중'

    def __init__(self,name,number,grade):
        self.name=name
        self.number=number
        self.grade=grade
    
# 객체 생성없이 사용가능
    @staticmethod
    def showSchoolName(count):
        Student.school='신암중'
        print(Student.school,count,sep='  ,  ')

    @classmethod
    def printSchool(cls,count):
        print(cls)
        print(cls.school,count,sep='  ,  ')

# 클래스 및 객체 사용
print(Student.school)
Student.showSchoolName(1)
Student.printSchool(1)


# ------------------------------------------------------------------------------------------
# 대학생 정보 클래스
# - 클래스명: BigStudent
# - 속    성
#      - 클래스 속성 : school
#      - 인스턴스 속성 : name, number, grade, major
# - 메서드
#      - 학교명 출력 
# ------------------------------------------------------------------------------------------
class BigStudent(Student):
    
    # 클래스 변수
    school='경북대'
    # 인스턴스 생성 및 속성 초기화 메서드
    def __init__(self, name, number, grade, major):
        super().__init__(name, number, grade)
        self.major=major

# 클래스 및 객체 사용
BigStudent.showSchoolName(1) # 정적메서드 (Static) : St-의 클래스의 바뀐 변수가져옴
BigStudent.printSchool(1)    # 클래스 메서드 : BigSt-의 클래스 변수가져옴