"""
 post 앱을 생성
 class Post(models.Model):
     photo = models.어떤필드를 써야할까요
    생성날짜 기록

 class PostComment:
     photo = 자신의 photo와 MTO으로 연결
     생성일자 기록
"""


"""
member  앱을 생성 
1. templates/member/sighup.html
    input 2개를 구현 
    namedms 
    
2. view.py
    def signup(request):
    request.POST username, password 값 이용해 
    새유저를 생성 (create_user()메서드를 사용)
    그리고 만든 유저의 username과 password를 HttpResponese로 리던  



3. 사용하는 URL은 
    /member/signup/
    """