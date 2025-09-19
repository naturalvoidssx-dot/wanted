#!/usr/bin/env python3
"""
Защищенный скрипт с проверкой переменной окружения
"""

import sys
import os

def check_user_agent():
    """Проверяет правильный ли User-Agent через переменную окружения"""
    user_agent = os.environ.get('USER_AGENT', '')
    
    if user_agent != 'Secure-Script-Executor/1.0':
        print("🚫 Доступ запрещен: Скрипт должен запускаться через безопасный исполнитель")
        print("ℹ️  Используйте: python3 secure_executor.py")
        sys.exit(1)

def main():
    """Основная логика вашего скрипта"""
    print("✅ Проверка пройдена! Запускаем основной код...")
    # Ваш основной код здесь

if __name__ == "__main__":
    check_user_agent()
    main()
