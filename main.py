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


def main():
    """메뉴를 계속 보여주고, 사용자가 고른 번호를 처리한다."""
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 번호입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()