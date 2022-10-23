from django.utils.deprecation import MiddlewareMixin                                          
from django.shortcuts import redirect                                                         
                                                                                              
'''                                                                                           
在app中新建 middleware 文件夹, 并新建auth.py 文件 , 还需要在Settings中加入这个Middleware                           
  'APP_MobileNum.middleware.auth.AuthMiddleware',  
'''                                                                                           
                                                                                              
                                                                                              
class AuthMiddleware(MiddlewareMixin):                                                        
    '''中间件1 '''                                                                               
    def process_request(self,request):                                                        
        # 0. 排除那些不需要登录就能访问的页面                                                                 
        #request.path_info  # 获取当前用户请求的URL  比如/login/                                         
        if request.path_info in ['/login/','/image/code/']:  #这里的链接以/开头以/结尾, 我已经被这里折磨疯了                                                     
            return                                                                            
                                                                                              
        # 1. 检查用户是否登录? 获取cookie中的随机字符串, 并在session中检查是否存在                                      
        info=request.session.get('info')  # 有则存在字典, 没有则为none                                  
        if info:                                                                              
            return   # 登录过,则继续                                                                
        # 2. 没有登录,返回登录界面                                                                      
        return redirect('/login/')                                                            
                                                                                              
                                                                                              
                                                                                              
    # def process_response(self,request,response):                                            
    #     print('M1.走了')                                                                      
    #     return response   #有返回值                                                             
                                                                                              
                                                                                              
# class M2(MiddlewareMixin):                                                                  
#     '''中间件2 '''                                                                             
#     def process_request(self,request):                                                      
#         print('M2.进来了')                                                                     
                                                                                              
#     def process_response(self,request,response):                                            
#         print('M2.走了')                                                                      
#         return response                                                                     
