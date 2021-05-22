

class Binary_Search_Tree:
  class __BST_Node
    def __init__(self, value):
      self.value = value
      self.left_child = None
      self.right_child = None
      self.height = 0
    def setUp(self):
      self.__BST = Binary_Search_Tree()

    def set_height_node(self, value):
      self.height = value

    def set_value(self, value):
      self.value = value

    def get_value(self):
      return self.value

    def get_left_node(self):
      return self.left_child

    def get_right_node(self):
      return self.right_child

    def get_left_value(self):
      if self.left_child == None:
        return None
      else:
        return self.left_child.get_value()

    def get_right_value(self):
      if self.right_child == None:
        return None
      else:
        return self.right_child.get_value()

    def set_left_child(self, node):
      self.left_child = node

    def set_right_child(self, node):
      self.right_child = node

    def get_minimum_value(self):
      node = self
      def __get_minimum_recursion(node):
        if node.get_left_node() == None:
          return node.get_value()
        else:
          return __get_minimum_recursion(node.get_left_node())
      return __get_minimum_recursion(node)

    def get_height_tree(self):
      firstNode = self
      def __get_height_recursion(node):
        if node.get_left_node() == None and node.get_right_node() == None:
          return 1
        elif node.get_left_node() == None and node.get_right_node() != None:
          return (__get_height_recursion(node.get_right_node()) + 1)
        elif node.get_left_node() != None and node.get_right_node() == None:
          return (__get_height_recursion(node.get_left_node()) + 1)
        elif node.get_left_node() == None and node.get_right_node() != None:
          return (__get_height_recursion(node.get_right_node()) + 1)
        elif node.get_left_node() != None and node.get_right_node() != None:
          if __get_height_recursion(node.get_right_node()) >= __get_height_recursion(node.get_left_node()):
            return (__get_height_recursion(node.get_right_node()) + 1)
          elif __get_height_recursion(node.get_right_node()) < __get_height_recursion(node.get_left_node()):
            return (__get_height_recursion(node.get_left_node()) + 1)
      return __get_height_recursion(firstNode)

    def display(self):
      lines, _, _, _ = self._display_aux()
      for line in lines:
        print(line)

    def _display_aux(self):

      # No child exists.
      if self.right_child is None and self.left_child is None:
        line = '%s' % self.value
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

      # Only left child exists.
      if self.right_child is None:
        lines, n, p, x = self.left_child._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

      # Only right child exists.
      if self.left_child is None:
        lines, n, p, x = self.right_child._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

      # Two children exist.
      left, n, p, x = self.left_child._display_aux()
      right, m, q, y = self.right_child._display_aux()
      s = '%s' % self.value
      u = len(s)
      first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
      second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '

      if p < q:
        left += [n * ' '] * (q - p)
      elif q < p:
        right += [m * ' '] * (p - q)

      zipped_lines = zip(left, right)
      lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
      return lines, n + m + u, max(p, q) + 2, n + u // 2

  def __init__(self):
    self.__root = None

  def disp(self):
    self.__root.display()

  def insert_element(self, value):
    def __rec_insert(value, node):
      if node == None:
        new_node = self.__BST_Node(value)
        new_node.set_height_node(new_node.get_height_tree())
        return new_node
      elif value == node.get_value():
        raise ValueError
      elif value < node.get_value():
        node.set_left_child(__rec_insert(value, node.get_left_node()))
      elif value > node.get_value():
        node.set_right_child(__rec_insert(value, node.get_right_node()))
      node.set_height_node(node.get_height_tree())
      return node
    self.__root = __rec_insert(value, self.__root)
    self.__height = self.__root.get_height_tree()


  def remove_element(self, value):
    def __rec_remove(value, node):
      if node == None:
        raise ValueError
      elif value == node.get_value():
        if node.get_left_node() == None and node.get_right_node() == None:
          return None
        elif node.get_left_node() == None and node.get_right_node() != None:
          node.get_right_node().set_height_node(node.get_right_node().get_height_tree())
          return node.get_right_node()
        elif node.get_left_node() != None and node.get_right_node() == None:
          node.get_left_node().set_height_node(node.get_left_node().get_height_tree())
          return node.get_left_node()
        elif node.get_left_node() != None and node.get_right_node() != None:
          replace_value = node.get_right_node().get_minimum_value()
          #node.set_val(node.get_right_node().get_min())
          node = __rec_remove(node.get_right_node().get_minimum_value(), node)
          node.set_value(replace_value)
      elif value < node.get_value():
        node.set_left_child(__rec_remove(value, node.get_left_node()))
      elif value > node.get_value():
        node.set_right_child(__rec_remove(value, node.get_right_node()))
      node.set_height_node(node.get_height_tree())
      return node
    self.__root = __rec_remove(value, self.__root)
    if self.__root == None:
      self.__height = 0
    if self.__root != None:
      self.__height = self.__root.get_height_tree()

  def in_order(self):
    def __rec_in_order(node, tree_list):
      if node == None:
        pass
      elif node.get_left_node() == None:
        pass
      else:
        __rec_in_order(node.get_left_node(), tree_list)
      if node != None:
        tree_list.append(node.get_value())
      if node == None:
        pass
      elif node.get_right_node() == None:
        return
      else:
       __rec_in_order(node.get_right_node(), tree_list)
       return
    tree_list = []
    __rec_in_order(self.__root, tree_list)

    #CONVERT LIST TO CORRECT STRING
    ret_list = "[ "
    if len(tree_list) == 0:
        ret_list += "]"
    else:
        cur_ind = 0
        ret_list += str(tree_list[cur_ind])
        while cur_ind != (len(tree_list)-1):
            cur_ind += 1
            ret_list += (", " + str(tree_list[cur_ind]))
        ret_list += " ]"
    return ret_list


  def pre_order(self):
    def __rec_pre_order(node, tree_list):
      if node != None:
        tree_list.append(node.get_value())
      if node == None:
        pass
      elif node.get_left_node() == None:
        pass
      else:
        __rec_pre_order(node.get_left_node(), tree_list)
      if node == None:
        pass
      elif node.get_right_node() == None:
        return
      else:
       __rec_pre_order(node.get_right_node(), tree_list)
       return
    tree_list = []
    __rec_pre_order(self.__root, tree_list)

    #CONVERT LIST TO CORRECT STRING
    ret_list = "[ "
    if len(tree_list) == 0:
        ret_list += "]"
    else:
        cur_ind = 0
        ret_list += str(tree_list[cur_ind])
        while cur_ind != (len(tree_list)-1):
            cur_ind += 1
            ret_list += (", " + str(tree_list[cur_ind]))
        ret_list += " ]"
    return ret_list


  def post_order(self):
    def __rec_post_order(node, tree_list):
      if node == None:
        pass
      elif node.get_left_node() == None:
        pass
      else:
        __rec_post_order(node.get_left_node(), tree_list)
      if node == None:
        pass
      elif node.get_right_node() == None:
        pass
      else:
       __rec_post_order(node.get_right_node(), tree_list)
      if node != None:
        tree_list.append(node.get_value())
      return

    tree_list = []
    __rec_post_order(self.__root, tree_list)

    #CONVERT LIST TO CORRECT STRING
    ret_list = "[ "
    if len(tree_list) == 0:
        ret_list += "]"
    else:
        cur_ind = 0
        ret_list += str(tree_list[cur_ind])
        while cur_ind != (len(tree_list)-1):
            cur_ind += 1
            ret_list += (", " + str(tree_list[cur_ind]))
        ret_list += " ]"
    return ret_list



  def get_height(self):
    if self.__root == None:
      return 0
    else:
      return self.__root.get_height_tree()


  def __str__(self):
    return self.in_order()


b=Binary_Search_Tree()


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QMessageBox


class EmittingStream(QtCore.QObject):

    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))
class Ui_Dialog(object):
    b = Binary_Search_Tree()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        sys.stdout = EmittingStream(textWritten=self.output_terminal_written)

        Dialog.resize(689, 523)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(190, 10, 321, 71))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(200, 30, 71, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pushed)

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(190, 90, 321, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 30, 71, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.delpushed)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 30, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(100, 170, 521, 251))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Binary Tree"))
        self.groupBox.setTitle(_translate("Dialog", "Insert Value"))
        self.pushButton.setText(_translate("Dialog", "Add"))
        self.groupBox_2.setTitle(_translate("Dialog", "Delete Value"))
        self.pushButton_2.setText(_translate("Dialog", "Delete"))

    def pushed(self):
        if (b.get_height() <6):
            a=int(self.lineEdit.text())
            if a<=999:

                try:
                    b.insert_element(a)
                    self.textEdit.clear()
                    b.disp()
                except ValueError:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("You have that element in the tree")
                    msg.setWindowTitle("Error")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("the biggest possible number that one can insert should be 999")
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("You can't add more elements the max height of the tree is 6")
            msg.setWindowTitle("Error")

            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()

    def delpushed(self):
      
        c=int(self.lineEdit_2.text())
        try:
            b.remove_element(c)
            self.textEdit.clear()
            b.disp()
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("You have not that element in the tree")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()


    def output_terminal_written(self, text):
        text='\t'+text
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
