from django.test import TestCase

# Create your tests here.
import requests

url = 'http://127.0.0.1:8000/json2pdf/'
json_data = {
    "json": [
        {
    "Name" : "LOREN IPSUM",
    "mobile" : "+91(123)456-7890",
    "email" : "abcdfldfdofksd@gmail.com",
    "linked" : "linkedin.com/in/akash-dholakiya-91599024b/",
    "github" : "github.com/akashdholakiya",
    "CareerSum" :{
        "data" : "lorem ipsum asa sa idsuiad auid jasjd suiad iuasd uias asid uiasdh uisa huiashd uisah sd lorem s sisisi si si jsi jsi js jis is isi si isj is lorem ipsum asa sa idsuiad auid jasjd suiad iuasd uias asid uiasdh uisa huiashd uisah sd lorem s sisisi si si jsi jsi js jis is isi si isj is lorem ipsum asa sa idsuiad auid jasjd suiad iuasd uias asid uiasdh uisa huiashd uisah sd lorem s sisisi si si jsi jsi js jis is isi si isj is lorem ipsum asa sa idsuiad auid jasjd suiad iuasd uias asid uiasdh uisa huiashd uisah sd lorem s sisisi si si jsi jsi js jis is isi si isj is lorem ipsum asa sa idsuiad auid jasjd suiad iuasd uias asid uiasdh uisa huiashd uisah sd lorem s sisisi si si jsi jsi js jis is isi si isj is"
    },
    "education" : {
        "Education-clg" : "This College",
        "ed-date" : "july 2001 - july 2005",
        "edu-details" : "dsa isa jdsa jsa"
    },
    "achievement" : [
        {
            "ach-details" : "dsa isa jdsa jsa"
        },
        {
            "ach-details" : "dsa isa jdsa jsa"
        },
        {
            "ach-details" : "dsa isa jdsa jsa"
        }
    ],
    "experience" : [
        {
            "exp-company" : "This Company",
            "exp-date" : "july 2001 - july 2005",
            "exp-details1" : "dsa isa jdsa jsa jdsa jsa",
            "exp-details2" : "dsa isa jdsa jsa jdsa jsa",
            "exp-details3" : [
                {
                    "exp_details" : "dsa isa jdsa jsa"
                },
                {
                    "exp_details" : "dsa isa jdsa jsa"
                },
                {
                    "exp_details" : "dsa isa jdsa jsa"
                }
            ]
        },
        {
            "exp-company" : "This Company",
            "exp-date" : "july 2001 - july 2005",
            "exp-details1" : "dsa isa jdsa jsa jdsa jsa",
            "exp-details2" : "dsa isa jdsa jsa jdsa jsa",
            "exp-details3" : [
                {
                    "exp_details" : "dsa isa jdsa jsa"
                },
                {
                    "exp_details" : "dsa isa jdsa jsa"
                },
                {
                    "exp_details" : "dsa isa jdsa jsa"
                }
            ]
        },
        {
            "exp-company" : "This Company",
            "exp-date" : "july 2001 - july 2005",
            "exp-details1" : "dsa isa jdsa jsa jdsa jsa",
            "exp-details2" : "dsa isa jdsa jsa jdsa jsa",
            "exp-details3" : [
                {
                    "exp_details" : "dsa isa jdsa jsa"
                },
                {
                    "exp_details" : "dsa isa jdsa jsa"
                },
                {
                    "exp_details" : "dsa isa jdsa jsa"
                }
            ]
        }
    ],
    "Internships" : [
        {
            "intern-company" : "This Company",
            "intern-date" : "july 2001 - july 2005",
            "intern-details1" : "dsa isa jdsa jsa jdsa jsa",
            "intern-details2" : "dsa isa jdsa jsa jdsa jsa",
            "intern-details3" : [
                {
                    "intern_details" : "dsa isa jdsa jsa"
                },
                {
                    "intern_details" : "dsa isa jdsa jsa"
                },
                {
                    "intern_details" : "dsa isa jdsa jsa"
                }
            ]
        },
        {
            "intern-company" : "This Company",
            "intern-date" : "july 2001 - july 2005",
            "intern-details1" : "dsa isa jdsa jsa jdsa jsa",
            "intern-details2" : "dsa isa jdsa jsa jdsa jsa",
            "intern-details3" : [
                {
                    "intern_details" : "dsa isa jdsa jsa"
                },
                {
                    "intern_details" : "dsa isa jdsa jsa"
                },
                {
                    "intern_details" : "dsa isa jdsa jsa"
                }
            ]
        },
        {
            "intern-company" : "This Company",
            "intern-date" : "july 2001 - july 2005",
            "intern-details1" : "dsa isa jdsa jsa jdsa jsa",
            "intern-details2" : "dsa isa jdsa jsa jdsa jsa",
            "intern-details3" : [
                {
                    "intern_details" : "dsa isa jdsa jsa"
                },
                {
                    "intern_details" : "dsa isa jdsa jsa"
                },
                {
                    "intern_details" : "dsa isa jdsa jsa"
                }
            ]
        }
    ],
    "Hackathon" : [
        {
            "hack-title" : "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. | Curabitur dictum gravida mauris.",
            "hack-date" : "2019",
            "hack-details" : [
                {
                    "hack_details1" : "Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
                },
                {
                    "hack_details1" : "Aliquam tincidunt urna."
                }
            ]
        },
        {
            "hack-title" : "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. | Curabitur dictum gravida mauris.",
            "hack-date" : "2019",
            "hack-details" : [
                {
                    "hack_details1" : "Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
                },
                {
                    "hack_details1" : "Aliquam tincidunt urna."
                }
            ]
        },
        {
            "hack-title" : "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. | Curabitur dictum gravida mauris.",
            "hack-date" : "2019",
            "hack-details" : [
                {
                    "hack_details1" : "Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
                },
                {
                    "hack_details1" : "Aliquam tincidunt urna."
                }
            ]
        }
    ],
    "Gitproj" : [
        {
            "gitproj-title" : "Lorem ipsum dolor sit amet, consectetuer adipiscing elit.  Curabitur dictum gravida mauris.",
            "gitproj-details" : [
                {
                    "gitproj_details1" : "Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
                },
                {
                    "gitproj_details1" : "Aliquam tincidunt urna."
                }
            ]
        },
        {
            "gitproj-title" : "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. | Curabitur dictum gravida mauris.",
            "gitproj-details" : [
                {
                    "gitproj_details1" : "Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
                },
                {
                    "gitproj_details1" : "Aliquam tincidunt urna."
                }
            ]
        },
        {
            "gitproj-title" : "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. | Curabitur dictum gravida mauris.",
            "gitproj-details" : [
                {
                    "gitproj_details1" : "Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
                },
                {
                    "gitproj_details1" : "Aliquam tincidunt urna."
                }
            ]
        }
    ]
}
    ]
}  # Your JSON data
response = requests.post(url, json=json_data)

print(response.status_code)
