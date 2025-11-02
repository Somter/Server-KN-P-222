import json
from datetime import datetime
import os

LOG_FILE = "exec_log.json"

def load_log():
    """Зчитує журнал запусків з файлу або створює новий, якщо його немає або файл пошкоджено."""
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content: 
                    raise ValueError("empty file")
                return json.loads(content)
        except (json.JSONDecodeError, ValueError):
            print("  Файл журналу пошкоджений або порожній — створюю новий.")
            return {"program": "exec logger", "execMoments": []}
    else:
        return {"program": "exec logger", "execMoments": []}

def save_log(log_data):
    """Зберігає журнал запусків у файл."""
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(log_data, f, indent=4, ensure_ascii=False)

def main():
    log_data = load_log()
    exec_moments = log_data.get("execMoments", [])

    if exec_moments:
        print(f"Програма запускалась попередньо {len(exec_moments)} раз(и) о:")
        print(", ".join(f'"{moment}"' for moment in exec_moments))
    else:
        print("Це перший запуск програми.")

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    exec_moments.append(current_time)
    log_data["execMoments"] = exec_moments

    save_log(log_data)

    print(f"\nПоточний момент запуску додано: \"{current_time}\"")

if __name__ == "__main__":
    main()
