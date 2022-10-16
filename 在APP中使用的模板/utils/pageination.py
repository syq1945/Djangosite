from .. import models                                                                                                                                                    
from django.utils.safestring import mark_safe                                                                                                                            
'''                                                                                                                                                                      
自定义的分页组件;  名为: pageination.py   放在APP文件夹内的utils文件夹中                                                                                                                                                               
'''                                                                                                                                                                      
                                                                                                                                                                         
                                                                                                                                                                         
class Pageination(object):                                                                                                                                               
                                                                                                                                                                         
    def __init__(self,request,data_list,page_size=10,page_param="page",plus=5 ):                                                                                       
        # 0.根据传入的request, 获取并格式化传入的page值.                                                                                                                                
        page=request.GET.get(page_param,"1")  # 后面的1,是默认值.                                                                                                             
        if page.isdecimal():                                                                                                                                             
            page=int(page)                                                                                                                                               
        else:                                                                                                                                                            
            page=1                                                                                                                                                       
                                                                                                                                                                         
        # 1. 根据传的page 值, 计算起止位置                                                                                                                                          
        self.page=page                                                                                                                                                   
        self.page_size=page_size                                                                                                                                         
        self.start=(page-1)*page_size                                                                                                                                    
        self.end=page*page_size                                                                                                                                          
        self.data_list_pages=data_list[self.start:self.end]  #生成类的page化的Data_list                                                                                        
                                                                                                                                                                         
                                                                                                                                                                         
        # 2. 总页码                                                                                                                                                         
        total_count=data_list.count()                                                                                                                                    
        total_pages,div=divmod(total_count,page_size)                                                                                                                    
        if div>0:                                                                                                                                                        
            total_pages += 1                                                                                                                                             
        self.total_pages=total_pages  # 生成类的总页码                                                                                                                          
                                                                                                                                                                         
        self.plus=plus                                                                                                                                                   
                                                                                                                                                                         
    def html_page(self):                                                                                                                                                 
                                                                                                                                                                         
        # 3. 计算出, 显示出当前页的前5页,每次显示10页                                                                                                                                     
                                                                                                                                                                         
        # 起始页码                                                                                                                                                           
        if self.page<=5:                                                                                                                                                 
            start_page=1  # 选择页码<=5,起始页码=1                                                                                                                               
        else:                                                                                                                                                            
            start_page=self.page-(self.plus-1)  # >5的情况时,起始页码= page-4                                                                                                    
        end_page=start_page+9   #结束页码=起始页+9, 确保每次有10页显示                                                                                                                  
        if end_page>self.total_pages: #如果结束页码>总页码, 那么结束页码=总页码                                                                                                            
            end_page=self.total_pages                                                                                                                                    
                                                                                                                                                                         
        # 4. 页码                                                                                                                                                          
        page_str_list=[]                                                                                                                                                 
        #  首页                                                                                                                                                            
        first=mark_safe("<li><a href='?page=1'><span class='glyphicon glyphicon-fast-backward' aria-hidden='true'></span></a></li>" )                                  
        page_str_list.append(first)                                                                                                                                      
        #  上一页                                                                                                                                                           
        if self.page>1:                                                                                                                                                  
            prev=mark_safe("<li ><a href='?page=%s'><span class='glyphicon glyphicon-backward' aria-hidden='true'></span></a></li>" % (self.page-1))                   
        else:                                                                                                                                                            
            prev=mark_safe("<li><a href='?page=1'><span class='glyphicon glyphicon-backward' aria-hidden='true'></span></a></li>" )                                    
        # 页码                                                                                                                                                             
        page_str_list.append(prev)                                                                                                                                       
        for i in range(start_page,end_page+1):                                                                                                                           
            if i==self.page:                                                                                                                                             
                ele=mark_safe("<li class='active'><a href='?page=%s'>%s</a></li>" % (i,i))                                                                             
            else:                                                                                                                                                        
                ele=mark_safe("<li><a href='?page=%s'>%s</a></li>" % (i,i))                                                                                            
            page_str_list.append(ele)                                                                                                                                    
                                                                                                                                                                         
        # 下一页                                                                                                                                                            
        if self.page<self.total_pages:                                                                                                                                   
            nex=mark_safe("<li><a href='?page=%s'><span class='glyphicon glyphicon-forward' aria-hidden='true'></span></a></li>" % (self.page+1))                      
        else:                                                                                                                                                            
            nex=mark_safe("<li><a href='?page=%s'><span class='glyphicon glyphicon-forward' aria-hidden='true'></span></a></li>" ) % (self.total_pages)                
        page_str_list.append(nex)                                                                                                                                        
                                                                                                                                                                         
        #  尾页                                                                                                                                                            
        last=mark_safe("<li><a href='?page=%s'><span class='glyphicon glyphicon-fast-forward' aria-hidden='true'></span></a></li>" % (self.total_pages) )              
        page_str_list.append(last)                                                                                                                                       
                                                                                                                                                                         
        #搜索页                                                                                                                                                             
        search_page='''                                                                                                                                                  
            <div class="col-xs-2" style="display:inline">                                                                                                            
            <form method="get" action="">                                                                                                                            
                <div class="input-group">                                                                                                                              
                <input type="text" class="form-control" placeholder="页码" name="page" />                                                                             
                <span class="input-group-btn">                                                                                                                         
                    <button class="btn btn-default" type="submit">跳转</button>                                                                                        
                </span>                                                                                                                                                  
                </div>                                                                                                                                                   
            </form>                                                                                                                                                      
            <!-- /input-group -->                                                                                                                                        
            </div>                                                                                                                                                       
        '''                                                                                                                                                              
                                                                                                                                                                         
        page_str_list.append(search_page)                                                                                                                                
        page_str=mark_safe("".join(page_str_list))                                                                                                                     
        return page_str                                                                                                                                                  

  