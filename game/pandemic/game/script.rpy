# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.

# 게임에서 사용할 캐릭터를 정의합니다.
define player_name = "플레이어이름"
define news = Character('뉴스', color='#000000')
define me = Character("player_name", dynamic=True, color="#000000")
define kwon = Character('권지웅 전문가', color="#000000")
define radiodj = Character('라디오 DJ', color="#000000")
define ddal = Character('딸', color="#000000")
define kkondae = Character('박 부장', color="#000000")
define jung = Character('정 인턴', color="#000000", image = "jung")
define gui.text_color = '#000000'
define gui.interface_text_color = '#ff0000'
define gender = ""
image side jung smile = "images/jung.png"
## 인-게임 글자에 사용됩니다.
define gui.text_font = "NanumBarunGothic.ttf"
## 캐릭터의 이름에 사용됩니다.
define gui.name_text_font = "NanumBarunGothicBold.ttf"
## 인터페이스에 사용됩니다.
define gui.interface_text_font = "NanumBarunGothicBold.ttf"



# 여기에서부터 게임이 시작합니다.
label start:

    "당신 이름은?"
    $player_name = renpy.input("내 이름은 ")##화면에 내 이름은 나오고 다음칸에 입력받는 칸이 나온다.
    me "내 이름은 [player_name]"##p는 위에 선언한 케릭터고, 대화창에 변수값을 나오게 할려면 [변수명]으로 사용한다.

    "당신의 성별은?"
    menu:
        "여자":
              $gender = "엄마"

        "남자":
              $gender = "아빠"

        "알리고 싶지 않음":
              $gender = "부모님"

    "Intro"
    news "...바이러스의 확산으로 인해 ...불가피한 희생... "

    me "..."

    news "...에서 발병한 것으로, ...로 감염된 환자의 ...의하면
         ...과 함께 정신 분열 증세가 나타나는 것으로 밝혀졌습니다.
         초기 감염 단계에서는 일반적인 호흡기 바이러스 증세와 비슷하여 이상 징후 발견에 난항을 겪을 것으로 예상되어집니다."

    me "...?"

    ddal "[gender]! 일어나요… 해가 이만큼! 이만큼 떴어요!"

    me "... 뭐야. 벌써 8시네. 딸! 유치원 가자."

    "차 안"

    radiodj "권지웅 전문가님을 모시고 얘기 한 번 나눠보겠습니다. {fast} 안녕하세요!"

    kwon "안녕하세요."

    radiodj "이번에 큰 이슈가 된 이 바이러스, 어디서부터 전파된 건가요?"

    kwon "남아프리카 공화국의 요하네스버그에서 시작된 바이러스가 미국으로 가는 선박으로 통해 미국에 퍼지게 되었고,{fast}
          그로 인해 자연스럽게 여러 유럽, 일본 등에 퍼져 결국 우리나라에도 퍼지게 되었죠."

    "{b}더 자세히 들어볼까?{/b}"

    menu:
        "예":
              $renpy.notify("Hint1 획득")
              radiodj "{b} 그렇다면 왜 감염되는 건가요? {/b}"
              kwon "{b} 바이러스는 나방의 분진에 의해서 감염된다고 추정되고 있습니다.
              온 몸이 가렵고, 피부 껍질이 올라오는 등의 증세가 보이며, 말기에는 정신 분열로 인해 의사소통 불능에 도달하는 사례까지 있었습니다. {/b}"


        "아니요":
              pass

    "(딸의 유치원에 도착했다.)"
    me "딸! 유치원 잘 갔다올 수 있지?"
    ddal "응 [gender]!{fast} (유치원 문 쪽으로 빠르게 뛰어간다.) "
    me "뛰지 말고 조심! 잘 갔다와!"

    "회사"
    "(직원들의 휴대폰이 일제히 울린다.)"
    kkondae "뭐야? 회사에선 무음으로 해놓던지 해야지... 하여간... "

    "{b}휴대폰을 확인해볼까?{/b}"
    menu:
        "예":
              "[긴급재난경보] 4월 5일 미림시 목구 동백동 동백포차 산악회 모임으로 인한 확진자 4명 발생, 증상을
	          보이는 방문자는 즉시 보건소로 가서 검사 부탁드립니다. 전국민 마스크 사용 및 외식 자제
	          부탁드립니다. {fast}"
              kkondae "[player_name[0]] 대리!!!!!!!!!!! 지금 휴대폰 확인할 정신이 있는 건가?
              그렇게 시간이 넉넉하면 이것도 좀 부탁하네.{fast} 내가 오늘 와이프랑 약속이 있어서~ "
              "(엄청난 양의 종이가 책상에 쌓였다… 꼼짝없이 {b}야근{/b}이다.)"
              "(야근하기 전에 딸을 먼저 집에 데려다주러 가자.)"


        "아니요":
              "(정 인턴이 낑낑대며 A4용지 더미를 가져온다.{fast} 도와줘야겠다.)"
              jung smile "감사합니다 대리님~ "
              "(정 인턴이 휴대폰을 힐끗 보았다.)"
              jung smile "헐~ 대박~ "
              me "뭔데 그래?"
              jung smile "저희 예전에 회식 장소 후보였던 동백포차 있잖아여.{fast}"
              jung smile "거기서 산악회 모임하다가 버그바이러스 단체로 감염됐대요."
              me "버그바이러스? {fast} 요새 한참 뉴스에서 나오던데.{fast} 근데 이름이 버그바이러스야?"
              jung smile "그… 버그로 끝나는 지역에서 시작된 거라서 그렇게 부를걸요?"
              jung smile "저도 얼핏 들은 거라 잘 몰라여. {fast}{b}(머리를 긁적인다.){/b}"
              "(고된 하루가 끝났다. 집으로 돌아가자.)"
    "집 안"
    ddal "[gender]... 나 몸이 간지러워"

    menu:
        "무슨 일 있었어?":
              ""


        "약 발라":
              "(정 인턴이 낑낑대며 A4용지 더미를 가져온다.{fast} 도와줘야겠다.)"
              jung "감사합니다 대리님~ "
              "(정 인턴이 휴대폰을 힐끗 보았다.)"
              jung "헐~ 대박~ "
              me "뭔데 그래?"
              jung "저희 예전에 회식 장소 후보였던 동백포차 있잖아여.{fast}
               거기서 산악회 모임하다가 버그바이러스 단체로 감염됐대요."
              me "버그바이러스? {fast} 요새 한참 뉴스에서 나오던데.{fast} 근데 이름이 버그바이러스야?"
              jung "그… 버그로 끝나는 지역에서 시작된 거라서 그렇게 부를걸요? {fast}
              저도 얼핏 들은 거라 잘 몰라여. {fast}{b}(머리를 긁적인다.){/b}"
              "(고된 하루가 끝났다. 집으로 돌아가자.)"
              ""





    return
