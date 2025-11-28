import os
from tkinter import Tk, filedialog

def select_files():
    """Функция для выбора файлов через диалоговое окно"""
    root = Tk()
    root.withdraw()  # Скрываем главное окно
    
    print("Выберите файлы с кодом (можно несколько):")
    file_paths = filedialog.askopenfilenames(
        title="Выберите файлы с кодом",
        filetypes=[
            ("Все файлы", "*.*"),
            ("Python файлы", "*.py"),
            ("HTML файлы", "*.html;*.htm"),
            ("CSS файлы", "*.css"),
            ("JavaScript файлы", "*.js;*.jsx;*.ts;*.tsx"),
            ("Java файлы", "*.java"),
            ("C/C++ файлы", "*.c;*.cpp;*.cc;*.cxx;*.h;*.hpp"),
            ("C# файлы", "*.cs"),
            ("PHP файлы", "*.php"),
            ("Ruby файлы", "*.rb"),
            ("Go файлы", "*.go"),
            ("Rust файлы", "*.rs"),
            ("Swift файлы", "*.swift"),
            ("Kotlin файлы", "*.kt;*.kts"),
            ("Scala файлы", "*.scala"),
            ("SQL файлы", "*.sql"),
            ("XML файлы", "*.xml"),
            ("JSON файлы", "*.json"),
            ("YAML файлы", "*.yml;*.yaml"),
            ("Markdown файлы", "*.md;*.markdown"),
            ("Config файлы", "*.ini;*.cfg;*.conf"),
            ("Shell файлы", "*.sh;*.bash;*.zsh"),
            ("Batch файлы", "*.bat;*.cmd"),
            ("PowerShell файлы", "*.ps1"),
            ("Lua файлы", "*.lua"),
            ("Perl файлы", "*.pl;*.pm"),
            ("R файлы", "*.r"),
            ("MATLAB файлы", "*.m"),
            ("Dart файлы", "*.dart"),
            ("Elixir файлы", "*.ex;*.exs"),
            ("Haskell файлы", "*.hs"),
            ("Erlang файлы", "*.erl;*.hrl"),
            ("Clojure файлы", "*.clj;*.cljs;*.cljc"),
            ("F# файлы", "*.fs;*.fsx;*.fsi"),
            ("VB файлы", "*.vb"),
            ("TypeScript файлы", "*.ts;*.tsx"),
            ("JSX файлы", "*.jsx"),
            ("TSX файлы", "*.tsx"),
            ("SASS/SCSS файлы", "*.sass;*.scss"),
            ("Less файлы", "*.less"),
            ("Stylus файлы", "*.styl"),
            ("Docker файлы", "Dockerfile;*.dockerfile"),
            ("Makefile файлы", "Makefile;*.mk"),
            ("Text файлы", "*.txt"),
            ("Log файлы", "*.log")
        ]
    )
    
    root.destroy()
    return file_paths

def create_code_file(file_paths, output_filename="combined_code.txt"):
    """Создает файл с кодом из выбранных файлов"""
    
    if not file_paths:
        print("Файлы не выбраны. Программа завершена.")
        return
    
    try:
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for i, file_path in enumerate(file_paths):
                # Получаем имя файла с расширением
                filename = os.path.basename(file_path)
                
                # Записываем название файла в новом формате
                output_file.write(f"название файла: {filename}\n")
                
                try:
                    # Читаем и записываем содержимое файла
                    with open(file_path, 'r', encoding='utf-8') as input_file:
                        code_content = input_file.read()
                        output_file.write(code_content)
                        
                    # Добавляем отступ (пустую строку) между файлами, кроме последнего
                    if i < len(file_paths) - 1:
                        output_file.write("\n\n")
                        
                except UnicodeDecodeError:
                    print(f"Ошибка: Не удалось прочитать файл {filename} (возможно, бинарный файл)")
                    output_file.write(f"[Не удалось прочитать файл {filename} - возможно, это бинарный файл]\n")
                    if i < len(file_paths) - 1:
                        output_file.write("\n\n")
                except PermissionError:
                    print(f"Ошибка: Нет прав на чтение файла {filename}")
                    output_file.write(f"[Нет прав на чтение файла {filename}]\n")
                    if i < len(file_paths) - 1:
                        output_file.write("\n\n")
                except Exception as e:
                    print(f"Ошибка при чтении файла {filename}: {e}")
                    output_file.write(f"[Ошибка при чтении файла {filename}: {e}]\n")
                    if i < len(file_paths) - 1:
                        output_file.write("\n\n")
        
        print(f"Файл '{output_filename}' успешно создан!")
        print(f"Обработано файлов: {len(file_paths)}")
        
        # Показываем расположение созданного файла
        full_path = os.path.abspath(output_filename)
        print(f"Файл создан по пути: {full_path}")
        
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")

def get_supported_extensions():
    """Возвращает список поддерживаемых расширений"""
    extensions = {
        'Python': ['.py'],
        'HTML': ['.html', '.htm'],
        'CSS': ['.css'],
        'JavaScript': ['.js', '.jsx'],
        'TypeScript': ['.ts', '.tsx'],
        'Java': ['.java'],
        'C/C++': ['.c', '.cpp', '.cc', '.cxx', '.h', '.hpp'],
        'C#': ['.cs'],
        'PHP': ['.php'],
        'Ruby': ['.rb'],
        'Go': ['.go'],
        'Rust': ['.rs'],
        'Swift': ['.swift'],
        'Kotlin': ['.kt', '.kts'],
        'SQL': ['.sql'],
        'XML': ['.xml'],
        'JSON': ['.json'],
        'YAML': ['.yml', '.yaml'],
        'Markdown': ['.md', '.markdown'],
        'Text': ['.txt']
    }
    
    print("\nПоддерживаемые типы файлов:")
    for lang, exts in extensions.items():
        print(f"  {lang}: {', '.join(exts)}")

def main():
    """Основная функция программы"""
    print("=== Программа для объединения кода из файлов ===\n")
    
    # Показываем поддерживаемые расширения
    get_supported_extensions()
    print("\n" + "="*50 + "\n")
    
    # Выбираем файлы
    selected_files = select_files()
    
    if selected_files:
        # Спрашиваем имя выходного файла
        output_name = input("Введите имя выходного файла (по умолчанию: combined_code.txt): ").strip()
        if not output_name:
            output_name = "combined_code.txt"
        
        # Добавляем расширение .txt если его нет
        if not output_name.lower().endswith('.txt'):
            output_name += '.txt'
        
        # Создаем результирующий файл
        create_code_file(selected_files, output_name)
    else:
        print("Файлы не выбраны.")

if __name__ == "__main__":
    main()