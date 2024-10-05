
Trees = []
HashTables = []


class StudentNode:
    def __init__(self, code, name):
        self.Code = code
        self.Name = name
        self.gr_num = 0
        self.next = None
        self.right = None
        self.tail = None


class CourseNode:
    def __init__(self, code, name):
        self.Code = code
        self.Name = name
        self.gr_num = 0
        self.next = None
        self.left = None
        self.tail = None


class GraphNode:

    def __init__(self, code):
        self.Code = code
        self.next = None
        self.prev = None


class HashNode:

    def __init__(self, code, pointer):
        self.Code = code
        self.next = None
        self.prev = None
        self.pointer = pointer


class GradeNode:
    def __init__(self, student_code, course_code, semester_code, grade):
        self.st_code = student_code
        self.co_code = course_code
        self.sem_code = semester_code
        self.grade = grade
        self.forward = None
        self.backward = None
        self.right_next = None
        self.right_prev = None
        self.left_next = None
        self.left_prev = None


# 0 means black and 1 means red
class NodeTree:
    def __init__(self, name, node):
        self.Name = name
        self.parent = None
        self.left = None
        self.right = None
        self.pointer = node
        self.color = 1


class RedBlackTree:
    # Balancing the tree after deletion
    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.left.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Node deletion
    def delete_node_helper(self, node, name):
        while node != self.TNULL and node.Name != name:
            if node.Name < name:
                node = node.right
            else:
                node = node.left

        if node.left == self.TNULL or node.right == self.TNULL:
            y = node
        else:
            y = self.successor(node)

        if node.left != self.TNULL:
            x = y.left
        else:
            x = y.right

        x.parent = y.parent
        if y.parent == self.TNULL:
            self.root = x
        else:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
        if y != node:
            node.Name = y.Name
            node.pointer = y.pointer
        if y.color == 0:
            self.delete_fix(x)
        return y

    # Balance the tree after insertion
    def fix_insert(self, k):
        while k.parent.color == 1 :
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def search_tree_helper(self, node, name):
        if node == self.TNULL or name == node.Name:
            return node
        if name < str(node.Name):
            return self.search_tree_helper(node.left, name)
        return self.search_tree_helper(node.right, name)

    def searchTree(self, k):
        return self.search_tree_helper(self.root, k)

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    def successor(self, x):
        if x.right != self.TNULL:
            return self.minimum(x.right)

        y = x.parent
        while y != self.TNULL and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self, x):
        if x.left != self.TNULL:
            return self.maximum(x.left)

        y = x.parent
        while y != self.TNULL and x == y.left:
            x = y
            y = y.parent

        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, name, node_s_c):
        node = NodeTree(name, node_s_c)
        node.parent = None
        node.Name = name
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.Name < x.Name:
                x = x.left
            else:
                if name > x.Name:
                    x = x.right
                else:
                    return

        node.parent = y
        if y is None:
            self.root = node
        else:
            if node.Name < y.Name:
                y.left = node
            else:
                y.right = node
        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return
        self.fix_insert(node)

    def get_root(self):
        return self.root

    def delete_node(self, item):
        self.delete_node_helper(self.root, item)

    def __print_helper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.Name) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def print_tree(self):
        self.__print_helper(self.root, "", True)

    def __init__(self, name):
        self.Name = name
        self.TNULL = NodeTree("a", None)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


class StudentLinkedList:
    students = LinkedList()

    def __init__(self, first):
        StudentLinkedList.students.head = first
        StudentLinkedList.students.tail = first

    # returns False if there wasn't duplicate
    @staticmethod
    def check_duplicate(student):
        node = StudentLinkedList.students.head
        while node is not None:
            if node.Code == student.Code or node.Name == student.Name:
                return True
            node = node.next
        return False

    @staticmethod
    def add_node(student):
        StudentLinkedList.students.tail.next = student
        StudentLinkedList.students.tail = student

    @staticmethod
    def edit_student(code, new_name):
        node = StudentLinkedList.students.head
        while node is not None:
            if node.Code == code:
                node.Name = new_name
                return
            node = node.next

    @staticmethod
    def delete_student(code):
        course_deleted = []
        node = StudentLinkedList.students.head
        if node.Code == code and StudentLinkedList.students.head == node:
            grade = node.right
            while grade is not None:
                if not isinstance(grade.backward, GradeNode):
                    if isinstance(grade.forward, GradeNode):
                        grade.forward.backward = grade.backward
                else:
                    if isinstance(grade.forward, GradeNode):
                        grade.backward.forward = grade.forward
                        grade.forward.backward = grade.backward
                    else:
                        grade.backward.forward = grade.forward

                if not isinstance(grade.right_prev, CourseNode):
                    if not isinstance(grade.right_next, GradeNode):
                        grade.right_prev.right_next = grade.right_next
                        node.next.tail = grade.right_next
                    else:
                        grade.right_prev.right_next = grade.right_next
                        grade.right_next.right_prev = grade.right_prev
                else:
                    if not isinstance(grade.right_next, GradeNode):
                        grade.right_prev.left = grade.right_next
                        node.next.tail = grade.right_next
                    else:
                        grade.right_prev.left = grade.right_next
                        grade.right_next.right_prev = grade.right_prev


                if not isinstance(grade.left_prev, StudentNode):
                    if not isinstance(grade.left_next, GradeNode):
                        grade.left_prev.left_next = grade.left_next
                        node.next.tail = grade.left_next
                    else:
                        grade.left_prev.left_next = grade.left_next
                        grade.left_next.left_prev = grade.left_prev
                else:
                    if not isinstance(grade.left_next, GradeNode):
                        grade.left_prev.right = grade.left_next
                        node.next.tail = grade.left_next
                    else:
                        grade.left_prev.right = grade.left_next
                        grade.left_next.left_prev = grade.left_prev
                pointer = grade
                course_deleted.append(grade.co_code)
                del grade
                grade = pointer
                grade = grade.left_next
            StudentLinkedList.students.head = node.next
            del node
            node2 = CourseLinkedList.courses.head
            while node2 is not None:
                if node2.Code in course_deleted:
                    node2.gr_num -= 1
                node2 = node2.next
            return
        while node.next is not None:
            if node.next.Code == code:
                grade = node.next.right
                while grade is not None:
                    if not isinstance(grade.backward, GradeNode):
                        if isinstance(grade.forward, GradeNode):
                            grade.forward.backward = grade.backward
                    else:
                        if isinstance(grade.forward, GradeNode):
                            grade.backward.forward = grade.forward
                            grade.forward.backward = grade.backward
                        else:
                            grade.backward.forward = grade.forward

                    if not isinstance(grade.right_prev, CourseNode):
                        if not isinstance(grade.right_next, GradeNode):
                            grade.right_prev.right_next = grade.right_next
                            node.next.tail = grade.right_next
                        else:
                            grade.right_prev.right_next = grade.right_next
                            grade.right_next.right_prev = grade.right_prev
                    else:
                        if not isinstance(grade.right_next, GradeNode):
                            grade.right_prev.left = grade.right_next
                            node.next.tail = grade.right_next
                        else:
                            grade.right_prev.left = grade.right_next
                            grade.right_next.right_prev = grade.right_prev


                    if not isinstance(grade.left_prev, StudentNode):
                        if not isinstance(grade.left_next, GradeNode):
                            grade.left_prev.left_next = grade.left_next
                            node.next.tail = grade.left_next
                        else:
                            grade.left_prev.left_next = grade.left_next
                            grade.left_next.left_prev = grade.left_prev
                    else:
                        if not isinstance(grade.left_next, GradeNode):
                            grade.left_prev.right = grade.left_next
                            node.next.tail = grade.left_next
                        else:
                            grade.left_prev.right = grade.left_next
                            grade.left_next.left_prev = grade.left_prev
                    pointer = grade
                    course_deleted.append(grade.co_code)
                    del grade
                    grade = pointer
                    grade = grade.left_next
                if StudentLinkedList.students.tail == node.next:
                    StudentLinkedList.students.tail = node
                    del node.next
                    node2 = CourseLinkedList.courses.head
                    while node2 is not None:
                        if node2.Code in course_deleted:
                            node2.gr_num -= 1
                        node2 = node2.next
                    return
                else:
                    pointer = node.next.next
                    del node.next
                    node.next = pointer
                    node2 = CourseLinkedList.courses.head
                    while node2 is not None:
                        if node2.Code in course_deleted:
                            node2.gr_num -= 1
                        node2 = node2.next
                    return
            node = node.next


    @staticmethod
    def check_existence(code):
        node = StudentLinkedList.students.head
        while node is not None:
            if node.Code == code:
                return True
            node = node.next
        return False

    @staticmethod
    def get_nameByCode(code):
        node = StudentLinkedList.students.head
        while node is not None:
            if node.Code == code:
                return node.Name
            node = node.next

    @staticmethod
    def get_graph():
        answer = []
        node = StudentLinkedList.students.head
        while node is not None:
            existence = False
            helper = 0
            for List in answer:
                if List.head.Code == node.Code:
                    existence = True
                    helper = List
                    break
            if existence:
                prime = node.next
                while prime is not None:
                    count_node = 0
                    count_prime = 0
                    count_lessons = 0
                    lesson_node = node.right
                    lesson_prime = prime.right
                    while lesson_node is not None:
                        while lesson_prime is not None:
                            if lesson_node.st_code == lesson_prime.st_code:
                                count_lessons += 1
                                if lesson_node.grade > lesson_prime.grade:
                                    count_node += 1
                                elif lesson_node.grade < lesson_prime.grade:
                                    count_prime += 1
                            lesson_prime = lesson_prime.left_next
                        lesson_node = lesson_node.left_next
                        lesson_prime = prime.right
                    if count_node > count_lessons / 2:
                        shit = GraphNode(prime.Code)
                        helper.tail.next = shit
                        shit.prev = helper.tail
                        helper.tail = shit
                    elif count_prime > count_lessons / 2:
                        existence2 = False
                        helper2 = 0
                        for List in answer:
                            if List.head.Code == prime.Code:
                                existence2 = True
                                helper2 = List
                                break
                        if existence2:
                            seg = GraphNode(node.Code)
                            helper2.tail.next = seg
                            seg.prev = helper2.tail.next
                            helper2.tail = seg
                        else:
                            b = LinkedList()
                            nigga = GraphNode(prime.Code)
                            seg = GraphNode(node.Code)
                            nigga.next = seg
                            seg.prev = nigga
                            b.head = nigga
                            b.tail = seg
            else:
                prime = node.next
                plus = GraphNode(node.Code)
                a = LinkedList()
                a.head = plus
                a.tail = plus
                while prime is not None:
                    count_node = 0
                    count_prime = 0
                    count_lessons = 0
                    lesson_node = node.right
                    lesson_prime = prime.right
                    while lesson_node is not None:
                        while lesson_prime is not None:
                            if lesson_node.st_code == lesson_prime.st_code:
                                count_lessons += 1
                                if lesson_node.grade > lesson_prime.grade:
                                    count_node += 1
                                elif lesson_node.grade < lesson_prime.grade:
                                    count_prime += 1
                            lesson_prime = lesson_prime.left_next
                        lesson_node = lesson_node.left_next
                        lesson_prime = prime.right
                    if count_node > count_lessons / 2:
                        shit = GraphNode(prime.Code)
                        a.tail.next = shit
                        shit.prev = a.tail
                        a.tail = shit
                    elif count_prime > count_lessons / 2:
                        existence2 = False
                        helper2 = 0
                        for List in answer:
                            if List.head.Code == prime.Code:
                                existence2 = True
                                helper2 = List
                                break
                        if existence2:
                            seg = GraphNode(node.Code)
                            helper2.tail.next = seg
                            seg.prev = helper2.tail.next
                            helper2.tail = seg
                        else:
                            b = LinkedList()
                            nigga = GraphNode(prime.Code)
                            seg = GraphNode(node.Code)
                            nigga.next = seg
                            seg.prev = nigga
                            b.head = nigga
                            b.tail = seg
            node = node.next
        return answer


class DynamicTable:
    a, b, p = 0, 0, 0

    def __init__(self, name):
        self.Name = name
        self.arr = [None]
        self.component_num = 0

    #index = 0 for students and 1 for courses
    @staticmethod
    def insert(node, i):
        if i == 1:
            if HashTables[0].Name == "courses":
                index = 0
            elif HashTables[1].Name == "courses":
                index = 1
        else:
            if HashTables[0].Name == "students":
                index = 0
            elif HashTables[1].Name == "students":
                index = 1
        if HashTables[index].component_num == len(HashTables[index].arr):
            new_arr = [None]*(2*len(HashTables[index].arr))
            sample = HashTables[index].arr
            HashTables[index].arr = new_arr
            for j in range(0, len(sample)):
                if sample[j] is not None:
                    node2 = sample[j].head
                    while node2 is not None:
                        HashTables[index].insert(HashNode(node2.Code, node2.pointer), i)
                        node2 = node2.next

        if HashTables[index].arr[DynamicTable.hashing(node.Code, index)] is None:
            a = LinkedList()
            a.head = node
            a.tail = node
            HashTables[index].arr[DynamicTable.hashing(node.Code, index)] = a
            HashTables[index].component_num +=1
        else:
            HashTables[index].arr[DynamicTable.hashing(node.Code, index)].tail.next = node
            node.prev = HashTables[index].arr[DynamicTable.hashing(node.Code, index)].tail
            HashTables[index].arr[DynamicTable.hashing(node.Code, index)].tail = node
            HashTables[index].component_num += 1

    @staticmethod
    def delete(code, i):
        if i == 1:
            if HashTables[0].Name == "courses":
                index = 0
            elif HashTables[1].Name == "courses":
                index = 1
        else:
            if HashTables[0].Name == "students":
                index = 0
            elif HashTables[1].Name == "students":
                index = 1

        if HashTables[index].component_num <= len(HashTables[index].arr)/4 and len(HashTables[index].arr) >= 4:
            sample = HashTables[index].arr
            HashTables[index].arr = [None]*(int(len(HashTables[index].arr)/2))
            for j in range(0, len(sample)):
                if sample[j] is not None:
                    node2 = sample[j].head
                    while node2 is not None:
                        HashTables[index].insert(HashNode(node2.Code, node2.pointer),i)
                        node2 = node2.next

        iterate = HashTables[index].arr[DynamicTable.hashing(code, index)].head
        while iterate is not None:
            if iterate.next is None:
                HashTables[index].arr[DynamicTable.hashing(code, index)] = None
                HashTables[index].component_num -= 1
            if (iterate.Code == code) and (HashTables[index].arr[DynamicTable.hashing(code, index)].head is not iterate) and (HashTables[index].arr[DynamicTable.hashing(code, index)].tail is not iterate):
                iterate.prev.next = iterate.next
                iterate.next.prev = iterate.prev
                HashTables[index].component_num -= 1
                del iterate
                return
            elif(iterate.Code == code) and (HashTables[index].arr[DynamicTable.hashing(code, index)].head is iterate):
                iterate.next.prev = None
                HashTables[index].arr[DynamicTable.hashing(code, index)].head = iterate.next
                HashTables[index].component_num -= 1
                del iterate
                return
            elif (iterate.Code == code) and (HashTables[index].arr[DynamicTable.hashing(code, index)].tail is not iterate):
                iterate.prev.next = None
                HashTables[index].arr[DynamicTable.hashing(code, index)].tail = iterate.prev
                HashTables[index].component_num -= 1
                del iterate
                return
            iterate = iterate.next

    @staticmethod
    def hashing(code, index):
        return (((DynamicTable.a * code) + DynamicTable.b) % DynamicTable.p) % len(HashTables[index].arr)

    @staticmethod
    def search(code, i):
        if i == 1:
            if HashTables[0].Name == "courses":
                index = 0
            elif HashTables[1].Name == "courses":
                index = 1
        else:
            if HashTables[0].Name == "students":
                index = 0
            elif HashTables[1].Name == "students":
                index = 1
        a = HashTables[index]
        iterate = HashTables[index].arr[DynamicTable.hashing(code, index)].head
        while iterate is not None:
            if iterate.Code == code:
                return iterate
            iterate = iterate.next


class CourseLinkedList:
    courses = LinkedList()

    def __init__(self, first):
        CourseLinkedList.courses.head = first
        CourseLinkedList.courses.tail = first

    # returns False if there wasn't duplicate
    @staticmethod
    def check_duplicate(course):
        node = CourseLinkedList.courses.head
        while node is not None:
            if node.Code == course.Code or node.Name == course.Name:
                return True
            node = node.next
        return False

    @staticmethod
    def check_existence(code):
        node = CourseLinkedList.courses.head
        while node is not None:
            if node.Code == code:
                return True
            node = node.next
        return False

    @staticmethod
    def add_node(course):
        CourseLinkedList.courses.tail.next = course
        CourseLinkedList.courses.tail = course

    @staticmethod
    def edit_course(code, new_name):
        node = CourseLinkedList.courses.head
        while node is not None:
            if node.Code == code:
                node.Name = new_name
                return
            node = node.next

    @staticmethod
    def delete_course(code):
        students_deleted = []
        node = CourseLinkedList.courses.head
        if node.Code == code and CourseLinkedList.courses.head == node:
            grade = node.left
            while grade is not None:
                if not isinstance(grade.backward, GradeNode):
                    if isinstance(grade.forward, GradeNode):
                        grade.forward.backward = grade.backward
                else:
                    if isinstance(grade.forward, GradeNode):
                        grade.backward.forward = grade.forward
                        grade.forward.backward = grade.backward
                    else:
                        grade.backward.forward = grade.forward

                if not isinstance(grade.right_prev, CourseNode):
                    if not isinstance(grade.right_next, GradeNode):
                        grade.right_prev.right_next = grade.right_next
                        node.next.tail = grade.right_next
                    else:
                        grade.right_prev.right_next = grade.right_next
                        grade.right_next.right_prev = grade.right_prev
                else:
                    if not isinstance(grade.right_next, GradeNode):
                        grade.right_prev.left = grade.right_next
                        node.next.tail = grade.right_next
                    else:
                        grade.right_prev.left = grade.right_next
                        grade.right_next.right_prev = grade.right_prev


                if not isinstance(grade.left_prev, StudentNode):
                    if not isinstance(grade.left_next, GradeNode):
                        grade.left_prev.left_next = grade.left_next
                        node.next.tail = grade.left_next
                    else:
                        grade.left_prev.left_next = grade.left_next
                        grade.left_next.left_prev = grade.left_prev
                else:
                    if not isinstance(grade.left_next, GradeNode):
                        grade.left_prev.right = grade.left_next
                        node.next.tail = grade.left_next
                    else:
                        grade.left_prev.right = grade.left_next
                        grade.left_next.left_prev = grade.left_prev
                pointer = grade
                students_deleted.append(grade.st_code)
                del grade
                grade = pointer
                grade = grade.right_next
            CourseLinkedList.courses.head = node.next
            del node
            node2 = StudentLinkedList.students.head
            while node2 is not None:
                if node2.Code in students_deleted:
                    node2.gr_num -= 1
                node2 = node2.next
            return
        while node.next is not None:
            if node.next.Code == code:
                grade = node.next.left
                while grade is not None:
                    if not isinstance(grade.backward, GradeNode):
                        if isinstance(grade.forward, GradeNode):
                            grade.forward.backward = grade.backward
                    else:
                        if isinstance(grade.forward, GradeNode):
                            grade.backward.forward = grade.forward
                            grade.forward.backward = grade.backward
                        else:
                            grade.backward.forward = grade.forward

                    if not isinstance(grade.right_prev, CourseNode):
                        if not isinstance(grade.right_next, GradeNode):
                            grade.right_prev.right_next = grade.right_next
                            node.next.tail = grade.right_next
                        else:
                            grade.right_prev.right_next = grade.right_next
                            grade.right_next.right_prev = grade.right_prev
                    else:
                        if not isinstance(grade.right_next, GradeNode):
                            grade.right_prev.left = grade.right_next
                            node.next.tail = grade.right_next
                        else:
                            grade.right_prev.left = grade.right_next
                            grade.right_next.right_prev = grade.right_prev


                    if not isinstance(grade.left_prev, StudentNode):
                        if not isinstance(grade.left_next, GradeNode):
                            grade.left_prev.left_next = grade.left_next
                            node.next.tail = grade.left_next
                        else:
                            grade.left_prev.left_next = grade.left_next
                            grade.left_next.left_prev = grade.left_prev
                    else:
                        if not isinstance(grade.left_next, GradeNode):
                            grade.left_prev.right = grade.left_next
                            node.next.tail = grade.left_next
                        else:
                            grade.left_prev.right = grade.left_next
                            grade.left_next.left_prev = grade.left_prev
                    pointer = grade
                    students_deleted.append(grade.st_code)
                    del grade
                    grade = pointer
                    grade = grade.right_next
                if CourseLinkedList.courses.tail == node.next:
                    CourseLinkedList.courses.tail = node
                    del node.next
                    node2 = StudentLinkedList.students.head
                    while node2 is not None:
                        if node2.Code in students_deleted:
                            node2.gr_num -= 1
                        node2 = node2.next
                    return
                else:
                    pointer = node.next.next
                    del node.next
                    node.next = pointer
                    node2 = StudentLinkedList.students.head
                    while node2 is not None:
                        if node2.Code in students_deleted:
                            node2.gr_num -= 1
                        node2 = node2.next
                    return
            node = node.next

    @staticmethod
    def get_nameByCode(code):
        node = CourseLinkedList.courses.head
        while node is not None:
            if node.Code == code:
                return node.Name
            node = node.next

    @staticmethod
    def get_graph():
        answer = []
        node = CourseLinkedList.courses.head
        while node is not None:
            existence = False
            helper = 0
            for List in answer:
                if List.head.Code == node.Code:
                    existence = True
                    helper = List
                    break
            if existence:
                prime = node.next
                while prime is not None:
                    count = 0
                    lesson_node = node.left
                    lesson_prime = prime.left
                    while lesson_node is not None:
                        while lesson_prime is not None:
                            if lesson_node.st_code == lesson_prime.st_code:
                                count += 1
                            lesson_prime = lesson_prime.right_next
                        lesson_node = lesson_node.right_next
                        lesson_prime = prime.left
                    if count > node.gr_num/2 and count > prime.gr_num/2:
                        a = LinkedList()
                        shit = GraphNode(prime.Code)
                        a.head = shit
                        a.tail = shit
                        answer.append(a)
                        pokh = GraphNode(prime.Code)
                        pokh.prev = helper.tail
                        helper.tail.next = pokh
                        helper.tail = pokh
            else:
                prime = node.next
                plus = GraphNode(node.Code)
                a = LinkedList()
                a.head = plus
                a.tail = plus
                while prime is not None:
                    count = 0
                    lesson_node = node.left
                    lesson_prime = prime.left
                    while lesson_node is not None:
                        while lesson_prime is not None:
                            if lesson_node.st_code == lesson_prime.st_code:
                                count += 1
                            lesson_prime = lesson_prime.right_next
                        lesson_node = lesson_node.right_next
                        lesson_prime = prime.left
                    if count > node.gr_num/2 and count > prime.gr_num/2:
                        shit = GraphNode(prime.Code)
                        a.tail.next = shit
                        shit.prev = a.tail
                        a.tail = shit
                answer.append(a)
            node = node.next
        return answer


class GradeLinkedList2Way:

    @staticmethod
    def add_node(grade):
        node = CourseLinkedList.courses.head
        while node is not None:
            if node.Code == grade.co_code:
                if node.left is None:
                    node.tail = grade
                    node.left = grade
                    node.gr_num += 1
                    grade.right_prev = node
                else:
                    grade.right_prev = node.tail
                    node.tail.right_next = grade
                    node.gr_num += 1
                    node.tail = grade
            node = node.next
        node = StudentLinkedList.students.head
        while node is not None:
            if node.Code == grade.st_code:
                if node.right is None:
                    node.tail = grade
                    node.right = grade
                    node.gr_num += 1
                    grade.left_prev = node
                else:
                    grade.left_prev = node.tail
                    node.tail.left_next = grade
                    node.gr_num += 1
                    node.tail = grade
            node = node.next

    @staticmethod
    def edit(st_code, co_code, new_grade):
        node = StudentLinkedList.students.head
        while node is not None:
            if node.Code == st_code:
                break
            node = node.next
        node = node.right
        while node is not None:
            if node.co_code == co_code:
                node.grade = new_grade
            node = node.left_next

    @staticmethod
    def delete(st_code, co_code):
        course_code = 0
        grade = StudentLinkedList.students.head
        while grade is not None:
            if grade.Code == st_code:
                grade.gr_num -= 1
                grade = grade.right
                break
            grade = grade.next
        while grade is not None:
            if grade.co_code == co_code:
                if not isinstance(grade.backward, GradeNode):
                    if isinstance(grade.forward, GradeNode):
                        grade.forward.backward = grade.backward
                else:
                    if isinstance(grade.forward, GradeNode):
                        grade.backward.forward = grade.forward
                        grade.forward.backward = grade.backward
                    else:
                        grade.backward.forward = grade.forward

                if not isinstance(grade.right_prev, CourseNode):
                    if not isinstance(grade.right_next, GradeNode):
                        grade.right_prev.right_next = grade.right_next
                    else:
                        grade.right_prev.right_next = grade.right_next
                        grade.right_next.right_prev = grade.right_prev
                else:
                    if not isinstance(grade.right_next, GradeNode):
                        grade.right_prev.left = grade.right_next
                    else:
                        grade.right_prev.left = grade.right_next
                        grade.right_next.right_prev = grade.right_prev


                if not isinstance(grade.left_prev, StudentNode):
                    if not isinstance(grade.left_next, GradeNode):
                        grade.left_prev.left_next = grade.left_next

                    else:
                        grade.left_prev.left_next = grade.left_next
                        grade.left_next.left_prev = grade.left_prev
                else:
                    if not isinstance(grade.left_next, GradeNode):
                        grade.left_prev.right = grade.left_next

                    else:
                        grade.left_prev.right = grade.left_next
                        grade.left_next.left_prev = grade.left_prev
                course_code = grade.co_code
                del grade
                node2 = CourseLinkedList.courses.head
                while node2 is not None:
                    if node2.Code == course_code:
                        node2.gr_num -= 1
                        break
                    node2 = node2.next
                return
            grade = grade.left_next

    @staticmethod
    def number_student(st_code):
        node = StudentLinkedList.students.head
        while node is not None:
            if node.Code == st_code:
                return node.gr_num
            node = node.next

    @staticmethod
    def number_course(st_code):
        node = CourseLinkedList.courses.head
        while node is not None:
            if node.Code == st_code:
                return node.gr_num
            node = node.next


class GradeLinkedList:
    grades = LinkedList()

    def __init__(self, first):
        GradeLinkedList.grades.head = first
        GradeLinkedList.grades.tail = first

    @staticmethod
    def add_node(grade):
        grade.backward = GradeLinkedList.grades.tail
        GradeLinkedList.grades.tail.forward = grade
        GradeLinkedList.grades.tail = grade


def numbers(args):
    print(GradeLinkedList2Way.number_course(int(args[1])))


def numberc(args):
    print(GradeLinkedList2Way.number_student(int(args[1])))


def deleteg(args):
    GradeLinkedList2Way.delete(int(args[1]), int(args[2]))


def deletec(args):
    name = CourseLinkedList.get_nameByCode(int(args[1]))
    CourseLinkedList.delete_course(int(args[1]))
    if Trees[0].Name == "courses":
        Trees[0].delete_node(name)
    elif Trees[1].Name == "courses":
        Trees[1].delete_node(name)
    DynamicTable.delete(int(args[1]), 1)


def deletes(args):
    name = StudentLinkedList.get_nameByCode(int(args[1]))
    StudentLinkedList.delete_student(int(args[1]))
    if Trees[0].Name == "students":
        Trees[0].delete_node(name)
    elif Trees[1].Name == "students":
        Trees[1].delete_node(name)
    DynamicTable.delete(int(args[1]), 0)


def editg(args):
    if 0 <= float(args[3]) <= 20 and args[3][::-1].find('.') <= 1:
        GradeLinkedList2Way.edit(int(args[1]), int(args[2]), args[3])


def editc(args):
    if len(args[2]) <= 10:
        correction = True
        for letter in args[2]:
            if not (65 <= ord(letter) <= 90):
                correction = False
        if len(args) > 3:
            correction = False
        if correction:
            name = CourseLinkedList.get_nameByCode(int(args[1]))
            CourseLinkedList.edit_course(int(args[1]), args[2])
            if Trees[0].Name == "courses":
                node = Trees[0].searchTree(name).pointer
                Trees[0].delete_node(name)
                Trees[0].insert(args[2], node)
            elif Trees[1].Name == "courses":
                node = Trees[1].searchTree(name).pointer
                Trees[1].delete_node(name)
                Trees[1].insert(args[2], node)


def edits(args):
    if len(args[2]) <= 30:
        correction = True
        for letter in args[2]:
            if not ((65 <= ord(letter) <= 90) or (97 <= ord(letter) <= 122)):
                correction = False
        if len(args) > 3:
            correction = False
        if correction:
            name = StudentLinkedList.get_nameByCode(int(args[1]))
            StudentLinkedList.edit_student(int(args[1]), args[2])
            if Trees[0].Name == "students":
                node = Trees[0].searchTree(name).pointer
                Trees[0].delete_node(name)
                Trees[0].insert(args[2], node)
            elif Trees[1].Name == "students":
                node = Trees[1].searchTree(name).pointer
                Trees[1].delete_node(name)
                Trees[1].insert(args[2], node)


def addg(args):
    if (args[3][4] == '1' or args[3][4] == '2' or args[3][4] == '3') and args[3][0] != '0':
        if 0 <= float(args[4]) <= 20 and args[4][::-1].find('.') <= 1:
            if StudentLinkedList.check_existence(int(args[1])) and CourseLinkedList.check_existence(int(args[2])):
                grade = GradeNode(int(args[1]), int(args[2]), int(args[3]), float(args[4]))
                if GradeLinkedList.grades.head is not None:
                    GradeLinkedList.add_node(grade)
                else:
                    GradeLinkedList(grade)
                GradeLinkedList2Way.add_node(grade)


def addc(args):
    if len(args[2]) <= 10:
        correction = True
        for letter in args[2]:
            if not (65 <= ord(letter) <= 90):
                correction = False
        if len(args) > 3:
            correction = False
        if correction:
            if len(args[1]) == 5:
                course = CourseNode(int(args[1]), args[2])
                if not CourseLinkedList.check_duplicate(course):
                    if CourseLinkedList.courses.head is not None:
                        CourseLinkedList.add_node(course)
                        if Trees[0].Name == "courses":
                            Trees[0].insert(course.Name, course)
                        elif Trees[1].Name == "courses":
                            Trees[1].insert(course.Name, course)
                        node = HashNode(int(args[1]), course)
                        HashTables[0].insert(node, 1)
                    else:
                        CourseLinkedList(course)
                        Trees.append(RedBlackTree("courses"))
                        if Trees[0].Name == "courses":
                            Trees[0].insert(course.Name, course)
                        elif Trees[1].Name == "courses":
                            Trees[1].insert(course.Name, course)
                        HashTables.append(DynamicTable("courses"))
                        node = HashNode(int(args[1]), course)
                        if HashTables[0].Name == "courses":
                            HashTables[0].insert(node, 1)
                        elif HashTables[1].Name == "courses":
                            HashTables[1].insert(node, 1)


def adds(args):
    if len(args[2]) <= 30:
        correction = True
        for letter in args[2]:
            if not ((65 <= ord(letter) <= 90) or (97 <= ord(letter) <= 122)):
                correction = False
        if len(args) > 3:
            correction = False
        if correction:
            if len(args[1]) == 8 and args[1][0] != '0':
                student = StudentNode(int(args[1]), args[2])
                if not StudentLinkedList.check_duplicate(student):
                    if StudentLinkedList.students.head is not None:
                        StudentLinkedList.add_node(student)
                        if Trees[0].Name == "students":
                            Trees[0].insert(student.Name,  student)
                        elif Trees[1].Name == "students":
                            Trees[1].insert(student.Name,  student)
                        node = HashNode(int(args[1]), student)
                        HashTables[0].insert(node, 0)
                    else:
                        StudentLinkedList(student)
                        Trees.append(RedBlackTree("students"))
                        if Trees[0].Name == "students":
                            Trees[0].insert(student.Name,  student)
                        elif Trees[1].Name == "students":
                            Trees[1].insert(student.Name,  student)
                        HashTables.append(DynamicTable("students"))
                        node = HashNode(int(args[1]), student)
                        if HashTables[0].Name == "students":
                            HashTables[0].insert(node, 0)
                        elif HashTables[1].Name == "students":
                            HashTables[1].insert(node, 0)


def searchsn(args):
    if Trees[0].Name == "students":
        node = Trees[0].searchTree(args[1]).pointer
        print(str(node.Code) + " " + node.Name + " " + str(node.gr_num))
        node = node.right
        while node is not None:
            print(str(node.co_code) + " " + str(node.sem_code) + " " + str(node.grade))
            node = node.left_next
    if Trees[1].Name == "students":
        node = Trees[1].searchTree(args[1]).pointer
        print(str(node.Code) + " " + str(node.Name) + " " + str( node.gr_num))
        node = node.right
        while node is not None:
            print(str(node.co_code) + " " + str(node.sem_code) + " " + str(node.grade))
            node = node.left_next


def searchcn(args):
    if Trees[0].Name == "courses":
        node = Trees[0].searchTree(args[1]).pointer
        print(str(node.Code) + " " + str(node.Name) + " " + str(node.gr_num))
        node = node.left
        while node is not None:
            print(str(node.co_code) + " " + str(node.sem_code) + " " + str(node.grade))
            node = node.right_next
    if Trees[1].Name == "courses":
        node = Trees[1].searchTree(args[1]).pointer
        print(str(node.Code) + " " + str(node.Name) + " " + str(node.gr_num))
        node = node.left
        while node is not None:
            print(str(node.co_code) + " " + str(node.sem_code) + " " + str(node.grade))
            node = node.right_next


def DFS(graph, code, visited):
    if code not in visited:
        for component in graph:
            if component.head.Code == code:
                visited.append(code)
                node = component.head.next
                while node is not None:
                    DFS(graph, node.Code, visited)
                    node = node.next
            break
    return visited


def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


def isrelative(args):
    graph = CourseLinkedList.get_graph()
    visited = []
    visited = DFS(graph, int(args[1]), visited)
    if int(args[2]) in visited:
        print("yes")
    else:
        print("no")


def allrelative(args):
    graph = CourseLinkedList.get_graph()
    visited = []
    visited = DFS(graph, int(args[1]), visited)
    quickSort(visited, 0, len(visited)-1)
    for element in visited:
        print(element, end=" ")


def compare(args):
    graph = CourseLinkedList.get_graph()
    visited1 = []
    visited1 = DFS(graph, int(args[1]), visited1)
    visited2 = []
    visited2 = DFS(graph, int(args[2]), visited2)
    if int(args[1]) in visited2:
        print("<")
    elif int(args[2]) in visited1:
        print(">")
    else:
        print("?")


def searchsc(args):
    if HashTables[0].Name == "students":
        index = 0
    elif HashTables[1].Name == "students":
        index = 1

    print(DynamicTable.hashing(int(args[1]), index))
    if HashTables[0].Name == "students":
        node = HashTables[0].search(int(args[1]), 0).pointer
        print(str(node.Code)+" "+str(node.Name)+" "+str(node.gr_num))
        node = node.right
        while node is not None:
            print(str(node.Code)+" "+str(node.sem_code)+" "+str(node.grade))
            node = node.left_next
    else:
        node = HashTables[1].search(int(args[1]), 0).pointer
        print(str(node.Code )+ " " + str(node.Name) + " " + str(node.gr_num))
        node = node.right
        while node is not None:
            print(str(node.Code) + " "+str(node.sem_code) + " " + str(node.grade))
            node = node.left_next


def searchcc(args):

    if HashTables[0].Name == "courses":
        index = 0
    elif HashTables[1].Name == "courses":
        index = 1

    print(DynamicTable.hashing(int(args[1]), index))
    if HashTables[0].Name == "courses":
        node = HashTables[0].search(int(args[1]), 1).pointer
        print(str(node.Code)+" "+node.Name+" "+str(node.gr_num))
        node = node.left
        while node is not None:
            print(str(node.Code)+" "+str(node.sem_code)+" "+str(node.grade))
            node = node.right_next
    else:
        node = HashTables[1].search(int(args[1]), 1).pointer
        print(str(node.Code) + " " + str(node.Name) + " " + str(node.gr_num))
        node = node.left
        while node is not None:
            print(str(node.Code) + " "+str(node.sem_code) + " " + str(node.grade))
            node = node.right_next


def print_st(args):
    if Trees[0].Name == "students":
        Trees[0].print_tree()
    else:
        Trees[1].print_tree()


def print_co(args):
    if Trees[0].Name == "courses":
        Trees[0].print_tree()
    else:
        Trees[1].print_tree()


funcs = globals()
commands = ["adds", "addc", "addg", "edits", "editc", "editg", "deletes",
            "deletec", "deleteg", "numberc", "numbers", "searchsn", "searchcn", "isrelative", "allrelative", "compare",
            "searchsc", "searchcc", "print_st", "print_co"]
command = input().split()
DynamicTable.a = int(command[1])
DynamicTable.b = int(command[2])
DynamicTable.p = int(command[3])
for i in range(0, int(command[0])):
    command = input()
    command_args = command.split()
    for command in commands:
        if (command_args[0]).lower() == command:
            try:
                funcs[command](command_args)
            except Exception as e:
                print(e)