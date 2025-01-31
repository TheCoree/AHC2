# Новая версия! AHC v2.0 CLI Tool

AHC - ASCII Hyper Coder - это CLI-инструмент для шифрования и дешифрования сообщений с использованием алгоритма смещения символов.

## 🚀 Установка и запуск на Linux

### 1. Установите Python (если не установлен)
```bash
sudo apt update && sudo apt install python3
```

### 2. Скачайте и установите AHC
```bash
git clone https://github.com/TheCoree/ahc2.git 
cd AHCturbo
chmod +x AHCturbo.py
```

### 3. Создайте символическую ссылку для удобного вызова
```bash
sudo ln -s $(pwd)/ahc.py /usr/local/bin/ahc
```

Теперь вы можете вызывать программу просто командой `ahc`:
```bash
ahc "Привет мир"
ahc -m 3 -k 2 "Привет мир"
ahc -d "⦙⫣⪓⩗⩵⫷ƣ⪻⪓⫣"
ahc -dv "⥖⪠⩐⨔⨲⪴Š⩸⩐⪠ mixing: 3, key: 2"
```

## 🔧 Аргументы

| Флаг | Короткий | Описание |
|------|---------|------------|
| `--decrypt` | `-d` | Расшифровать текст с указанными `mixing` и `key` (по умолчанию 9) |
| `--decrypt-values` | `-dv` | Расшифровать текст, содержащий `mixing` и `key` внутри себя |
| `--mixing` | `-m` | Указать значение `mixing` (по умолчанию 9) |
| `--key` | `-k` | Указать значение `key` (по умолчанию 9) |

## 📝 Примеры использования

### 🔐 Кодирование текста
```bash
ahc "Привет мир"
```
**Вывод:**
```bash
⦙⫣⪓⩗⩵⫷ƣ⪻⪓⫣
```

С кастомными `mixing` и `key`:
```bash
ahc -m 3 -k 2 "Привет мир"
```
**Вывод:**
```bash
⥖⪠⩐⨔⨲⪴Š⩸⩐⪠ mixing: 3, key: 2
```

### 🔓 Декодирование текста

Без указанных `mixing` и `key`:
```bash
ahc -d "⦙⫣⪓⩗⩵⫷ƣ⪻⪓⫣"
```

С указанными `mixing` и `key` внутри строки:
```bash
ahc -dv "⥖⪠⩐⨔⨲⪴Š⩸⩐⪠ mixing: 3, key: 2"
```

## 🎯 Лицензия
Проект распространяется под лицензией MIT.

