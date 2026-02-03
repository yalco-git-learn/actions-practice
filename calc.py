import datetime  # 이 부분이 반드시 필요합니다!

num1 = 10
num2 = 2

print(f"### 🧮 사칙연산 결과 보고서")
print(f"- **첫 번째 숫자:** {num1}")
print(f"- **두 번째 숫자:** {num2}")
print(f"---")
print(f"- **덧셈 (+):** {num1 + num2}")
print(f"- **뺄셈 (-):** {num1 - num2}")
print(f"- **곱셈 (*):** {num1 * num2}")
print(f"- **나눗셈 (/):** {num1 / num2 if num2 != 0 else '0으로 나눌 수 없습니다.'}")
print(f"\n_작성 시간: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_")