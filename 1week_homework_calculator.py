# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 16:16:17 2018

@author: MSI
"""

class calculator:
    def __init__(self):
        self.value = []
        self.user_input = []
        self.operator = ['+', '-', '*', '/']
        self.bracket = ['(', ')']
        self.post_list = []
        self.ans = ''

    def input(self):
        ipt = input()
        for i in ipt:
            
            if self.user_input == []:
                if i.isdigit():
                    self.user_input.append(int(i))
                elif i in self.bracket:
                    self.user_input.append(i)
            elif (i in self.operator) | (i in self.bracket):
                self.user_input.append(i)
            elif i == " ":
                pass
            else:
                try:
                    self.user_input[-1] = int(self.user_input[-1])*10 + int(i)
                except ValueError:
                    self.user_input.append(int(i))

        print(self.user_input)
        self.to_postfix()
        print(self.output())
        # print("결과 : " , self.output())

    def to_postfix(self):
        oplist = []
        pre = {"(":0, ")":0, "+" : 1, "-" : 1, "*" : 2, "/" : 2}
        for i in range(0,len(self.user_input)):
            if type(self.user_input[i]) == int :
                self.post_list.append(self.user_input[i])
            elif self.user_input[i] == "(":
                oplist.append(self.user_input[i])
            elif self.user_input[i] == ")":
                while (len(oplist) != 0):
                    op = oplist.pop()
                    if (op == "(") :
                        break
                    else :
                        self.post_list.append(op)
            elif self.user_input[i] in self.operator:
                while(len(oplist) != 0):
                    op = oplist[-1]
                    if ( pre[self.user_input[i]] <= pre[op] ):
                        self.post_list.append(op)
                        oplist.pop()
                    else:
                        break
                oplist.append(self.user_input[i])
        while(len(oplist) != 0):
            op = oplist.pop()
            self.post_list.append(op)

        print(self.post_list)
        return self.post_list

    def output(self):
        for i in range(0,len(self.post_list)):
            c = self.post_list[i]
            if type(c) == int :
                self.value.append(c)
            else :
                temp2 = self.value.pop()
                temp1 = self.value.pop()
                self.opr(temp1, temp2, c)

        return self.value.pop()


    def opr(self, num1, num2, operator):
        if operator == self.operator[0]:
            self.value.append(num1 + num2)
        elif operator == self.operator[1]:
            self.value.append(num1 - num2)
        elif operator == self.operator[2]:
            self.value.append(num1 * num2)
        elif operator == self.operator[3]:
            try:
                self.value.append(num1 / num2)
            except ZeroDivisionError:
                print("0으로는 나눌 수 없습니다")
                


cal = calculator()
cal.input()