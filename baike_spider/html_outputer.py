class HtmlOutputer(object):
    def __init__(self):
       self.self_data = []

    def collect_data(self, new_data):
        self.self_data.append(new_data)

    def output_html(self):
        output = open('output.html','w')
        output.write("<html>")
        output.write("<body>")
        output.write("<table>")
        for data in self.self_data:
            output.write("<tr>")
            output.write("<td>%s</td>" % data['url'].encode('utf-8'))
            output.write("<td>%s</td>" % data['title'].encode('utf-8'))
            output.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            output.write("</tr>")
        output.write("</table>")
        output.write("</body>")
        output.write("</html>")

        output.close()
