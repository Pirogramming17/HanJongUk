페이지 링크 : https://www.erdcloud.com/d/CMeixjNScpb2jvDox
![Faceboock ERD](https://user-images.githubusercontent.com/90972240/179505661-dfb8a34c-5605-439b-9833-9ecf16cea6c3.png)

1. 게시글과 사용자를 이어주는 relation을 만들었지만 굳이 필요없을 것 같아 제거
2. 페이스북은 전화번호와 이메일로 로그인이 가능하지만, 여기선 이메일로 로그인한다고 가정하고, 이메일을 기본키로 설정
3. 댓글의 하위댓글, 상위댓글은 대댓글도 댓글이기 때문에, 대댓글의 db를 만드는 건 비효율적이라 생각
