from bs4 import BeautifulSoup

html = '''
<html><body>
  <img src="a.png"><img src="b.png">
  <script src="app.js"></script>
  <a href="https://example.com">Link 1</a>
  <a href="https://owasp.org">Link 2</a>
</body></html>
'''

soup = BeautifulSoup(html, "html.parser")
for tag in ["img", "script", "a"]:
    found = soup.find_all(tag)
    print(f"<{tag}> count: {len(found)}")
    for item in found:
        print(" ", item)
