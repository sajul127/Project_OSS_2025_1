from budget import Budget
from colorama import Fore, Back, Style, init

init(autoreset=True)


def main():
    budget = Budget()
    is_dark_mode = False

    def print_menu():
        if is_dark_mode:
            print(Back.BLACK + Fore.WHITE + "==== 간단 가계부 (다크모드) ====")
        else:
            print(Back.WHITE + Fore.BLACK + "==== 간단 가계부 (라이트모드) ====")

        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 모드 전환")
        print("5. 종료")

    while True:
        print_menu()
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            is_dark_mode = not is_dark_mode
            print("다크 모드로 전환되었습니다.\n" if is_dark_mode else "라이트 모드로 전환되었습니다.\n")
            

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()