from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core .window import Window

class Mylayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def clear_entry(self):
        prior=self.ids.calc_input.text
        lt=list(prior)
        lt.pop()
        st=''
        for i in lt:
            st+=i
        self.ids.calc_input.text=st
        
    def clear(self):
        self.ids.calc_input.text='0'
        self.ids.calc_input.background_color= 1,1,1

    def button_press(self,button):
        prior = self.ids.calc_input.text
        if prior == '0':
            self.ids.calc_input.text=''
            self.ids.calc_input.text=f'{button}'        
        else:
            self.ids.calc_input.text=f'{prior}{button}'
        self.ids.calc_input.background_color= 1,1,1

    def add(self):
        prior=self.ids.calc_input.text
        self.ids.calc_input.text=f'{prior}+'
        self.ids.calc_input.background_color= 1,1,1

    def sub(self):
        prior=self.ids.calc_input.text
        self.ids.calc_input.text=f'{prior}-'
        self.ids.calc_input.background_color= 1,1,1

    def mul(self):
        prior=self.ids.calc_input.text
        self.ids.calc_input.text=f'{prior}*'
        self.ids.calc_input.background_color= 1,1,1

    def div(self):
        prior=self.ids.calc_input.text
        self.ids.calc_input.text=f'{prior}/'
        self.ids.calc_input.background_color= 1,1,1

    def mod(self):
        prior=self.ids.calc_input.text
        self.ids.calc_input.text=f'{prior}%'
        self.ids.calc_input.background_color= 1,1,1
        
    def equals(self):
        prior=self.ids.calc_input.text
        self.ids.calc_input.background_normal= ''
        self.ids.calc_input.background_color= 75/225, 240/225, 36/225
        #Addition
        if '+' in prior:
            num_list=prior.split('+')
            ans=0
            #loop in list
            for num in num_list:
                ans=ans+float(num)
            self.ids.calc_input.text=str(ans)
        #substraction
        if '-' in prior:
            num_list=prior.split('-')
            ans=0
            #loop in list
            for num in num_list:
                ans=ans-float(num)
            self.ids.calc_input.text=str(ans)
        #Multiplication
        if '*' in prior:
            num_list=prior.split('*')
            ans=1
            #loop in list
            for num in num_list:
                ans=ans*float(num)
            self.ids.calc_input.text=str(ans)
        #division
        if '/' in prior:
            num_list=prior.split('/')
            #loop in list
            ans=float(num_list[0])
            for i in range(len(num_list)):
                if i!=len(num_list)-1:
                    ans=ans/float(num_list[i+1])
            self.ids.calc_input.text=str(ans)
        #modulus
        if '%' in prior:
            num_list=prior.split('%')
            ans=float(num_list[0])
            for i in range(len(num_list)):
                if i!=len(num_list)-1:
                    ans=ans%float(num_list[i+1])
            self.ids.calc_input.text=str(ans)
    pass


class MyApp(App):
    def build(self):
        return Mylayout()
    
if __name__=="__main__":
    Window.size=(500,600)
    Builder.load_file("Calc.kv")
    MyApp().run()
    
