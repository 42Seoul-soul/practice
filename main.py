# 나만의 프롬프트 관리 프로그램

# 카테고리 목록
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

# 기본 프롬프트 데이터 (이전 미션에서 쓴 프롬프트)
prompts = [
    {
        "title": "USAKI 광고 콘셉트 기획",
        "content": "당신은 10년 경력의 광고 크리에이티브 디렉터입니다. "
                   "'USAKI: AFTER 6' 퇴근 후 운동 캠페인의 30초 광고 콘셉트를 3가지 제안해주세요.",
        "category": "텍스트 생성",
        "favorite": False,
    },
    {
        "title": "퇴근길 직장인 키비주얼",
        "content": "Cinematic photo of a Korean office worker leaving the office at 6 PM, "
                   "city lights, warm golden hour lighting, hopeful mood, 16:9.",
        "category": "이미지 생성",
        "favorite": False,
    },
    {
        "title": "AFTER 6 광고 영상 씬",
        "content": "An office worker steps out of a subway station, then runs along "
                   "the Han River at dusk. Smooth tracking shot, cinematic, 8 seconds.",
        "category": "영상 생성",
        "favorite": False,
    },
]


def show_menu():
    """메뉴를 화면에 보여준다."""
    print()
    print("=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def input_not_empty(message):
    """빈 값이 아닐 때까지 계속 다시 입력받는다."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("값을 입력해주세요.")


def choose_category():
    """카테고리 목록을 보여주고 하나를 고르게 한다. (직접 입력 가능)"""
    print("카테고리 선택:")
    for i, category in enumerate(CATEGORIES, start=1):
        print(f"{i}) {category}")
    print(f"{len(CATEGORIES) + 1}) 직접 입력")

    while True:
        choice = input("선택: ").strip()
        if choice.isdigit():
            number = int(choice)
            if 1 <= number <= len(CATEGORIES):
                return CATEGORIES[number - 1]
            if number == len(CATEGORIES) + 1:
                return input_not_empty("카테고리 이름: ")
        print("올바른 번호를 입력해주세요.")


def add_prompt():
    """새 프롬프트를 입력받아 목록에 추가한다."""
    print()
    print("=== 프롬프트 추가 ===")
    title = input_not_empty("제목: ")
    content = input_not_empty("내용: ")
    category = choose_category()

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
    })
    print("프롬프트가 추가되었습니다!")


def print_prompt_line(number, prompt):
    """프롬프트 한 줄을 '번호. [카테고리] 제목 ⭐' 형태로 출력한다."""
    star = " ⭐" if prompt["favorite"] else ""
    print(f"{number}. [{prompt['category']}] {prompt['title']}{star}")


def show_list():
    """저장된 모든 프롬프트를 번호와 함께 보여준다."""
    print()
    print("=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, start=1):
        print_prompt_line(i, prompt)
    print()
    print(f"총 {len(prompts)}개의 프롬프트")


def main():
    """메뉴를 계속 보여주고, 사용자가 고른 번호를 처리한다."""
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 번호입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()