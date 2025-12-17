def loading(percentage: int) -> str:

    percent = percentage / 10
    dots = 10 - percent

    if percent < 10:
        result = f"{percentage}% [{'%' * int(percent)}{'.' * int(dots)}]\nStill loading..."
        return result

    else:
        result = "100% Complete!\n[%%%%%%%%%%]"
        return result

def main():
    loaded_percentage = int(input())

    visualised_result = loading(loaded_percentage)

    print(visualised_result)

main()