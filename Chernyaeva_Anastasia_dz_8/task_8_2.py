import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    line = fr.readline()
    while line:
        # parse a line from the log file
        pattern = re.compile(
            r'(.+)(?:\s-\s-\s\[)(.+)(?:]\s\")(.+)(?:\s)(.+)(?:\s)(?:.+)(?:"\s)(\d+)(?:\s)(\d+)')
        print(*pattern.findall(line))
        line = fr.readline()
