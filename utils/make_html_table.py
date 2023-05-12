

def make_html_table(table_title,table_header,table_content):
    table_title = '<table border="1" bordercolor="#c8c9cc" width=%s \
        cellpadding="5" cellspacing="0" "style=""微软雅黑",Helvetica,\
        Arial,sans-serif;font-weight:bold;font-size:14px;">\
        <tr><td colspan="8" bgcolor="#e1e4eb" style="font-weight:bold" border:none;\
        font-size:16px;padding-bottom:16px">%s</td>\
        </tr>' % (1000, table_title)
    
    html_header = '<tr>'
    for header in table_header:
        html_header += '<td style="font-weight:bold">%s\
                </td>' % (header)
    html_header += '</tr>'
    
    content = ''
    for item in table_content:
        content += '<tr>'
        for value in item:
            content += '<td>%s</td>' % (value)
        content += '</tr>'

    return table_title + html_header + content + '<br>'