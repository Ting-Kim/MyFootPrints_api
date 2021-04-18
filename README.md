# MyFootPrints API (Django REST Framework)

### ✏ Description

- 내가 방문한 장소를 기록하는 서비스이다.
- 장소 정보는 네이버 지역 검색 API를 통해 받아올 수 있다. (최대 5개)
- 장소는 최근 visited_at 기준으로 정렬된다.
- 유저마다 팔로우 멤버들을 등록할 수 있다.

### Model Composition

```python
User {
	id: number;        // 숫자, 자동 생성
	name: string;     // 문자열, 필수값
	email: string;     // 문자열(이메일 형식), 필수값
	followers: many_to_many;    // User를 담은 배열, 팔로우 리스트, default=[]
}

History {
    id: number;        // 숫자, 자동 생성
    location_name: string;    // 문자열, 필수값 - 장소 이름
    score: float;        // 실수형, 필수값 - 장소에 대한 평점
    nutshell: string;  // 문자열, 필수값 - 장소에 대해 남길 한마디
    address: string;  // 문자열, 필수값 - 장소의 지번 주소
    road_address: string;  // 문자열, 필수값 - 장소의 도로명 주소
    visited_date: Date;      // 날짜형, 필수값 - 방문 날짜 (defalut=<today>)
    visited_time: string;    // 문자열, 필수값 - 방문 시간대 (아침, 점심, 저녁 중 택1) (default="dinner")
    created_at;         // 날짜형(시간포함), 필수값 - 생성된 시각 (자동 생성)
    updated_at;        // 날짜형(시간포함), 필수값 - 수정된 시각 (자동 생성)
    user;                   // User 객체, Foreign_Key - 등록한 사용자
}
```

### ⚙ Envirionments (python 3.8.0)

> pip install django==3.1.7

> pip install djangorestframework==3.12.4

> pip install django-dotenv==1.4.2

❗ And, you have to create `.env` file in root.

```
Project tree
------------
root
├── .env            ### here
├── README.md
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── history
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
└── user
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

then, please insert secret key (you can get at https://djskgen.herokuapp.com/)

```
SECRET_KEY="value"
DEBUG=True
```

<br>

### 📃 API Descriptions

<b>User</b>

- GET "users/" - User list read
- POST "users/" - User create
- GET "users/<int:user_id>" -User detail read
- PATCH "users/<int:user_id>" - User update
- DELETE "users/<int:user_id>" - User delete

<b>History</b>

- GET "histories/" - History list read
- POST "histories/" - History create
- PATCH "histories/<int:history_id>" - History update
- DELETE "histories/<int:history_id>" - History delete
- GET "histories/search/?query=<location_keyword>" - Location search(naver search api, get 5 results)
  <br>

### ▶ Execution

> pip install httpie

```python
python manage.py makemigrations

python manage.py migrate

# execute django web server
python manage.py runserver

# if you see error "No such table Todo",
## python manage.py makemigrations todo
## python manage.py migrate
## python manage.py runserver

""" in another cmd """
# please user httpie for test

```

<br>
