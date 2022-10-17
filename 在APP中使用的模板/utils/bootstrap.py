from django import forms                                                                                      
'''                                                                                                           
自定义的分页组件;  名为: bootstrap.py   放在APP文件夹内的utils文件夹中                                                             
'''                                                                                                           
                                                                                                              
class BootStrapModelForm(forms.ModelForm):  # 为  forms.ModelForm类自定义增加了对应的class属性                                                       
                                                                                                              
   def __init__(self,*args, **kwargs):                                                                        
       super().__init__(*args, **kwargs)                                                                      
       #循环所有插件, 并增加相应的类                                                                                                                 
       for name, field in self.fields.items():                                                                
           if field.widget.attrs:  # 之前有属性, 曾变更对应的属性                                                          
               field.widget.attrs["class"]="form-control"                                                 
               field.widget.attrs["placeholder"]=field.label                                                
           field.widget.attrs={"class":"form-control","placeholder":field.label}  # 没有属性则增加             
