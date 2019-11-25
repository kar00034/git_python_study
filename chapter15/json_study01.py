import json

python_dict = {
    "이름": "홍길동",
    "나이": 25,
    "거주지": "서울",
    "신체정보": {
        "키": 175.4,
        "몸무게": 71.2
    },
    "취미": [
        "등산",
        "자전거타기",
        "독서"
    ]
}

json_data = json.dumps(python_dict)

print(type(python_dict))
print(type(json_data), json_data)
print(python_dict)

json_data = json.dumps(python_dict, indent=4, sort_keys=True, ensure_ascii=False)
print(type(json_data), json_data)

python_dict2 = json.loads(json_data)
print(type(python_dict2), python_dict2)

student = [
    {
        'no': 1,
        'name': "김승영",
        'score': {"국어": 90, "영어": 90, "수학": 90}
    },
    {
        'no': 2,
        'name': "지재삼",
        'score': {"국어": 80, "영어": 79, "수학": 69}
    }
]
json_student = json.dumps(student)
print(type(student), student)
with open('json_student', 'w', encoding='utf-8') as f:
    json.dump(json_student, f)

with open('json_student', 'r', encoding='utf-8')as f:
    x = json.load(f)
    print(type(x), x)

students = json.loads(x)
type(students)
for std in students:
    print("{} {} {} {} {}"
          .format(type(std['no']),
                  type(std['name']),
                  type(std['score']['국어']),
                  type(std['score']['영어']),
                  type(std['score']['수학'])))
    print(std['no'],std['name'],end = '\t')
    total = sum([x for x in std['score'].values()])
    [print(score, end = '\t') for score in std['score'].values()]
    print(total, total / float(3))

