from .. import models                                                                                                                                   
from django import forms                                                                                                                                
from django.core.validators import RegexValidator                                                                                                       
from django.core.exceptions import ValidationError                                                                                                      
from .bootstrap import BootStrapModelForm                                                                                                               
                                                                                                                                                        
'''                                                                                                                                                     
自定义的Model中类对象的ModeForm生成组件;  名为: bootstrap.py   放在APP文件夹内的utils文件夹中                                                                                     
'''                                                                                                                                                     
                                                                                                                                                        
class MobileNumADDModelForm(BootStrapModelForm):                                                                                                        
   mobile=forms.CharField(                                                                                                                              
       min_length=11,max_length=11,label="手机号",                                                                                                       
       validators=[RegexValidator(r'^[0-9]+$', '请输入数字'), RegexValidator(r'^1[3-9]\d{9}$', '数字必须以1开头,第二位位3-9,并且为11位数字')]                                 
       )   # 校验                                                                                                                                             
                                                                                                                                                        
   class Meta:                                                                                                                                          
       model=models.MobileNum                                                                                                                           
       exclude=['del_flag']  #排查某项,其他都显示                                                                                                                
    #    fields="__all__"   #所有的项                                                                                                                     
    #    fields=["mobile","price","level","status"]  #自定义的项                                                                                     
                                                                                                                                                        
   def clean_mobile(self):   # 以后可以验证数据是否已经存在 为 form.is_valid():提供支持                                                                                    
        txt_mobile=self.cleaned_data["mobile"]                                                                                                        
        exists=models.MobileNum.objects.filter(mobile=txt_mobile).exists()                                                                              
        if exists:                                                                                                                                      
            raise ValidationError("手机号已存在")                                                                                                           
        return txt_mobile                                                                                                                               
                                                                                                                                                        
                                                                                                                                                        
class MobileNumEditModelForm(BootStrapModelForm):                                                                                                       
#    mobile=forms.CharField(disabled=True,label="手机号")   # 显示但是不能编辑                                                                                                         
                                                                                                                                                        
   class Meta:                                                                                                                                          
       model=models.MobileNum                                                                                                                           
       exclude=['del_flag']  #排查某项,其他都显示                                                                                                                
    #    fields="__all__"   #所有的项                                                                                                                     
    #    fields=["mobile","price","level","status"]  #自定义的项                                                                                     
                                                                                                                                                        
   def clean_mobile(self):   # 在修改界面验证修改后的数据是否已经存在 为 form.is_valid():提供支持                                                                               
       #当前编辑行的ID(.pk)                                                                                                                                   
       nid=self.instance.pk                                                                                                                             
       txt_mobile=self.cleaned_data["mobile"]                                                                                                         
       # 把自己排除后,查修改后的内容是否存在                                                                                                                             
       exists=models.MobileNum.objects.exclude(id=nid).filter(mobile=txt_mobile).exists()                                                               
       if exists:                                                                                                                                       
           raise ValidationError("手机号已存在")                                                                                                            
       return txt_mobile                                                                                                                                
