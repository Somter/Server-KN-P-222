#!C:\Users\alecs\source\repos\Server-KN-P-222\.venv\Scripts\python.exe

import codecs, os, sys
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())

rows = "".join(
    f"<tr><td>{k}</td><td>{v}</td></tr>"
    for k, v in sorted(os.environ.items())
)

envs = f"""
<table border="1" cellspacing="0" cellpadding="5">
  <tr>
    <th>Имя переменной</th>
    <th>Значение</th>
  </tr>
  {rows}
</table>
"""

html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Переменные окружения</title>
    <link rel="icon" href="/python.png" />
</head>
<body>
    <h1>Переменные окружения (CGI)</h1>
    {envs}
</body>
</html>"""

print("Content-Type: text/html; charset=utf-8")
print()
print(html)
