from .. import models                                                                                                                                                   
from django import forms                                                                                                                                                
from django.core.validators import RegexValidator                                                                                                                       
from django.core.exceptions import ValidationError                                                                                                                      
from .bootstrap import BootStrapModelForm                                                                                                                               
from .encrypt import md5                                                                                                                                                
                                                                                                                                                                        
'''                                                                                                                                                                     
自定义的Model中类对象的ModeForm生成组件;  名为: form.py   放在APP文件夹内的utils文件夹中                                                                                                          
'''                                                                                                                                                                     
                                                                                                                                                                        
# class MobileNumADDModelForm(BootStrapModelForm):                                                                                                                      
#    mobile=forms.CharField(                                                                                                                                            
#        min_length=11,max_length=11,label='手机号',                                                                                                                       
#        validators=[RegexValidator(r'^[0-9]+$', '请输入数字'), RegexValidator(r'^1[3-9]\d{9}$', '数字必须以1开头,第二位位3-9,并且为11位数字')]                                               
#        )   # 校验                                                                                                                                                           
                                                                                                                                                                        
#    class Meta:                                                                                                                                                        
#        model=models.MobileNum                                                                                                                                         
#        exclude=['del_flag']  #排查某项,其他都显示                                                                                                                              
#     #    widgets={'password':forms.PasswordInput(render_value=True)}  # 给数据库有的字段, 为特定的字段password 设置了passwordinput的样式的input标签                                          
#     #    fields='__all__'   #所有的项                                                                                                                                     
#     #    fields=['mobile','price','level','status']  #自定义的项                                                                                                           
                                                                                                                                                                        
#    def clean_mobile(self):   # 以后可以验证数据是否已经存在 为 form.is_valid():提供支持                                                                                                  
#         txt_check=self.cleaned_data['mobile']                                                                                                                         
#         exists=models.MobileNum.objects.filter(mobile=txt_check).exists()                                                                                             
#         if exists:                                                                                                                                                    
#             raise ValidationError('手机号已存在')                                                                                                                           
#         return txt_mobile                                                                                                                                             
                                                                                                                                                                        
                                                                                                                                                                        
# class MobileNumEditModelForm(BootStrapModelForm):                                                                                                                     
# #    mobile=forms.CharField(disabled=True,label='手机号')   # 显示但是不能编辑                                                                                                                         
                                                                                                                                                                        
#    class Meta:                                                                                                                                                        
#        model=models.MobileNum                                                                                                                                         
#        exclude=['del_flag']  #排查某项,其他都显示                                                                                                                              
#     #    widgets={'password':forms.PasswordInput(render_value=True)}  # 给数据库有的字段, 为特定的字段password 设置了passwordinput的样式的input标签                                          
#     #    fields='__all__'   #所有的项                                                                                                                                     
#     #    fields=['mobile','price','level','status']  #自定义的项                                                                                                           
                                                                                                                                                                        
#    def clean_mobile(self):   # 在修改界面验证修改后的数据是否已经存在 为 form.is_valid():提供支持                                                                                             
#        #当前编辑行的ID(.pk)                                                                                                                                                 
#        nid=self.instance.pk                                                                                                                                           
#        txt_check=self.cleaned_data['mobile']                                                                                                                          
#        # 把自己排除后,查修改后的内容是否存在                                                                                                                                           
#        exists=models.MobileNum.objects.exclude(id=nid).filter(mobile=txt_check).exists()                                                                              
#        if exists:                                                                                                                                                     
#            raise ValidationError('手机号已存在')                                                                                                                            
#        return txt_mobile                                                                                                                                              
                                                                                                                                                                        
                                                                                                                                                                        
# class UserInfoADDModelForm(BootStrapModelForm):                                                                                                                       
                                                                                                                                                                        
#     class Meta:                                                                                                                                                       
#        model=models.UserInfo                                                                                                                                          
#        exclude=['del_flag']  #排查某项,其他都显示                                                                                                                              
#        widgets={'password':forms.PasswordInput(render_value=True)}  # 给数据库有的字段, 为特定的字段password 设置了passwordinput的样式的input标签                                            
#     #    fields='__all__'   #所有的项                                                                                                                                     
#     #    fields=['mobile','price','level','status']  #自定义的项                                                                                                           
                                                                                                                                                                        
#     def clean_username(self):   # 以后可以验证数据是否已经存在 为 form.is_valid():提供支持                                                                                               
#         txt_check=self.cleaned_data['username']                                                                                                                       
#         exists=models.UserInfo.objects.filter(username=txt_check).exists()                                                                                            
#         if exists:                                                                                                                                                    
#             raise ValidationError('用户名已存在')                                                                                                                           
#         return txt_check                                                                                                                                              
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# class UserInfoEditModelForm(BootStrapModelForm):                                                                                                                      
# #    mobile=forms.CharField(disabled=True,label='手机号')   # 显示但是不能编辑                                                                                                                         
                                                                                                                                                                        
#    class Meta:                                                                                                                                                        
#        model=models.UserInfo                                                                                                                                          
#        exclude=['del_flag']  #排查某项,其他都显示                                                                                                                              
#        widgets={'password':forms.PasswordInput(render_value=True)}  # 给数据库有的字段, 为特定的字段password 设置了passwordinput的样式的input标签                                            
#     #    fields='__all__'   #所有的项                                                                                                                                     
#     #    fields=['mobile','price','level','status']  #自定义的项                                                                                                           
                                                                                                                                                                        
#    def clean_username(self):   # 在修改界面验证修改后的数据是否已经存在 为 form.is_valid():提供支持                                                                                           
#        #当前编辑行的ID(.pk)                                                                                                                                                 
#        nid=self.instance.pk                                                                                                                                           
#        txt_check=self.cleaned_data['username']                                                                                                                        
#        # 把自己排除后,查修改后的内容是否存在                                                                                                                                           
#        exists=models.UserInfo.objects.exclude(id=nid).filter(username=txt_check).exists()                                                                             
#        if exists:                                                                                                                                                     
#            raise ValidationError('用户名已存在')                                                                                                                            
#        return txt_check                                                                                                                                               
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# class DepartmentADDModelForm(BootStrapModelForm):                                                                                                                     
#     class Meta:                                                                                                                                                       
#        model=models.Department                                                                                                                                        
#        exclude=['del_flag']  #排查某项,其他都显示                                                                                                                              
#     #    widgets={'password':forms.PasswordInput(render_value=True)}  # 给数据库有的字段, 为特定的字段password 设置了passwordinput的样式的input标签                                          
#     #    fields='__all__'   #所有的项                                                                                                                                     
#     #    fields=['mobile','price','level','status']  #自定义的项                                                                                                           
                                                                                                                                                                        
#     def clean_deparment(self):   # 以后可以验证数据是否已经存在 为 form.is_valid():提供支持                                                                                              
#         txt_check=self.cleaned_data['deparment']                                                                                                                      
#         exists=models.Department.objects.filter(deparment=txt_check).exists()                                                                                         
#         if exists:                                                                                                                                                    
#             raise ValidationError('部门已存在')                                                                                                                            
#         return txt_check                                                                                                                                              
                                                                                                                                                                        
                                                                                                                                                                        
# class DepartmentEditModelForm(BootStrapModelForm):                                                                                                                    
# #    mobile=forms.CharField(disabled=True,label='手机号')   # 显示但是不能编辑                                                                                                                         
                                                                                                                                                                        
#    class Meta:                                                                                                                                                        
#        model=models.Department                                                                                                                                        
#        exclude=['del_flag']  #排查某项,其他都显示                                                                                                                              
#     #    widgets={'password':forms.PasswordInput(render_value=True)}  # 给数据库有的字段, 为特定的字段password 设置了passwordinput的样式的input标签                                          
#     #    fields='__all__'   #所有的项                                                                                                                                     
#     #    fields=['mobile','price','level','status']  #自定义的项                                                                                                           
                                                                                                                                                                        
#    def clean_deparment(self):   # 在修改界面验证修改后的数据是否已经存在 为 form.is_valid():提供支持                                                                                          
#        #当前编辑行的ID(.pk)                                                                                                                                                 
#        nid=self.instance.pk                                                                                                                                           
#        txt_check=self.cleaned_data['deparment']                                                                                                                       
#        # 把自己排除后,查修改后的内容是否存在                                                                                                                                           
#        exists=models.Department.objects.exclude(id=nid).filter(deparment=txt_check).exists()                                                                          
#        if exists:                                                                                                                                                     
#            raise ValidationError('部门已存在')                                                                                                                             
#        return txt_check                                                                                                                                               
                                                                                                                                                                        
###----------------管理员部分--密码加密以及含确认密码的设置--------------------------------                                                                                                
                                                                                                                                                                        
class AdminADDModelForm(BootStrapModelForm):                                                                                                                            
    confirm_password=forms.CharField(label='确认密码',widget=forms.PasswordInput(render_value=True))   #手动增加了确认密码字段, 并给了passwordinput的样式的input标签                                                                            
    class Meta:                                                                                                                                                         
       model=models.Admin                                                                                                                                               
       fields='__all__'  #排查某项,其他都显示                                                                                                                                    
       #    fields=['mobile','price','level','status']  #自定义的项                                                                                                          
       widgets={'password':forms.PasswordInput(render_value=True)}  # 给数据库有的字段, 为特定的字段password 设置了passwordinput的样式的input标签                                              
                                                                                                                                                                        
    def clean_username(self):   #钩子方法  # 以后可以验证数据是否已经存在 为 form.is_valid():提供支持                                                                                          
        txt_check=self.cleaned_data['username']                                                                                                                         
        exists=models.Admin.objects.filter(username=txt_check).exists()                                                                                                 
        if exists:                                                                                                                                                      
            raise ValidationError('username已存在')                                                                                                                        
        return txt_check   # 返回什么, 就向数据库中保存什么                                                                                                                           
                                                                                                                                                                        
    def clean_password(self):  #钩子方法                                                                                                                                    
        pwd=self.cleaned_data.get('password')                                                                                                                           
        return md5(pwd)     # 返回什么, 就向数据库中保存什么                                                                                                                          
                                                                                                                                                                        
    def clean_confirm_password(self):  #钩子方法                                                                                                                            
        pwd=self.cleaned_data.get('password')                                                                                                                           
        confirm=md5(self.cleaned_data.get('confirm_password'))                                                                                                          
        if pwd !=confirm:                                                                                                                                               
            raise ValidationError('两次输入的密码不一致,请重新输入')                                                                                                                   
        return confirm     # 返回什么, 就向数据库中保存什么                                                                                                                           
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
class AdminEditModelForm(BootStrapModelForm):                                                                                                                           
#    username=forms.CharField(disabled=True,label='手机号')   # 显示但是不能编辑                                                                                                                         
#    confirm_password=forms.CharField(label='确认密码',widget=forms.PasswordInput(render_value=True))    #手动增加了确认密码字段, 并给了passwordinput的样式的input标签                                                                          
   class Meta:                                                                                                                                                          
       model=models.Admin                                                                                                                                               
       fields=['username'] #排查某项,其他都显示                                                                                                                                  
    #    widgets={'password':forms.PasswordInput(render_value=True)}  # 给数据库有的字段, 为特定的字段password 设置了passwordinput的样式的input标签                                            
                                                                                                                                                                        
   def clean_username(self):   # 在修改界面验证修改后的数据是否已经存在 为 form.is_valid():提供支持                                                                                             
       #当前编辑行的ID(.pk)                                                                                                                                                   
       nid=self.instance.pk                                                                                                                                             
       txt_check=self.cleaned_data['username']                                                                                                                          
       # 把自己排除后,查修改后的内容是否存在                                                                                                                                             
       exists=models.Admin.objects.exclude(id=nid).filter(username=txt_check).exists()                                                                                  
       if exists:                                                                                                                                                       
           raise ValidationError('username已存在')                                                                                                                         
       return txt_check    # 返回什么, 就向数据库中保存什么                                                                                                                           
                                                                                                                                                                        
                                                                                                                                                                        
class AdminResetModelForm(BootStrapModelForm):                                                                                                                          
#    username=forms.CharField(disabled=True,label='手机号')   # 显示但是不能编辑                                                                                                                         
   confirm_password=forms.CharField(label='确认密码',widget=forms.PasswordInput(render_value=True))    #手动增加了确认密码字段, 并给了passwordinput的样式的input标签                                                                            
   class Meta:                                                                                                                                                          
       model=models.Admin                                                                                                                                               
       fields=['password','confirm_password']  #排查某项,其他都显示                                                                                                              
       #    fields=['mobile','price','level','status']  #自定义的项                                                                                                          
       widgets={'password':forms.PasswordInput(render_value=True)}  # 给数据库有的字段, 为特定的字段password 设置了passwordinput的样式的input标签                                              
                                                                                                                                                                        
   def clean_password(self):  #钩子方法                                                                                                                                     
        pwd=self.cleaned_data.get('password')                                                                                                                           
        md5_pwd= md5(pwd)                                                                                                                                               
                                                                                                                                                                        
        exists=models.Admin.objects.filter(id=self.instance.pk,password=md5_pwd).exists()                                                                               
        if exists:                                                                                                                                                      
            raise ValidationError('不能与以前的密码相同')                                                                                                                         
        return md5_pwd     # 返回什么, 就向数据库中保存什么                                                                                                                           
                                                                                                                                                                        
   def clean_confirm_password(self):  #钩子方法                                                                                                                             
        pwd=self.cleaned_data.get('password')                                                                                                                           
        confirm=md5(self.cleaned_data.get('confirm_password'))                                                                                                          
        if pwd !=confirm:                                                                                                                                               
            raise ValidationError('两次输入的密码不一致,请重新输入')                                                                                                                   
        return confirm     # 返回什么, 就向数据库中保存什么                                                                                                                           
                                                                                                                                                                        
                                                                                                                                                                        
class AdminLoginModelForm(BootStrapModelForm):                                                                                                                          
    #增加一个文本框, 来让用户输入验证码                                                                                                                                                                                 
    code=forms.CharField(label='验证码',widget=forms.TextInput,required=True)   #手动增加了确认密码字段, 并给了passwordinput的样式的input标签                                                                                                
                                                                                                                                                                        
    class Meta:                                                                                                                                                         
       model=models.Admin                                                                                                                                               
       fields='__all__'   #所有的项                                                                                                                                         
       widgets={'password':forms.PasswordInput(render_value=True)}  # 给数据库有的字段, 为特定的字段password 设置了passwordinput的样式的input标签                                              
    #    fields=['mobile','price','level','status']  #自定义的项                                                                                                             
                                                                                                                                                                        
    def clean_password(self):  #钩子方法                                                                                                                                    
        pwd=self.cleaned_data.get('password')                                                                                                                           
        return  md5(pwd)                                                                                                                                                
                                                                                                                                                                        
                                                                                                                                                                        
# class TaskADDModelForm(BootStrapModelForm):                                                                                                                           
                                                                                                                                                                        
#     class Meta:                                                                                                                                                       
#        model=models.Task                                                                                                                                              
#        fields='__all__'  #排查某项,其他都显示                                                                                                                                  
                                                                                                                                                                        
                                                                                                                                                                        
class WorkOrderADDModelForm(BootStrapModelForm):                                                                                                                        
                                                                                                                                                                        
    class Meta:                                                                                                                                                         
       model=models.WorkOrder                                                                                                                                           
    #    exclude=['name','other']  #例外多个字段                                                                                                                              
    #    fields='__all__'  #排查某项,其他都显示                                                                                                                                  
       exclude=['name']                                                                                                                                                 
                                                                                                                                                                        
class WorkOrderEditModelForm(BootStrapModelForm):                                                                                                                       
                                                                                                                                                                        
    class Meta:                                                                                                                                                         
       model=models.WorkOrder                                                                                                                                           
    #    fields='__all__'  #排查某项,其他都显示                                                                                                                                  
       exclude=['name']                                                                                                                                                 
              
