import argparse
import sys
import os


def validate_args(args):
    # Проверка имени пакета
    if not args.package or args.package.strip() == "":
        raise ValueError("Ошибка: имя пакета не может быть пустым.")

    # Проверка режима тестирования (bool)
    if args.test not in ["true", "false"]:
        raise ValueError("Ошибка: параметр --test должен быть 'true' или 'false'.")

    # Проверка пути/URL
    if args.test == "true":
        # В тестовом режиме repo должен быть путём к файлу
        if not os.path.exists(args.repo):
            raise ValueError("Ошибка: в тестовом режиме --repo должен быть путём к файлу, файл не найден.")
    else:
        # В реальном режиме хотя бы проверяем, что строка похожа на URL
        if not args.repo.startswith("http://") and not args.repo.startswith("https://"):
            raise ValueError("Ошибка: в обычном режиме --repo должен быть URL.")

    return True


def main():
    parser = argparse.ArgumentParser(description="Dependency graph tool (Stage 1, Variant 2)")

    # Аргументы командной строки
    parser.add_argument("--package", type=str, help="Имя анализируемого пакета")
    parser.add_argument("--repo", type=str, help="URL или путь к тестовому файлу")
    parser.add_argument("--test", type=str, help="Режим тестирования: true/false")
    parser.add_argument("--filter", type=str, default="", help="Подстрока для фильтрации пакетов")

    args = parser.parse_args()

    # Обработка ошибок
    try:
        validate_args(args)
    except Exception as e:
        print(str(e))
        sys.exit(1)

    # Вывод параметров в формате ключ-значение
    print("Параметры конфигурации:")
    print(f"package = {args.package}")
    print(f"repo = {args.repo}")
    print(f"test = {args.test}")
    print(f"filter = {args.filter}")


if __name__ == "__main__":
    main()
