

def make_html_table(table_title,table_header,table_content):
    table_title = '<table border="1" bordercolor="#c8c9cc" width: 100%%; max-width: 1200px; \
        cellpadding="5" cellspacing="0" "style=""微软雅黑",Helvetica,\
        Arial,sans-serif;font-weight:bold;font-size:14px; table-layout:fixed">\
        <tr><td colspan="8" bgcolor="#e1e4eb" style="font-weight:bold" border:none;\
        font-size:16px;padding-bottom:16px">%s</td>\
        </tr>' % (table_title)
    
    html_header = '<tr>'
    for header in table_header:
        if header == '接口响应结果':
            html_header += '<td style="text-align: center; background-color: #f2f2f2; border: 1px solid #ccc;font-weight:bold; width:50%%;">%s\
                </td>' % (header)
        else:
            html_header += '<td style="text-align: center; background-color: #f2f2f2; border: 1px solid #ccc;font-weight:bold; width:10%%;">%s\
                </td>' % (header)
    html_header += '</tr>'
    
    content = ''
    for item in table_content:
        content += '<tr>'
        for value in item:
            content += '<td word-break: break-all;>%s</td>' % (value)
        content += '</tr>'

    return table_title + html_header + content + '<br>'