class Budget :
    def __init__(self):
        self.__salary = 0
        self.__Increase=0
        self.__cal_increase=0
        self.__personalsp=0
        self.__family=0 
        self.__saving=0

    def cal_increase(self,salary,increase):
        self.__salary = salary
        self.__Increase=increase
        self.__cal_increase= salary + increase
        return self.__cal_increase

    
    def Personal_Expense(self,apartment,clothes,public_transportation,car,travel):
          self.__apartment=apartment
          self.__travel=travel  
          self.__clothes=clothes
          self.__car=car
          self.__public_transportation=public_transportation
          self.__personalsp=apartment+travel+clothes+public_transportation+car
          return self.__personalsp
    
    def family_Expense(self,school_installments,university_fees,home_bills):
         self.__school_installments=school_installments   
         self.__university_fees=university_fees
         self.__home_bills=home_bills
         self.__family=home_bills+school_installments+university_fees
         return self.__family
 
    def remaining_salary_p(self) :
         self._remainder=self.cal_increase - self._personalsp
         return self.__remainder


    def  remaining_salary_f(self):
         self._remainderf= self.cal_increase - self._family
         return self.__remainderf

budget = Budget()