from main import StudentsinMLOPS

def test_enroll_students():
    mlops_class = StudentsinMLOPS(initial_strength=0)
    mlops_class.enrollStudents(10)
    assert mlops_class.getTotalStrength() == 10, "Enrollment test failed"

    print("Enroll Students test passed successfully!")

def test_drop_students():
    mlops_class = StudentsinMLOPS(initial_strength=0)
    mlops_class.enrollStudents(10)
    mlops_class.dropStudents(5)
    assert mlops_class.getTotalStrength() == 5, "Drop test failed"

    print("Drop Students test passed successfully!")

def test_get_class_name():
    mlops_class = StudentsinMLOPS(initial_strength=0)
    assert mlops_class.getClassName() == "StudentsinMLOPS", "Class name test failed"
    print("Get Class Name test passed successfully!")

if __name__ == "__main__":
    test_enroll_students()
    test_drop_students()
    test_get_class_name()
