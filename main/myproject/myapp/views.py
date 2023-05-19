from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def keyboard(request):
    return JsonResponse({
        'type': 'text'
    })
    
@csrf_exempt
def message(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    
    # 뉴스 스크래핑 txt 파일 읽어오기
    Suncheon_path = '/home/ubuntu/main/myproject/myapp/Suncheon.txt'
    Suncheon_fp = open(Suncheon_path, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in Suncheon_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    Suncheon_list = list(tmp_str.split('\n'))
    Suncheon_fp.close()
    
    if return_str == '전라남도 순천' or return_str == '전라도 순천' or return_str == '전남 순천' or return_str == '순천' or return_str == '전라남도순천' or return_str == '전라도순천' or return_str == '전남순천':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [
                  {
                    "carousel": {
                    "type": "listCard",
                    "items": [{
                        "header": {
                            "title": "순천 인기 여행지 추천"
                        },
                        "items": [
                            {
                                "title": Suncheon_list[0],
                                #"description": "",
                                "imageUrl": Suncheon_list[30],
                                "link": {
                                    "web": Suncheon_list[1]
                                }
                            },
                            {
                                "title": Suncheon_list[2],
                                #"description": "",
                                "imageUrl": Suncheon_list[31],
                                "link": {
                                    "web": Suncheon_list[3]
                                }
                            },
                            {
                                "title": Suncheon_list[4],
                                #"description": "",
                                "imageUrl": Suncheon_list[32],
                                "link": {
                                    "web": Suncheon_list[5]
                                }
                            },
                            {
                                "title": Suncheon_list[6],
                                #"description": "",
                                "imageUrl": Suncheon_list[33],
                                "link": {
                                    "web": Suncheon_list[7]
                                }
                            },
                            {
                                "title": Suncheon_list[8],
                                #"description": "",
                                "imageUrl": Suncheon_list[34],
                                "link": {
                                    "web": Suncheon_list[9]
                                }
                            },
                        ],
                        "buttons": [
                            {
                                "label": "홈페이지",
                                "action": "webLink",
                                "webLinkUrl": "https://trip.place.naver.com/list?query=%EC%88%9C%EC%B2%9C%20%EA%B0%80%EB%B3%BC%EB%A7%8C%ED%95%9C%EA%B3%B3&level=top&zoomLevel=10.000&theme=all"
                            }
                        ]
                    },
                    {
                        "header": {
                            "title": "순천 자연명소 추천"
                        },
                        "items": [
                            {
                                "title": Suncheon_list[10],
                                #"description": "",
                                "imageUrl": Suncheon_list[35],
                                "link": {
                                    "web": Suncheon_list[11]
                                }
                            },
                            {
                                "title": Suncheon_list[12],
                                #"description": "",
                                "imageUrl": Suncheon_list[36],
                                "link": {
                                    "web": Suncheon_list[13]
                                }
                            },
                            {
                                "title": Suncheon_list[14],
                                #"description": "",
                                "imageUrl": Suncheon_list[37],
                                "link": {
                                    "web": Suncheon_list[15]
                                }
                            },
                            {
                                "title": Suncheon_list[16],
                                #"description": "",
                                "imageUrl": Suncheon_list[38],
                                "link": {
                                    "web": Suncheon_list[17]
                                }
                            },
                            {
                                "title": Suncheon_list[18],
                                #"description": "",
                                "imageUrl": Suncheon_list[39],
                                "link": {
                                    "web": Suncheon_list[19]
                                }
                            },
                        ],
                        "buttons": [
                            {
                                "label": "홈페이지",
                                "action": "webLink",
                                "webLinkUrl": "https://trip.place.naver.com/list?query=%EC%88%9C%EC%B2%9C%20%EA%B0%80%EB%B3%BC%EB%A7%8C%ED%95%9C%EA%B3%B3&level=top&zoomLevel=10.000&theme=all"
                            }
                        ]  
                    },  
                    {
                        "header": {
                            "title": "순천 피크닉 추천"
                        },
                        "items": [
                            {
                                "title": Suncheon_list[20],
                                #"description": "",
                                "imageUrl": Suncheon_list[40],
                                "link": {
                                    "web": Suncheon_list[21]
                                }
                            },
                            {
                                "title": Suncheon_list[22],
                                #"description": "",
                                "imageUrl": Suncheon_list[41],
                                "link": {
                                    "web": Suncheon_list[23]
                                }
                            },
                            {
                                "title": Suncheon_list[24],
                                #"description": "",
                                "imageUrl": Suncheon_list[42],
                                "link": {
                                    "web": Suncheon_list[25]
                                }
                            },
                            {
                                "title": Suncheon_list[26],
                                #"description": "",
                                "imageUrl": Suncheon_list[43],
                                "link": {
                                    "web": Suncheon_list[27]
                                }
                            },
                            {
                                "title": Suncheon_list[28],
                                #"description": "",
                                "imageUrl": Suncheon_list[44],
                                "link": {
                                    "web": Suncheon_list[29]
                                }
                            },
                        ],
                        "buttons": [
                            {
                                "label": "홈페이지",
                                "action": "webLink",
                                "webLinkUrl": "https://trip.place.naver.com/list?query=%EC%88%9C%EC%B2%9C%20%EA%B0%80%EB%B3%BC%EB%A7%8C%ED%95%9C%EA%B3%B3&level=top&zoomLevel=10.000&theme=all"
                            }
                        ]  
                    }                                              
                    ]
                    }
                }],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "6466fb5a2ecb0e7d2bec3910",
                        "label": "홈"
                    },
                    {
                        "action": "block",
                        "messageText": "BBC요약1",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "추천 여행 경로"
                    },

                ],
            }
        })