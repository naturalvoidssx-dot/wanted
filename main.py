#!/usr/bin/env python3
"""
Защищенный скрипт с проверкой User-Agent
"""

import sys
import os

def check_user_agent():
    """Проверяет правильный ли User-Agent"""
    # Получаем информацию о родительском процессе
    try:
        # Для Linux/MacOS
        if os.name == 'posix':
            parent_pid = os.getppid()
            with open(f'/proc/{parent_pid}/cmdline', 'rb') as f:
                cmdline = f.read().decode('utf-8', errors='ignore')
            
            if 'Secure-Script-Executor/1.0' not in cmdline:
                print("🚫 Доступ запрещен: Неверный User-Agent")
                sys.exit(1)
                
        # Для Windows (альтернативный метод)
        else:
            # Проверка через переменные окружения или другие методы
            # Этот метод менее надежен на Windows
            user_agent = os.environ.get('USER_AGENT', '')
            if 'Secure-Script-Executor/1.0' not in user_agent:
                print("🚫 Доступ запрещен: Неверный User-Agent")
                sys.exit(1)
                
    except Exception as e:
        print(f"🚫 Ошибка проверки доступа: {str(e)}")
        sys.exit(1)

# Проверяем при запуске
if __name__ == "__main__":
    check_user_agent()
    print("✅ Проверка User-Agent пройдена успешно")

print('hi by wanted')
